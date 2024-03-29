from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCLink

def myNetwork():
	net = Mininet( topo=None,build=False, ipBase='10.0.0.0/8',autoStaticArp=True)
	info( '*** Adding controller\n')
	c0=net.addController('c0',controller=OVSController,port=6633)
	info( '*** Add switches\n')
	s9 = net.addSwitch('s9')
	s10 = net.addSwitch('s10')
	s11 = net.addSwitch('s11')
	s12 = net.addSwitch('s12')
	s13 = net.addSwitch('s13')
	s14 = net.addSwitch('s14')
	s15 = net.addSwitch('s15')
	info( '*** Add host\n')
	h1 = net.addHost('h1', ip='10.0.1.10/24')
	h2 = net.addHost('h2', ip='10.0.1.11/24')
	h3 = net.addHost('h3', ip='10.0.1.12/24')
	h4 = net.addHost('h4', ip='10.0.1.13/24')
	h5 = net.addHost('h5', ip='10.0.2.10/24')
	h6 = net.addHost('h6', ip='10.0.2.11/24')
	h7 = net.addHost('h7', ip='10.0.2.12/24')
	h8 = net.addHost('h8', ip='10.0.2.13/24')
	h9 = net.addHost('h9', ip='10.0.1.1/24')
	h10 = net.addHost('h10', ip='10.0.2.1/24')
	info( '*** Add Links\n')
	net.addLink(h1, s11)
	net.addLink(h2, s11)
	net.addLink(h3, s12)
	net.addLink(h4 ,s12)
	net.addLink(h5, s14)
	net.addLink(h6, s14)
	net.addLink(h7, s15)
	net.addLink(h8, s15)
	net.addLink(h9, s9)
	net.addLink(h10, s9)
#-------------------------------------------
	net.addLink(s9, s10)
	net.addLink(s9, s13, cls=TCLink, bw=20)
	net.addLink(s10, s11)
	net.addLink(s10, s12)
	net.addLink(s13, s14, cls=TCLink, bw=20, delay='5ms')
	net.addLink(s13, s15)
#------------------------------------------
	info( '***Starting network\n')
	net.build()
	info( '*** Starting controller\n')
	for controller in net.controllers:
		controller.start()
	net.get('s9').start([c0])
	net.get('s10').start([c0])
	net.get('s11').start([c0])
	net.get('s12').start([c0])
	net.get('s13').start([c0])
	net.get('s14').start([c0])
	net.get('s15').start([c0])
	
	info( '*** Post configure switches and hosts\n')
	CLI(net)
	net.stop()
	
if __name__ == '__main__':
	setLogLevel( 'info')
	topo=myNetwork()
