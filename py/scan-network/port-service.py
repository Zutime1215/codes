import socket 
import threading

def port_scanner(port):
    try:
        # my_ip_address = socket.gethostbyname(socket.gethostname())   #get user IP address

        my_ip_address = '207.174.214.206'

        #initialize socket 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set a connection timeout
        s.settimeout(0.5)

        #connect to the IP address port number
        s.connect((my_ip_address, port))
        try:
            service = s.recv(2048).decode()  #get the open port banner(if any)
            print(f"Port {port} is open[+] using service {service}")
        except:
            print(f"Port {port} is open [+]")
    except:
        pass


for port in range(0,5536):
    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()