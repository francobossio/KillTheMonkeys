# coding: utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random
TIEMPO = 4
fin_de_juego = False
pilas = pilasengine.iniciar()
# Usar un fondo estándar
pilas.fondos.Pasto()
# Añadir el conmutador de Sonido
pilas.actores.Sonido()
# Variables y Constantes
bala = pilas.actores.Bala
monos = []
# Funciones
def mono_destruido(bala, mono):
    mono.eliminar()
    bala.eliminar()
    puntos.aumentar(1)
    puntos.escala=[3,1,]


def crear_mono():
	# Crear un enemigo nuevo
    enemigo = pilas.actores.Mono()
    enemigo.rotacion=(1080)
    efecto=random
    enemigo.escala=[2,.4]

	    # Hacer que se aparición sea con un efecto bonito
	##la escala varíe entre 0,25 y 0,75 (Ojo con el radio de colisión)
    enemigo.escala = .4
	# Dotarle de la habilidad de que explote al ser alcanzado por un 	disparo
    enemigo.aprender(pilas.habilidades.PuedeExplotar)
	# Situarlo en una posición al azar, no demasiado cerca del jugador
    x = random.randrange(-320, 320)
    y = random.randrange(-240, 240)
    if x >= 0 and x <= 100:
        x = 180
    elif x <= 0 and x >= -100:
        x = -180
    if y >= 0 and y <= 100:
        y = 180
    elif y <= 0 and y >= -100:
		y = -180
    enemigo.x = x
    enemigo.y = y
# Dotarlo de un movimiento irregular más impredecible	
    tipo_interpolacion = ['lineal',
	'aceleracion_gradual',
	'desac	eleracion_gradual',
	'rebote_inicial',
	'rebote_final']	
    duracion = 3 +random.random()*5
    pilas.utils.interpolar(enemigo, 'x', 0, duracion)
    pilas.utils.interpolar(enemigo, 'y', 0, duracion)
#enemigo.x = pilas.interpolar(0,tiempo,tipo=random.choice(tipo_interpolacion))
#enemigo.y = pilas.interpolar(0, tiempo,tipo=random.choice(tipo_interpolacion))
# Añadirlo a la lista de enemigos
    monos.append(enemigo)
# Permitir la creación de enemigos mientras el juego esté en activo
    if fin_de_juego:
        return False
    else:
        return True
# Añadir la torreta del jugador
torreta = pilas.actores.Torreta(enemigos=monos, cuando_elimina_enemigo=mono_destruido)
pilas.tareas.agregar(1, crear_mono)
puntos=pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.amarillo)
puntos.magnitud= 40
def cuando_colisiona(enemigo, bala):
    enemigo.eliminar()
    bala.eliminar()
    texto1=pilas.actores.Texto("FIN DEL JUEGO")
    texto1.y=0
    texto1.escala=[3,1,3]
    texto2=pilas.actores.Texto("TU PUNTAJE ES:")
    texto2.y=-100
    puntos.y=10
    puntos.x 20


    fin_de_juego=True
#pilas.mundo.agregar_tarea(1, crear_mono) <-- sintaxis vieja
# Arrancar el juego
pilas.colisiones.agregar(torreta, monos, cuando_colisiona)
pilas.ejecutar()
pilas.ejecutar()