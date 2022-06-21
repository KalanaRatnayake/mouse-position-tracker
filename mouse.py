import usb.core

idVendorName = 0x10c4
idProductName = 0x8108

dev = usb.core.find(idVendor= idVendorName, idProduct=idProductName)

ep = dev[0].interfaces()[0].endpoints()[0]

i = dev[0].interfaces()[0].bInterfaceNumber

dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()

eaddr = ep.bEndpointAddress

while True:
    try:
        r = dev.read(eaddr, 1024)
        print(r)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
