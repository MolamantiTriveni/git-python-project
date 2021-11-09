from pymongo import MongoClient
#client object
client=MongoClient('127.0.0.1',27017)
db=client['kits']
c=db["ml"]


#insert data
k=input("enter msg")
dummy={"msg":k}
c.insert_one(dummy)



#to check data is insertednor not
for i in c.find():
	pass
else:
	print(i)
#to print only msg
for i in c.find():
	pass
else:
	print(i['msg'])