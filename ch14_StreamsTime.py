__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/6/16'
__revision__ = '$'
__revision_date__ = '$'



from Class14.streamsExample import streamExample, parseArguenents, \
    optionalParser



#streamExample()

#parseArguenents()
optionalParser()




#
#
# #!/usr/bin/python
#
# # import io module
# import io
#
# print("StringIO : ")
# f = open("myfile.txt", "r", encoding="utf-8")
# f = io.StringIO("some initial text data")
# print("Get Value : ", f.getvalue())
# f.close()
#
# print("\nBytesIO : ")
# f = open("myfile.jpg", "rb")
# f = io.BytesIO(b"some initial binary data: \x00\x01")
# print("Get Buffer : ", f.getbuffer())
# print("Get Value : ", f.getvalue())
# f.close()
#
# print("\nUnbufferedIO : ")
# f = open("myfile.jpg", "rb", buffering=0)
# print("Get Value : ", f.readall)
# f.close()
#
#
# import time
#
# print("strftime with gmtime : ",time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
#
# print("strptime : ", time.strptime("30 Nov 00", "%d %b %y"))
