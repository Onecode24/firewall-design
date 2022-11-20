#CODE TO CONSTRUCT TOPOLOGY

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch

def topology():

    print ("*** Creation des differents controleur")
    net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
    
    #CREATION DES HOTES
    h1 = net.addHost('h1', mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', mac="00:00:00:00:00:02")
    h3 = net.addHost('h3', mac="00:00:00:00:00:03")
    
    #CREATION DES SWITCHES
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2') 
    s3 = net.addSwitch('s3') 
    
    
    #CREATION DU CONTROLEUR
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633) 
    
    #CREATION DES LINS
    
    net.addLink(h1, s1)  
    net.addLink(h2, s1) 
    net.addLink(h3, s1) 
    net.addLink(s1, s2)
    net.addLink(s3, s2)
    

    #CONSTRUCTION DU RESEAU 
    net.build()	
    c0.start()	
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    
    h1.setIP('192.168.1.1', 24)
    h2.setIP('192.168.1.2', 24)
    h3.setIP('192.168.1.3', 24)
    
    print ("*** Running CLI")
    
    #INVOKING CLI
    CLI(net)
    
    print ("*** Stopping network")
  
		
if __name__ == '__main__':
    setLogLevel('info')
    topology()
