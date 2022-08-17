import serial
import re

ser = serial.Serial('COM14', 9600)
print(ser.name)
s = ser.read_all().decode('utf-8')
print(s)


def filterData(rawS):
    # s = "Humidity: 79.00%  Temperature: 31.30C 88.34F  Heat index: 41.52C 106.74F"
    if len(rawS) < 48:
        print(rawS)
        return
        
    humid = re.findall(r'\d{2}.\d{2}%', rawS)[0].split('%')[0]
    print("Humidity: ", humid)

    temp = re.findall(r'\d{2}.\d{2}C', rawS)[0].split('C')[0]
    print("Temperature: ", temp)

    return (humid, temp)

# send commend to the MCU
# wait for 2s until respond comes to the serial buffer
# read the respond from the serial buffer
# extract temperature and humidity from the response

def load_data():
    try:       
        ser.write(bytes('%a%\n', 'utf-8'))
        ser.flush()
        s = ser.read_all().decode('utf-8')
        print(s)
        (humid, temp) = filterData(s)
    except Exception as e:
        print(e)
        print("Problem with the com port. Please check it and connect again...")
        s = "Humidity: 00.00%  Temperature: 00.00C 88.34F  Heat index: 41.52C 106.74F"
        (humid, temp) = filterData(s)
    
    return (humid, temp)

def sendCommend(msg):
    try:
        # s = ser.read_all().decode('utf-8')
        # print(s)
        # ser.flush()
        ser.write(bytes(msg, 'utf-8'))
        ser.flush()
    except Exception as e:
        print(e)

def readData():
    s = ""
    try:
        s = ser.read_all().decode('utf-8')
        # print(s)
    except Exception as e:
        print(e)
    
    return s
    
    










   