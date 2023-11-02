class Canon:
    
    def __init__(self,pos):
        self.pos=pos
        
    def __str__(self):
        return '¥' 
    
    def deplacerAGauche(self):
        if (self.pos>1):
            self.pos = self.pos-1
            
    def deplacerADroite(self):
            self.pos = self.pos+1
