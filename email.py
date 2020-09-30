import random
names=["Chirag Singh","Ambrish Singh","Richa Singh","Bruno Singh","Ragini Singh"]


index_email=0   # i have to make it increase

email=[]
for j in range(0,5):
    for i in range(0,len(names)):
        email_choose=random.randint(1,2)
        email_rand_int2=random.randint(10,99)
        email_rand_int4=random.randint(1000,9999)
        x=names[i]
        index=x.find(" ")
        y=x[0:index]
        y=y.lower()
        if(email_choose==1):
            tempemail=y+str(email_rand_int2)+"@gmail.com"
            email.append(tempemail)
        else:
            tempemail=y+str(email_rand_int4)+"@gmail.com"
            email.append(tempemail)
    print(email[index_email])
    index_email+=1
