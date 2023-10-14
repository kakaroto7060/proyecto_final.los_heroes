from cmu_graphics import *

def procesadora():
    # ¡Llena esta página de código!
    #Fondo
    Rect(0,0,400,150,relleno=gradiente('azulGandul','naranja','amarillo',inicio='superior'))
    Circulo(10,120,30,relleno=gradiente('oro','naranja','amarillo',inicio='superior'))
    #Nuves
    Circulo(0,0,40,relleno='blanco')
    Circulo(70,0,40,relleno='blanco')
    Circulo(138,0,40,relleno='blanco')
    
    Poligono(400,100,400,400,0,400,0,140,160,80,relleno='verde')
    Rect(160,0,240,100,relleno='verde')
    Poligono(0,300,188,110,314,144,140,400,0,400,relleno='grisClaro')
    Linea(10,400,205,170,relleno='blanco',anchuraDeLinea=8,guión=Verdadero)
    
    #Prosesadora
    prosesadora=Grupo(
        Poligono(190,194,287,138,282,114,276,95,262,76,245,66,222,63,95,100,84,105,73,116,60,138,54,168,relleno='grisPizarraClaro',borde='negro'),
        Poligono(75,125,161,139,161,190,75,173,relleno='gainsboro',borde='negro'),
        Poligono(75,173,161,190,130,218,124,237,54,220,56,200,relleno='gris',borde='negro'),
        Linea(56,200,130,218)
    )
    
    prosesadora.centroX=294
    prosesadora.centroY=100
    #Luz
    luz1=Grupo(
    Ovalo(35,254,20,10,relleno='tierra'),
    Linea(35,254,40,180,relleno='blanco',anchuraDeLinea=4),
    Linea(38,180,55,180,relleno='blanco',anchuraDeLinea=4),
    Circulo(55,180,10,relleno='gris'),
    Rect(45,170,20,9,relleno='verde'))
    
    
    luz2=Grupo(
    Ovalo(35,254,20,10,relleno='tierra'),
    Linea(35,254,40,180,relleno='blanco',anchuraDeLinea=4),
    Linea(38,180,55,180,relleno='blanco',anchuraDeLinea=4),
    Circulo(55,180,10,relleno='gris'),
    Rect(45,170,20,9,relleno='verde'))
    luz2.centroX=100
    luz2.centroY=160
    
    #arbol
    arbol=Grupo(
    Rect(375, 200, 25, 200, relleno=gradiente('naranjaMarrón', 'marrónCuero', inicio='izquierda')),
    Círculo(325, 200, 50, relleno=gradiente('marVerdeMedio', 'verde', 'verde',
                                       inicio='izquierda')),
    Círculo(400, 200, 50, relleno='verde'),
    Círculo(350, 150, 50, relleno=gradiente('marVerdeMedio', 'verde', 'verde',
                                       inicio='izquierda-superior')),
    Círculo(375, 100, 50, relleno=gradiente('marVerdeMedio', 'verde', 'verde',
                                       inicio='izquierda-superior')),
    Círculo(400, 50, 50, relleno=gradiente('marVerdeMedio', 'verde', 'verde',
                                      inicio='izquierda-superior')))
    arbol.centroY=250
                                      
    #Cartel
    cartel=Grupo(
    Rect(150, 170, 100, 50, relleno='verde',borde='blanco', anchuraDeBorde=4),
    Rótulo('Procesadora', 200, 190, relleno='azul', tamaño=16))
    cartel.centroX=250
    cartel.centroY=50
    cartel.rotarAngulo =8
    
    #
    logo=Grupo(
    Circulo(120,115,10,relleno=None,borde='blanco',anchuraDeBorde=3),
    Linea(100,115,150,115,relleno='gainsboro',anchuraDeLinea=5),
    PoligonoRegular(112,112,5,3,relleno='blanco',rotarAngulo=-7),
    PoligonoRegular(128,118,5,3,relleno='blanco',rotarAngulo=25))
    logo.centroX=240
    logo.centroY=110
    logo.rotarAngulo=-16
    
    
    Linea(287,300,287,370,relleno='madera',anchuraDeLinea=6)
    Rect(230, 300, 60, 30,relleno='amarillo')
    Rect(230, 315, 60, 30,relleno='azul')
    Rect(230, 330, 60, 20,relleno='rojo')
    
    carro_de_basura=Grupo(
    Rect(67,125,120,20),
    Poligono(60,130,60,92,74,77,180,77,180,130,60,130,relleno='verdeAmarillento',borde='verde'),
    Linea(90,77,90,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Linea(108,77,108,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Linea(128,77,128,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Linea(148,77,148,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Linea(166,77,166,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Linea(74,77,74,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
    Rect(155,132,27,15,relleno='grisClaro'),
    
    
    #llantas
    Circulo(92,149,13),
    Circulo(130,149,13),
    Circulo(210,149,13),
    Circulo(92,149,9,relleno='gris'),
    Circulo(130,149,9,relleno='gris'),
    Circulo(210,149,9,relleno='gris'),
    Circulo(92,149,6,relleno='grisClaro'),
    Circulo(130,149,6,relleno='grisClaro'), 
    Circulo(210,149,6,relleno='grisClaro'),
    
    Circulo(92,145,1),
    Circulo(130,145,1),
    Circulo(210,146,1),
    
    Circulo(92,152,1),
    Circulo(130,152,1),
    Circulo(210,152,1),
    
    Circulo(89,149,1),
    Circulo(126,149,1),
    Circulo(205,149,1),
    
    Circulo(95,148,1),
    Circulo(134,149,1),
    Circulo(214,149,1),
    #
    Poligono(188,88,214,88,235,113,235,145,229,146,195,140,187,140,188,88,relleno='verdeAmarillento'),
    Rect(234,121,3,4,relleno='rojo'),
    Rect(228,133,10,10,relleno='blanco'),
    Poligono(195,93,214,93,226,115,195,115,relleno='azulCielo',borde='negro'),
    #EMPRESA
    Rotulo('TRASH',120,92,tamaño=20),
    Circulo(120,115,10,relleno=None,borde='blanco',anchuraDeBorde=3),
    Linea(100,115,150,115,relleno='verdeAmarillento',anchuraDeLinea=5),
    Linea(68,137,58,137,anchuraDeLinea=6),
    Rect(56,135,2,4,relleno='rojo'),
    PoligonoRegular(112,112,5,3,relleno='blanco',rotarAngulo=-7),
    PoligonoRegular(128,118,5,3,relleno='blanco',rotarAngulo=25))
    carro_de_basura.centroX=140
    carro_de_basura.centroY=250
    carro_de_basura.rotarAngulo=-54


#Fondo y sol
Rect(0,0,400,400,relleno=gradiente('azulGandul','salmon','oro',inicio='superior'))
Circulo(0,260,40,relleno=gradiente('oro','naranja','amarillo'))
#Estrella(0,260,40,10,relleno=gradiente('naranja','oro'))
#nuves
Circulo(240,0,60,relleno='blanco')
Circulo(30,0,60,relleno='blanco')
Circulo(130,0,60,relleno='blanco')
Circulo(350,0,60,relleno='blanco')
#carretera
Poligono(400,220,260,260,160,400,210,350,400,275,relleno='gris')
Poligono(400,275,210,350,210,400,400,400,relleno='tierra')
Rect(0,260,260,140,relleno='azulGandul')
Linea(260,290,400,245,relleno=gradiente('gris','plateado'),anchuraDeLinea=3,guión=(10,2))

#muelle
Linea(172,320,260,400,relleno='marrón',anchuraDeLinea=4)
Linea(172,320,170,400,relleno='marrón',anchuraDeLinea=4)
Linea(170,260,190,400,relleno='marrón',anchuraDeLinea=4)
Poligono(166,260,260,260,260,332,170,332,170,260,relleno=gradiente('naranjaMarrón','tierra',inicio='izquierda'))


#bandera
barco=Grupo(
Poligono(135,150,135,200,70,190,relleno=gradiente('amarillo','amarillo','verde',inicio='superior-izquierda')
,borde='negro'),
Linea(135,265,135,160,relleno='negro',anchuraDeLinea=14),
Circulo(135,160,10,relleno='madera',borde='negro'),
Linea(135,265,135,160,relleno='madera',anchuraDeLinea=10),
#Barco
Poligono(205,225,170,265,100,265,60,225,relleno='madera',borde='negro'),
Óvalo(100,245,10,10,relleno='azulCielo',borde='negro'),
Óvalo(115,245,10,10,relleno='azulCielo',borde='negro'),
Óvalo(130,245,10,10,relleno='azulCielo',borde='negro'),
Poligono(205,225,193,236,75,236,60,225,relleno='verde',borde='negro'))
barco.centroX=-40
barco.centroY=230
pala=Grupo(
Linea(205,225,216,333,relleno='madera',anchuraDeLinea=4),
Ovalo(216,333,30,35,relleno='madera'))
pala.centroX=40
pala.centroY=310
#carro
carro_de_basura=Grupo(
Rect(67,125,120,20),
Poligono(60,130,60,92,74,77,180,77,180,130,60,130,relleno='verdeAmarillento',borde='verde'),
Linea(90,77,90,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Linea(108,77,108,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Linea(128,77,128,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Linea(148,77,148,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Linea(166,77,166,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Linea(74,77,74,129,relleno='verde',anchuraDeLinea=1,guión=(15,2)),
Rect(155,132,27,15,relleno='grisClaro'),


#llantas
Circulo(92,149,13),
Circulo(130,149,13),
Circulo(210,149,13),
Circulo(92,149,9,relleno='gris'),
Circulo(130,149,9,relleno='gris'),
Circulo(210,149,9,relleno='gris'),
Circulo(92,149,6,relleno='grisClaro'),
Circulo(130,149,6,relleno='grisClaro'), 
Circulo(210,149,6,relleno='grisClaro'),

Circulo(92,145,1),
Circulo(130,145,1),
Circulo(210,146,1),

Circulo(92,152,1),
Circulo(130,152,1),
Circulo(210,152,1),

Circulo(89,149,1),
Circulo(126,149,1),
Circulo(205,149,1),

Circulo(95,148,1),
Circulo(134,149,1),
Circulo(214,149,1),
#
Poligono(188,88,214,88,235,113,235,145,229,146,195,140,187,140,188,88,relleno='verdeAmarillento'),
Rect(234,121,3,4,relleno='rojo'),
Rect(228,133,10,10,relleno='blanco'),
Poligono(195,93,214,93,226,115,195,115,relleno='azulCielo',borde='negro'),
#EMPRESA
Rotulo('TRASH',120,92,tamaño=20),
Circulo(120,115,10,relleno=None,borde='blanco',anchuraDeBorde=3),
Linea(100,115,150,115,relleno='verdeAmarillento',anchuraDeLinea=5),
Linea(68,137,58,137,anchuraDeLinea=6),
Rect(56,135,2,4,relleno='rojo'),
PoligonoRegular(112,112,5,3,relleno='blanco',rotarAngulo=-7),
PoligonoRegular(128,118,5,3,relleno='blanco',rotarAngulo=25))
carro_de_basura.centroX=300
carro_de_basura.centroY=250
carro_de_basura.rotarAngulo=-16

#


#basura
basura=Grupo(
Rect(120,300,24,10,relleno='verde'),
Rect(117,302,3,5),

Rect(90,320,24,10,relleno='blanco'),
Rect(87,322,3,5),

Circulo(45,300,20,relleno=None,borde='negro',anchuraDeBorde=8),
Poligono(90,346,62,338,44,357,78,371,96,345,94,343,relleno='blanco'),

Rect(120,340,10,10,relleno='rojo'),
Ovalo(125,340,10,5),
Poligono(127,350,104,350,115,360),
Ovalo(115,377,27,40),
Linea(112,359,119,359,relleno='blanco'))
basura.centroY=330
#pala

mensaje=Rotulo('presiona tecla izquierda',177,105,tamaño=20)
    


def mover_carro():
        carro_de_basura.centroX+=4
        carro_de_basura.centroY-=2


def enTeclaRetenida(tecla):
    if 'izquierda' in tecla and barco.centroX<140:
        barco.centroX+=4
        basura.centroX +=3
        basura.centroY -=1
        pala.centroX +=4

    if basura.centroX>160:
        pala.rotarAngulo =-50
    if basura.centroX>210:
        basura.visible=False
        mensaje.valor='presiona tecla derecha'
        if 'derecha' in tecla:
            mover_carro()
    if carro_de_basura.centroX>480:
        procesadora()
        mover_carro()
   
       

cmu_graphics.run()