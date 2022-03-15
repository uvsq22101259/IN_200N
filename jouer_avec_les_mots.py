
import random as rd




def nb_lignes(nom):
    """retourne le nombre de lignes du fichier dont le nom est passé en argument commechaîne de caractère."""
    nom += ".txt"
    fic = open(str(nom),"r")
    compteur = 0
    for ligne in fic:
        compteur += 1
    return compteur


def ecrit_liste_mots(nom,n):
    nom += ".txt"
    fic = open(str(nom),"r")
    wordsn = []
    for ligne in fic:
        if len(ligne) == n+1 :
            wordsn.append(ligne)
    fic.close()
    nom = "word" + str(n) + ".txt"
    fic_n = open(nom,"w")
    for i in wordsn:
        fic_n.write(i)


def melange_mots(nom):
    nomtxt = nom + ".txt"
    fic = open(nomtxt,"r")
    ligne = fic.readlines()
    rd.shuffle(ligne)
    fic.close()
    nommel = nom + ".mel"
    fic_2 = open(nommel,"w")
    for i  in ligne:
        fic_2.write(i)


def compare_mots(m1,m2):
    if len(m1) != len(m2):
        return
    m1l = list(m1)
    m2l = list(m2)
    m2l_c = list(m2)
    profil = [0]* len(m1)
    exclu = []
    
    for i in range (len(m1l)):
        if m1l[i] ==  m2l[i]:
            profil[i] = 1
        elif m1l[i] in m2l_c:
            m2l_c.remove(m1l[i])
            profil[i] = 2
        else :
            profil[i] = 0
    return profil


def ecrit_liste_compatible(fichier,m,profil):
    
    fic = open(fichier,"r")
    ligne = fic.readlines()
    profil_compatible = []
    for i in ligne:
        i = i.strip("\n")
        a = compare_mots(i,m)
        if a == profil :
            profil_compatible.append(i)
    fic.close()
    fic_2 = open("fichier.txt", "w")
    for i in profil_compatible :
        fic_2.write(i)
    fic_2.close()

mot = "chello"
ecrit_liste_compatible("word.txt",mot,([1])*(len(mot)))

# print(compare_mots("chello","chello"))

#ecrit_liste_mots("word",5)
# print(nb_lignes("word5"))
# melange_mots("word")

