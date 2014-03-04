from ctypes import c_byte
from struct import *
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep, localtime, strftime

import PyFacadeMaps

#Set the socket parameters
host = "localhost"
port = 0000
buf = 1024
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

packageSize = 5;		#///< size of a package (address+color)
nrAddresses = 1085;   #///< total number of packages;
offsetRed = 2;		#///< offset of red color in package
offsetGreen = 3;		#///< offset of green color in package
offsetBlue = 4;		#///< offset of blue color in package

frameBuffer = (c_byte * (nrAddresses * packageSize))()

def sendFrame(frameBuffer):
  if(UDPSock.sendto(frameBuffer,addr)):
    print "Sending message '",frameBuffer,"'....."
    
def rotateBar(rotationTime, colorList):
  
  addressBuffer = []
  
  totalNumberOfColumns =
  MainStreetLevelFutureLabConnectDic['nrColumns']
  + MainSouthAndStreetLevelDic['nrColumns']
  + MainNorthDic['nrColumns']
  + MainWestDic['nrColumns']
  + FuturelabEastDic['nrColumns']
  + FuturelabNorthDic['nrColumns']
  
  sleepTime = float(rotationTime) / float(totalNumberOfColumns)  
  
  for col in range (0, MainSouthAndStreetLevelDic['nrColumns']):
    for row in range(MainSouthAndStreetLevelDic['startRow'], MainSouthAndStreetLevelDic['endRow'] + 1):    

      address = MainSouthAndStreetLevelDic[str(row)][col]
      if (address <> -1):

        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)

    colorOff((addressBuffer[0], addressBuffer[-1]))
  
  addressBuffer = []
  
  for col in range (0, MainStreetLevelFutureLabConnectDic['nrColumns']):
    for row in range(MainStreetLevelFutureLabConnectDic['startRow'], MainStreetLevelFutureLabConnectDic['endRow'] + 1):    

      address = MainStreetLevelFutureLabConnectDic[str(row)][col]
      if (address <> -1):

        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)
    colorOff((MainSouthAndStreetLevelDic['startAddr'], MainSouthAndStreetLevelDic['endAddr']))
    colorOff((FuturelabSouthDic['startAddr'], FuturelabSouthDic['endAddr']))
    colorOff((addressBuffer[0], addressBuffer[-1]))
    
  addressBuffer = []
  
  for col in range (0, FuturelabEastDic['nrColumns']):
    for row in range(FuturelabEastDic['startRow'], FuturelabEastDic['endRow'] + 1):    

      address = FuturelabEastDic[str(row)][col]
      if (address <> -1):

        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)

    colorOff((addressBuffer[0], addressBuffer[-1]))
    
  addressBuffer = []
  
  for col in range (0, FuturelabNorthDic['nrColumns']):
    for row in range(FuturelabNorthDic['startRow'], FuturelabNorthDic['endRow'] + 1):    

      address = FuturelabNorthDic[str(row)][col]
      if (address <> -1):

        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)

    colorOff((addressBuffer[0], addressBuffer[-1]))

  addressBuffer = []
  
  for col in range (0, MainNorthDic['nrColumns']):
    for row in range(MainNorthDic['startRow'], MainNorthDic['endRow'] + 1):    

      address = MainNorthDic[str(row)][col]
      if (address <> -1):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)
    
    colorOff((MainNorthDic['startAddr'], MainNorthDic['endAddr']))

  addressBuffer = []

  for col in range (0, MainWestDic['nrColumns']):
    for row in range(MainWestDic['startRow'], MainWestDic['endRow'] + 1):    
      #print MainSouthDic[str(row)][col]
      address = MainWestDic[str(row)][col]
      if (address <> -1):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
        frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
        frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        addressBuffer.append(address)
    sendFrame(frameBuffer)
    sleep(sleepTime)

    colorOff((addressBuffer[0], addressBuffer[-1]))
    
    addressBuffer = []

def drawSign (signList, colorList):
  for address in signList:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
    frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
    
  sendFrame(frameBuffer)

def wholeColorIn(inTime, colorList):

  colorList = colorProtect (colorList)
  sleepTime = float(inTime) / float(255)
  
  for i in range(1, 255):
    for address in range(0, 1084):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(i)
        frameBuffer[address*packageSize + offsetGreen] = c_byte(i)
        frameBuffer[address*packageSize + offsetBlue] = c_byte(i)
    
    sendFrame(frameBuffer)
    sleep(sleepTime)
    
def wholeColorOut(outTime, colorList):
  
  colorList = colorProtect (colorList)
  sleepTime = float(outTime) / float(255)
  
  for i in range(255, 1, -1):
    for address in range(0, 1084):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(i)
        frameBuffer[address*packageSize + offsetGreen] = c_byte(i)
        frameBuffer[address*packageSize + offsetBlue] = c_byte(i)
    
    sendFrame(frameBuffer)
    sleep(sleepTime)

