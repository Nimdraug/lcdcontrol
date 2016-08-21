# lcdcontrol
Control backlighting on a [Chalkboard Electronics](http://www.chalk-elec.com/) LCD Touch Screen

## usage

```
usage: lcdcontrol [-h] [-s] [-o {state,full,json}] [command]

control backlighting on a Chalkboard Electronics LCD Touch Screen

positional arguments:
    command     command to send to device ( auto, toggle, max, min, +,
                - or backlight level (0 - 18) )
                          
                optional arguments:
                    -h, --help      show this help message and exit
                    -s, --status    display device status
                    -o {state,full,json}, --output {state,full,json}
                                    status output type
```

## notes

this script has only been tested on a [10" LCD Touch Screen](http://www.chalk-elec.com/?page_id=1280#!/10-universal-LCD-with-HDMI-interface-and-capacitive-multi-touch/p/42545413/category=3094861) with single-touch firmware and cannot be guaranteed to work with other devices. testing on other devices would be highly appreciated, tho :D
