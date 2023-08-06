def two_terminal_netlist_generation(zero_order_file):
    '''
    Function to generate all possible L/C section matching circuits for a user-input order.
    All possible combinations of netlist file of all previous orders will also be generated.
    The netlist files will contain a 50 Ohm terminal to ground as each port.
    
    Inputs: Zero order netlist file
    
    Outputs: All netlist files for each order before and including a user-input order
    
    Returns: None
    '''
    
    import glob
    
    max_order = int(input(f'Enter desired order (integer \u2265 1) -->')) # User input maximum order
    if max_order < 1: # Check if maximum order is positive
        print(f'Must be an integer value \u2265 1')
        max_order = int(input(f'Enter desired order (integer \u2265 1) -->'))
    
    order_count = 1 # count the current order to compare to max_order
    gnd = 0 # ground node is always 0
    node_count = 0 # counter for the nodes, nodes will be N__{node_count}
    l_count = 1 # counter for inductors
    c_count = 1 # counter for capacitors
    
    first_order_items = ["sc", "sl", "pc", "pl"] # list of possible components at first order
    f_head = open(zero_order_file) # Copy header from ADS generated file
    header = f_head.read()
    for item in first_order_items: 
        with open(f"Order_{order_count:02d}_{item}.txt", "w") as f:
            f.write(header)
            if item == "sc": # Write series capacitor file
                f.write(f"C:C{c_count} N__{node_count} N__{node_count+1} C=c{c_count} pF\nc{c_count}=1.0\n")
                f.write(f"Port:TermG2  N__{node_count+1} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                f.close()
            elif item == "sl": # Write series inductor file
                f.write(f"L:L{l_count} N__{node_count} N__{node_count+1} L=l{l_count} nH\nl{l_count}=1.0\n")
                f.write(f"Port:TermG2  N__{node_count+1} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                f.close()
            elif item == "pc": # Write parallel capacitor file
                f.write(f"C:C{c_count} N__{node_count} {gnd} C=c{c_count} pF\nc{c_count}=1.0\n")
                f.write(f"Port:TermG2  N__{node_count} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                f.close()
            elif item == "pl": # Write parallel inductor file
                f.write(f"L:L{l_count} N__{node_count} {gnd} L=l{l_count} nH\nl{l_count}=1.0\n")
                f.write(f"Port:TermG2  N__{node_count} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                f.close()

    order_count += 1 # Increase counter to second order
    
    series_items = ["sc", "sl"] # List of possible series components for higher orders
    parallel_items = ["pc", "pl"] # List of possible parallel components for higher orders
    
    while order_count <= max_order: # Generate netlist files for all orders up to the desired maximum order
        previous_order_files = glob.glob(f"Order_{order_count-1:02d}*") # Find all previous order files
        for file_name in previous_order_files: # Add components to the already generated previous order files
            l_count = int(file_name.count("sl") + file_name.count("pl")) # count inductors in the circuit
            c_count = int(file_name.count("sc") + file_name.count("pc")) # count capacitors in the circuit
            node_count = int(file_name.count("sl") + file_name.count("sc")) # count the nodes in the circuit
            f_head = open(file_name)
            header = f_head.readlines() # Read the previous order file line by line
            if file_name[-6:-4] == "sc" or file_name[-6:-4] == "sl": # Check if the highest order component is in series
                for item in parallel_items: # Write the parallel components
                    with open(f"Order_{order_count:02d}_{file_name[9:-4]}_{item}.txt","w") as f: # Write everything from previous order file 
                        if item == "pc":                                                      # except terminal 2
                            for line in header:
                                if line[0:11] != "Port:TermG2":
                                    f.write(line)
                            f.write(f"C:C{c_count+1} N__{node_count} {gnd} C=c{c_count+1} pF\nc{c_count+1}=1.0\n")
                            f.write(f"Port:TermG2  N__{node_count} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                            f.close()
                        elif item == "pl":
                            for line in header:
                                if line[0:11] != "Port:TermG2":
                                    f.write(line)
                            f.write(f"L:L{l_count+1} N__{node_count} {gnd} L=l{l_count+1} nH\nl{l_count+1}=1.0\n")
                            f.write(f"Port:TermG2  N__{node_count} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                            f.close()
            elif file_name[-6:-4] == "pc" or file_name[-6:-4] == "pl": # Check if the highest order component is in parallel
                for item in series_items: # Write the series components
                    with open(f"Order_{order_count:02d}_{file_name[9:-4]}_{item}.txt","w") as f: # Write everything from previous order file
                        if item == "sc":                                                      # except terminal 2
                            for line in header:
                                if line[0:11] != f"Port:TermG2":
                                    f.write(line)
                            f.write(f"C:C{c_count+1} N__{node_count} N__{node_count+1} C=c{c_count+1} pF\nc{c_count+1}=1.0\n")
                            f.write(f"Port:TermG2  N__{node_count+1} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                            f.close()
                        elif item == "sl":
                            for line in header:
                                if line[0:11] != "Port:TermG2":
                                    f.write(line)
                            f.write(f"L:L{l_count+1} N__{node_count} N__{node_count+1} L=l{l_count+1} nH\nl{l_count+1}=1.0\n")
                            f.write(f"Port:TermG2  N__{node_count+1} {gnd} Num=2 Z=50 Ohm Noise=yes\n")
                            f.close()
        order_count += 1 # Increase the order
        
    print(f"All two-terminal netlist files up to order {max_order:02d} have been created.")