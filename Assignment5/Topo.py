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
	sS= net.addSwitch('sS')
	sT = net.addSwitch('sT')
	sU = net.addSwitch('sU')
	sV = net.addSwitch('sV')
	sW = net.addSwitch('sW')
	sX = net.addSwitch('sX')
	sY = net.addSwitch('sY')
  sZ = net.addSwitch('sZ')
	info( '*** Add host\n')
	h1 = net.addHost('h1', ip='10.0.0.1/24')
	h2 = net.addHost('h2', ip='10.0.0.2/24')
	info( '*** Add Links\n')
	net.addLink(h1, sX)
	net.addLink(h2, sT)
#-------------------------------------------
	net.addLink(sS, sT, cls=TCLink, bw=1)
	net.addLink(sS, sU, cls=TCLink, bw=4)
  net.addLink(sT, sZ, cls=TCLink, bw=2)
  net.addLink(sT, sY, cls=TCLink, bw=4)
  net.addLink(sT, sV, cls=TCLink, bw=9)
  net.addLink(sT, sU, cls=TCLink, bw=2)
  net.addLink(sU, sV, cls=TCLink, bw=1)
  net.addLink(sU, sW, cls=TCLink, bw=3)
  net.addLink(sV, sW, cls=TCLink, bw=1)
  net.addLink(sV, sX, cls=TCLink, bw=3)
  net.addLink(sV, sY, cls=TCLink, bw=2)
  net.addLink(sW, sX, cls=TCLink, bw=1)
  net.addLink(sX, sY, cls=TCLink, bw=4)
  net.addLink(sY, sZ, cls=TCLink, bw=12)
  
#------------------------------------------
	info( '***Starting network\n')
	net.build()
	info( '*** Starting controller\n')
	for controller in net.controllers:
		controller.start()
	net.get('sS').start([c0])
	net.get('sT').start([c0])
	net.get('sU').start([c0])
	net.get('sV').start([c0])
	net.get('sW').start([c0])
	net.get('sX').start([c0])
	net.get('sY').start([c0])
  net.get('sZ').start([c0])
	
	info( '*** Post configure switches and hosts\n')
	CLI(net)
	net.stop()
	
if __name__ == '__main__':
	setLogLevel( 'info')
	topo=myNetwork()
