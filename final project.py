
print("------------------------ RANDOM PASSWAORD GENERATOR ------------------------\n\n")

m=1

while m==1:
    strn="qwertyuiopasdfghjklzxcvbnmQAZWSXEDCRFVTGBYHNU?JMIKOLP1478520369@#$%&"             #string declaration
    l2=[]                                                                                   #an empty list
    strn3=""                                                                                #an empty string
    s1={}                                                                                   #an empty set
    
    l1=[]
    print("\n")                                                                             #to change the line
    n=int(input("Enter the length of the passwaord : "))                            #tking input of the length of the new password
    s1= set(strn)                                               #string Type converted to set
    for i in range (n):
        

        l1=list(s1)
    for i in range (n):

        l2.append(l1[i])                        #adding elements to the list
    for x in l2:
        strn3+=x
    print("\n\nThe new generated password is : ",strn3)  #to display new password
    print("\n\n")
    m+=1
    m=int(input("Press 1 to change the length of the password and generate another password or press another key to exit : "))   #inputtng key value to decide the program to continue
    print("\n")
print("                       ~~ ACTION TERMINATED ~~                            \n")
