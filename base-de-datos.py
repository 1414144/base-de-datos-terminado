from cProfile import label
from cgitb import text
from email import message
from enum import auto
from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.simpledialog import SimpleDialog
import mysql.connector

#------------------ventana-------------------------------

j = Tk()
j.title('Biblioteca virtual')
j.geometry('500x300')
j.config(bg='#A8EBE7')
j.resizable(0,0)

#-------------------------------mysql-------------------------------------------------------------------

conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="")
bd=conexion.cursor()
bd.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
bd.close()

conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="biblioteca")
bd=conexion.cursor()
bd.execute("CREATE TABLE IF NOT EXISTS inventario(Codigo VARCHAR(25),Libro VARCHAR(55),Autor VARCHAR(55),Año_Publicado VARCHAR(55),genero VARCHAR(55))")
bd.execute("CREATE TABLE IF NOT EXISTS cliente(Identificacion VARCHAR(25),Nombre VARCHAR(55),Seccion VARCHAR(55))")
bd.execute("CREATE TABLE IF NOT EXISTS prestamo(cod_libro VARCHAR(25),Nombre_libro VARCHAR(55),Genero_libro VARCHAR(55),cantidad VARCHAR(55),identificacion_cliente VARCHAR(55),nombre_cliente VARCHAR(55))")
bd.close()

#--------------------------ventana secundaria-------------------------------

