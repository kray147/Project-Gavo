import random
import time
from unidecode import unidecode 

def dumper():
    
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
        prenoms_masculins =  ["Thibault", "Maxime", "Antoine", "Lucas", "Hugo", "Nicolas", "Arthur", "Thomas", "Alexandre", "Quentin", "Paul", "Louis", "Julien", "Gabriel", "Matthieu", "Vincent", "Baptiste", "Romain", "Simon", "Pierre", "Mathieu", "Adrien", "Clément", "Guillaume", "David", "Damien", "Jules", "Benjamin", "Cédric", "Rémi", "Sébastien", "Laurent", "Étienne", "Alexis", "Anthony", "Michaël", "Florian", "Olivier", "François", "Sylvain", "Jonathan", "Xavier", "Raphaël", "Jean", "Cyril", "Dylan", "Christophe", "Kevin", "Mickaël", "Philippe", "Jimmy", "Dimitri", "Morgan", "Julian", "Arnaud", "Éric", "Christian", "Fabien", "Noël", "Alain", "Théo", "Robert", "Joseph", "Marc", "Georges", "Patrick", "André", "René", "Raymond", "Gérard", "Roland", "Léon", "Albert", "Claude", "Bertrand", "Émile", "Denis", "Maurice", "Yves", "Marcel", "Vincent", "Jacques", "Roger", "Fernand", "François", "Henri", "Pierre", "Bruno", "Charles", "Sébastien", "Jean-Claude", "André", "Éric", "François", "Luc"]
        prenoms_feminins = ["Camille", "Sarah", "Emma", "Manon", "Léa", "Chloé", "Inès", "Louise", "Jade", "Alice", "Anna", "Juliette", "Lola", "Clara", "Zoé", "Romane", "Lina", "Charlotte", "Eva", "Margaux", "Lisa", "Maëlle", "Louna", "Mathilde", "Léna", "Lucie", "Mila", "Nina", "Eléna", "Laura", "Elsa", "Océane", "Jeanne", "Olivia", "Noémie", "Rose", "Margot", "Agathe", "Sofia", "Alicia", "Ambre", "Lou", "Julie", "Julia", "Anaïs", "Amandine", "Mélanie", "Marine", "Pauline", "Capucine", "Valentine", "Émilie", "Maelle", "Salomé", "Manon", "Louisa", "Laure", "Romane", "Diane", "Hélène", "Céline", "Caroline", "Nathalie", "Sandra", "Mélissa", "Stéphanie", "Clémentine", "Sabrina", "Elodie", "Aurélie", "Fanny", "Marion", "Agnès", "Véronique", "Laetitia", "Colette", "Coralie", "Claire", "Élodie", "Nicole", "Sylvie", "Cécile", "Marguerite", "Monique", "Nadine", "Christine", "Sophie", "Catherine", "Marie", "Isabelle", "Véronique", "Patricia", "Annie", "Valérie", "Catherine", "Suzanne", "Josette"]
        noms = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard", "Andre", "Lefevre", "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez", "Legrand", "Garnier", "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Roussel", "Nicolas", "Perrin", "Morin", "Mathieu", "Clement", "Gauthier", "Dumont", "Lemaire", "Marie", "Noel", "Meunier", "Jacques", "Caron", "Carre", "Menard", "Barbier", "Brun", "Guy", "Prevost", "Perez", "Sanchez", "Joly", "Marchand", "Dumas", "Blanchard", "Huet", "Brunet", "Schmitt", "Dufour", "Ruiz", "Delaunay", "Albert", "Colin", "Renard", "Picard", "Chevalier", "Leclerc", "Lopez", "Gomez", "Leclercq", "Bourgeois", "Devaux", "Benoit", "Guillaume", "Bertin", "Roger", "Rolland", "Roche", "Marty", "Payet", "Pierre", "Denis", "Robin", "Rodriguez"]

        nb_freres_soeurs = ["0", "1", "2", "3", "4"]
        metiers = ["ingénieur", "artiste", "médecin", "enseignant", "avocat", "informaticien", "pompier", "policier", "chef", "architecte", "comptable", "pharmacien", "vétérinaire", "jardinier", "boulanger", "cuisinier", "journaliste", "plombier", "électricien", "maçon", "carpenter", "charpentier", "plâtrier", "menuisier", "peintre", "serrurier", "mécanicien", "garagiste", "tailleur", "couturier", "coiffeur", "esthéticien", "serveur", "barman", "gérant", "banquier", "économiste", "psychologue", "conseiller", "consultant", "directeur", "manager", "receptionniste", "technicien", "analyste", "chercheur", "professeur", "thérapeute", "ergothérapeute", "diététicien", "orthophoniste", "infirmier", "aide-soignant", "secrétaire", "assistante", "opérateur", "ouvrier", "chauffeur", "livreur", "magasinier", "réparateur", "agent", "technicien", "technologiste", "téléopérateur", "développeur", "webdesigner", "graphiste", "artiste", "photographe", "cinéaste", "musicien", "chanteur", "acteur", "athlète", "coach", "athlétique", "entraîneur", "astronome", "biologiste", "chimiste", "géologue", "mathématicien", "physicien", "statisticien", "zoologiste", "horticulteur", "marin", "généraliste", "géomètre", "nutritionniste", "opticien", "préparateur", "psychiatre", "radiologue"]

        hobbies = ["lecture", "voyage", "peinture", "cuisine", "sport", "musique", "jardinage", "photographie", "bricolage", "couture", "randonnée", "natation", "équitation", "cinéma", "théâtre", "danse", "yoga", "pêche", "plongée", "escalade", "ski", "surf", "kitesurf", "volleyball", "basketball", "football", "tennis", "golf", "badminton", "vélo", "course", "karaté", "judo", "aïkido", "boxe", "taekwondo", "bowling", "billard", "chasse", "astronomie", "lecture", "écriture", "calligraphie", "peinture", "sculpture", "poterie", "modélisme", "philatélie", "numismatique", "cuisine", "oenologie", "mixologie", "cuisine", "bénévolat", "écologie", "jardinage", "bricolage", "voyage", "aventure", "découverte", "photo", "vidéo", "informatique",  "self-defense", "méditation", "relaxation", "lecture", "écriture", "musique", "chant", "danse", "théâtre", "improvisation", "couture", "tricot", "crochet", "maroquinerie", "photographie", "vidéo", "astronomie", "archéologie", "généalogie", "course", "marche", "yoga", "fitness", "crossfit", "pilates", "escalade"]

        animaux = ["Chien", "Chat", "Poisson", "Oiseau", "Lapin", None]  # Ajout de None pour signifier l'absence d'animal
        surnoms_animaux = ["Titi", "Minou", "Coco", "Loulou", "Mimi", "Doudou", "Félix", "Mistigri", "Bella", "Moustique"]


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
        
        if animal is not None:
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
    print(mdp)
    return mdp
    #time.sleep(1000)
        
#dumper()