import tkinter
import plaque

#Fenetre principale
window = tkinter.Tk()
window.wm_minsize(500, 500)

fenetre = tkinter.Frame(window) #crée une sous-fenetre dans la fentre

#---fenetre nécessaire pour tester switch90()-----------------
fenetre2 = tkinter.Frame(window)

class DrawCase(tkinter.Canvas):     #classe DrawCase dérivée de Canvas (permet de créer l'affichage des case)
    #parametres des cases
    wallColor = "grey"
    wallSize = 5
    caseColor = "#CFC1B0"
    caseSize = 40

    def __init__(self,master, case):
        super(DrawCase, self).__init__(master, bd = -2, width = self.caseSize, height = self.caseSize)    #créé un canvas (élément de dessin)
        self.create_rectangle(0, 0, self.caseSize-1, self.caseSize-1, fill = self.caseColor)    #créé un rectangle qui rempli le canvas
        #ajoute les murs en fonction des cases
        if case.haut :
           self.create_rectangle(0, 0, self.caseSize-1, self.wallSize, fill = self.wallColor)
        if case.bas :
           self.create_rectangle(0, self.caseSize-1-self.wallSize,  self.caseSize-1, self.caseSize-1, fill = self.wallColor)
        if case.droit:
            self.create_rectangle(self.caseSize-1-self.wallSize, 0, self.caseSize - 1, self.caseSize-1, fill=self.wallColor)
        if case.gauche:
            self.create_rectangle(0, 0, self.wallSize, self.caseSize - 1, fill=self.wallColor)

#-----------------affichage de chaque case---------------------------

for i in range(0, 8):
    for j in range(0, 8):
        DrawCase(fenetre, plaque.plaque1.element[j][i]).grid(row = i, column = j)
fenetre.pack(expand = True)



# -------------te montre ce qu'il faut corriger pour la méthode switch90()
plaque.plaque1.switch90()

for i in range(0, 8):
    for j in range(0, 8):
        print("i=" + str(i) + " j=" + str(j))
        DrawCase(fenetre2, plaque.plaque1.element[j][i]).grid(row = i, column = j)

fenetre2.pack(expand = True, pady = 5)

window.mainloop()   #lance la fenetre