def pantalla_inventario ():
    def agregar_libro():
        cur=conexion.cursor()
        cod=txt_codigo.get()
        lib=txt_libro.get()
        aut=txt_autor.get()
        an=txt_año.get()
        gen=txt_genero.get()
        cur.execute("insert into inventario(Codigo,Libro,Autor,Año_publicado,genero)values('{}','{}','{}','{}','{}')".format(cod,lib,aut,an,gen))
        conexion.commit()#actualizar el envio de datos
        cur.close()
        messagebox.showinfo(message="El nuevo libro se guardo en forma exitosa",title="informacion")
        txt_codigo.delete(0,END)
        txt_libro.delete(0,END)
        txt_autor.delete(0,END)
        txt_año.delete(0,END)
        txt_genero.delete(0,END)
        txt_codigo.focus()
    def buscar_libro():
        cur=conexion.cursor()
        cur.execute("select * from inventario")
        datos=cur.fetchall()
        txt_libro.delete(0,END)
        txt_autor.delete(0,END)
        txt_año.delete(0,END)
        txt_genero.delete(0,END)
        for columna in datos:
            if columna[0]==txt_codigo.get():
                txt_libro.insert(0,columna[1])
                txt_autor.insert(0,columna[2])
                txt_genero.insert(0,columna[3])
                txt_año.insert(0,columna[4])
        #txt_codigo.delete(0,END)
        txt_codigo.focus()
        cur.close()
        
                  
  #----------------------------------------------------------------------------------------------       
    inventario = Tk()
    inventario.title('Biblioteca virtual')
    inventario.geometry('800x400')
    inventario.config(bg='#A8EBE7')
    inventario.resizable(0,0)
    
 #------------------------titulo de la segunda ventana-------------------------------

    etiqueta_inventario = Label (inventario,font=('century',18,'bold'),text='INVENTARIO',bg='#A8EBE7',width=20,height=1,bd=5,fg="#E31C1C")
    etiqueta_inventario.place(x=25,y=10)
 
    etiqueta_codigo = Label (inventario,font=('century',14,'bold'),text='CODIGO',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_codigo.place(x=1,y=80)

    etiqueta_libro = Label (inventario,font=('century',14,'bold'),text='LIBRO',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_libro.place(x=1,y=130)

    etiqueta_autor = Label (inventario,font=('century',14,'bold'),text='AUTOR',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_autor.place(x=1,y=180)

    etiqueta_año = Label (inventario,font=('century',14,'bold'),text='Año de la Publicación',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_año.place(x=5,y=240)

    etiqueta_genero = Label (inventario,font=('century',14,'bold'),text='GENERO',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_genero.place(x=450,y=240)

 #------------------------------entry-----------------------------------------------------

    txt_codigo = Entry(inventario,font=('century',18,'bold'),width=17,)
    txt_codigo.place(x=230,y=80)
    txt_codigo.bind("<Return>",(lambda event:buscar_libro()))

    txt_libro = Entry(inventario,font=('century',18,'bold'),width=17,)
    txt_libro.place(x=230,y=130)

    txt_autor = Entry(inventario,font=('century',18,'bold'),width=17,)
    txt_autor.place(x=230,y=180)

    txt_año = Entry(inventario,font=('century',18,'bold'),width=17,)
    txt_año.place(x=230,y=240)

    txt_genero = Entry(inventario,font=('century',18,'bold'),width=12,)
    txt_genero.place(x=600,y=240)


    #---------------------------------boton----------------------------------------

    boton_inventario = Button(inventario , text="Agregar Libro",width=30,height=3,command=agregar_libro)
    boton_inventario.place(x=300,y=295)

    boton_buscar = Button(inventario , text="buscar",width=25,height=2,command=buscar_libro)
    boton_buscar.place(x=500,y=80)

#-------------------------tercera ventana--------------------------------

def pantalla_prestamos ():
    prestamos = Tk()
    prestamos.title('Biblioteca virtual')
    prestamos.geometry('800x400')
    prestamos.config(bg='#A8EBE7')
    prestamos.resizable(0,0)

    etiqueta_prestamos = Label (prestamos,font=('century',18,'bold'),text='Prestamos',bg='#A8EBE7',width=20,height=1,bd=5,fg="#E31C1C")
    etiqueta_prestamos.place(x=25,y=10)

    etiqueta_codigo = Label (prestamos,font=('century',14,'bold'),text='CODIGO Del Libro',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_codigo.place(x=1,y=80)

    etiqueta_libro = Label (prestamos,font=('century',14,'bold'),text='Nombre Del Libro',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_libro.place(x=1,y=130)

    etiqueta_autor = Label (prestamos,font=('century',14,'bold'),text='Genero Del Libro',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_autor.place(x=1,y=180)

    etiqueta_cantidad = Label (prestamos,font=('century',14,'bold'),text='Cantidad',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_cantidad.place(x=470,y=180)

    etiqueta_año = Label (prestamos,font=('century',14,'bold'),text='Identificacion Del cliente',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_año.place(x=8,y=240)

    etiqueta_genero = Label (prestamos,font=('century',14,'bold'),text='Nombre del Cliente',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_genero.place(x=8,y=290)
 #-----------------------------------------entry-----------------------------------

    txt_codigo = Entry(prestamos,font=('century',18,'bold'),width=17,)
    txt_codigo.place(x=230,y=80)

    txt_libro = Entry(prestamos,font=('century',18,'bold'),width=17,)
    txt_libro.place(x=230,y=130)

    txt_autor = Entry(prestamos,font=('century',18,'bold'),width=17,)
    txt_autor.place(x=230,y=180)

    txt_autor = Entry(prestamos,font=('century',18,'bold'),width=17,)
    txt_autor.place(x=230,y=240)

    txt_genero = Entry(prestamos,font=('century',18,'bold'),width=17,)
    txt_genero.place(x=230,y=290)

    txt_cantidad = Entry(prestamos,font=('century',18,'bold'),width=7,)
    txt_cantidad.place(x=630,y=180)

  #----------------------------botones----------------------------------------

    boton_inventario = Button(prestamos , text="Buscar",width=20,height=2,)
    boton_inventario.place(x=620,y=78)    


  #---------------------------cuarta pantalla-------------------------------------#
     
def pantalla_clientes ():
    clientes = Tk()
    clientes.title('Biblioteca virtual')
    clientes.geometry('500x300')
    clientes.config(bg='#A8EBE7')
    clientes.resizable(0,0)

 #-------------titulos de la cuarta parte------------------------

    etiqueta_clientes = Label (clientes,font=('century',18,'bold'),text='Clientes',bg='#A8EBE7',width=20,height=1,bd=5,fg="#E31C1C")
    etiqueta_clientes.place(x=25,y=10)
 
    etiqueta_identificacion = Label (clientes,font=('century',14,'bold'),text='identificación',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_identificacion.place(x=1,y=80)

    etiqueta_nombre = Label (clientes,font=('century',14,'bold'),text='Nombre',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_nombre.place(x=1,y=130)

    etiqueta_seccion = Label (clientes,font=('century',14,'bold'),text='Seccion',bg='#A8EBE7',width=15,height=1,bd=5,fg="#E31C1C")
    etiqueta_seccion.place(x=1,y=180)

 #--------------------------entry de la cuarta parte-------------------------------

    txt_identificacion = Entry(clientes,font=('century',18,'bold'),width=17,)
    txt_identificacion.place(x=230,y=80)

    txt_nombre = Entry(clientes,font=('century',18,'bold'),width=17,)
    txt_nombre.place(x=230,y=130)

    txt_seccion = Entry(clientes,font=('century',18,'bold'),width=17,)
    txt_seccion.place(x=230,y=180)
 #------------------------------botnes de la cuarta parte---------------------

    boton_agregarCliente = Button(clientes,text="Agregar Clientes",width=20,height=2,)
    boton_agregarCliente.place(x=250,y=230)

 #--------------------botones--------------------------

boton_inventario = Button(j, text="inventario",width=20,height=2,command=pantalla_inventario)
boton_inventario.place(x=50,y=50)

boton_prestamos = Button(j, text="Prestamos de Libros",width=46,height=2,command=pantalla_prestamos)
boton_prestamos.place(x=50,y=100)

boton_clientes = Button(j, text="Clientes",width=20,height=2,command=pantalla_clientes)
boton_clientes.place(x=230,y=50)

#-----------------titulo------------------------

etiqueta = Label (j,font=('century',18,'bold'),text='BIBLIOTECA VIRTUAL',bg='#A8EBE7',width=20,height=1,bd=5,fg="#E31C1C")
etiqueta.place(x=25,y=10)

j.mainloop()
