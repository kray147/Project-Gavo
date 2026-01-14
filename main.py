from itertools import permutations,product,combinations
import time
import os
import random
import sys
from termcolor import colored
import dumper



########################################################
#THIS IS WHERE YOU CHOOSE THE ENGLISH OR FRENCH DATASET

filetoread="englishdata.csv" #or "frenchdata.csv" if you want the french version

##########################################################

def loading_animation(total_iterations):
    for i in range(1, total_iterations + 1):
        progress_bar = "-" * i
        spaces = " " * (total_iterations - i)
        loading_text = f"{progress_bar}{spaces}"
        print(loading_text, end="\r")
        time.sleep(0.01)
    print("\n")


def mix(table):
    tableinf=[]
    for i in range(1,5):
        for combo in combinations(table, i):
            for perm in permutations(combo):
                tableinf.append(''.join(perm))
    
    return tableinf

def caps(table):
    for i in range(len(table)):
        if table[i].isalpha() :
            table.append(table[i].upper())
            

    return table
    

def pluscara(table):
    print("Do you wish to add basic characters like '1,2,3,4,5,6,7,8,9,!,_,-' ? [y/n]:")
    base=input()
    if base=="y":
        table.extend(["1","2","3","4","5",'6',"7","8","9","!","_","-"])
        return table
    elif base!="n":
        print("Wrong answer, type a valid answer! \n")
        pluscara(table)
    return table

def wordlist(bucle,wd):
    crit="/quit"
    
    if(wd == []):
        print(f"Type the words you want to mix up, when you're finished type '{crit}' ")
        i=1
        stopval=0
        while stopval != crit:
            print(f"word n°{i}: ")
            ask=input()
            if ask!=crit:
                wd.append(ask)
            stopval=ask
            i=i+1
        
        wd=pluscara(wd)
        print(wd)
        print("Done, creating the list... \n")
    
    wd=caps(wd)
    fin=mix(wd)


    print(f"Name the output file (add .txt at the end): ")
    filename=input()
    dir=os.path.dirname(__file__)
    path = os.path.join(dir, filename)
    file=open(path,"w+")
    for i in range(len(fin)):
        file.write(fin[i]+"\n")
    file.close()

    print("\n Done !")
    print("Returning to main menu :)")
    time.sleep(0.5)
    loading_animation(50)
    if bucle=="":
        __main__()
    return filename



def opt5():
    wdg = str(input("Which file would you use to mix-shake ?:\n"))

    """
    dir=os.path.dirname(__file__)
    path = os.path.join(dir, wdg)
    file=open(path,"r")
"""


    os.chdir(os.path.dirname(__file__))
    file=open(wdg, mode="r",encoding='utf8')
    #file.readline()
    data=[]  
    for line in file:
        
        reader=line #.split("\n")
        #print(reader)
        data.append(reader.strip("\n"))
        
    file.close()
    print("\n")
    #print(data)
    wordlist("", data)

    return 0





def passw(passa,patha):
    if passa=="":
        print("What password do you choose ?")
        print("Type 'quit' if you wanna go back to main menu")
        ask=str(input())
        if ask=="quit":
            __main__()
    else:
        ask=passa
    if patha=="":
        ff=input("What dictionnary do u wanna use ?: ")
    else:
        ff=patha
    dir=os.path.dirname(__file__)
    path = os.path.join(dir, ff)
    
    if not os.path.exists(path):
        print(f"The file {ff} does not exist. Don't forget to put your dictionary in the same directory as this program ! \n")
        time.sleep(5)
        __main__()

    file=open(path,"r+")
    temp=[]
    for line in file:
        line=line.strip()
        temp.append(line)
    file.close()
    
    i=0
    g=-5
  
    for i in range(len(temp)):
        if temp[i]==ask:
            g=i
            time.sleep(1)
            print("Password Cracked!")
            print(f"It's {temp[g]}")
            loading_animation(50)
            __main__()
            return
        
    
    print("No luck :(")
    time.sleep(5)
    print("")
    loading_animation(50)
    __main__()


def help():
    print("""\nAn important thing to know is that you can change whether you want people to be generated
in French (my mother tongue) or in English. Profiles are generated in english by default.
You can do so by changing the csv file used in the "gavo.py" file at line 10.
          """)
    ask=input("Type enter to go back to main menu !\n")
    if ask!=None:
        __main__()

def animation():
    # Définit le texte à afficher
    texte = r"""
______                                 
| ___ \                                
| |_/ /_ _ ___ ___     __ _  ___ _ __  
|  __/ _` / __/ __|   / _` |/ _ \ '_ \ 
| | | (_| \__ \__ \  | (_| |  __/ | | |
\_|  \__,_|___/___/   \__, |\___|_| |_|
                ______ __/ |           
               |______|___/                         
                    """

    # Découpe le texte en lignes
    lignes = texte.split("\n")

    # Fonction pour afficher une ligne colorée et avec effet de délai
    def afficher_ligne(ligne):
        for caractere in ligne:
            sys.stdout.write(caractere)

            sys.stdout.flush()
            time.sleep(0.005)
        print()

    # Lance l'animation
    for ligne in lignes:
        afficher_ligne(ligne)

    loading_animation(50)
    print("Welcome, what do you seek stranger ?\n")
    return 0



mark=0

def opt4():
    print("Here is a random person:\n")
    dumper.dumper(filetoread)
    print("\n")
    ask=input("Type enter to go back to main menu or 'm' if you want another generation!\n")
    if ask!=None and ask!="m":
         __main__()
    elif ask=="m":
        print("\n")
        print("------------------------------------------")
        opt4()

    return 0



def __main__():
    global mark
    if mark==0:
        animation()
    print("Type 0 if you want some help \n")
    print("Type 1 if you wanna create your custom wordlist \n")
    print("Type 2 if you wanna test if your dictionnary contain a password\n")
    print("Type 3 if you wanna generate a fake person (profile generator) and test a dictionnary of your own against em\n")
    print("Type 4 if you want to use the profile generator alone\n")
    print("Type 5 if you want to mix-shake and add fun to a wordlist you already have\n")
    

    
    take=int(input("Your choice ?: "))
    if take==1:
        mark=1
        wordlist("",[])
         
             
    elif take==2:
        mark=1
        passw("","")

    elif take==3:
        mark=1
        mdp=dumper.dumper(filetoread)
        print("\nNow do ur magic with the dictionnary")
        pathom=wordlist("ara",[]) #the "ara" thing is here only to not leave wordlist() blank or else it won't do as intended
        #print("Pour l'instant voilà l'état des choses:", mdp,"et ",pathom)
        passw(mdp,pathom)

    elif take==0:
        mark=1
        help()
        
    elif take==4:
        mark=1
        opt4()

    elif take == 5: 
        mark = 1
        opt5()
        
    else:
        mark=1
        print("\nType a valid input !!! \n")
        print("------------------------------------------------")
        __main__()
    return 0



__main__()

