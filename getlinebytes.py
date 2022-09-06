import os
from hurry.filesize import size

total_bytes = -1

with open("MYFILE") as file_in:
    for line in file_in:
        bytes_on_this_line = len(line) + 1
        hrsize = size(bytes_on_this_line)
        print("Row {} Size is {}".format (line,hrsize))
        total_bytes += bytes_on_this_line
