
LARGEUR = 400
HAUTEUR = 600

inte = 0
id = 0
cord = []



import tkinter as tk
import random as rd


def creer_balle():
    """dessine un cercle rempli de bleu au milieu du canevas de rayon 20 pixels;retourne une liste contenant l’identifiant de l’object graphique créé (la balle) suivi dedeux entiers choisis au hasard entre 1 et 7; cette liste sera appelée “balle” dans la suite"""
    balle =[]
    balle.append(terrain.create_oval(((LARGEUR//2)-10,(HAUTEUR//2)-10),((LARGEUR//2)+10,(HAUTEUR//2)+10), fill="blue",))
    for i in range (2):
        balle.append(rd.randint(1,7))
    return(balle)


def mouvement(balle):
    global inte, cord
    cord = terrain.coords(balle[0])
    print(cord)
    if  inte == 0:
        demarrer.config(text= "arreter")
        inte += 1
        mouv_infinie(balle)
    else :
        racine.after_cancel(id)
        demarrer.config(text="Démarrer")
        inte -= 1


def mouv_infinie(balle):
    global id
    terrain.move(balle[0],balle[1],balle[2])
    id = racine.after(200,lambda : mouv_infinie(balle))
    
   


racine = tk.Tk()
racine.title("rebonds balle")

terrain = tk.Canvas(racine, width=LARGEUR, height= HAUTEUR, bg ="black")
terrain.grid(column=0, row=0)

creation = creer_balle()

demarrer = tk.Button(racine,text="Démarrer", command= lambda: mouvement(creation),   )
demarrer.grid(column=0,row=1)



racine.mainloop()