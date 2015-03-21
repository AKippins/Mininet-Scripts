"""command is 'sudo mn --mac --controller=remote,ip=192.168.56.1 --custom ~/mininet/custom/MaristNetwork.py --topo MaristNetwork' """

from mininet.topo import Topo

class MaristNetwork( Topo ):
	"Marist topology example."

	def __init__( self ):
		"Create custom topo."
		#initialize
		Topo.__init__( self )

		#add
		HA1 = self.addHost( 'HA1' )
		HA2 = self.addHost( 'HA2' )
		HB1 = self.addHost( 'HB1' )
		HB2 = self.addHost( 'HB2' )
		HC1 = self.addHost( 'HC1' )
		HC2 = self.addHost( 'HC2' )
		SA = self.addSwitch( 's2' )
		SB = self.addSwitch( 's3' )
		SC = self.addSwitch( 's4' )
		ADVA = self.addSwitch( 's1' )

		#links
		self.addLink( HA1, SA )
		self.addLink( SA, HA2 )
		self.addLink( ADVA, SA )
		self.addLink( ADVA, SB )
		self.addLink( ADVA, SC )
		self.addLink( HB1, SB )
		self.addLink( SB, HB2 )
		self.addLink( HC1, SC )
		self.addLink( SC, HC2 )
topos = { 'MaristNetwork': ( lambda: MaristNetwork() ) }
