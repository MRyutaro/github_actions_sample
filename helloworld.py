import datetime
now = datetime.datetime.now()
f = open("sample.txt", "w")
f.write("書き込みました。ねねねね！！！！！！！")
f.write(f"今の時間は{now}です")
f.close()
