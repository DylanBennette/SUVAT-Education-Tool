import math
from A2_Physics_Propulsion import *
from A2_Physics_Projectile import *

class SUVAT(Propulsion,Projectile):
    
    def __init__(self):
        super().__init__()
        
    def CalculateInitialVelocity(self):
        SUVATlist = self.GetSuvat(Propulsion)
        print(SUVATlist)

if __name__ == "__main__":
    
    SUVAT.CalculateInitialVelocity(SUVAT)
    
        
    
