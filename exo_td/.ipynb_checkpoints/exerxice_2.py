
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


def mouvement(ball):
    global inte, cord, id
    cord = terrain.coords(ball[0])
    
    
    if  inte == 1 :
        demarrer.config(text= "arreter")
        cord = terrain.coords(ball[0])
        if cord[0] <= 0 or cord[2] >= LARGEUR or cord[1] <= 0 or cord[3] >= HAUTEUR:
            rebond2(creation)
        terrain.move(ball[0],ball[1],ball[2])
        id = racine.after(20,lambda : mouvement(creation))
    if inte == 2:
        racine.after_cancel(id)
        demarrer.config(text="Démarrer")

    


def stop(event):
    global inte
    if event.widget == demarrer:
        inte += 1 
        if inte == 2:
            inte = 0
        print(inte)

    
def rebond1(ball_rebond):
    
    if cord[0] <= 0 or cord[2] >= LARGEUR:
        creation[1] = -ball_rebond[1]
    if cord[1] <= 0 or cord[3] >= HAUTEUR:
        creation[2] = -ball_rebond[2]
    
   



def rebond2(ball_rebond):
    if  cord[0] <= 0:
        terrain.move(creation[0],LARGEUR,creation[2])
    if cord[2] >= LARGEUR:
        terrain.move(creation[0],-LARGEUR,creation[2])
    if cord[1] <= 0:
        terrain.move(creation[0],creation[1],HAUTEUR)
    if cord[3] >= HAUTEUR:
         terrain.move(creation[0],creation[1],-HAUTEUR)




racine = tk.Tk()
racine.title("rebonds balle")

terrain = tk.Canvas(racine, width=LARGEUR, height= HAUTEUR, bg ="black")
terrain.grid(column=0, row=0)

creation = creer_balle()
demarrer = tk.Button(racine,text="Démarrer", command= lambda : mouvement(creation))
demarrer.grid(column=0,row=1)
racine.bind("<Button-1>", stop)


racine.mainloop()