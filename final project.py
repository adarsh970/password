
print("------------------------ RANDOM PASSWAORD GENERATOR ------------------------\n\n")

m=1

while m==1:
    strn="qwertyuiopasdfghjklzxcvbnmQAZWSXEDCRFVTGBYHNU?JMIKOLP1478520369@#$%&"
    l2=[]
    strn3=""
    s1={}
    
    l1=[]
    print("\n")
    n=int(input("Enter the length of the passwaord : "))
    s1= set(strn)
    for i in range (n):
        

        l1=list(s1)
    for i in range (n):

        l2.append(l1[i])
    for x in l2:
        strn3+=x
    print("\n\nThe new generated password is : ",strn3)
    print("\n\n")
    m+=1
    m=int(input("Press 1 to change the length of the password and generate another password or press another key to exit : "))
    print("\n")
print("                       ~~ ACTION TERMINATED ~~                            \n")
