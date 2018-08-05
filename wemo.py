from ouimeaux.device import Device

device_ip = '192.168.x.x'

device = Device(f'http://{device_ip}:49153/setup.xml')

def turn_on():
    device.basicevent.SetBinaryState(BinaryState=1)

def turn_off():
    device.basicevent.SetBinaryState(BinaryState=0)
