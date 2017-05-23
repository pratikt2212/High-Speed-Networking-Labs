from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSController
from mininet.link import TCLink
import multiprocessing
import time
import sys
class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')
		host4 = self.addHost('h4')
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')

		self.addLink(host1,switch1,bw=10,delay='2ms')
		self.addLink(host2,switch1,bw=20,delay='10ms')
		self.addLink(switch1,switch2,bw=20,delay='2ms',loss=10)
		self.addLink(host3,switch2,bw=10,delay='2ms')
		self.addLink(host4,switch2,bw=20,delay='10ms')

#topos={'mytopo':(lambda:MyTopo())}
def f1():
		
	h3 = net.get('h3')
	h1 = net.get('h1')

	print h3.cmd('iperf -s &')
	print h1.cmd('iperf -c 10.0.0.3 -i 0.5 -t 20')
	 
def f2():

	
	h4 = net.get('h4')
	h2 = net.get('h2')
	print h4.cmd('iperf -s &')
	time.sleep(10)
	print h2.cmd('iperf -c 10.0.0.4 -i 0.5 -t 20')
	net.stop()
if __name__ == '__main__':
	setLogLevel('info')
	topo = MyTopo()
        net = Mininet(topo = topo, controller = OVSController,link = TCLink)
	net.start()
	h1 = multiprocessing.Process(name='f1',target = f1)
	h1.f1 = True
	h2 = multiprocessing.Process(name='f2',target = f2)
	h2.f2 = False

	h1.start()
	h2.start()

