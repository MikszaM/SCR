import serial

ser = serial.Serial('/dev/rfcomm1',19200,timeout=5)
file = open("/home/pi/temp.txt","w")
#print(ser.name)
print("cos")
ser.write('i')

a=ser.read(1)
b=ser.read(1)
c=ser.read(1)
d=ser.read(1)
e=ser.read(1)

if e!=' ':
    print a+b+c+d#+u"\u00b0"+'C'
    file.write(a+b+c+d+' ')
else:
    print a+b+c+d+e#+u"\u00b0"+'C'
    file.write(a+b+c+d+e+' ')


ser.write('o')

a=ser.read(1)
b=ser.read(1)
c=ser.read(1)
d=ser.read(1)
e=ser.read(1)

if e!=' ':
    print a+b+c+d#+u"\u00b0"+'C'
    file.write(a+b+c+d+' ')
else:
    print a+b+c+d+e#+u"\u00b0"+'C'
    file.write(a+b+c+d+e+' ')
ser.close
file.close()
