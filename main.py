def voter_id():
    import csv
    import random
    import string
    c1=""
    file=open('First.csv','w')
    col=["List Of Voters::"]
    file=csv.DictWriter(file,fieldnames=col)
    file.writeheader()
    for i in range(0,4000):
        z=random.randint(345000,1033345)
        c1=c1+(str(z))
        #c1+="".join(random.choices(string.ascii_letters+string.digits+str(z)))
        if(len(c1)==8):
            file.writerow({col[0]:c1})
            c1=""
            print(".\t")
