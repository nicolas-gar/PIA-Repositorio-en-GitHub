
import nmap

escaner = nmap.PortScanner()
scaner.scan('192.168.1.4','1-1024','-v-sV')
scaner.command_line() 
scaner.all_hosts()
scaner['192.168.1.4'].state() 
scaner['192.168.1.4'].all_protocols() 
scaner['192.168.1.4']['tcp'].keys() 
scaner['192.168.1.4'].has_tcp(21) 
scaner['192.168.1.4'].has_tcp(22)
print(escanner['192.168.1.4']['tcp'][22])
print(escanner['192.168.1.4']['tcp'][22]['product'])

#Nombre: Nicolás Alberto Garza Galicia 
#Matricula: 1998776