import random
import subprocess

def mac():
    generate = "" 
    for  i in range(0,6) :
         
         generate = generate + ":" + hex(random.randint(0,255)) [2:]
    return generate [1:]
    
       
def main() :
    macaddr = mac()
    subprocess.call("ifconfig eth0 down", shell=True)
    subprocess.call("ifconfig eth0 hw ether macaddr", shell=True)
    subprocess.call("ifconfig  eth0 up", shell=True)
main()    
       