import os
import sys, getopt

def creds_to_env():
    paths = {
        "input" : os.path.expanduser("~/.aws/credentials"),
        "output" : ""
    }

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["input=","output="])
    except getopt.GetoptError:
        print ('creds-to-env -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('creds-to-env -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            paths['input'] = arg
        elif opt in ("-o", "--output"):
            paths["output"] = arg

    if (not os.path.exists(paths["input"])):
        print (f'Input file {paths["input"]} does not exist.')
        sys.exit()
    elif (not os.path.isfile(paths["input"])):
        print (f'Input file {paths["input"]} cannot be a directory.')
        sys.exit()

    if (not paths["output"]):
        paths["output"] = os.path.splitext(paths["input"])[0] +  '.env'
    elif (not os.path.isdir(os.path.dirname(paths["output"]))):
        print (f'Output folder {os.path.dirname(paths["output"])} does not exist.')
        sys.exit()
    elif (os.path.isdir(paths["output"])):
        basename = os.path.basename(os.path.splitext(paths["input"])[0]) + '.env'
        paths["output"] = os.path.join(paths["output"], basename)

    print (f'Reading credentials from {paths["input"]}')
    print (f'Writing credentials to {paths["output"]}')

    with open(paths["input"], 'r') as creds:
        with open(paths["output"], 'w') as modified:
            lines = creds.readlines()
            for row in lines:
                row = row.strip()
                if (len(row) > 0):
                    parts = row.strip().split('=',2)
                    if (len(parts) == 1):
                        modified.write(row + '\n')
                    else:
                        key = parts[0].strip().upper()
                        val = parts[1].strip()
                        line = (f'{key}={val}\n')
                        modified.write(line)

    print ('Completed')