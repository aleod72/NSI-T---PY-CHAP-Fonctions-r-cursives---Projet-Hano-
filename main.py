from classes import hanoi

setup = hanoi.Setup(2)
setup.jouer()
setup.text.config(text=" Terminé ", background="green")
setup.root.title(f"Hanoï : {setup.nbdisques} disque.s [FINI]")
setup.root.mainloop()