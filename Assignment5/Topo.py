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
	net = Mininet( topo=None,build=False,link=TCLink, ipBase='10.0.0.0/8',autoStaticArp=True)
	info( '*** Adding controller\n')
	c0=net.addController('c0',controller=RemoteController ,port=6633)
	info( '*** Add switches\n')
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	s5 = net.addSwitch('s5')
	s6 = net.addSwitch('s6')
	s7 = net.addSwitch('s7')
  	s8 = net.addSwitch('s8')
	info( '*** Add host\n')
	h1 = net.addHost('h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01')
	h2 = net.addHost('h2', ip='10.0.0.2/24', mac='00:00:00:00:00:02')
	info( '*** Add Links\n')
	net.addLink(h1, s6)
	net.addLink(h2, s2)
#-------------------------------------------
	net.addLink(s1, s2, bw=1)
	net.addLink(s1, s3, bw=4)
	net.addLink(s2, s8, bw=2)
	net.addLink(s2, s7, bw=4)
	net.addLink(s2, s4, bw=9)
	net.addLink(s2, s3, bw=2)
	net.addLink(s3, s4, bw=1)
	net.addLink(s3, s5, bw=3)
	net.addLink(s4, s5, bw=1)
	net.addLink(s4, s6, bw=3)
	net.addLink(s4, s7, bw=2)
	net.addLink(s5, s6, bw=1)
	net.addLink(s6, s7, bw=4)
	net.addLink(s7, s8, bw=12)
  
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
	net.get('s6').start([c0])
	net.get('s7').start([c0])
	net.get('s8').start([c0])
	
	info( '*** Post configure switches and hosts\n')
	CLI(net)
	net.stop()
	
if __name__ == '__main__':
	setLogLevel( 'info')
	topo=myNetwork()
