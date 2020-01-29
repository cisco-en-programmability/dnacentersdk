"""List any possible scripts to run otherwise exit(0)"""
import os

# Where are the scripts residing?  (Should be /usr/src/app/scripts that is mounted at Docker run.)
script_dir = "/usr/src/app/scripts"
if not os.path.isdir(script_dir):
    script_dir = os.path.join(os.getcwd(), "example_scripts")
files_in_dir = os.listdir(script_dir)

list_of_scripts = []
# Ensure that we only show the python files.  (Those ending in .py)
for file in files_in_dir:
    if file[-3:] == ".py":
        list_of_scripts.append(file)

# Sort list alphabetically by filename.
list_of_scripts.sort()
if list_of_scripts:
    # Display a menu
    print("")
    print("Select which Python script to run:")
    for counter, file in enumerate(list_of_scripts):
        print(f'\t{counter}: {file}')
    qty_of_scripts = len(list_of_scripts)
    try:
        choice = int(input(f'Select 0-{qty_of_scripts - 1}: '))
        if 0 <= choice <= qty_of_scripts - 1:
            # A valid choice has been made.
            os.system(f"/usr/bin/python3 {os.path.join(script_dir, list_of_scripts[choice])}")
    except ValueError:
        print("Inputted value out of range.")
else:
    print(f"There were no Python scripts in {script_dir}.")
