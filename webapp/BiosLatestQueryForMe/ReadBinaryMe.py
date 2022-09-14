import os
import sys

def ME_TXE_Version(Data2):
   Data=Data2
   try:
     Tag = "$MN2"
     Offset = 0
     Size = len(Data)
     Base = Data.find( Tag, 0, Size)
     Offset = 8
     ME_TXE_Version_1 = Data[Base+Offset].encode("hex")
     ME_TXE_Version_2 = Data[Base+Offset+2].encode('hex')
     ME_TXE_Version_3 = Data[Base+Offset+4].encode('hex')
     ME_TXE_Version_4_Low = Data[Base+Offset+6].encode('hex')
     ME_TXE_Version_4_High = Data[Base+Offset+7].encode('hex')
     ME_TXE_Version_4 = ME_TXE_Version_4_High + ME_TXE_Version_4_Low
     FinalVersion = str(int( ME_TXE_Version_1, 16))+ "." + str(int( ME_TXE_Version_2, 16)) + "." + str(int( ME_TXE_Version_3, 16)) + "." + str(int( ME_TXE_Version_4, 16))
     return FinalVersion
   except:
     return "0.0.0.0"

def ReadMeVersion(FilePath):
   f = open(FilePath, "rb")
   try:
     Data = f.read()
     print(ME_TXE_Version(Data))
   finally:
     f.close()

ReadMeVersion(sys.argv[1])
