from mininet.topo import Topo
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

topos={'mytopo':(lambda:MyTopo())}
