import re
with open('C:\\verilog_file.sv', 'r') as file:
    file_content = file.read()
# port[0] is input|output|inout, port[1] is reg|wire|logic, port[2] is width, port[3] is name
port_pattern = r"\n\s*(input|output|inout)\s+(reg|wire|logic)?\s*(\[\d+:\d+\])?\s+(\w+)\s*"
ports = re.findall(port_pattern, file_content)
len_longest_name = 0
for port in ports:
    name_len = len(port[3])
    if name_len > len_longest_name:
        len_longest_name = name_len
for port in ports:
    # white_space goes after name, before parenthesis
    white_space = (len_longest_name - len(port[3]) + 1) * " "
    # input and inout are 5 characters in width, output is 6 characters
    if (len(port[0]) == 5):
        print("." + port[3] + white_space + "()," + 10 * " " + "\\\\ " + port[0] + "  " + port[2])
    else:
        print("." + port[3] + white_space + "()," + 10 * " " + "\\\\ " + port[0] + " " + port[2])
