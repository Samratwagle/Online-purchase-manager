#!§Samrat wagle3§!

import sys

items=[]     #products storage
items_price=[]  #price of each products storage

samsung=["tv 200💲","washing machine 300💲","fridge 400💲"] 

sam_prod=["tv","washing machine","fridge"] # items of sam (samsung)store

dico={"tv":200,"washing machine":300,"fridge":400,"iphone":1000,"ipad":600,"imac":800,"car":2000000,
"bus":100000,"jeep":50000}

appel=["iphone 1000💲","ipad 600💲","imac 800💲"] #products of app(appel) store
app_prod=["iphone","ipad","imac"]
renault=["car 2000000💲","bus 100000💲","jeep 50000💲"] #products of tata store
ren_prod=["car","bus","jeep"]


print('')
print("")

budget=int(input("enter your budget 💲-------> "))    #asking client budget


print(budget)

print('')

def storef(user_choice):
    
    cmpt=0
    while user_choice!="Samsung" and user_choice!="Renault" and user_choice!="Appel": #check if the store name entered by client is valid
                                                                               #if not we ask him again to enter a valid store name
        print("!! invalide store")
        user_choice=input("Please enter a valide store:  ")

    return user_choice

user_choice=input("select a store,---Appel,---Samsung,---Renault ------->  ") #passing store names to the parameter
storef(user_choice)

print("")
red='\033[34m'

##########################################################################################################################################


def choices():
    #alerting => client
    print("<<<<<Note: PLz dont input unwanted keywords(ex.ygfygu ,ygye) else you will be permanently blocked from this site!!!>>>>>")
    print("")
    check=0

    if user_choice=="Appel":
        print(appel)
        print("")
        print(red+"welcome \033[34mto Appel store")
        print("")
        print("")
        print("")
        user_selection=input("chose an item : ")  #asking client to choose some  items
        print("")
     
          
        while user_selection not in app_prod:
            print("please chose valide product")
            print("")

            user_selection=input("chose an item : ")
            check+=1
            if check>2:
                print("we think you are not here for buying  :) !!! Get lost !")
                exit()

        print("")
        price=dico[user_selection]  #asking seller the price of items selected by client
        
        items_price.append(price)    #stocking prices in the list
        items.append(user_selection)  #stocking selected items in another list 
        print("items in your bucket----------->",items) 
        print("")
        print("selected items price --------------->",items_price)

    elif user_choice=="Samsung":      
        
        """  same logics are  applide in remaning conditions""" 
        print(samsung)
        print("")
        print(">>>>>welcome to Samsung store<<<<<<")
        print("")
        print("")
        print("")
        user_selection=input("chose an item  ")

        print("")
      
        while user_selection not in sam_prod:
            print("!!!!please chose valide product!!!")
            print("")
            user_selection=input("chose an item : ")
            check+=1
            if check>2:
                print("-------->we think you are not here for buying  :) ! Get lost !")
                exit()
              
        print("")
        price=dico[user_selection]
       
        items_price.append(price)
        items.append(user_selection)
        
        print("items in your bucket-------------->",items)
        print("")
        print("selected items price----------------->",items_price)
    
    else:
        print(renault)
        print("")
        print("welcome to Renault show room")
        print("")
        print("")
        print("")
        user_selection=input("chose an item  ")
        print("")
       
        while user_selection not in ren_prod:
            print("please chose valide product")
            print("")
            user_selection=input("chose an item : ")
            check+=1
            if check>2:
                print("we think you are not here for buying  :) !!! Get lost !")
                exit()
        print("")
        price=dico[user_selection]
        items_price.append(price)
        items.append(user_selection)   

        print("items in your bucket------------->",items)
        print("")
        print("selected items price-------------------->",items_price)
    return items_price
choices()


print("")
####################################################################################################################################



def calcul():
    
    total=0 
    for elem in items_price:  #browsing the liste to get all prices of the items selected
        
        total+=elem #total prices of items selected
        total+=  0.13*total 
    #adding tax
    
    print("your total with tax ---------->",total ,"💲")
    if budget <total:
     
        print("you don't have enough money to buy this product :(")
    return total
calcul()
print("")
##########################################################################################################################

def recall():
    bud=calcul()
    if budget-bud<0:
        print(">>>>>sorry you dont have enough money to buy it!!!!!<<<<<<<<<<")
        exit()
        print("")
        
    else:
        budget- bud>0
        print("you have now----->",budget-bud,"💲") #substracting total budget of client with **>money  spend at the store
        print("")
    
        buy_again=input("would you like to buy more stuffs from this store?  : y/n  : ") #asking client that if he want to continue buying
        
        if buy_again=="n":


            storef(user_choice)
            
    
        else:
             buy_again=="y"#if he say yes and if he have enough money he can continue buying else back to main menu
             choices()
             calcul()
             recall()
        
    




recall()
 #######################################################################################################################################   

#!§§!


