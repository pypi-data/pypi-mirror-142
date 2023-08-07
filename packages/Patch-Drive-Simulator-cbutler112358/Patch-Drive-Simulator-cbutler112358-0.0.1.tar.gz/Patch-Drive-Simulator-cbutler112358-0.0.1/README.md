
Patch Drive Simulator (PaDS)

This program simulates gene drive spreading in a population of organisms over a patch-based landscape.
The user specifies population, drive, and system parameters in a .yaml file. 
Upon completion, a .yaml file is returned containing the target population size after a user-defined
number of generations. 

The program can be installed directly via GitHub or on the command line as follows:
1. Navigate to the location of patch_drive_simulator.py
2. To install using pip, type:

py run_patch_drive.py -i input_file.yaml -o output_file.yaml

on a Windows machine and 

python3 run_patch_drive.py -i input_file.yaml -o output_file.yaml

on macOS/Unix. 

**Important note:** Line 4 in run_patch_drive.py must be changed to point to the modules located on
the user's systems. Future versions will correct for this. See the corresponding final report
for more information on this.

Citation: 

PaDS (2022). Cole Butler, v. 1.0.0. GitHub: https://github.com/cbutler112358/course-projects-w2022.