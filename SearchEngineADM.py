# Desenvolvedor: Bl4ck
import os
import urllib
import requests
import socket
import random
from termcolor import *
from time import *
try:
    def banner():
        banners = colored("""
\t\t\t\t ____        _                      _       _____ _            _        \n
\t\t\t\t/ ___| _ __ (_)_ __ _ __   __ _  __| |___  |  ___| | __ _  ___| | _____ \n
\t\t\t\t\___ \| '_ \| | '__| '_ \ / _` |/ _` / __| | |_  | |/ _` |/ __| |/ / __| \n
\t\t\t\t ___) | |_) | | |  | | | | (_| | (_| \__ \ |  _| | | (_| | (__|   <\__ \ \n
\t\t\t\t|____/| .__/|_|_|  |_| |_|\__,_|\__,_|___/ |_|   |_|\__,_|\___|_|\_\___/  \n
\t\t\t\t      |_|                                                                  \n
\t\t\t\t                                 Desenvolvedor:  \n
\t\t\t\t                        ____  _    _  _    ____ _  __\n
\t\t\t\t                       | __ )| |  | || |  / ___| |/ / \n
\t\t\t\t                       |  _ \| |  | || |_| |   | ' / \n
\t\t\t\t                       | |_) | |__|__   _| |___| . \ \n
\t\t\t\t                       |____/|_____| |_|  \____|_|\_\ \n
\t\t\t\t ____                      _       _____             _            
\t\t\t\t/ ___|  ___  __ _ _ __ ___| |__   | ____|_ __   __ _(_)_ __   ___ \n
\t\t\t\t\___ \ / _ \/ _` | '__/ __| '_ \  |  _| | '_ \ / _` | | '_ \ / _ \ \n
\t\t\t\t ___) |  __/ (_| | | | (__| | | | | |___| | | | (_| | | | | |  __/\n
\t\t\t\t|____/ \___|\__,_|_|  \___|_| |_| |_____|_| |_|\__, |_|_| |_|\___|\n
\t\t\t\t                                               |___/   \n           
                         \t\t\t\t    _    ____  __  __ \n
                         \t\t\t\t   / \  |  _ \|  \/  |\n
                         \t\t\t\t  / _ \ | | | | |\/| |\n
                         \t\t\t\t / ___ \| |_| | |  | |\n
                         \t\t\t\t/_/   \_\____/|_|  |_|\n
                         
                \t\t\t\t BUSCADOR DE PAGINAS LOGINS,ADMINS.\n
          \t\t\t\t EXEMPLO DE USO: HTTPS ou HTTP://WWW.SITE.COM.BR\n                       

        ""","green")
        return banners
        
    os.system("clear")
    try:
        print banner()
        site = str(raw_input(" SITE: "))
        url = requests.get(site)
        code = url.status_code
    except Exception:
        print '\nERRO DE SINTAXE'
        raise KeyboardInterrupt
    print banner()

    if code !=200:
        os.system('clear')
        print banner()
        print 'NAO FOI POSSIVEL SE CONECTAR NESTE SITE. '
        raise SystemExit
    else:
        try:
            os.system('clear')
            print banner()
            host = site.replace("http://","")
            ip = socket.gethostbyname(host)
            print 'IP: ',ip,'\n'
        except socket.gaierror:
            print "POR FAVOR NAO COLOCAR / NO FINAL PARA NAO OCORRER ERROS"
    sleep(3)
    links = ['admin.php','login.php','admin','adm.php','adm','phpmyadmin','PMA','pma',
            'phpMyAdmin','dbadmin','mysql','myadmin','phpmyadmin2','phpMyAdmin2','phpMyAdmin-2',
            'php-my-admin','webadmin','cpanel','webmail','log.php','log','login','administracao',
            'administrador','include','database','mail.txt','logins.txt','logins.html','logins.php',
            'mysqli','painel.php','painel.html','painel','administrator','user.html','user.php',
            'users.html','users.php','user.txt','users.txt','wp','wp-admin','wordpress','usuarios.html','usuarios.php',
             'administracion','painel-control','myadmin','acess','acesso','member','membros',
             'clientes','client','cliente','cliente.php','client.php','clientes.php']
    for directory_scan in links:
        new_link = site+"/"+directory_scan
        url2 = requests.get(new_link)
        code2 = url2.status_code

        if code2 ==404:
            print colored("INEXISTENTE "+new_link,"red")
        elif code2 ==403:
            print colored("PROIBIDO 403 "+new_link,"yellow")
        elif code2 ==200:
            print colored('OK Encontrado => '+new_link,"blue")
  
except KeyboardInterrupt:
    print '\nPrograma Interrompido!'