def wholeGlowIn(glowTime, maxBrightness):

  sleepTime = float(glowTime) / float(maxBrightness)

  for i in range(1, maxBrightness):
    for address in range(0, 1084):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(i)
        frameBuffer[address*packageSize + offsetGreen] = c_byte(i)
        frameBuffer[address*packageSize + offsetBlue] = c_byte(i)
    sendFrame(frameBuffer)
    sleep(sleepTime)

def wholeGlowOut(glowTime, maxBrightness):
  
  sleepTime = float(glowTime) / float(maxBrightness)
  
  for i in range(maxBrightness, 1, -1):
    for address in range(0, 1084):
        frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
        frameBuffer[address*packageSize + 1] = c_byte(address / 256)
        frameBuffer[address*packageSize + offsetRed] = c_byte(i)
        frameBuffer[address*packageSize + offsetGreen] = c_byte(i)
        frameBuffer[address*packageSize + offsetBlue] = c_byte(i)
    sendFrame(frameBuffer)
    sleep(sleepTime)

def pulseGlowSign (signList, pulseTime, timesToGlow, maxBrightness, stepBrightness):
  
  # timeToGlow * (maxBrightness / stepBrightness) * sleepTime * 2 = pulseTime 
  
  sleepTime = float(pulseTime * stepBrightness) / float(timesToGlow * maxBrightness * 2)
  
  for i in range (1, timesToGlow):
    
    for j in xrange(1, maxBrightness, stepBrightness):

      glowSign(signList, j)

      sleep(sleepTime)
    
    for j in reversed(xrange(1, maxBrightness, stepBrightness)):

      glowSign(signList, j)

      sleep(sleepTime)

def pulseGlowSignMulti (signList1, signList2, signList3, signList4, pulseTime, timesToGlow, maxBrightness, stepBrightness):
  
  # timeToGlow * (maxBrightness / stepBrightness) * sleepTime * 2 = pulseTime 
  
  sleepTime = float(pulseTime * stepBrightness) / float(timesToGlow * maxBrightness * 2)
  
  for i in range (1, timesToGlow):
    
    for j in xrange(1, maxBrightness, stepBrightness):

      glowSign2(signList1, signList2, signList3, signList4, j)
      sleep(sleepTime)
    
    for j in reversed(xrange(1, maxBrightness, stepBrightness)):

      glowSign2(signList1, signList2, signList3, signList4, j)
      sleep(sleepTime)


def glowSign (signList, glowLevel):
  
  for address in signList:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(glowLevel)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(glowLevel) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(glowLevel)
    
  sendFrame(frameBuffer)

def glowSign2 (signList1, signList2, signList3, signList4, glowLevel):
  
  for address in signList1:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(glowLevel)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(glowLevel) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(glowLevel)
    
  for address in signList2:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(glowLevel)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(glowLevel) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(glowLevel)
    
  for address in signList3:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(glowLevel)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(glowLevel) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(glowLevel)
    
  for address in signList4:
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(glowLevel)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(glowLevel) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(glowLevel)
    
  sendFrame(frameBuffer)

def colorProtect(colorList):
  # Don't let the LEDs go totally off. Might damage them.
    if colorList[0]== 0:
      colorList[0] = 1
    
    if colorList[1] == 0:
      colorList[1] = 1
    
    if colorList[2] == 0:
      colorList[2] = 1
      
    return (colorList)

def colorOff(rangeTuple):
  for address in range(rangeTuple[0], rangeTuple[1]+1):
    frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
    frameBuffer[address*packageSize + 1] = c_byte(address / 256)
    frameBuffer[address*packageSize + offsetRed] = c_byte(1)
    frameBuffer[address*packageSize + offsetGreen] = c_byte(1) 
    frameBuffer[address*packageSize + offsetBlue] = c_byte(1)
  
  sendFrame(frameBuffer)

def colorFillSide(sideDic, colorList):
  
  colorList = colorProtect (colorList)
  
  for address in range(sideDic['startAddr'], sideDic['endAddr'] + 1):
    if (address <> -1):
      frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
      frameBuffer[address*packageSize + 1] = c_byte(address / 256)
      frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
      frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
      frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])

  sendFrame(frameBuffer)
  
def colorFill(list, colorList):

  colorList = colorProtect (colorList)
  
  for address in list:
    if (address <> -1):
      frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
      frameBuffer[address*packageSize + 1] = c_byte(address / 256)
      frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
      frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
      frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])

  sendFrame(frameBuffer)

