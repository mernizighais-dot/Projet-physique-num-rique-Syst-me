#On demande a l'utilisateur les paramêtre du tracé on definie aussi les valeurs par défaut. 
read -p "Entrez la borne inferieur de l'intervalle de tracé (par défaut 0) : " arg1
arg1=${arg1:-0}  

read -p "Entrez la borne superieur de l'intervalle de tracé (par défaut 1500) : " arg2
arg2=${arg2:-1500} 

read -p "Entrez le pas du tracé (par défaut 10) : " arg3
arg3=${arg3:-10} 

#On établie le fichier par defaut 
fichier_defaut="Spectre_photoluminescence.txt"


read -p "Entrez le chemin du fichier .txt a traiter (par défaut '$fichier_defaut'): " fichier
fichier=${fichier:-$fichier_defaut} 

#On verifie que le fichier fournie en argument existe.
if [ ! -f "$fichier" ]; then
    echo "Erreur : Le fichier '$fichier' est introuvable. Veuillez verifier que le chemin est correcte."
    exit 1
fi

#On verifie que le fichier fournie en arguement est bien un fichier .txt 
fichier_entree="$fichier"
if [[ "$fichier_entree" != *.txt ]]; then
    echo "Erreur : l'argument 4 ne semble pas être un fichier .txt"
    exit 1
fi

#On appel le script python avec les arguments definie par l'utilisateur 
python3 recherche_plot.py "$arg1" "$arg2" "$arg3" "$fichier"