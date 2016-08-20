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

    def backlight_toggle( self ):
        self.write( [ 0, 0, 16 ] )

        self.parse_status( self.read( 2 ) )

    @property
    def autobright_on( self ):
        if self._autobright_on == None:
            self.update()

        return self._autobright_on

    def autobright_toggle( self ):
        self.write( [ 0, 0, 2 ] )

        self.parse_status( self.read( 2 ) )

    @property
    def backlight_level( self ):
        if self._backlight_level == None:
            self.update()

        return self._backlight_level

    @backlight_level.setter
    def backlight_level( self, level ):
        self.write( [ 0, 0, 32, level ] )

        self.parse_status( self.read( 2 ) )

    def backlight_max( self ):
        self.write( [ 0, 0, 4 ] )

        self.parse_status( self.read( 2 ) )

    def backlight_min( self ):
        self.write( [ 0, 0, 8 ] )

        self.parse_status( self.read( 2 ) )

    def backlight_dec( self ):
        self.write( [ 0, 0, 64 ] )

        self.parse_status( self.read( 2 ) )

    def backlight_inc( self ):
        self.write( [ 0, 0, 128 ] )

        self.parse_status( self.read( 2 ) )

class multitouch_device( cb_elec_device ):
    pid = 0xf724
    name = '7" and 10" multi-touch firmware'

class singletouch_device( cb_elec_device ):
    pid = 0xf723
    name = '7" and 10" single-touch firmware'

class dualLVDS_FullHD_device( cb_elec_device ):
    pid = 0x003f
    name = 'dualLVDS/FullHD+'

supported_devices = [
    multitouch_device,
    singletouch_device,
    dualLVDS_FullHD_device
]

def find_supported_device():
    for d in hid.enumerate():
        for dev in supported_devices:
            if dev.vid == d['vendor_id'] and dev.pid == d['product_id']:
                return dev
    else:
        raise Exception, 'No supported device found!'

try:
    print "Opening device"
    h = singletouch_device()
    h.open()

    print "Manufacturer: %s" % h.manufacturer
    print "Product: %s (%s)" % ( h.product, h.name )
    print "Serial No: %s" % h.serial_number

    h.backlight_level = 10

    print "Backlight on?", h.backlight_on
    print "Backlight Level", h.backlight_level
    print "Auto Brightness on?", h.autobright_on
    print "Ambient Light Level", h.ambient_level

    time.sleep( 2 )

    h.backlight_max()

    print "Closing device"
    h.close()

except IOError, ex:
    print ex
    print "You probably don't have the hard coded test hid. Update the hid.device line"
    print "in this script with one from the enumeration list output above and try again."

print "Done"
