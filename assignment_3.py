'''
It is the day of interview in a company
and the chance is only for first 10 candidates.
The receptionist has the duty of noting the name
and degree of every candidate.
She was using a register book so far but wishes
to switch this task to a computer operation.
So, she requires your Python programming skills
to make a solution for her problem. 

You have to write a program to note the names and degree
of candidates approaching. Also, create a parallel
database (file) in the local machine with this data.
Bring out the best solution!
'''







var="-"
slnoq=[]
nameq=[]
degreeq=[]
slno=0

filename1="C:/Users/Skanda/Desktop/roughfile.txt"

file = open(filename1,"r+")
file. truncate(0)
file. close()
while(True):
    print("Welcome\nPlease Enter your name")
    name=input()
    print("Please Enter your degree details")
    degree=input()
    print("Thank You\n\n")
    if (name==var and degree==var):
        break
    slno+=1
    slnoq.append(slno)
    nameq.append(name)
    degreeq.append(degree)


    
    file=open(filename1,'a')
    
   
    file.write(str(slno))
    file.write(". ")
    file.write(name)
    file.write(" -> ")
    file.write(degree)
    file.write("\n")
    
       
        
    file.close()

    
    

   
 
file=open(filename1,'r')
for i in range(0,10):
    data=file.readline()
    print(data)

file.close()


