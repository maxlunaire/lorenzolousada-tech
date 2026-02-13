from random import*
class game():
    def __init__(self,nom,heart,handicape):
        self.nom=nom
        self.heart=heart
        self.objet=[]
        if handicape=="":
            self.handicape=None
        else:
            self.handicape=handicape
    def lost_heart(self,nb):
        self.heart-=nb
    def objet(self):
        objet=[]
    def info(self):
        print(f"je suis {self.nom} ma vie est actuelement de {self.heart} coeur , mes objets sont {self.objet}, mon handicape est {self.handicape}")
    def handicape(self,handicape):
        if handicape=="to fast":
            pass

class boss(game):
    def __init__(self,*arg):
        super().__init__(*arg)
    def second_phase(self,objet):
        self.heart+=2
        self.objet.append(objet)
        self.hadicape=""
    def dificulty(self,mode):
        if mode=="easy":
            self.heart//=2
            self.objet=[""]
            self.handicape=["to slow"]
        if mode=="normal":
            self.heart*=2
            self.objet=["pile ou face"]
            self.handicape=["imprevisible"]
        if mode=="hard":
            self.heart*=2
            self.objet=["segond shot"]
            self.handicape=["to fast"]
def party():
    nom=int(input("dit moi votre pseudo"))
    player=game(nom,3,"")
    verif=False
    while verif==False:
        difficulte=int(input("vous avez lz choix enter 3 difficulte easy medium hard"))
        if difficulte in ["eazy","medium","hard"]:
            verif=True
        else:
             print("la difficulte n'est pas bonne")


karlito=boss("karlito",2,"dummies")
karlito.dificulty("hard")
karlito.info()




