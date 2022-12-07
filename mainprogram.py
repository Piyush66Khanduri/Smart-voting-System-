import Votername
import voter_image
n=input("Enter your name::-\n")
password="****"
c=Votername.name(n)
if(c==False):
    print("Sorry name not in Voter list")
    quit(0)
else:
    id=input("Enter your voter id::-\n")
    c=Votername.voterid_identify(id)
    if(c==False):
        print("Sorry Wrong Voter id::-\n")
        quit(0)
    else:
        c=voter_image.voter_identification(n)
        if(c==True):
            pt1=0
            pt2=0
            pt3=0
            choose_party=input("For  BJP Enter B J P::\nEnter C O N G for Congress::\nEnter A A P for AAp::-\n")
            if(choose_party=="B J P"):
                pt1+=1
                Votername.done(choose_party)
            elif(choose_party=="C O N G"):
                pt2+=1
                Votername.done(choose_party)
            elif(choose_party=="A A P"):
                pt3+=1
                Votername.done(choose_party)
            else:
                print("No Party of such name::-\n")
                quit(0)
            pas=input("To see the results enter password else enter space::-\n")
            if(pas==password):
                print("Results are::\n")
                print("BJP::- ",pt1,"\nCongress::- ",pt2,"\nAAP::- ",pt3)
                quit(0)
            else:
                print("Thankyou Mr/Mrs.",n)
                quit(0)
        else:
            print("Either you are not the  person or your picture is not clear.\n")
            quit(0)
