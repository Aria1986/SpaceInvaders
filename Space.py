import Invader
import Canon
import time
import keyboard

class Space:
    
    grille = []
    
    def __init__(self, nb_c,nb_l, positionCanonInitiale):
        self.nb_l=nb_l
        self.nb_c=nb_c
        self.score=0
        self.positionCanonInitiale=positionCanonInitiale
        self.canon = Canon.Canon(positionCanonInitiale)
        self.grille = [[0]*nb_c for l in range(nb_l+1)]      
        for l in range(nb_l+1):
            for c in range(nb_c):
                if(l == 0):
                    self.grille[l][c] =str(Invader.Invader())
                else:self.grille[l][c] = ' '
        self.grille[self.nb_l][self.positionCanonInitiale] =str(self.canon) 
        
        # grille = [[colonne + ligne for colonne in ('A', 'B', 'C')] for ligne in ('1', '2', '3')] 
        
    def cadreLigne(self, caractereDebut, caractereFin):
        lign=caractereDebut
        for i in range(1,self.nb_c):    
            lign= lign+'-'
        lign= lign+ caractereFin
        print(lign) 
        
    def afficher(self):
        print(f'Votre score est de: {self.score}')
        self.cadreLigne('┌',' ┐')
        for l in self.grille:                 
            col="|"
            for item in l:               
                col = str(col)+str(item)
                
            print(col+"|")
            
        self.cadreLigne('└', ' ┘')
        
            
    def __repr__(self):
        return self.data
        
    def tirer(self):
        self.grille[self.nb_l-1][self.canon.pos]="^"
        self.afficher()
        self.grille[self.nb_l-1][self.canon.pos]=" "
        for d in range(2,self.nb_l+1):
            if(self.grille[self.nb_l-d][self.canon.pos]=="#"):
                self.score+=1
            self.grille[self.nb_l-d][self.canon.pos]="^"
            time.sleep(d/10) 
            self.afficher()
            self.grille[self.nb_l-d][self.canon.pos]=" "
            
    # def onkeypress(self,event):
    #     time.sleep(5)
    def deplacerCanonLeft(self):
        if(self.canon.pos>1): 
            self.grille[self.nb_l][self.canon.pos] =' '
            self.canon.deplacerAGauche()   
            self.grille[self.nb_l][self.canon.pos] =str(self.canon)        
            self.afficher()  
    
    def deplacerCanonRight(self):
        if(self.canon.pos < (self.nb_c -1)): 
            self.grille[self.nb_l][self.canon.pos] =' '
            self.canon.deplacerADroite()   
            self.grille[self.nb_l][self.canon.pos] =str(self.canon)
            self.afficher()
            
    # keyboard.on_press(onkeypress)  
    
    
                
space = Space(6,4,2)
space.afficher()
# space.tirer()
# print(space)
# print(space.canon)
while True:
        if keyboard.is_pressed("Left"):
            space.deplacerCanonLeft()
            time.sleep(0.2)
        
        elif keyboard.is_pressed("Right"):
            space.deplacerCanonRight()
            time.sleep(0.2)
            
        elif keyboard.is_pressed("Space"):
            space.tirer()
            time.sleep(0.2)
            
        elif keyboard.is_pressed("Esc"):
            break  