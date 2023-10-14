from cmu_graphics import *
import time
print('En unintento por  detener  la contaminacion y generar consiencia en la juventud tu eres el unico que puede ayudar ala tierra. salva la tierra de la contaminacion...recicla ')
time.sleep(15)

app.fondo='negro'
Rotulo('elimina todas los basuras...',200,10,tamaño=20,relleno='blanco')

Rotulo('luego de eso abanza...',200,390,tamaño=18 ,relleno='blanco')


avion=Grupo(Poligono(50,190,100,210,50,234,57,210,relleno='blanco'),
    Poligono(58,200,58,220,33,211,relleno='gris'))


lx= Linea(avion.centroX-10,avion.centroY,avion.centroX+20,avion.centroY,relleno='rojo', )
lx.dx= 5

b1=Poligono(340,40,370,40,365,80,350,80,relleno='tierra')


b2=Grupo(Circulo(300,160,20,relleno='rojo',),
PoligonoRegular(300,140,15,3,relleno='rojo',rotarAngulo=+60))


b3=Poligono(340,40,370,40,365,80,350,80,relleno='tierra')
b3.centroX=300
b3.centroY=320

b5=Poligono(340,40,370,40,365,80,350,80,relleno='tierra')
b5.centroX=410


b6=Poligono(340,40,370,40,365,80,350,80,relleno='tierra')
b6.centroX=410
b6.centroY=230


b4=Grupo(Circulo(300,160,20,relleno='azul',),
PoligonoRegular(300,140,15,3,relleno='azul',rotarAngulo=+60))
b4.centroX=390
b4.centroY=250


def mover_adelante():
   lx.centroX+=lx.dx
  
    

def enTeclaRetenida(tecla):
    if avion.centroY>0:
        if 'arriba'in tecla:
            avion.centroY-=10
           
    if avion.centroY<400:
        if 'abajo' in tecla:
            avion.centroY+=10
           
    if avion.centroX<430:
        if 'derecha' in tecla:
            avion.centroX+=10                                               
       
    if avion.centroX>0:
        if 'izquierda'in tecla:
            avion.centroX-=10
def enTeclaPresionada(tecla):
    if (tecla=='espacio'):
        lx.centroX=avion.centroX
        lx.centroY=avion.centroY
def enPaso():
    pass
    mover_adelante()
    b1.centroX-=3
    b2.centroX-=2
    b3.centroX-=3
    b4.centroX-=2                     
    b5.centroX-=2                     
    b6.centroX-=3                     
    if b4.centroX <=0:
         b1.centroX=410
         b2.centroX=410
         b3.centroX=417
         b4.centroX=420
         b5.centroX=425
         b6.centroX=415
    if lx.tocaFigura(b1)==True:
       app.grupo.quitar(b1)
       
    if lx.tocaFigura(b2)==True:
       app.grupo.quitar(b2)
       
    if lx.tocaFigura(b3)==True:
       app.grupo.quitar(b3)
       
    if lx.tocaFigura(b4)==True:
       app.grupo.quitar(b4)
       
    if lx.tocaFigura(b5)==True:
       app.grupo.quitar(b5)
       
    if lx.tocaFigura(b6)==True:
       app.grupo.quitar(b6)
##ganaste##

    if avion.centroX>=415:
        Rotulo('¡acabaste con la contaminacion!',200,200,tamaño=25,relleno=gradiente('rojo','verde','azul','blanco',inicio='izquierda'))
cmu_graphics.run()




