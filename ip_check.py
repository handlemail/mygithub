from IPy import IP

ips=open("./ips.txt",'r',encoding='UTF-8',errors='ignore').readlines()

games_subnet=["10.110.0.0/16","10.252.0.0/16"]
for i in ips:
    for sub_net in games_subnet:
        if i.strip() in IP(sub_net):
            print(i.strip())

"""
ip = "10.10.8.222"
ip_block = "10.100.8.0/24"
if ip in IPy.IP(ip_block):
    print("true")
else:
    print("false")
    """
