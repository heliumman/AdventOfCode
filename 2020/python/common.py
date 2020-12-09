def readFile(filename):

    lines = []

    in_file = open(filename, 'r') 
    
    for line in in_file: 
        lines.append(line.strip())
    
    return lines
    
    in_file.close() 