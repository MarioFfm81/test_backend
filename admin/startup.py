import datetime
file = open("testfile.txt","w")
file.write(str(datetime.datetime.now()))
file.close()