import hid
import time

class cb_elec_device( hid.device ):
    vid = 0x04d8

class multitouch_device( cb_elec_device ):
    pid = 0xf724
    name = '7" and 10" multi-touch firmware'

class singletouch_device( cb_elec_device ):
    pid = 0xf723
    name = '7" and 10" single-touch firmware'

class singletouch_device( cb_elec_device ):
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
    h = hid.device()
    h.open(0x461, 0x20)
    #h.open(0x1941, 0x8021) # Fine Offset USB Weather Station

    print "Manufacturer: %s" % h.get_manufacturer_string()
    print "Product: %s" % h.get_product_string()
    print "Serial No: %s" % h.get_serial_number_string()

    # try non-blocking mode by uncommenting the next line
    #h.set_nonblocking(1)

    # try writing some data to the device
    for k in range(10):
        for i in [0, 1]:
            for j in [0, 1]:
                h.write([0x80, i, j])
                d = h.read(5)
                if d:
                    print d
                time.sleep(0.05)

    print "Closing device"
    h.close()

except IOError, ex:
    print ex
    print "You probably don't have the hard coded test hid. Update the hid.device line"
    print "in this script with one from the enumeration list output above and try again."

print "Done"
