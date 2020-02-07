##Librerias

##Para hacer la ventana visual
from tkinter import *
##Para las cajas de mensaje
from tkinter import messagebox
##Para las combobox
from tkinter import ttk
import tkinter as tk
##Para los tiempos de duración de los Gif´s
import time
##Para mostrar los datos de la base de datos con espacios
from random import randint
##Para la Conexion a Base de Datos
import pymysql
##Para abrir las ventanas de los catalogos
import subprocess

##Ubicacion de los jugadores y la ignorancia 
x1 = 5
y1 = 246
x2 = 5
y2 = 335
xI = 5
yI = 417

##Id's definidos para usarlos con la conexión con la base de datos
idmateria = ""
idplayer = ""

##Diseño de la Ventana del juego
game = Tk()
game.resizable(0,0)
game.title ("Game of the Ignorance")
game.iconbitmap("Icono.ico")
game.geometry("1000x480")
game.config(bg ="Black")

##Str´s de las Entry´s
str_ale = StringVar()
str_ale.set("")
str_nom = StringVar()
str_nom.set("")
str_id = StringVar()
str_id.set("")
str_aux = StringVar()
str_aux.set("")
str_op1 = StringVar()
str_op1.set("")
str_op2 = StringVar()
str_op2.set("")
str_op3 = StringVar()
str_op3.set("")
str_op3.set("")
str_opc = StringVar()
str_opc.set("")

##Contadores
Cont1 = StringVar()
Cont1.set("0")
Num1 = StringVar()
Num1.set("1")
Cont2 = StringVar()
Cont2.set("0")
Num2 = StringVar()
Num2.set("1")

##Posición
Posición = StringVar()
Posición.set("PLAYER-1")
v1=StringVar()
v1.set("1")
v2=StringVar()
v2.set("2")
##Definiciones
##Para la concexión con la base de datos
maximo = 0

##Para seleccionar las Radiobutton´s
seleccion = IntVar()
##Para el turno de los Jugadores y la ignorancia
turno = 1

##Imagenes Png´s
dados = PhotoImage(file = "dados.png")
grunt = PhotoImage(file = "grunt.png")
pista = PhotoImage(file = "pista.png")
j1 = PhotoImage(file = "mongoose.png")
j2 = PhotoImage(file = "ghost.png")
question = PhotoImage(file = "reach.png")
noble_team = PhotoImage(file = "noble_team.png")
gif = PhotoImage(file = "fond.png")
reset_m = PhotoImage(file = "reset3.png")
reset_g = PhotoImage(file = "reset_game.png")
meta = PhotoImage(file = "meta.png")

##Def´s para abrir las ventanas de los catalogos de Usuario, Materia y Preguntas
def cat_materia():
	subprocess.Popen(["python" , "cat-materia.py"])
def cat_pregunta():
	subprocess.Popen(["python" , "cat-pregunta.py"])
def cat_usuario():
	subprocess.Popen(["python" , "cat-usuario.py"])

##Def´s de los Gif´s de jugador 

##Celebra Jugador 1
def celebra_player1():
	##Abre la carpeta correspondiente y los archivos PNG's
	vec_img = [PhotoImage(file = "./gifplayer1/player1-01.gif")] 
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-02.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-03.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-04.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-05.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-06.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-07.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-08.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-09.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-10.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-11.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-12.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-13.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-14.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-15.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-16.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-17.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-18.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-19.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-20.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-21.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-22.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-23.gif"))                                                                                                                                                                                                                                                                                                                       
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-24.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-25.gif"))	
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-26.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-27.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-28.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-29.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-30.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-31.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-32.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-33.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-34.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-35.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-36.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-37.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-38.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-39.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-40.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-41.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-42.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer1/player1-43.gif"))

	##Para mostrar las images en un rango de 1 a la numero 43, p se configura como vector y ejecuta en tiempo de .1
	for x in range(1,43):
		p.config(image = vec_img[x])
		game.update()
		time.sleep(.1)
	p.config(image = gif)
	game.update()
##Celebra Jugador 2
def celebra_player2():
	##Abre la carpeta correspondiente y los archivos PNG's
	vec_img = [PhotoImage(file = "./gifplayer2/player2-01.gif")] 
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-02.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-03.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-04.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-05.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-06.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-07.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-08.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-09.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-10.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-11.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-12.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-13.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-14.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-15.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-16.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-17.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-18.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-19.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-20.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-21.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-22.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-23.gif"))                                                                                                                                                                                                                                                                                                                      
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-24.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-25.gif"))	
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-26.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-27.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-28.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-29.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-30.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-31.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-32.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-33.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-34.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-35.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-36.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-37.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-38.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-39.gif"))
	vec_img.append(PhotoImage(file = "./gifplayer2/player2-40.gif"))

	##Para mostrar las images en un rango de 1 a la numero 40, p se configura como vector y ejecuta en tiempo de .1
	for x in range(1,40):
		p.config(image = vec_img[x])
		game.update()
		time.sleep(.1)
	p.config(image = gif)
	game.update()
