# import re
#
# fw=open('inp1.txt','r+')
# fw.write('hi\n')
# fw.write('hello\n')
# fw.write('how are you')
# fw.seek(0)
# out=fw.read()
# # print(fw.mode)
# # print(fw.name)
# # print(fw.closed)
#
# out1=re.search(r'\d+',out)
# if out1:
#     print(out1.group())


import re

fw = open('inp1.txt', 'r+')
fw.write('hi\n')
fw.write('hello\n')
fw.write('how are you')
fw.write('how are youfsfs')

# Move the file pointer back to the beginning before reading
fw.seek(0)

out = fw.read()

# Use findall to find digits
out1 = re.findall(r'\d+', out)
# Check if any digits were found and print them
if out1:
    print(out1)  # Just print the list, no need for .group()

# Close the file to release resources
fw.close()

