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
	s1 = net.addswitch('s1')
	s2 = net.addswitch('s2')
	s3 = net.addswitch('s3')
	s4 = net.addswitch('s4')
	s5 = net.addswitch('s5')
	s8 = net.addswitch('s8')
	s9 = net.addswitch('s9')
  	s10 = net.addswitch('s10')
	info( '*** Add host\n')
	h1 = net.addHost('h1', ip='10.0.0.1/24')
	h2 = net.addHost('h2', ip='10.0.0.2/24')
	info( '*** Add Links\n')
	net.addLink(h1, s8)
	net.addLink(h2, s2)
#-------------------------------------------
	net.addLink(s1, s2, cls=TCLink, bw=1)
	net.addLink(s1, s3, cls=TCLink, bw=4)
	net.addLink(s2, s10, cls=TCLink, bw=2)
	net.addLink(s2, s9, cls=TCLink, bw=4)
	net.addLink(s2, s4, cls=TCLink, bw=9)
	net.addLink(s2, s3, cls=TCLink, bw=2)
	net.addLink(s3, s4, cls=TCLink, bw=1)
	net.addLink(s3, s5, cls=TCLink, bw=3)
	net.addLink(s4, s5, cls=TCLink, bw=1)
	net.addLink(s4, s8, cls=TCLink, bw=3)
	net.addLink(s4, s9, cls=TCLink, bw=2)
	net.addLink(s5, s8, cls=TCLink, bw=1)
	net.addLink(s8, s9, cls=TCLink, bw=4)
	net.addLink(s9, s10, cls=TCLink, bw=12)
  
#------------------------------------------
	info( '***starting network\n')
	net.build()
	info( '*** starting controller\n')
	for controller in net.controllers:
		controller.start()
	net.get('s1').start([c0])
	net.get('s2').start([c0])
	net.get('s3').start([c0])
	net.get('s4').start([c0])
	net.get('s5').start([c0])
	net.get('s8').start([c0])
	net.get('s9').start([c0])
	net.get('s10').start([c0])
	
	info( '*** Pos2 configure switches and hosts\n')
	CLI(net)
	net.stop()
	
if __name__ == '__main__':
	setLogLevel( 'info')
	topo=myNetwork()