##Celebra Ignorancia
def celebra_ignorance():
	##Abre la carpeta correspondiente y los archivos PNG's
	vec_img = [PhotoImage(file = "./gifignorance/ignorance-01.gif")] 
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-02.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-03.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-04.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-05.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-06.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-07.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-08.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-09.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-10.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-11.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-12.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-13.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-14.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-15.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-16.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-17.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-18.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-19.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-20.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-21.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-22.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-23.gif"))                                                                                                                                                                                                                                                                                                                       
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-24.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-25.gif"))	
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-26.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-27.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-28.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-29.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-30.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-31.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-32.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-33.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-34.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-35.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-36.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-37.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-38.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-39.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-40.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-41.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-42.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-43.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-44.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-45.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-46.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-47.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-48.gif"))
	vec_img.append(PhotoImage(file = "./gifignorance/ignorance-49.gif"))
	##Para mostrar las images en un rango de 1 a la numero 43, p se configura como vector y ejecuta en tiempo de .1
	for x in range(1,49):
		p.config(image = vec_img[x])
		game.update()
		time.sleep(.1)
	p.config(image = gif)
	game.update()
##Def para conexion para mostrar las materias de la combobox de materia
def lista_materias():
	## Combo de Usuarios
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
	cursor = conn.cursor()
	cursor.execute('select Descripcion from materia')
	mts = []
	for row in cursor:
		mts.append(row[0])
	cursor.close()
	conn.close()
	return mts
##Def para conexión para mostrar los usuarios de las combobbox´s de usuario
def lista_players():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
	cursor = conn.cursor()
	cursor.execute('select Nombre from usuario')
	ply = []
	for row in cursor:
		ply.append(row[0])
	cursor.close()
	conn.close()
	return ply
##Def para la combobox de materia usando global's para agregar con espacios 
def materia(event):
	global idmateria
	global maximo
	men = mat.get()
	sql = "select id_materia from materia where descripcion='" + men + "'"
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	cursor.execute(sql)
	idmateria = cursor.fetchone()[0]
	sql = "select max(id_pregunta) from pregunta"
	cursor.execute(sql)
	maximo = cursor.fetchone()[0]
	Dados.config(state = NORMAL)
	mat.config(state = DISABLED)	
	##messagebox.showinfo(message=idmateria)
##Def para la combobox de jugador 1 usando global's para agregar con espacios 
def player_1 (event):
	global idplayer
	global maximo
	plyer=playr.get()
	sql = "select Id_usuario from usuario where Nombre ='" + plyer +"'"
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	cursor.execute(sql)
	idplayer = cursor.fetchone()[0]
	sql = "select max(Id_usuario) from usuario"
	cursor.execute(sql)
	maximo = cursor.fetchone()[0]
	playr.config(state = DISABLED)
	mat.config(state = NORMAL)	
##Def para la combobox de jugador 2 usando global´s para agregar con espacios 
def player_2 (event):
	global idplayer
	global maximo
	plyer1=playr1.get()
	sql = "select Id_usuario from usuario where Nombre ='" + plyer1 +"'"
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	cursor.execute(sql)
	idplayer = cursor.fetchone()[0]
	sql = "select max(Id_usuario) from usuario"
	cursor.execute(sql)
	maximo = cursor.fetchone()[0]
	playr1.config(state = DISABLED)
	playr.config(state = NORMAL)
##Def usado despues de seleccionar el boton de dados que muestra la pregunta, opciones y saca un alateorio
def mostrar_pregunta():
	global idmateria
	global maximo
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	registros = 0
	while registros==0:
		str_ale.set(str(randint(0,maximo)))
		sql = "select count(*) from pregunta where Id_materia=" + str(idmateria) + " and Id_pregunta =" + str_ale.get()
		cursor.execute(sql)
		registros = cursor.fetchone()[0]
	sql = "select id_pregunta, Descripcion, opcion1, opcion2, opcion3, correcto from pregunta where id_materia="
	sql = sql + str(idmateria) + " and id_pregunta=" + str_ale.get()
	cursor.execute(sql)
	for row in cursor:
		str_nom.set(row[1])
		str_op1.set(row[2])
		str_op2.set(row[3])
		str_op3.set(row[4])
		str_opc.set(row[5])
	image_question.place(x = 360, y = 18)
	fond_pregunta.config(width = 26)
	fond_pregunta.place(x = 470, y = 30)
	text_pregunta.config(width = 52)
	text_pregunta.place(x = 375, y = 60)
	select_opc1.config(width = 0)
	select_opc1.place(x = 380, y = 95)
	opc1.config(width = 15)
	opc1.place(x = 415, y = 96)
	select_opc2.config(width = 0)
	select_opc2.place(x = 380, y = 130)
	opc2.config(width = 16)
	opc2.place(x = 415, y = 131)
	select_opc3.config(width = 0)
	select_opc3.place(x = 380, y = 165)
	opc3.config(width = 15)
	opc3.place(x = 415, y = 166)
	cursor.close()
	db.close()
