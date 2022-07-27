import fileinput
import re
from zipfile import ZipFile
# ----------------Method 1------------------------
# if we can read line by line and find ipaddress
print('----------------Method 1------------------------')
ipAddress = []
try:
    with open('sample.txt','r') as r:
        fString = r.readlines()
        # regex pattern for ipaddress
        findIpString = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        
        for ip in fString:
            ipAddress.append(findIpString.search(ip)[0])
        print(ipAddress)
except Exception as e:
    print(e)

# ----------------Method 2------------------------
# 
print('----------------Method 2------------------------')
IpAddress = []
for line in fileinput.input(files='sample1.txt'):
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',line)
    if ip:
        for i in ip:
            # print(i)
            IpAddress.append(i)
print(IpAddress)

# for correct ip pattern
# pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

print('----------Excatrct file from zip and read it and agian zip it-------------')
# ----------Excatrct file from zip and read it-------------
# IpAddress1 = []
# zipname = 'demo.zip'
# with ZipFile(zipname,'r') as zip:
#     for info in zip.infolist():
#         print(info.filename)
#         for line in fileinput.input(files=info.filename):
#             ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',line)
#             if ip:
#                 for i in ip:
#                     IpAddress1.append(i+" \n")
#         print(IpAddress1)

#         with open("ipaddressdata.txt",'w') as w:
#             w.writelines(IpAddress1)

#         with ZipFile(info.filename+".zip",'w') as wzip:
#             # add file into zip
#             wzip.write("ipaddressdata.txt")

print("success")