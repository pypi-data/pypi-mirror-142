def create_new_dir(type):
    '''
    Creates a new directory to store the netlist files
    
    Inputs: Type of netlist file
            (1) two_terminal: netlist file with each port as a terminal to ground
            (2) resistor_terminal: netlist file with a 50 Ohm resistor as port 1 and a terminal to ground as port 2
            (c) SnP: netlist file with a terminal to ground as port 1 and a SnP file block as port 2
    
    Outputs: If the new directory was created or not
    
    Returns: Directory name
    '''
    
    import os
    from datetime import datetime
    
    now = datetime.now()
    date = now.strftime("%Y_%m_%d__%H_%M_%S")
    if type == 1:
        directory = str(f"{date}_two_terminal_netlist_files")
    elif type == 2:
        directory = str(f"{date}_resistor_terminal_netlist_files")
    elif type == 3:
        directory = str(f"{date}_SnP_netlist_files")
    try:
        os.makedirs(directory, exist_ok = True)
        print(f"Directory '{directory}' created successfully")
    except OSError as error:
        print(f"Directory '{directory}' can not be created")
        
    return directory