##Def para el boton de dado en cuanto se selecciona se hace pequeño el dado y muestra la pregunta(mostrar_pregunta)
def selec_pregunta():
	Dados.config(height = 3)
	Dados.config(width = 3)
	image_question.config(height = 190)
	image_question.config(width = 450)
	mostrar_pregunta()
	##raiz.update()
##Def para que avance el jugador 1 y muestre el mensaje cuando llegue a la linea meta
def avanza_p1():
	global turno
	global x1
	global y1
	x1 = x1 + 100
	player1.place(x=x1, y=y1)
	if x1>=943:
		celebra_player1()
		Cont1.set(int(Cont1.get()) +  int(Num1.get()))
		messagebox.showinfo("B U N G I E", message = "Congratulation the Player " +  playr.get()  + " has won")
		Reset_game.config(state = NORMAL)
		Reset_marcador.config(state = NORMAL)
		Dados.config(state = DISABLED)
		mat.config(state = DISABLED)
		playr.config(state = DISABLED)
		playr1.config(state = DISABLED)
		player1.config(state = DISABLED)
		player2.config(state = DISABLED)
		ignorance.config(state = DISABLED)
	turno = 2
##Def para que avance el jugador 2 y muestre el mensaje cuando llegue a la linea meta
def avanza_p2():
	global turno
	global x2
	global y2
	x2 = x2 + 100
	player2.place(x=x2, y=y2)
	if x2>=943:
		celebra_player2()
		Cont2.set(int(Cont2.get()) +  int(Num2.get()))			
		messagebox.showinfo("B U N G I E" , message = "Congratulation the Player " +  playr1.get()  + " has won")
		Reset_game.config(state = NORMAL)	
		Reset_marcador.config(state = NORMAL)
		Dados.config(state = DISABLED)
		mat.config(state = DISABLED)
		playr.config(state = DISABLED)
		playr1.config(state = DISABLED)	
		player1.config(state = DISABLED)
		player2.config(state = DISABLED)
		ignorance.config(state = DISABLED)
	turno = 1
##Def para que avance la ignorancia y muestre el mensaje cuando llegue a la linea meta
def avanza_ignorance():
	global turno
	global xI
	global yI
	xI = xI + 100
	ignorance.place(x = xI, y = yI)
	if turno==1:
		turno = 2
	else:
		turno = 1
	if xI>= 943:

		celebra_ignorance()
		messagebox.showinfo("B U N G I E" , message = "The Ignorance has won")
		Reset_game.config(state = NORMAL)	
		Reset_marcador.config(state = NORMAL)
		Dados.config(state = DISABLED)
		mat.config(state = DISABLED)
		playr.config(state = DISABLED)
		playr1.config(state = DISABLED)
		player1.config(state = DISABLED)
		player2.config(state = DISABLED)
		ignorance.config(state = DISABLED)
##Def para validar si la respuesta seleccionada es correcta, arroja el mensaje y manda la accion para que avance a quien le corresponda
def seleccionado():
	global turno
	global xI
	global yI
	global x2
	global y2
	if str(seleccion.get())==str_opc.get():
		messagebox.showinfo("B U N G I E" , message = "Your Answer is Correct")
		if turno==1:
			avanza_p1()
			Posición.set("PLAYER-2")

		else:
			avanza_p2()
			Posición.set("PLAYER-1")

	else:
		messagebox.showinfo("B U N G I E" , message = "Your Answer is Incorrect")
		avanza_ignorance()
		Posición.set("PLAYER-1")
	seleccion.set(" ")
	aleatorio.config(state = DISABLED)
	str_ale.set("") 
	mat.config(state = NORMAL)
	mat.set("")
	Dados.config(height=180)
	Dados.config(width=210)
	image_question.config(height=3)
	image_question.config(width=3)
	fond_pregunta.config(width=0)
	fond_pregunta.place(x=780, y=20)
	text_pregunta.config(width=0)
	text_pregunta.place(x=780, y=40)
	select_opc1.config(width=0)
	select_opc1.place(x=780, y=60)
	opc1.config(width=0)
	opc1.place(x=800, y=60)
	select_opc2.config(width=0)
	select_opc2.place(x=780, y=80)
	opc2.config(width=0)
	opc2.place(x=800, y=80)
	select_opc3.config(width=0)
	select_opc3.place(x=780, y=100)
	opc3.config(width=0)
	opc3.place(x=800, y=100)
	str_nom.set("")
	str_id.set("")
	str_op1.set("")
	str_op2.set("")
	str_op3.set("")
	str_opc.set("")
