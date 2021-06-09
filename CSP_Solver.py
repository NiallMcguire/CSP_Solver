# -*- coding: utf-8 -*-
import copy
"""
Created on Mon May 24 12:05:03 2021

@author: niall


"""


def Start():
    x = 0
    Arcs = []
    Domains = {}
    print("\nHello and Welcome to the CSP_Solver")
    while x != "0":
        print("\n######################################")
        print("\nCurrent Domains: ", Domains)
        print("Current Arcs: ", Arcs)
        
        print("\n1.How to use!")
        print("2.Enter Domain")
        print("3.Enter Constraints")
        print("4.Print Domains")
        print("5.Run AC3")
        print("0.Exit")
        x = input("\nPlease select one of the above:")
        if(x == "1"):
            HowToUse()         
        if(x == "2"):
            Domains = EnterDomains() 
        if(x == "3"):
            Arcs = EnterConstraints()
        if(x == "4"):
            print("\n######################################\n")
            for k,v in Domains.items():
                print(k ,"=", [v])
        if(x == "5"):
            print("\n######################################")
            Domains = AC3(Arcs, Domains) 
            print("\nFINISHED!!!", Domains)
            print("\nYour Domains after running the AC3 algorithm are as follows:\n- ", Domains)
                                                                                                                                                                                                                                                                                                                                                                        

def HowToUse():
    print("\n######################################")
    print("HOW TO USE THE CSP SOLVER")
    print("\nTo begin, there are three main sections in the CSP solver")
    print("\nDomains:")
    print("Domains contain the information that the constraints will act apon.\nWhen you select the Enter Domain option it will prompt you to give the domain a UNIQUE name followed by the contents of the domain seperated by a comma.\ne.g. X1 is the name, 1,2,3 are the contents.")
    print("\nConstraints:")
    print("Constraints are the rules that you wish to make the Domains fit into.\nWhen you select the Enter Constraints option it will ask you to enter a constrain in the following format:\n'Name of constraint 1' 'operator' 'Name of constraint 2'.\nThe Constraints support the operators '>' '<' '=' '!='\nAn example input would be as follows 'X1 < X2'.")
    print("\nAC3:")
    print("Once you have entered all of your Domains and Constraints you can then select the AC3 algorithm.\nThis algorithm will apply all of your Constraints to your Domains and give you a final output of Domains that fit the Constraints\ne.g. Constraint: X1 > X2, Domain: X1 = [1,2,3] X2 = [1,2,3] Output: X1 = [2,3] X2 = [1,2]")
    
    
def AC3(Arcs, Domains):
    #print(Arcs)
    
    Agenda = copy.copy(Arcs)
    x = 0    
   
    while Agenda != []:
        Changed = False
        #print(Domains)
        #print(Agenda)        
        current_arc = Agenda[x]
        
        ArcData = getDataFromArc(current_arc)
        #print(ArcData)
        
        DomainOne = Domains[ArcData[0]]
        DomainOne = list(DomainOne.split(","))
        
        
        DomainTwo = Domains[ArcData[1]]
        DomainTwo = list(DomainTwo.split(","))
                
        #print(DomainOne)
        #print(DomainTwo)
        
        if(DomainOne == [''] or DomainTwo == ['']):
            Agenda = []
            break
        
        #print(DomainTwo)
                
        if(ArcData[2] == ">"):
            for i in range(0, len(DomainOne)):
                #print("\n"+DomainOne[i])
                for z in range(0, len(DomainTwo)):
                    #print(DomainTwo[z])                   
                    if(int(DomainOne[i]) > int(DomainTwo[z])):
                        #print("True")
                        break
                    elif(z == len(DomainTwo)-1):
                        #print("remove " + DomainOne[i])
                        DomainOne[i] = None
                        Changed = True
                    
        if(ArcData[2] == "<"):
            for i in range(0, len(DomainOne)):
                #print("\n"+DomainOne[i])
                for z in range(0, len(DomainTwo)):
                    #print(DomainTwo[z])                   
                    if(int(DomainOne[i]) < int(DomainTwo[z])):
                        #print("True")
                        break
                    elif(z == len(DomainTwo)-1):
                        #print("remove " + DomainOne[i])
                        DomainOne[i] = None
                        Changed = True
        
        if(ArcData[2] == "=="):
            for i in range(0, len(DomainOne)):
                #print("\n"+DomainOne[i])
                for z in range(0, len(DomainTwo)):
                    #print(DomainTwo[z])                   
                    if(int(DomainOne[i]) == int(DomainTwo[z])):
                        #print("True")
                        break
                    elif(z == len(DomainTwo)-1):
                        #print("remove " + DomainOne[i])
                        DomainOne[i] = None
                        Changed = True
                        
                        
        if(ArcData[2] == "!="):
            for i in range(0, len(DomainOne)):
                #print("\n"+DomainOne[i])
                for z in range(0, len(DomainTwo)):
                    #print(DomainTwo[z])                   
                    if(int(DomainOne[i]) != int(DomainTwo[z])):
                        #print("True")
                        break
                    elif(z == len(DomainTwo)-1):
                        #print("remove " + DomainOne[i])
                        DomainOne[i] = None
                        Changed = True
                        
        
        DomainOne = list(filter(None, DomainOne))
        DomainOne = ",".join(DomainOne)
        Domains[ArcData[0]] = DomainOne

        del Agenda[0]
                        
        if(Changed == True):  
            for c in range(0, len(Arcs)):
                SearchData = getDataFromArc(Arcs[c])
                if(SearchData[1] == ArcData[0]):
                    if(Arcs[c] not in Agenda):
                        Agenda.append(Arcs[c])
        
        
        
    #print(DomainOne)    
    #print(DomainTwo)
    #print(Domains)
    return Domains

    
