
import nmap
escaner = nmap.PortScanner()
opcion = int(input("""Bienvenido al menú nmap, seleccione la opción que desea
                    1. Escaneo UDP
                    2. Escaneo completo
                    3. Detectar sistema operativo
                    4. Escaneo de red con  ping
                    """))
if opcion == 1:
    ip = input("Direccion ip a escanear: ")
    puerto1 = input("Ingrese el puerto con el que desea comenzar el escaneo: ")
    puerto2 = input("Ingrese el puerto con el que desea terminar el escaneo: ")
    print("Iniciando escaneo UDP......")
    escaner.scan(ip, puerto1 + '-' + puerto2, '-sU')
    for host in escaner.all_hosts():       
        print('Host : %s (%s)' % (host,escaner[host].hostname()))   
        print('State : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 
            print('protocol : %s' % proto )                     
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                 
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if opcion ==2:
    ip = input("Direccion ip a escanear: ")
    print("Iniciando escaneo completo....")
    escaner.scan(ip)
    for host in escaner.all_hosts():       
        print('Host : %s (%s)' % (host,escaner[host].hostname()))    
        print('State : %s' % escaner[host].state())                  
        for proto in escaner[host].all_protocols():                  
            print('-----------------------------------------------------')
            print('protocol : %s' % proto )                    
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                 
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if opcion==3:
    ip = input("Ingrese la direccion ip a escanear: ")
    scan_raw_result = escaner.scan(ip, arguments='-v -n -A')
    
    for host, result in scan_raw_result['scan'].items():
        if result['status']['state'] == 'up':
            for os in result['osmatch']:
                print('El sistema operativo es:' + os['name'] + ' ' * 3)
if opcion ==4:
    ip=input("Ingrese la ip que desea escanear: ")
    #
    escaner.scan(hosts=ip, arguments='-sP')
    print("Iniciando escaneo con ping...")
    for host in escaner.all_hosts():       
        print('---------------------------------------------------------')
        print('Host : %s (%s)' % (host,escaner[host].hostname()))   
        print('State : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 
            print('-----------------------------------------------------')
            print('Protocolo : %s' % proto )                    
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                  
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))


#Nombre: Nicolás Alberto Garza Galicia
#Matricula: 1998776
