import sys
import getopt

# Usage: ArgParsing2.py filename message
filename = sys.argv[1]
message = sys.argv[2]
with open(filename, 'w+') as f:
    f.write(message)

# Usage: ArgParsing2.py -p 8080
# Optional Arguments

opts, args = getopt.getopt(sys.argv[1:], 'f:m:', 'filename:message:')
print(opts)
print(args)

for opt, arg in opts:
    if opt == "-m":
        message = arg
    if opt == "-f":
        filename = arg

with open(filename, 'a') as f:
    f.write("\n"+message)