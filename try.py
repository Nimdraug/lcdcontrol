import hid
import time

class simple_hid_device( hid.device ):
    vid = None
    pid = None
    name = ''

    @property
    def manufacturer( self ):
        return self.get_manufacturer_string()

    @property
    def product( self ):
        return self.get_product_string()

    @property
    def serial_number( self ):
        return self.get_serial_number_string()

    def open( self ):
        super( simple_hid_device, self ).open( self.vid, self.pid )

class cb_elec_device( simple_hid_device ):
    vid = 0x04d8
    _backlight_on = None
    _autobright_on = None
    _backlight_level = None
    ambient_level = None

    def update( self ):
        self.write( [ 0, 0, 0 ] )
        self.parse_status( self.read( 2 ) )

    def parse_status( self, status ):
        b1, b2 = status

        self._backlight_on = b2 & 128 and True
        self._autobright_on = b2 & 64 and True
        self._backlight_level = b2 & 0b111111
        self.ambient_level = b1

    @property
    def backlight_on( self ):
        if self._backlight_on == None:
            self.update()

        return self._backlight_on

    @property
    def autobright_on( self ):
        if self._autobright_on == None:
            self.update()

        return self._autobright_on

    @property
    def backlight_level( self ):
        if self._backlight_level == None:
            self.update()

        return self._backlight_level

class multitouch_device( cb_elec_device ):
    pid = 0xf724
    name = '7" and 10" multi-touch firmware'

class singletouch_device( cb_elec_device ):
    pid = 0xf723
    name = '7" and 10" single-touch firmware'

class dualLVDS_FullHD_device( cb_elec_device ):
    pid = 0x003f
    name = 'dualLVDS/FullHD+'

for d in hid.enumerate():
    keys = d.keys()
    keys.sort()
    for key in keys:
        print "%s : %s" % (key, d[key] if isinstance( d[key], basestring ) else hex( d[key] ) )
    print ""

try:
    print "Opening device"
    h = singletouch_device()
    h.open()

    print "Manufacturer: %s" % h.manufacturer
    print "Product: %s" % h.product
    print "Serial No: %s" % h.serial_number

    print "Backlight on?", h.backlight_on

    print "Closing device"
    h.close()

except IOError, ex:
    print ex
    print "You probably don't have the hard coded test hid. Update the hid.device line"
    print "in this script with one from the enumeration list output above and try again."

print "Done"