def getDataFromArc(x):
    A1 = x.find('<')
    A2 = x.find('>')
    A3 = x.find('==')
    A4 = x.find('!=')
    
    if(A1!=-1):
        var1 = x[:A1]
        var2 = x[A1+1:]        
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")    
        return(var1,var2,"<")               
            
    if(A2!=-1):
        var1 = x[:A2]
        var2 = x[A2+1:]     
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")    
        return(var1,var2,">")  
           
    if(A3!=-1):
        var1 = x[:A3]
        var2 = x[A3+2:]   
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")    
        return(var1,var2,"==")  

    if(A4!=-1):
        var1 = x[:A4]
        var2 = x[A4+2:]    
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")    
        return(var1,var2,"!=")  

        

def EnterDomains():    
    Domains = {}
    x = 0
    while x != "2":
        print("\n######################################")
        print("Current Domains: ", Domains)
        print("\n1. add new Domain")
        print("2. continue with current Domains")
        x = input("\nPlease select one of the above: ")
        if(x == "1"):
            k=input("Please enter the name of the domain: ")
            v=input("Please enter the conents of the domain (seperated by comma): ")
            Domains[k] = v                
    return Domains

  
def EnterConstraints():
    Constraints = []
    x = 0
    Arcs = []
    
    while x != "2":
        print("\n######################################")
        print("Current Constraints: ", Constraints)
        print("\n1. add new Constraint")
        print("2. continue with current Constraints")
        x = input("\nPlease select one of the above: ")
        if(x == "1"):
            constraint = input("please enter your constraint: ")
            Constraints.append(constraint)
       
    Arcs = GenArcs(Constraints)
    return Arcs
    
    
def GenArcs(Constraints):
    Arcs = []
    print("\n######################################")
    print("\nGenerating arcs from given constraints")
    for x in Constraints:
        Arcs.append(x)
        Arcs.append(ReverseConstraint(x))
    for x in Arcs:
        print(x)

    return Arcs

def ReverseConstraint(x):
    A1 = x.find('<')
    A2 = x.find('>')
    A3 = x.find('==')
    A4 = x.find('!=')
    
    if(A1!=-1):
        var1 = x[:A1]
        var2 = x[A1+1:]        
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")       
        newArc = var2 + " > " + var1
        return(newArc)
                
    if(A2!=-1):
        var1 = x[:A2]
        var2 = x[A2+1:]        
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")        
        newArc = var2 + " < " + var1
        return(newArc)
           
    if(A3!=-1):
        var1 = x[:A3]
        var2 = x[A3+2:]       
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")       
        newArc = var2 + " == " + var1
        return(newArc)

    if(A4!=-1):
        var1 = x[:A4]
        var2 = x[A4+2:]        
        var1 = var1.replace(" ", "")
        var2 = var2.replace(" ", "")        
        newArc = var2 + " != " + var1
        return(newArc)




Start()

