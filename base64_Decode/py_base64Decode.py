import base64
f_base64String = open ("i_base64_String.txt", "r")
coded_string = f_base64String.read()
#print(coded_string)
#print("****")
coded_str_stripped = coded_string.strip()
#print(coded_str_stripped)
#print("****")
fl = open("o_base64_decoded_binary","wb")
print(base64.b64decode(coded_str_stripped))
fl.write(base64.b64decode(coded_str_stripped))
fl.close()
f_base64String.close()