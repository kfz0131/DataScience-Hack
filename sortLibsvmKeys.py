def sortLibsvmKeys(inputPath,outputPath):
    '''
    This function requires an inputPath string and an outputPath string
    
    The input file must already be in libsvm format as shown below
    
    label key:value key:value key:value .......
    
    The sorted libsvm file will be write to outputPath
    '''
    
    # Initialize line counter
    # count = 0

    # Open input file and output file
    with open(inputPath) as f,open(outputPath,"w") as out:
        # Read lines in input file one by one
        for line in f.readlines():
            # Split the lines
            col = line.split(' ')
            # First column is label
            label = col[0]
            # Initialize an empty diciontary to store current line key-value pairs information
            d = {}
            # Starting from second column are key-value pairs
            for kv in col[1:]:
                # If the current line does not contain any key-value pairs, do nothing
                if(kv == '\n'):
                    next
                # If the current line has key-value pairs
                else:
                    # Split the key and values
                    [k,v] = kv.split(':')
                    # Store key-value information in dictionary
                    d[int(k)] = int(v)
            # If the current line does not contain any key-value pairs, do not write to output file, jump to the next line
            if(len(d) == 0):
                next
            # Sort the dictionary by keys in ascending order
            else:
                sortD = sorted(d.items(), reverse=False)
                # Prepare output string
                output = ''
                # For sorted key-value pairs
                for kv in sortD:
                    k = kv[0]
                    v = kv[1]
                    # Add the current key-value pairs to output string
                    output = output + '{}:{} '.format(k,v)
                # Write the output string to file
                out.write("%s %s\n" %(sex,output.rstrip()))

#             if(count % 1000 == 0):
#                 print("Line {} is done".format(count))

#             count += 1
