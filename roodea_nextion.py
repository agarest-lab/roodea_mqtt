#
#Script per display Nextion
#Rossoni Omar
#14/12/2020 inizio operazione a cuore aperto
#

#import smbus2
#import bme280
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
ipw = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
#ni.ifaddresses('eth0')
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
time.sleep(0.05)
#stampo t0
#ser.write(display_t21.encode())
#ser.write(cmd1.encode())
#ser.write(display_ipl.encode())
#ser.write(cmd1.encode())
#ser.write(unhexlify(my_string))
#ser.write(unhexlify(my_string))
#ser.write(unhexlify(my_string))
#time.sleep(0.05)

#stampo t1
ser.write(display_t1.encode())
ser.write(cmd1.encode())
ser.write(display_ipw.encode())
ser.write(cmd1.encode())
ser.write(unhexlify(my_string))
ser.write(unhexlify(my_string))
ser.write(unhexlify(my_string))
time.sleep(0.05)

bar_p1 = 0
bar_t_amb = 0
month = 0
year = 0
print ("DATA: ", time.strftime("%d"), time.strftime("%m"), time.strftime("%Y"))
print ('******* Fine inizializzazione *******')
#display_value(bar_p1, bar_t_amb)

#def display_value(bar_p1, bar_t_amb):
while True:
    print ("display_page_boot")
    #global ip
    ser = serial.Serial ("/dev/ttyAMA0", 9600)    #Open port with baud rate
    print ("seriale aperta")
    #print (ser)
    my_string='FF'
    display_t0= ("t0.txt=")
    display_t1= ("t1.txt=")
    display_t2= ("t2.txt=")
    display_t3= ("t3.txt=")
    display_t4= ("t4.txt=")
    display_t5= ("t5.txt=")
    display_t6= ("t6.txt=")
    display_t7= ("t7.txt=")
    display_t8= ("t8.txt=")
    display_t9= ("t9.txt=")
    display_t10= ("t10.txt=")
    display_t11= ("t11.txt=")
    display_t12= ("t12.txt=")
    display_t13= ("t13.txt=")
    display_t14= ("t14.txt=")
    display_t15= ("t15.txt=")
    display_t16= ("t16.txt=")
    display_t17= ("t17.txt=")
    display_t18= ("t18.txt=")
    display_t21= ("t21.txt=")
    display_t22= ("t22.txt=")
    display_t23= ("t23.txt=")
    display_t24= ("t24.txt=")
    display_t25= ("t25.txt=")
    display_t26= ("t26.txt=")
    display_t27= ("t27.txt=")
    display_t28= ("t28.txt=")
    display_t29= ("t29.txt=")
    display_t30= ("t30.txt=")
    display_t31= ("t31.txt=")
    display_t32= ("t32.txt=")
    display_t60= ("t60.txt=")
    display_t61= ("t61.txt=")
    display_j0= ("j0.val=")
    #display_j1= ("j1.val=")
    r.set("time", str(time.strftime("%d/%m/%Y %H:%M:%S ")))
    #r.set("ipw", str(ipw))
    #r.set("ipl", str(ipl))
    #print (bar)
    #print ("settati campi di stampa")
    cmd1= ("\"")
    #print ("leggo da redis")
    display_time = r.get("time").decode("utf-8")
    display_ipw = r.get("ipw").decode("utf-8")
    display_avvio = r.get("avvio").decode("utf-8")
    display_temp1 = r.get("temp1").decode("utf-8")
    display_p1 = r.get("p1").decode("utf-8")
    display_en1 = r.get("en1").decode("utf-8")
    display_prev_en1 = r.get("prev_en1").decode("utf-8")
    display_prev_m_en1 = r.get("prev_m_en1").decode("utf-8")
    display_pf1 = r.get("pf1").decode("utf-8")
    display_p1max = r.get("p1max").decode("utf-8")
    display_q1 = r.get("q1").decode("utf-8")
    display_s1 = r.get("s1").decode("utf-8")
    display_vol1 = r.get("vol1").decode("utf-8")
    display_cur1 = r.get("cur1").decode("utf-8")
    display_m_en1 = r.get("m_en1").decode("utf-8")
    display_t_amb = r.get("t_amb").decode("utf-8")
    display_t_pann = r.get("t_pann").decode("utf-8")
    display_t_ut = r.get("t_ut").decode("utf-8")
    display_t_amb_min = r.get("t_amb_min").decode("utf-8")
    display_t_amb_max = r.get("t_amb_max").decode("utf-8")
    display_bar_p1 = r.get("bar_p1").decode("utf-8")
    display_en_gen = r.get("energy_gen").decode("utf-8")
    display_en_feb = r.get("energy_feb").decode("utf-8")
    display_en_mar = r.get("energy_mar").decode("utf-8")
    display_en_apr = r.get("energy_apr").decode("utf-8")
    display_en_mag = r.get("energy_mag").decode("utf-8")
    display_en_giu = r.get("energy_giu").decode("utf-8")
    display_en_lug = r.get("energy_lug").decode("utf-8")
    display_en_ago = r.get("energy_ago").decode("utf-8")
    display_en_set = r.get("energy_set").decode("utf-8")
    display_en_ott = r.get("energy_ott").decode("utf-8")
    display_en_nov = r.get("energy_nov").decode("utf-8")
    display_en_dic = r.get("energy_dic").decode("utf-8")
    #setto luminosità in base ad orario
    daylight = ("dims=40")
    nightlight = ("dims=5")
    if int(time.strftime("%H")) >= 8 and int(time.strftime("%H")) <= 22:
        ser.write(daylight.encode())
        ser.write(unhexlify(my_string))
        ser.write(unhexlify(my_string))
        ser.write(unhexlify(my_string))
        time.sleep(0.01)
    else:
        ser.write(nightlight.encode())
        ser.write(unhexlify(my_string))
        ser.write(unhexlify(my_string))
        ser.write(unhexlify(my_string))
        time.sleep(0.01)

    #print ("inizio trasmissione seriale")
    #stampo valore per progress bar potenza
    ser.write(display_j0.encode())
    bar_p1_str = str(display_bar_p1)
    #bar_t_amb_str = str(bar_t_amb)
    ser.write(bar_p1_str.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t0
    ser.write(display_t0.encode())
    ser.write(cmd1.encode())
    ser.write(display_time.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t1

    #ser.write(display_t1.encode())
    #ser.write(cmd1.encode())
    #ser.write(display_ipl.encode())
    #ser.write(cmd1.encode())
    #ser.write(unhexlify(my_string))
    #ser.write(unhexlify(my_string))
    #ser.write(unhexlify(my_string))
    #time.sleep(0.01)
    #print ("stampo cose")
    #stampo t2

    ser.write(display_t2.encode())
    ser.write(cmd1.encode())
    ser.write(display_avvio.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t3

    ser.write(display_t3.encode())
    ser.write(cmd1.encode())
    ser.write(display_temp1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t4

    ser.write(display_t4.encode())
    ser.write(cmd1.encode())
    ser.write(display_p1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t5

    ser.write(display_t5.encode())
    ser.write(cmd1.encode())
    ser.write(display_en1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t6

    ser.write(display_t6.encode())
    ser.write(cmd1.encode())
    ser.write(display_prev_en1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t7

    ser.write(display_t7.encode())
    ser.write(cmd1.encode())
    ser.write(display_prev_m_en1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t8

    #ser.write(display_t8.encode())
    #ser.write(cmd1.encode())
    #ser.write(display_freq.encode())
    #ser.write(cmd1.encode())
    #ser.write(unhexlify(my_string))
    #ser.write(unhexlify(my_string))
    #ser.write(unhexlify(my_string))
    #time.sleep(0.05)
    #print ("stampo cose")
    #stampo t9

    ser.write(display_t9.encode())
    ser.write(cmd1.encode())
    ser.write(display_pf1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t10

    ser.write(display_t10.encode())
    ser.write(cmd1.encode())
    ser.write(display_p1max.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t11

    ser.write(display_t11.encode())
    ser.write(cmd1.encode())
    ser.write(display_q1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t12

    ser.write(display_t12.encode())
    ser.write(cmd1.encode())
    ser.write(display_s1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t13

    ser.write(display_t13.encode())
    ser.write(cmd1.encode())
    ser.write(display_vol1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t14

    ser.write(display_t14.encode())
    ser.write(cmd1.encode())
    ser.write(display_cur1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t15

    ser.write(display_t15.encode())
    ser.write(cmd1.encode())
    ser.write(display_m_en1.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t16

    ser.write(display_t16.encode())
    ser.write(cmd1.encode())
    ser.write(display_t_amb.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t17

    ser.write(display_t17.encode())
    ser.write(cmd1.encode())
    ser.write(display_t_amb_max.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")
    #stampo t18

    ser.write(display_t18.encode())
    ser.write(cmd1.encode())
    ser.write(display_t_amb_min.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)

#inizio stampa energia annuale

    #stampo t21
    ser.write(display_t21.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_gen.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t22
    ser.write(display_t22.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_feb.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t23
    ser.write(display_t23.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_mar.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t24
    ser.write(display_t24.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_apr.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t25
    ser.write(display_t25.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_mag.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t26
    ser.write(display_t26.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_giu.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t27
    ser.write(display_t27.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_lug.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t28
    ser.write(display_t28.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_ago.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t29
    ser.write(display_t29.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_set.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t30
    ser.write(display_t30.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_ott.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t31
    ser.write(display_t31.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_nov.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t32
    ser.write(display_t32.encode())
    ser.write(cmd1.encode())
    ser.write(display_en_dic.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t60
    ser.write(display_t60.encode())
    ser.write(cmd1.encode())
    ser.write(display_t_pann.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    #stampo t61
    ser.write(display_t61.encode())
    ser.write(cmd1.encode())
    ser.write(display_t_ut.encode())
    ser.write(cmd1.encode())
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    time.sleep(0.01)
    #print ("stampo cose")

    print ("fine display boot")
    #return