def fillRows(sideDic, topRow, bottomRow, colorList):
      
      colorList = colorProtect (colorList)
            
      if (bottomRow > sideDic['endRow']):
        bottomRow = sideDic['endRow']
      if (topRow < sideDic['startRow']):
        topRow = sideDic['startRow']
      
      for row in range(topRow, bottomRow + 1):
        for address in sideDic[str(row)]:
          if (address <> -1):
            frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
            frameBuffer[address*packageSize + 1] = c_byte(address / 256)
            frameBuffer[address*packageSize + offsetRed] = c_byte(colorList[0])
            frameBuffer[address*packageSize + offsetGreen] = c_byte(colorList[1]) 
            frameBuffer[address*packageSize + offsetBlue] = c_byte(colorList[2])
        
      sendFrame(frameBuffer)

def calcFillRows(value, valueTotal):
  
  valuePerRow = float(valueTotal / 27)
  
  rowNumber = value / valuePerRow
  
  return int(rowNumber + 1)

def glowIn(maxBrightness):

  for address in range(0, 1084):
      frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
      frameBuffer[address*packageSize + 1] = c_byte(address / 256)
      frameBuffer[address*packageSize + offsetRed] = c_byte(maxBrightness)
      frameBuffer[address*packageSize + offsetGreen] = c_byte(maxBrightness)
      frameBuffer[address*packageSize + offsetBlue] = c_byte(maxBrightness)
  sendFrame(frameBuffer)

def glow(minBrightness, maxBrightness, sleepTime):

  for address in range(0, 1084):
      frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
      frameBuffer[address*packageSize + 1] = c_byte(address / 256)
      frameBuffer[address*packageSize + offsetRed] = c_byte(maxBrightness)
      frameBuffer[address*packageSize + offsetGreen] = c_byte(maxBrightness)
      frameBuffer[address*packageSize + offsetBlue] = c_byte(maxBrightness)
  sendFrame(frameBuffer)
  
  sleep(sleepTime)
  
  for address in range(0, 1084):
      frameBuffer[address*packageSize + 0] = c_byte(address % 256) 
      frameBuffer[address*packageSize + 1] = c_byte(address / 256)
      frameBuffer[address*packageSize + offsetRed] = c_byte(minBrightness)
      frameBuffer[address*packageSize + offsetGreen] = c_byte(minBrightness)
      frameBuffer[address*packageSize + offsetBlue] = c_byte(minBrightness)
  sendFrame(frameBuffer)

######## BEGIN MAIN ############

# Sample values for positive and negative sentiment analysis in text.
valuePositive = 3.06
valueNegative = 2.10

valueTotal = valuePositive + valueNegative  

# 20 seconds 
wholeColorIn(20, [128, 128, 128])

# sudden glow sync (3 times)
for i in range(0, 3):
  glow(0, 255, 1)
  sleep(1)

# 10 seconds
wholeColorOut(10, [128, 128, 128])

# 513 seconds
for k in range (0, 3):
  
  colorOff((0, 1084))
  
  fillRows(MainSouthDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(MainWestDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(MainEastDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(MainNorthDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(MainSouthAndStreetLevelDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(MainSouthStreetLevelDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(FuturelabSouthDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(FuturelabEastDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  fillRows(FuturelabNorthDic, 27 - calcFillRows(valuePositive, valueTotal), 27, [0, 255, 0])
  
  drawSign(plusSignMainSouth, [255, 255, 255])
  drawSign(plusSignMainNorth, [255, 255, 255])
  drawSign(plusSignMainWest, [255, 255, 255])
  drawSign(plusSignMainEast, [255, 255, 255])
  
  # 60 seconds
  
  pulseGlowSignMulti (plusSignMainSouth, plusSignMainNorth, plusSignMainWest, plusSignMainEast, 65, 20, 255, 10)
  
  # 3 seconds
  sleep(3)
  colorOff((0, 1084))
  
  # 15 seconds
  for i in range (0, 3):
    rotateBar(5, [255, 254, 255])
    
  fillRows(MainSouthDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(MainWestDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(MainEastDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(MainNorthDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(MainSouthAndStreetLevelDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(MainSouthStreetLevelDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(FuturelabSouthDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(FuturelabEastDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  fillRows(FuturelabNorthDic, 27 - calcFillRows(valueNegative, valueTotal), 27, [255, 0, 0])
  
  drawSign(minusSignMainSouth, [255, 255, 255])
  drawSign(minusSignMainNorth, [255, 255, 255])
  drawSign(minusSignMainWest, [255, 255, 255])
  drawSign(minusSignMainEast, [255, 255, 255])
  
  # 60 seconds
  pulseGlowSignMulti (minusSignMainSouth, minusSignMainNorth, minusSignMainWest, minusSignMainEast, 65, 20, 255, 10)

  # 3 seconds
  sleep(3)
  colorOff((0, 1084))
  
  # 30 seconds
  if (k < 2):
    for i in range (0, 3):
      rotateBar(5, [255, 255, 255])

# 3 seconds
sleep(3)

# 10 seconds
wholeColorIn(10, [128, 128, 128])
# 10 seconds
wholeColorOut(20, [128, 128, 128])

# Close socket
UDPSock.close()
