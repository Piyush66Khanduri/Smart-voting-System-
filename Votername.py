import csv
def name(name):
    file=open('names.csv','r')
    c=0
    file1=csv.reader(file)
    for i in file1:
        for j in i:
            if(j==name):
                return True

    return False

def voterid_identify(id):
    c=0
    file=open('First.csv','r')
    file1=csv.reader(file)
    for i in file1:
        for j in i:
            if(j==id):
                return True
    return False
def done(c):
    print("You voted",c)