
import math


def division(tupla1,tupla2):
        preal = round((tupla1[0]*tupla2[0] + tupla1[1]*tupla2[1]) / (tupla2[0]**2 + tupla2[1]**2),2)
        pimag = round((tupla1[1]*tupla2[0] - tupla1[0]*tupla2[1]) / (tupla2[0]**2 + tupla2[1]**2),2)
        return (preal,pimag)

def multiplicacion(tupla1,tupla2):

        preal = tupla1[0]*tupla2[0] - tupla1[1]*tupla2[1]
        pimag = tupla1[0]*tupla2[1] + tupla1[1]*tupla2[0]
        return (preal,pimag)

def resta(tupla1,tupla2):            
        preal = tupla1[0] - tupla2[0]
        pimag = tupla1[1] - tupla2[1]
        return (preal,pimag)
            
def suma(tupla1,tupla2):
        preal = tupla1[0] + tupla2[0]
        pimag = tupla1[1] + tupla2[1]
        return (preal,pimag)
        
        
def fase(self):

        r =  round(math.atan(self[1]/self[0]),2)
        return r
        
def cartesiano_polar(self):
        r=modulo(self)
        r2=fase(self)

        return r,r2
def polar_cartesiano(self):
        r=round(self[0]*math.cos(self[1]),2)
        r2=round(self[0]*math.sin(self[1]),2)
        return r,r2
        

        
def modulo(self): 
        r = round((self[0]**2 + self[1]**2)**(1/2),2)
        return r

def conjugado(self ):
        return (self[0] , - self[1])
            



            

