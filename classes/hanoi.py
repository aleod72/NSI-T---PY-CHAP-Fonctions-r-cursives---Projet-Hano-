import tkinter as tk
from tkinter import font
import time
from . import disques


class Setup:
    def __init__(self, nbdisques):

        self.disques = [[], [], []]
        for taille in range(nbdisques):
            self.disques[0].append(disques.Setup(taille + 1))
        self.nbdisques = len(self.disques[0])

        self.tk = tk
        self.root = self.tk.Tk()
        self.root.resizable(False, False)
        self.canvas = self.tk.Canvas(self.root, width=800, height=250)
        self.canvas.pack()
        self.text = tk.Label(
            self.root,
            text=f"                                                            Le jeu de Hanoï avec {nbdisques} disques...                                                            ",
            background="orangered",
            foreground="white",
            font=font.Font(family="Lucida Console", size="14"),
        )
        self.text.place(relx=0.5, rely=1, y=-13, anchor="center")
        self.root.title(f"Hanoï : {self.nbdisques} disque.s")
        self.buildCanvas()
        self.root.update()

    def __str__(self):
        return str(self.disques)

    def jouer(self):
        self.afficher()
        self.root.update()

        def bouge(x, y):
            """
            Fonction qui "déplace" les disques si c'est possible
            """
            if self.disques[x] != [] and self.disques[y] == []:
                self.disques[y].insert(0, self.disques[x].pop(0))
                self.afficher()
                self.root.update()
                return True

            elif (
                self.disques[x] != []
                and self.disques[x][0].taille < self.disques[y][0].taille
            ):
                self.disques[y].insert(0, self.disques[x].pop(0))
                self.afficher()
                self.root.update()
                return True

            else:
                return False

        def deplace2pions(depart, arrivee, intermediaire):
            """
            Fonction qui permet de deplacer deux disques si c'est possible
            """
            if bouge(depart, intermediaire) == False:
                return f"Erreur 1 deplacer2pions() {self.disques[depart][0].taille, self.disques[intermediaire][0].taille}"
            if bouge(depart, arrivee) == False:
                bouge(intermediaire, depart)
                return f"Erreur 2 deplacer2pions() {self.disques[intermediaire][0].taille, self.disques[depart][0].taille}"
            if bouge(intermediaire, arrivee) == False:
                bouge(arrivee, depart)
                bouge(intermediaire, depart)
                return f"Erreur 1 deplacer2pions() {self.disques[intermediaire][0].taille, self.disques[arrivee][0].taille}"
            return "OK"

        def deplaceNpions(n, depart, arrivee, intermediaire):
            """
            La fameuse fonction récursive qui permet de déplacer N disques
            """
            if n > self.nbdisques:
                # n'arrivera jamais sauf démonstration
                print(
                    f"Impossible de deplacer {n} disques, puisqu'il y en a {self.nbdisques}"
                )
                return
            if n == 0:
                # "Hum.. pourquoi?"
                return
            if n == 1:
                # trop facile
                bouge(depart, arrivee)
                return
            if n == 2:
                # ça va
                deplace2pions(depart, arrivee, intermediaire)
                return
            else:
                # ben là tout dépend du n
                # déplace les pions sur la tour intermédiaire (attention au cerveau les prochaines lignes sont dangereuses)
                # en gros... ça va déplacer les pions sur une tour intermédiaire mais... 1/2 c'est la tour d'arrivée qui sert de tour intermédiaire
                deplaceNpions(n - 1, depart, intermediaire, arrivee)
                # bon une fois qu'il ne reste plus que le plus gros dans la première tour on le déplace dans la dernière tour (à ne pas sortir de son contexte)
                bouge(depart, arrivee)
                # et là... ça va [bla bla] mais... maintenant 1/2 la tour de départ sert de tour intermédiaire
                deplaceNpions(n - 1, intermediaire, arrivee, depart)

                # c'était la seule chose à vraiment expliquer de tout le code, merci

        deplaceNpions(
            self.nbdisques, 0, 2, 1
        )  # il y a surement mieux que ça mais voilà, tant que ça fonctionne c'est bon !

    def afficher(self):
        self.buildCanvas()

        time.sleep(0.5)
        self.root.update()
    
    def buildCanvas(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(150, 200, 150, 50)
        self.canvas.create_rectangle(400, 200, 400, 50)
        self.canvas.create_rectangle(650, 200, 650, 50)
        self.canvas.create_rectangle(50, 200, 750, 200)

        for tour in range(len(self.disques)):
            for disque in range(len(self.disques[tour])):
                taille = self.disques[tour][-1 - disque].taille + 1.5
                largeur = taille * 20
                hauteur = 20
                x = 150 + tour * 250 - taille * 10
                y = 200 - hauteur * (disque + 1)
                self.canvas.create_rectangle(
                    x,
                    y,
                    x + largeur,
                    y + hauteur,
                    fill=self.disques[tour][-1 - disque].couleur,
                )
