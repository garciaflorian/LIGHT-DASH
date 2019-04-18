import re
import serial

def cleanSerial(data):
    try:
        data = data.decode()        #Convert into string
        data = data.strip('\n\r')   #Clean
        data = data.split(" ")      #Convert into array
        line = []
        if(len(data) >= 2):
            line.append(data[0])
            line.append(data[1])
        else:
            line.append("")
            line.append("")
        return line
    except:
        print("error with :"+str(data))
        line = []
        line.append("")
        line.append("")
        return line

def linkyParsing(serialName):
    serialObj = serial.Serial(serialName, 1200, parity=serial.PARITY_EVEN, bytesize=7)
    
    line_list = cleanSerial(serialObj.readline())   #Read a line

    while(line_list[0]!="MOTDETAT"):
        line_list = cleanSerial(serialObj.readline())

    while True:
        info = {}
        info[line_list[0]] = line_list[1]

        line_list = cleanSerial(serialObj.readline())
        while(line_list[0]!="MOTDETAT"):
            info[line_list[0]]=line_list[1]
            line_list = cleanSerial(serialObj.readline())
        
        if(int(info["MOTDETAT"])==0):
            break
        
    return info


#print(linkyParsing("COM5"))

        
        

