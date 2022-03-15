fic = open("note.txt","r")
liste = []
moyenne = []
for i in fic:
    liste = i.split()
    m = (int(liste[1]) + int(liste[2]) + int(liste[3]))/ 3
    liste.append(str(m))
    moyenne.append(liste)
fic.close()

fic_2 = open("moyenne.txt","w")
for i in range (len(moyenne)) :
    phrase = " "
    for j in moyenne[i]:
        phrase += j + " "
    fic_2.write(phrase+ "\n")
fic_2.close()