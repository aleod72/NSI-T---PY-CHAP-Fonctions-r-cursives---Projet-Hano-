from classes.hanoi import *

setup = Hanoi(5)
setup.jouer()
setup.text.config(
    text="                                                            Terminé                                                            ",
    background="green",
)
setup.root.title("Hanoï : %s disque.s [FINI]" % setup.nbdisques)
setup.root.mainloop()
