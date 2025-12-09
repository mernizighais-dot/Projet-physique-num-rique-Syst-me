import os, sys, re

#On verifie que on ne definie pas un pas négatif.                      
if float(sys.argv[3]) > 0:
    tailleFenetre = float(sys.argv[3])

#On éxtrait les valeurs du fichier en utilisant une RegEx qui identifie les couples de valeurs.
def valeurs(texte):
    ondes = []
    intensites = []
    comp = re.compile("^(\d+\.\d{2})\s(\-?\d+\.\d{3})$") #La RegEx
    for ligne in texte:
        donnee = comp.match(ligne)
        if donnee:
            ondes.append(float(donnee.group(1)))      #on stocke les valeurs trouver dans 2 listes une pour les longueurs d'ondes et une pour les intensités.
            intensites.append(float(donnee.group(2)))
    return ondes, intensites

#On crée un dictionnaire qui contient les valeurs extraites précedemment 
def dicovaleur(pas, texte):
    i = 0
    ondes, intensites = valeurs(texte)
    longueurOnde = {}
    debutPas = 0
    finPas = debutPas + pas
    longueurOnde[debutPas]=[] #le dictionnaire est un dico de liste qui contient pour chaque plage de longueur d'onde les intensités associées.
    while i < (len(ondes)) : 
        if debutPas <= ondes[i] < finPas : #Tant que les longueurs d'onde sont dans la plage on ajoute les intensités correspondantes.
            longueurOnde[debutPas].append(intensites[i])
            i+=1
        else :  #Si la longueur d'onde est pas dans la plage on passe à la plage suivante et on recommance.
            debutPas = finPas
            finPas = finPas+pas
            longueurOnde[debutPas]=[]
    return longueurOnde

#On crée un dictionnaire qui contient pour chaque plage des informations sur les intensités de cette plage.
def dicoinfo(D):
    infofenetres = {}  
    for clef in D :
        if len(D[clef]) > 0 : #Si la plage contient des intensités on inscris les informations.
            nbIntensite = len(D[clef])
            minIntensite = min(D[clef])
            moyenneIntensite = sum(D[clef])/len(D[clef])
            maxIntensite = max(D[clef])
            infofenetres[clef] = [nbIntensite, minIntensite, moyenneIntensite, maxIntensite]
        else :       #Si la plage ne contient pas d'intensités on remplie les informations avec None
            infofenetres[clef]=[0, None, None, None]
    return infofenetres