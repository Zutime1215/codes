import subprocess as sp
import ips as lst


ip_list = lst.ip_list
for ip in ip_list:
    status,result = sp.getstatusoutput("ping -c1 -w1 " + ip)    

    if status == 0:
        
        print("System " + ip + " is UP !")
    else:
        print("System " + ip + " is DOWN !")
