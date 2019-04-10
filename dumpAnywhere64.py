import idautils 
import idaapi
import sys

print ("dumpAnywhere64 by GeoSn0w (@FCE365)")

if len(sys.argv) != 3:
    print ("[i] Usage example: dumpAnywhere64(\"/Users/GeoSn0w/Desktop/file.bin\", 0xFFFFFF, 64)")
def dumpAnywhere64(where, address, size):
    extractedBinary = idc.GetManyBytes(address, size)
    print ("[i] Will extract " + str(size) + " bytes from " + str(address) + " and will save to " + str(where))
    with open(where, "wb+") as file:
     try:
        file.write(extractedBinary)
        print ("[i] Successfully extracted binary data")
     except IOError:
        print ("[!] Failed to extract binary data! Could not write file.")
