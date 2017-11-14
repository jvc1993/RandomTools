import bincopy

binfile = bincopy.BinFile()

binfile.add_srec_file("filename.s19")

target = open("fileName.hex", 'w')


target.write(binfile.as_ihex(16))

target.close()