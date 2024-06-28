import random
import time
from unidecode import unidecode 
import os

def dumper(dataset):
    
    def bartester(mot):
        temp=[]
        if "/" in mot[0:2]:
            temp.append(mot[0:1])  
            if "/" in mot[2:4]:
                temp.append(mot[2:3])
            else:
                temp.append(mot[2:4])
        else:
            temp.append(mot[0:2]) 
            if "/" in mot[3:5]:
                temp.append(mot[3:4])
            else:
                temp.append(mot[3:5])
        temp.append(mot[-4:])
        return temp


    def generer_date_naissance(mark,gap):
        # Génère une date de naissance aléatoire entre 1950 et 2010
        gap=int(gap)
        if mark==0:
            return f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1970, 2010)}"
        elif mark==1:
            return f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(gap-10, gap+10)}"
        elif mark==2:
            return f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(gap-30, gap-20)}"


            
    


    def generer_personnage():

        """
        Exploitation du csv
        
        """
        os.chdir(os.path.dirname(__file__))
        file=open(dataset,mode="r",encoding='utf8')
        file.readline()
        data=[]  
        for line in file:
            reader=line.split(";")
            reader[7]=reader[7].replace("\n","")
            data.append(reader)
        file.close()


        def tablewriter(row):
            table=[]
            i=0
            j=0
            for i in range(0,len(data)):
                j=data[i][row]
                if j=="":
                    break
                table.append(j)
            return table



        prenoms_masculins=tablewriter(0)
        prenoms_feminins=tablewriter(1)
        noms=tablewriter(2)
        nb_freres_soeurs=tablewriter(3)
        metiers=tablewriter(4)
        hobbies=tablewriter(5)
        animaux=tablewriter(6)
        surnoms_animaux=tablewriter(7)

        
#######################################################

        prenom = random.choice(prenoms_masculins + prenoms_feminins)
        nom = random.choice(noms)
        nb_freres_soeurs = random.choice(nb_freres_soeurs)
        date_naissance = generer_date_naissance(0,1)
        basedate=bartester(date_naissance)
        basedate=basedate[2]
        

        

        # Sélection aléatoire d'un prénom masculin pour le premier parent et d'un prénom féminin pour le deuxième parent
        parent1 = random.choice(prenoms_masculins)
        parent2 = random.choice(prenoms_feminins)
        
        metier = random.choice(metiers)
        hobby = random.choice(hobbies)
        animal = random.choice(animaux)
        
        if nb_freres_soeurs != "0":
                freres_soeurs = [[random.choice(prenoms_masculins + prenoms_feminins).lower(), generer_date_naissance(1,basedate)] for _ in range(int(nb_freres_soeurs))]
        else:
            freres_soeurs = ""
        
        if animal !="None":
            surnom_animal = random.choice(surnoms_animaux)
        else:
            surnom_animal = ""
            animal=""

        # Transformation en minuscules
        prenom = prenom.lower()
        nom = nom.lower()
        parent1 = parent1.lower()
        parent2 = parent2.lower()
        metier = metier.lower()
        hobby = hobby.lower()
        animal = animal.lower() 
        surnom_animal=surnom_animal.lower()
        
        return [prenom,nom, date_naissance,nb_freres_soeurs,freres_soeurs, [[parent1,generer_date_naissance(2,basedate)], [parent2,generer_date_naissance(2,basedate)]], metier,hobby,animal,surnom_animal]



    



    def generer_mot_de_passe(personnage):
        mot=[]
        mot_de_passe=""
        
        """
        while i<4:
            temp=random.sample(personnage,1)
            #temp=random.choice(personnage)
            if temp!=None and temp!="aucun":
                mot.append(temp)
                i=i+1
        """
        mot=random.sample(personnage,4)
        
            
            
        for i in range(len(mot)):
            r=random.randint(0, 1)
            
            if type(mot[i])==str:
                if not "/" in mot[i]:
                    if r==0:
                        mot_de_passe=mot_de_passe +(mot[i].upper())
                    else:
                        mot_de_passe=mot_de_passe+(mot[i].lower())
                else:           #Condition pour exploiter correctement les dates, passage probable en fonction réutilisable
                    """
                    temp=[]
                    if "/" in mot[i][0:2]:
                        temp.append(mot[i][0:1])  
                        if "/" in mot[i][2:4]:
                            temp.append(mot[i][2:3])
                        else:
                            temp.append(mot[i][2:4])
                    else:
                        temp.append(mot[i][0:2]) 
                        if "/" in mot[i][3:5]:
                            temp.append(mot[i][3:4])
                        else:
                            temp.append(mot[i][3:5])
                    temp.append(mot[i][-4:])
                    """
                    temp=bartester(mot[i])
                    mot_de_passe=mot_de_passe+random.choice(temp)
            if type(mot[i])==list:
                mar=[]
                for m in range(len(mot[i])):
                    mar.append(mot[i][m][0])
                    mar2=(bartester(mot[i][m][1]))
                    mar=mar+mar2
                
                mot_de_passe=mot_de_passe+random.choice(mar)
                 
        return mot_de_passe

    # Utilisation
    personnage = generer_personnage()
    print("\nPROFIL: \n")
    print("PRENOM:", personnage[0].capitalize())
    print("NOM:", personnage[1].upper())
    print("DATE DE NAISSANCE:", personnage[2])
    print("NOMBRE DE FRÈRES ET SŒURS:", personnage[3])
    if personnage[4]:
        print("FRÈRES ET SŒURS:")
        for frere_soeur in personnage[4]:
            print("  - Nom:", frere_soeur[0].capitalize())
            print("    Date de naissance:", frere_soeur[1])
    print("PARENTS:")
    for num in range(0,2):
            print("  - Nom:", personnage[5][num][0].capitalize())
            print("    Date de naissance:", personnage[5][num][1])
    print("MÉTIER:", personnage[6])
    print("HOBBY:", personnage[7])
    print("ANIMAL DE COMPAGNIE:", personnage[8])
    if personnage[8] != "":
        print("SURNOM DE L'ANIMAL:", personnage[9])


    personnage.pop(3)
    mot_de_passe = generer_mot_de_passe(personnage)
    mdp=unidecode(mot_de_passe)
    #print(mdp)
    return mdp
    #time.sleep(1000)
        
#dumper("frenchdata.csv")
