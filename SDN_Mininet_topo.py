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
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	s5 = net.addSwitch('s5')
	s6 = net.addSwitch('s6')
	info( '*** Add host\n')
	h1 = net.addHost('h1', ip='10.0.0.1')
	h2 = net.addHost('h2', ip='10.0.0.2')
	h3 = net.addHost('h3', ip='10.0.0.3')
	h4 = net.addHost('h4', ip='10.0.0.4')
        h5 = net.addHost('h5', ip='10.0.0.5')
        h6 = net.addHost('h6', ip='10.0.0.6')
	h7 = net.addHost('h7', ip='10.0.0.7')
	info( '*** Add Links\n')
	net.addLink(h1, s1)
	net.addLink(h2, s2)
	net.addLink(h3, s5)
	net.addLink(h4 ,s5)
	net.addLink(h5, s6)
	net.addLink(h6, s4)
	net.addLink(h7, s4)
#-------------------------------------------
	net.addLink(s1, s2, cls=TCLink, bw=10)
	net.addLink(s1, s3, cls=TCLink, bw=10)
	net.addLink(s1, s5, cls=TCLink, bw=5)
	net.addLink(s2, s4, cls=TCLink, bw=15)
	net.addLink(s3, s4, cls=TCLink, bw=5)
	net.addLink(s4, s6, cls=TCLink, bw=10)
	net.addLink(s5, s6, cls=TCLink, bw=5)
#------------------------------------------
	info( '***Starting network\n')
	net.build() 
	info( '*** Starting controller\n')
	for controller in net.controllers:
		controller.start()
	net.get('s1').start([c0])
	net.get('s2').start([c0])
	net.get('s3').start([c0])
	net.get('s4').start([c0])
	net.get('s5').start([c0])
	net.get('s6').start([c0])

	info( '*** Post configure switches and hosts\n')
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info')
	topo=myNetwork()
