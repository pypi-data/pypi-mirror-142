def move_to_dir(directory):
    '''
    Moves netlist files to the new directory
    
    Inputs: Directory the netlist files need to be moved to
    
    Outputs: Files that cannot be copied correctly
    
    Returns: None
    '''
    
    import glob
    import shutil
    
    path = "C:/Users/Phillip/Circuit_generation/Automation/Automatic_netlist_generation"
    netlist_files = glob.glob("*sc.txt") + glob.glob("*sl.txt") + glob.glob("*pc.txt") + glob.glob("*pl.txt")
    for file in netlist_files:
        with open(f"{file}") as f:
            f.close()
        source = f"{path}/{file}"
        destination = f"{path}/{directory}"
        try:
            dest = shutil.move(source, destination, copy_function = shutil.copytree)
        except:
            print(f"{file} could not be moved into new directory")