##Def para resetear el juego
def reset_game():
	mat.config(state = DISABLED)
	playr.config(state = DISABLED)
	playr1.config(state = NORMAL)
	Reset_game.config(state = DISABLED)
	Reset_marcador.config(state = DISABLED)
	player1.config(state = NORMAL)
	player2.config(state = NORMAL)
	ignorance.config(state = NORMAL)
	playr1.set("")
	playr.set("")
	aleatorio.config(state = DISABLED)
	str_ale.set("")
	player1.place(x = 5, y = 246)
	player2.place(x = 5, y = 335)
	ignorance.place(x = 5, y = 417)
	fond_pregunta.config(width=0)
	fond_pregunta.place(x=780, y=20)
	text_pregunta.config(width=0)
	text_pregunta.place(x=780, y=40)
	select_opc1.config(width=0)
	select_opc1.place(x=780, y=60)
	opc1.config(width=0)
	opc1.place(x=800, y=60)
	select_opc2.config(width=0)
	select_opc2.place(x=780, y=80)
	opc2.config(width=0)
	opc2.place(x=800, y=80)
	select_opc3.config(width=0)
	select_opc3.place(x=780, y=100)
	opc3.config(width=0)
	opc3.place(x=800, y=100)
	str_nom.set("")
	str_id.set("")
	str_op1.set("")
	str_op2.set("")
	str_op3.set("")
	str_opc.set("")
	Posición.set("PLAYER-1")
##Def para restear el marcadores, y combobox´s
def reset_marcador():
	Cont1.set("0")
	Num1.set("1")
	Cont2.set("0")
	Num2.set("1")
	mat.config(state = DISABLED)
	playr.config(state = NORMAL)
	playr1.config(state = NORMAL)
	Reset_marcador.config(state = DISABLED)
	playr1.set("")
	playr.set("")
	mat.set("")

##Imagen de fondo abajo de todo
diseño = Label(game, bg = "Black", image = noble_team)
diseño.place(x = 1, y = 1)
##Combobox para seleccionar Materia, conectada a la base de datos
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 12 bold', text = "Materia", width = 8, height = 1).place(x = 8, y = 48)
mat = ttk.Combobox(game, font = "Arial 10 bold", width = 12, state = DISABLED)
mat.place(x = 104, y = 50)
mat.bind("<<ComboboxSelected>>", materia)
lista = lista_materias()
mat["values"] = lista

##Combobox´s para seleccionar Usuarios, conectada a la base de datos
Label(game, bg = "DarkKhaki", fg = "Black", font = "Arial 12 bold", text = "Player", width = 8, height = 1).place(x = 8, y = 90)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 12 bold', textvariable = Cont1, width = 1,).place(x = 235, y = 79)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 12 bold', textvariable = Cont2, width = 1,).place(x = 235, y = 109)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 11 bold', textvariable = Posición, width = 9).place(x = 72, y = 205)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 11 bold', text = "TURNO", width = 6).place(x = 8, y = 205)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 11 bold', text = "AC", width = 3).place(x = 65, y = 152)
Label(game, bg = "DarkKhaki", fg = "Black", font = 'Arial 11 bold', text = "AG", width = 3).place(x = 235, y = 152)
playr = ttk.Combobox(game, font = "Arial 10 bold", width = 15, state = DISABLED)
playr.place(x = 104, y = 80)
playr.bind("<<ComboboxSelected>>", player_1)
lista = lista_players()
playr["values"] = lista
playr1 = ttk.Combobox(game, font = "Aria 10 bold", width = 15)
playr1.place(x = 104, y = 110)
playr1.bind("<<ComboboxSelected>>", player_2)
lista = lista_players()
playr1["values"] = lista

##Entry de opción correcta antes de las otras Entry´s para estar oculta
opcc = Entry(game, bg = "Black", fg = "White", textvariable = str_opc, font = "Arial 11 bold", width = 0)
opcc.place(x = 780, y = 120)


