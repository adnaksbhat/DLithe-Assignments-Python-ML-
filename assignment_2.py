'''
'Aroma' Coffee factory has started producing a new blend of coffee.
They want to know the customer feedback for this new variety
that they decided to give people for a try on this coffee.
On this regard, they setup a coffee kiosk in front of
INOX movie theatres intended to deliver a free cup of coffee to
outgoing viewers after the movie.
The only thing people have to do is to remark their rating
after the coffee in a special alphanumeric feedback device available
at the kiosk. The rating is accepted in a scale of 1-5
(Terrible - Tongueblaster). When all people completes giving feedback,
the staff enters a password to see the average rating for the coffee.
'''
#   NOTE:
#   1. Logically, it is not possible to get an initial count of number of people who are willing to drink the coffee
#   2. Some people might leave after having the coffee without marking the feedback
#   3. Rating value is not considered other than 1-5







import math
import time

def coffee(argument): 
    switcher = { 
        
        1: "1 - Terrible", 
        2: "2 - Okay",
        3: "3 - Not Bad",
        4: "4 - Good",
        5: "5 - ToungeBlaster",
        2020: "Staff Forum"
        
    }
    
    return switcher.get(argument, "Invalid")
    

sum=0
response=0
s=2020

while(True):
    
    
    ppl=int(input("         --Give Feedback--\n           Scale: 1 to 5\n           1-(Terrible)\n           2-(Okay)\n           3-(Not Bad)\n           4-(Good)\n           5-(ToungeBlaster)\n---- >"))
    if(ppl<6):
        print("\n          Thanks for your feedback\n\n          ",coffee(ppl),"\n\n")
        time.sleep(5)

        response+=1
        sum+=ppl
        avg=(sum/response)
    
    elif(ppl==s):
        break
    else:
        print("Invalid")




while(True):
    print("Enter password for Staff section")
    passq=str(input("Enter -> "))
    if(passq=="qwerty"):
        print("Average is -> "+str(math.ceil(avg)))
        break
    else:
        print("Invalid Password")
    

