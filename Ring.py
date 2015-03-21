from mininet.topo import Topo

class Ring( Topo ):
	"Ring topology example."
    
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
        HD1 = self.addHost( 'HD1' )
        HD2 = self.addHost( 'HD2' )
        HE1 = self.addHost( 'HE1' )
        HE2 = self.addHost( 'HE2' )
        HF1 = self.addHost( 'HF1' )
        HF2 = self.addHost( 'HF2' )
        HG1 = self.addHost( 'HG1' )
        HG2 = self.addHost( 'HG2' )
        HH1 = self.addHost( 'HH1' )
        HH2 = self.addHost( 'HH2' )
        SwitchA = self.addSwitch( 'SA' )
        SwitchB = self.addSwitch( 'SB' )
        SwitchC = self.addSwitch( 'SC' )
        SwitchD = self.addSwitch( 'SD' )
        SwitchE = self.addSwitch( 'SE' )
        SwitchF = self.addSwitch( 'SF' )
        SwitchG = self.addSwitch( 'SG' )
        SwitchH = self.addSwitch( 'SH' )

		#links
        self.addLink( SA, SB )
        self.addLink( SB, SC )
        self.addLink( SC, SD )
        self.addLink( SD, SE )
        self.addLink( SE, SF )
        self.addLink( SF, SG )
        self.addLink( SG, SH )
        self.addLink( SH, SA )
        self.addLink( SA, HA1 )
        self.addLink( SA, HA2 )
        self.addLink( SB, HB1 )
        self.addLink( SB, HB2 )
        self.addLink( SC, HC1 )
        self.addLink( SC, HC2 )
        self.addLink( SD, HD1 )
        self.addLink( SD, HD2 )
        self.addLink( SE, HE1 )
        self.addLink( SE, HE2 )
        self.addLink( SF, HF1 )
        self.addLink( SF, HF2 )
        self.addLink( SG, HG1 )
        self.addLink( SG, HG2 )
        self.addLink( SH, HH1 )
        self.addLink( SH, HH2 )
topos = { 'Ring': ( lambda: Ring() ) }
