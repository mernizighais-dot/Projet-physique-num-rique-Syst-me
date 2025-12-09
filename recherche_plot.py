import intensite as sity  #On importe le scripte intensite.py avec l'alias sity
import os, sys, re
import matplotlib.pyplot as plt

#Rappel des indices de dicoinfo dans le script intensite.py
nbIntensite = 0
minIntensite = 1
moyenneIntensite = 2
maxIntensite = 3

#Création d'une fonction qui verifie qu'un argument est un float positif.
def is_positive_float(valeur):
    try :
        flotant = float(valeur)
        if flotant >= 0 :
            return True
        else :
            return False
    except ValueError :
        return False

#On ouvre le fichier et on le stocke ligne par ligne dans une liste Spectre.     
fichier = sys.argv[4] 
with open(fichier) as file:
    Spectre = file.readlines()

#On verifie que on ne definie pas un pas négatif.
if is_positive_float(sys.argv[3]) :
    tailleFenetre = float(sys.argv[3])
else : 
    print("Le pas doit être positif")
    sys.exit(0)

#On verifie que on ne definie pas des bornes négatives ou un intervalle trop petit.
if (is_positive_float(sys.argv[1])) and (is_positive_float(sys.argv[2])) :
    if (float(sys.argv[2])-float(sys.argv[1])) > tailleFenetre:
        intervaled = float(sys.argv[1])
        intervalef = float(sys.argv[2])
    else : 
        print("La taille de l'intervale doit être supererieur au pas")
        sys.exit(0)
else : 
    print("Les bornes doivent être des nombres flottant positifs.")
    sys.exit(0)

#On utilise le scripte intensite.py pour extraitre les valeurs du fichier et les mettre sous forme de dictionnaire.
infos=sity.dicoinfo(sity.dicovaleur(tailleFenetre, Spectre))

#on initialise les listes qui contiendrons respectivement les valeur de x, les legendes de x, les valeur de y et sa marge d'erreur.
x=[]
labelsx=[]
y=[] 
yerror=[]

#On verifie pour chaque palge dans infos si elles sont contenus dans l'intervalle et quelle contiennent des valeur.
#Si tel est le cas alors on rentre les valeurs pour nos 4 liste definie plus haut.
for clef in infos :
    if (intervaled <= clef <= (intervalef-tailleFenetre)) and (infos[clef][nbIntensite] != 0):
        x.append(clef)
        labelsx.append(f"{round(clef, 5)}-{round((clef + tailleFenetre), 5)}")
        y.append(infos[clef][moyenneIntensite])
        yerror.append((infos[clef][maxIntensite]-infos[clef][minIntensite])/((2)**(0.5)))  #Formule de la marge d'erreur : max-min/sqrt(2)

#On s'assure que les legendes serons lisibles en limitant le nombre a 50.
pas = max(1, len(x)//50)
positionlabel=x[::pas]
labels=labelsx[::pas]

#On trace la figure 
plt.figure()
plt.plot(x, y, 'o-')
plt.errorbar(x, y, yerror, fmt='o', capsize=5)
plt.xticks(positionlabel, labels, rotation=90)
plt.title("Intensitée lumineuse en fonction de la longueur d'onde")
plt.xlabel("Plage de longueur d'onde en nm")
plt.ylabel("Intensitée lumineuse moyenne")
plt.subplots_adjust(bottom=0.205, top=0.925, left=0.075, right=0.970)
plt.show()