##Entry para la pregunta Aleatoria
aleatorio = Entry(game, textvariable = str_ale, font = "Arial 11 bold", width = 1, state = DISABLED)
aleatorio.place(x = 215, y = 50)

image_question = Label(game, image = question, bg = "Black", relief = "ridge", width = 3, height = 3)
image_question.place(x = 780 , y = 1)
##Label´s de la pregunta y texto

fond_pregunta = Label(game, bg = "Brown", fg = "White", text = "Pregunta", font = "Arial 11 bold", width = 0)
fond_pregunta.place(x = 780, y = 20)
text_pregunta = Entry(game, textvariable = str_nom, font = "Arial 11 bold", width = 0)
text_pregunta.place(x = 780, y = 40)

##Entry's encima del fondo que dan las Opciones de las preguntas
opc1 = Entry(game, bg = "Black", fg = "White", textvariable = str_op1, font = "Arial 13 bold", width = 0)
opc1.place(x = 800, y = 60)
opc2 = Entry(game, bg = "Black", fg = "White", textvariable = str_op2, font = "Arial 13 bold", width = 0)
opc2.place(x = 800, y = 80)
opc3 = Entry(game,  bg = "Black", fg = "White", textvariable = str_op3, font = "Arial 13 bold", width = 0)
opc3.place(x = 800, y = 100)

##Radiobutton's para validar la opcion correcta con comando seleccionado y variable de selección para marcarla
select_opc1 = Radiobutton(game, value = 1, variable = seleccion, command = seleccionado, width = 0)
select_opc1.place(x = 780, y = 60)
select_opc2 = Radiobutton(game, value = 2, variable = seleccion, command = seleccionado, width = 0)
select_opc2.place(x = 780, y = 80)
select_opc3 = Radiobutton(game, value = 3, variable = seleccion, command = seleccionado, width = 0)
select_opc3.place(x = 780, y = 100)

##Pista´s de los Jugadores en Label´s
pista_j1 = Label(game, bg = "Black", relief = "ridge", width = 500, height = 5)
pista_j1.place(x = 1, y = 235)
pista_j2 = Label(game, bg = "Black", relief = "ridge", width = 500, height = 5)
pista_j2.place(x=1, y=320)
pista_Ign = Label(game, bg = "Black", relief = "ridge", width = 500, height = 5)
pista_Ign.place(x = 1, y = 405)

##Player´s con imagen sobre sus referentes pistas
player1 = Label(game, bg = "Black", relief="flat", image = j1 ) 
player1.place(x = x1, y = y1)
player2 = Label(game, bg = "Black", relief="flat", image = j2)
player2.place(x = x2, y = y2)
ignorance = Label(game, bg = "Black", image = grunt)
ignorance.place(x = xI, y = yI)

##Meta's para cada pista con imagen
Meta = Label(game, image = meta).place(x = 943, y = 237)
Meta = Label(game, image = meta).place(x = 943, y = 322)
Meta = Label(game, image = meta).place(x = 943, y = 407)

##Dados con cursor de mause, con imagen, comando sel_pregunta y DESABILITADO
Dados= Button(game, cursor = "mouse", bg = "Black", image = dados, command = selec_pregunta, width = 210, height = 180, state = DISABLED)
Dados.place(x = 780, y = 8)

##Boton Reset Game con cursor de mause, con imagen, comando Reset_game
Reset_marcador = Button(game, cursor = "mouse", bg = "Black" , image = reset_m, command = reset_marcador, state = DISABLED)
Reset_marcador.place(x = 104, y = 143)
Reset_game = Button(game, cursor = "mouse", bg = "Black" , image = reset_g, command = reset_game, state = DISABLED)
Reset_game.place(x = 170, y = 141)
##Botones con comandos que abren los catalogos, y con cursores mause
U = Button(game, command = cat_usuario, bg = "DarkKhaki", font = "Arial 12 bold", text = "Usuario", cursor = "mouse", width = 8, height = 1).place(x = 8, y = 10)
M = Button(game, command = cat_materia, bg = "DarkKhaki", font = "Arial 12 bold", text = "Materia", cursor = "mouse", width = 8, height = 1).place(x = 104, y = 10)
P = Button(game, command = cat_pregunta, bg = "DarkKhaki", font = "Arial 12 bold", text = "Preguntas", cursor = "mouse", width = 8, height = 1).place(x = 200, y = 10)

##Pixel en la esquina de la pantalla que muestra los Gif´s cuando hay un ganador
p = Label(game, image = gif)
p.place(x = 1, y = 1)

##Cierra Juego
game.mainloop()