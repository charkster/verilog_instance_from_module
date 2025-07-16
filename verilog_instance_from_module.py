import re
with open('C:\\temp\\jhelum_rtl_snapshot\\dig_core.sv', 'r') as file:
    file_content = file.read()
port_pattern = r"\n\s*(input|output|inout)\s+(reg|wire|logic)?\s*(\[\d+:\d+\])?\s+(\w+)\s*"
ports = re.findall(port_pattern, file_content)
len_longest_name = 0
for port in ports:
    name_len = len(port[3])
    if name_len > len_longest_name:
        len_longest_name = name_len
for port in ports:
    white_space = (len_longest_name - len(port[3]) + 1) * " "
    if (len(port[0]) == 5):
        print("." + port[3] + white_space + "()," + 10 * " " + "\\\\ " + port[0] + "  " + port[2])
    else:
        print("." + port[3] + white_space + "()," + 10 * " " + "\\\\ " + port[0] + " " + port[2])
