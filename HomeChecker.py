import os
import time
import re
erikDeviceName = "RedmiNote8Pro-phone"
erikMacAdress = '4c-63-71-1b-47-22'
eliseDeviceName = "TBD"
eliseMacAdress = "TBD"
devices = []
valuechanged = 0
count = 0
erikLastConnectedIp = []
eliseLastConnectedIp = []
start_time = time.time()
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
arpAnswer= []
erikHome = 0
eliseHome = 0
while True:
    try:
        for device in os.popen('nmap -sn 192.168.1.190/24'): devices.append(device)
        for device in range (len(devices)):
            if erikDeviceName in devices[device]:
                erikLastConnectedIp = re.findall( r'[0-9]+(?:\.[0-9]+){3}', devices[device])
            if eliseDeviceName in devices[device]:
                eliseLastConnectedIp = re.findall( r'[0-9]+(?:\.[0-9]+){3}', devices[device])
        devices.clear()
        #Erik Ping & ARP
        os.popen("ping %s" % erikLastConnectedIp[0])
        for line in os.popen('arp -a %s' % erikLastConnectedIp[0]): arpAnswer.append(line)
        for line in range (len(arpAnswer)):
            if erikMacAdress in arpAnswer[line]:
                erikHome = 1
        arpAnswer.clear()
        #Elise Ping & ARP
        os.popen("ping %s" % eliseLastConnectedIp[0])
        for line in os.popen('arp -a %s' % eliseLastConnectedIp[0]): arpAnswer.append(line)
        for line in range (len(arpAnswer)):
            if eliseMacAdress in arpAnswer[line]:
                eliseHome = 1
        arpAnswer.clear()

        if erikHome == 1:
            print("Erik connected")
        else:
            print ("Device disconnected")
        if eliseHome == 1:
            print ("Elise connected")
        else:
            print("Elise disconnected")
        erikHome = 0
        eliseHome = 0
        arpAnswer.clear()
    except Exception as error:
        print(error)