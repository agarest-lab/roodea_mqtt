#
#Script motore MQTT
#Rossoni Omar
#14/12/2020 inizio operazione a cuore aperto
#

from binascii import unhexlify
import subprocess
import time
import json
import paho.mqtt.client as mqtt
from gpiozero import Button
from gpiozero import LED
import socket
import netifaces as ni
from datetime import datetime
import serial
from time import sleep
import struct
import redis

print ('****************Avvio****************')
lastMessage = 0
# Richiesta IP.
ni.ifaddresses('wlan0')
ipw = ("non connesso")
ipw = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
#ni.ifaddresses('eth0')
#ipl = ("non connesso")
#ipl = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
cont = 0
ser = serial.Serial ("/dev/ttyAMA0", 9600)    #Open port with baud rate
my_string='FF'
cmd1= ("\"")
display_t21= ("t21.txt=")
display_t1= ("t1.txt=")
display_ipw = str(ipw)
#display_ipl = str(ipl)
print ("IPw: ", str(ipw))
#print ("IPl: ", str(ipl))
display_time = (time.strftime("%d/%m/%Y %H:%M:%S "))
r=redis.Redis(host='localhost', port=6379, db=0)
time.sleep(0.0)

display_en_gen = r.set("energy_gen",0)
display_en_feb = r.set("energy_feb",0)
display_en_mar = r.set("energy_mar",0)
display_en_apr = r.set("energy_apr",0)
display_en_mag = r.set("energy_mag",0)
display_en_giu = r.set("energy_giu",0)
display_en_lug = r.set("energy_lug",0)
display_en_ago = r.set("energy_ago",0)
display_en_set = r.set("energy_set",0)
display_en_ott = r.set("energy_ott",0)
display_en_nov = r.set("energy_nov",0)
display_en_dic = r.set("energy_dic",0)

bar_p1 = 0
month = 0
year = 0
print ("DATA: ", time.strftime("%d"), time.strftime("%m"), time.strftime("%Y"))
print ('******* Fine inizializzazione *******')

def on_connect(client, userdata, flags, rc):
    print ("Connected with result code "+str(rc))
    client.subscribe("roodea/power_meter_1")
    client.subscribe("roodea/temp_meter_1")
    #client.subscribe("roodea/temp_meter_2")
    #client.subscribe("roodea/#")
    #display_page_boot()

def on_message(client, userdata, msg):
    if datetime.now().timestamp() - globals()['lastMessage'] > 0.025: #da provare, era 0.05
        globals()['lastMessage'] = datetime.now().timestamp()
        #print ("messaggio= ",msg.topic+" "+str(msg.payload))
        print ("topic= ", msg.topic)
        pacdata = msg.payload
        #print ("pacdata= ",pacdata)
        my_set = json.loads(pacdata)
        #print ('my_set= ',str(my_set))
    on_data(my_set, cont, msg)

def on_data(my_set, cont, msg):
    #print ("on_data")
    #my_set = str(pacdata)
    my_var = []
    my_var1 = []
    global bar_p1
    for x,y in my_set.items():
        #print (x,"=",y)
        x = y
    #print ("setto su redis")
    if msg.topic == "roodea/power_meter_1":
        r.set("time", str(time.strftime("%d/%m/%Y %H:%M:%S ")))
        r.set("ipw", str(ipw))
        r.set("avvio", str(my_set['u_avvio']))
        r.set("temp1", str("%.1f" % (my_set['temp1'])))
        r.set("p1", str("%.1f" % (my_set['p1'])))
        r.set("en1", str("%.1f" % (my_set['en1'])))
        r.set("prev_en1", str("%.1f" % (my_set['prev_en1'])))
        r.set("prev_m_en1", str("%.1f" % (my_set['prev_m_en1'])))
        r.set("pf1", str("%.1f" % (my_set['pf1'])))
        r.set("p1max", str("%.1f" % (my_set['p1max'])))
        r.set("q1", str("%.1f" % (my_set['q1'])))
        r.set("s1", str("%.1f" % (my_set['s1'])))
        r.set("vol1", str("%.1f" % (my_set['vol1'])))
        r.set("cur1", str("%.1f" % (my_set['cur1'])))
        r.set("m_en1", str("%.1f" % (my_set['m_en1'])))
        bar_p1 = int((my_set["p1"])*100/4000)
        r.set("bar_p1", int(bar_p1))
        global year
        global month
        actualyear = int(time.strftime("%Y"))
        #print ("YEAR: ",time.strftime("%Y"))
        actualmonth = int(time.strftime("%m"))
        #print ("MONTH: ",time.strftime("%m"))
        if actualyear > year:
            month = 0
            year = actualyear
        if actualmonth > month:
            if actualmonth == 1:
                 r.set("energy_gen", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 2:
                 r.set("energy_feb", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 3:
                 r.set("energy_mar", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 4:
                 r.set("energy_apr", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 5:
                 r.set("energy_mag", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 6:
                 r.set("energy_giu", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 7:
                 r.set("energy_lug", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 8:
                 r.set("energy_ago", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 9:
                 r.set("energy_set", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 10:
                 r.set("energy_ott", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 11:
                 r.set("energy_nov", str("%.1f" % (my_set['m_en1'])))
            elif actualmonth == 12:
                 r.set("energy_dic", str("%.1f" % (my_set['m_en1'])))
            month = actualmonth

    elif msg.topic == "roodea/temp_meter_1":    #temperatura da temp meter 1
        r.set("t_amb", str(my_set['t_amb']))
        r.set("t_pann", str(my_set['t_pann']))
        r.set("t_ut", str(my_set['t_ut']))
        r.set("t_amb_min", str(my_set['t_amb_min']))
        r.set("t_amb_max", str(my_set['t_amb_max']))
        bar_t_amb = int(((my_set["t_amb"])+30)*100/75)
    '''
    elif msg.topic == "roodea/temp_meter_2":    #temperatura da BME280
        r.set("t_amb", str(my_set['temperature']))
        r.set("t_amb_min", str(my_set['temperature_min']))
        r.set("t_amb_max", str(my_set['temperature_max']))
        r.set("humidity", str(my_set['humidity']))
        r.set("pressure", str(my_set['pressure']))
    '''
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
