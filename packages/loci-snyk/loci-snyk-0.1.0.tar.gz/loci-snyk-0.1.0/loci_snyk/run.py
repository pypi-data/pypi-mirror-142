import json
import click
import os
import pathlib
from rich.progress import Progress

import pendulum
import loci_snyk.utils as lcu


@click.command()
@click.option("-i", "--input-file",
              prompt="Snyk JSON file",
              help="The Snyk JSON file with the output of a test",
              required=True,
              type=str)
@click.option("-b", "--base-path",
              help="Base path of the repo used in artifact calculation",
              required=False,
              type=str)
@click.option("--src-root-dir",
              help="Name of LN Source Root directory, used for autodetection of artifacts",
              required=True,
              type=str,
              default="_src")
@click.option("--cvss-score-min",
              help="Minimum CVSS Score needed to import to Loci Notes",
              required=True,
              type=float,
              default=4.0)
def run(input_file, src_root_dir, base_path, cvss_score_min):
    """Process a Snyk JSON file and add results to Loci Notes"""

    lcu.print_info("Getting directory project information...")
    project_id, project_name = lcu.get_project_id_from_config_in_dir(os.getcwd())
    if project_id is None or project_name is None:
        lcu.print_error("Unable to determine associated project. To correct this, run this under a directory "
                        "associated with a Loci Notes project.")
        quit(-1)
    lcu.print_success(f"Using [bold]{project_name}[/bold].")

    lcu.print_info("Opening Snyk JSON file...")
    try:
        with open(input_file, "r", encoding="utf-8") as fd:
            file_contents_str = fd.read()
            results_dict = json.loads(file_contents_str)
    except FileNotFoundError:
        lcu.print_error(f"Failed to open the file '{input_file}'. Please check to make sure it exists.")
        quit(-1)
    except json.JSONDecodeError:
        lcu.print_error(f"Failed to parse the file '{input_file}'. It does not appear to be valid JSON.")
        quit(-1)

    lcu.print_info("Processing Snyk JSON file...")

    try:
        # Everything that follows is based on the state of Snyk JSON files as of March 2022. Since there is no schema,
        # this is likely to change over time. Correct things here if they do.

        # First thing we do is see if there's a source root directory we can use to autodetect artifact names for
        # *all* runs. If not, we kick back an error with some possibilities.
        has_unknown_paths = False
        possible_basenames = []
        total_vulns = 0

        for run in results_dict:
            fq_file_path = str(pathlib.Path(run["path"], run["displayTargetFile"]).as_posix())

            if "/" + src_root_dir + "/" not in fq_file_path:
                has_unknown_paths = True
                file_base_path = os.path.basename(run["path"])

                if file_base_path not in possible_basenames:
                    # NOTE - There's a good possibility we could get this from "projectName" directly without needing
                    # to ask for it.
                    possible_basenames.append(file_base_path)
            total_vulns += len(run["vulnerabilities"])

        if has_unknown_paths:
            lcu.print_error("Some file paths in the Snyk file have ambiguous artifact paths. To ensure "
                            "consistent calculation of artifacts for files outside of the standard Loci Notes source "
                            "directory (\"_src\"), you need to manually provide the base path. The following are some "
                            "possibilities:", fatal=False)
            for name in possible_basenames:
                print("    * " + name)
            quit(-1)

        with Progress() as progress_bar:
            total_progress = total_vulns
            task = progress_bar.add_task("Importing...", total=total_progress)

            # At the top level of each file is an array of "runs" on each of the detected packages within the repo
            for run in results_dict:
                # This is the FQ path of the file which "imports" the vulnerable dependency
                fq_file_path = str(pathlib.Path(run["path"], run["displayTargetFile"]).as_posix())

                # This is the calculated artifact filename.
                artifact_filename = lcu.calculate_artifact_from_fq_filename(fq_file_path, src_root_dir, base_path)

                # Tag the top of the file to let users know this file was checked by Snyk
                new_note = {}
                # For this type of note, just put it at the top of the file.
                new_note["artifact_descriptor"] = artifact_filename + ":1"
                new_note["submission_tool"] = "Snyk"
                new_note["note_type"] = "LOG"
                new_note["contents"] = "This file was reviewed for vulnerable dependencies."
                # Detection and prevention of duplicate notes is handled by the server.
                lcu.loci_api_req(f"/api/projects/{project_id}/notes", method="POST", data=new_note, show_loading=False)
                # The API call function has error output already.

                # Next see if there were any vulns.
                if len(run["vulnerabilities"]) > 0:
                    # For this flow, there was at least one vulnerability in the run.
                    num_of_vulns = run["uniqueCount"]
                    if num_of_vulns == 1:
                        lcu.print_info(f"The file \"{artifact_filename}\" had {num_of_vulns} reported unique "
                                       "vulnerable dependency. Adding the dependency as a tracked artifact.")
                    else:
                        # Grammer.
                        lcu.print_info(f"The file \"{artifact_filename}\" had {num_of_vulns} reported unique "
                                       "vulnerable dependencies. Adding each dependency as a tracked artifact.")

                    for vuln in run["vulnerabilities"]:
                        # See if the CVSS Score meets the threshold for us to try an
                        # import (to help minimize noise)
                        cvss_score = vuln["cvssScore"]
                        title = vuln["title"]
                        ultimate_vuln_dep = vuln["packageName"]

                        if cvss_score >= cvss_score_min:
                            # Extract a bunch of the information we need
                            humanized_age = pendulum.parse(vuln["disclosureTime"]).diff_for_humans()
                            snyk_id = vuln["id"]
                            ultimate_vuln_dep_version = str(vuln["version"])
                            try:
                                source_vuln_dep_raw = vuln["from"][1]
                            except IndexError:
                                source_vuln_dep_raw = vuln["from"][0]

                            source_vuln_dep = source_vuln_dep_raw.split("@")[0]
                            # source_vuln_dep_version = source_vuln_dep_raw.split("@")[1]

                            # So the line calculation of the artifact gets a bit weird here, because we need to
                            # basically find the source_vuln_dep manually, and then attach the result to that
                            # line in the original package file as an artifact. There's not a good "standard"
                            # way to do this across all possible dependency management files, so here were
                            # just trying to find it by string search.

                            # First, open the package file
                            try:
                                with open(fq_file_path, "r") as fd:
                                    package_file_lines = fd.readlines()

                            except FileNotFoundError:
                                lcu.print_error(f"Unable to find the file '{fq_file_path}'. Loci Notes needs this "
                                                "file to properly tag the dependency as an artifact, and this should "
                                                "be run on the same host where the original scan was performed.")
                                quit(-1)

                            # Next, see if we can find the source
                            artifact_line = None

                            for n in range(len(package_file_lines)):
                                current_line = package_file_lines[n]
                                if source_vuln_dep in current_line:
                                    artifact_line = n + 1
                                    break

                            if artifact_line is None:
                                # Maybe in the future we can try to ask for it manually.
                                lcu.print_error(f"Unable to find the dependency '{source_vuln_dep}' in '{fq_file_path}'"
                                                ". This dependency will not be imported.", fatal=False)

                            full_artifact = artifact_filename + ":" + str(artifact_line)

                            # Send the info to the LN server
                            new_note = {}
                            new_note["artifact_descriptor"] = full_artifact
                            new_note["submission_tool"] = "Snyk"
                            new_note["note_type"] = "LOG"
                            new_note["contents"] = "**Possible Vulnerable Dependency Found**\n\n"
                            new_note["contents"] += "**Description** - " + title + "\n"
                            new_note["contents"] += "**CVSS Score** - " + str(cvss_score) + "\n"
                            new_note["contents"] += "**Discovered** - " + humanized_age + "\n"
                            new_note["contents"] += "**Vulnerable Dependency** - " + ultimate_vuln_dep + " v" \
                                + ultimate_vuln_dep_version + "\n"
                            new_note["contents"] += "**Root Dependency** - " + source_vuln_dep + "\n"
                            new_note["contents"] += "**Snyk ID** - " + snyk_id

                            # Detection and prevention of duplicate notes is handled by the server.
                            lcu.loci_api_req(f"/api/projects/{project_id}/notes", method="POST",
                                             data=new_note, show_loading=False)

                        else:
                            lcu.print_warning(f"From {artifact_filename}, the dependency {ultimate_vuln_dep} has "
                                              f"a CVSS score of {cvss_score} which did not meet the minimum "
                                              "threshold, and will not be imported.")

                        progress_bar.update(task, advance=1)

    except KeyError:
        # In the future we can turn this into a warning and just try and push through.
        lcu.print_error("Failed to parse the file '{input_file}'. It does not appear to be a valid Snyk "
                        "JSON results file.")
        quit(-1)
