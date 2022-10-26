from tkinter import *
from unittest import result
import mysql.connector 
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

v =Tk()
v.title("Registro")
v.geometry("500x400")
v.config(bg="#B4C7E7")
v.resizable(0,0)
#---------------------------------------------------------------------------------------------------------
conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="")
bd=conexion.cursor()
bd.execute("CREATE DATABASE IF NOT EXISTS base_de_datos")
bd.close()

conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="base_de_datos")
bd=conexion.cursor()
bd.execute("CREATE TABLE IF NOT EXISTS login(usuario VARCHAR(25),contrasena VARCHAR(55))")
bd.execute("CREATE TABLE IF NOT EXISTS registro(identificacion VARCHAR(25),nombre_y_apellidos VARCHAR(55),puesto_de_trabajo VARCHAR(55),usuario VARCHAR(55),contrasena VARCHAR(55))")
bd.close()
#-----------------------------------------------------------------------------------------------------------------
def registro():
    def agregar_usuario():
        cur=conexion.cursor()
        ide=txt_identificacion.get()
        nom=txt_nombre.get()
        tra=txt_trabajo.get()
        usu=txt_usuario.get()
        con=txt_contraseña.get()
        cur.execute("insert into registro(identificacion,nombre_y_apellidos,puesto_de_trabajo,usuario,contrasena) values('{}','{}','{}','{}','{}')".format(ide,nom,tra,usu,con))
        conexion.commit()
        cur.close()
        messagebox.showinfo(message="El nuevo usuario se guardo de forma exitosa", title="informacion al guardar")
        txt_identificacion.delete(0,END)
        txt_nombre.delete(0,END)
        txt_trabajo.delete(0,END)
        txt_usuario.delete(0,END)
        txt_contraseña.delete(0,END)
        txt_identificacion.focus()

    def buscar_usuario():
        cur=conexion.cursor()
        cur.execute("select * from registro")
        datos=cur.fetchall()
        txt_nombre.delete(0,END)
        txt_trabajo.delete(0,END)
        txt_usuario.delete(0,END)
        txt_contraseña.delete(0,END)
        for columna in datos:
            if columna[0]==txt_identificacion.get():
                txt_nombre.insert(0,columna[1])
                txt_trabajo.insert(0,columna[2])
                txt_usuario.insert(0,columna[3])
                txt_contraseña.insert(0,columna[4])
        txt_identificacion.focus()
        cur.close()
    
    def limpiar():
        txt_identificacion.delete(0,END)
        txt_nombre.delete(0,END)
        txt_trabajo.delete(0,END)
        txt_usuario.delete(0,END)
        txt_contraseña.delete(0,END)
        txt_identificacion.focus()

    def eliminar_usuario():
        cur=conexion.cursor()
        ide=txt_identificacion.get()
        cur.execute("delete from registro where identificacion='{}'".format(ide))
        conexion.commit()
        limpiar()
        cur.close()
        messagebox.showinfo(message="El usuario se borro con exito", title="informacion al eliminar")

    def modificar_usuario():
        cur=conexion.cursor()
        modificar_datos=txt_nombre.get(),txt_trabajo.get(),txt_usuario.get(),txt_contraseña.get(),txt_identificacion.get()
        cur.execute("update registro set nombre_y_apellidos=%s, puesto_de_trabajo=%s, usuario=%s, contrasena=%s where identificacion=%s",modificar_datos)
        conexion.commit()
        cur.close()
        messagebox.showinfo(message="El usuario se modifico con exito", title="informacion al actualizar")
        limpiar()
#-------------------------------------------------------------------------------------------    
    inv = Tk()
    inv.title("usuario")
    inv.geometry("700x400")
    inv.config(bg="#B4C7E7")
    inv.resizable(0,0)
#---------------------------------------------------------------------------------------------------    
    etiqueta=Label(inv,font=("arial",18,"bold"),text="registro",bg="#B4C7E7",).place(x=125,y=5)
    etiqueta=Label(inv,font=("arial",18,"bold"),text="identificacion",bg="#B4C7E7",).place(x=15,y=50)    
    txt_identificacion=Entry(inv,font=("arial",18,"bold"),bg="#D0CECE")
    txt_identificacion.place(x=200,y=50)
    txt_identificacion.bind("<Return>",(lambda event:buscar_usuario()))
    etiqueta=Label(inv,font=("arial",18,"bold"),text="nombre",bg="#B4C7E7",).place(x=15,y=100)
    txt_nombre=Entry(inv,font=("arial",18,"bold"),bg="#D0CECE")
    txt_nombre.place(x=200,y=100)
    etiqueuta=Label(inv,font=("arial",18,"bold"),text="trabajo",bg="#B4C7E7",).place(x=15,y=150)
    txt_trabajo=Entry(inv,font=("arial",18,"bold"),bg="#D0CECE")
    txt_trabajo.place(x=200,y=150)
    etiqueta=Label(inv,font=("arial",18,"bold"),text="usuario",bg="#B4C7E7",).place(x=15,y=200)
    txt_usuario=Entry(inv,font=("arial",18,"bold"),bg="#D0CECE")
    txt_usuario.place(x=200,y=200)
    etiqueta=Label(inv,font=("arial",18,"bold"),text="contrasena",bg="#B4C7E7",).place(x=15,y=250)
    txt_contraseña=Entry(inv,font=("arial",18,"bold"),bg="#D0CECE")
    txt_contraseña.place(x=200,y=250)
#----------------------------------------------------------------------------------------------------------------    
    boton_inv2=Button(inv,font=("arial",10,"bold"),text="agregar usuario",width=15,bg="#0077CA",command=agregar_usuario).place(x=250,y=300)
    boton_inv3=Button(inv,font=("arial",10,"bold"),text="modificar usuario",width=15,bg="#0077CA",command=modificar_usuario).place(x=50,y=300)
    boton_inv4=Button(inv,font=("arial",10,"bold"),text="eliminar usuario",width=15,bg="#0077CA",command=eliminar_usuario).place(x=450,y=300)
    boton_inv5=Button(inv,font=("arial",10,"bold"),text="buscar",width=15,bg="#0077CA",command=buscar_usuario).place(x=500,y=50)
    boton_inv6=Button(inv,font=("arial",10,"bold"),text="cancelar",width=15,bg="#0077CA",command=limpiar).place(x=400,y=350)
#--------------------------------------------funcion de ventana registro-----------------------------------------------------    
def login():
    def ingresar_sisitema():
      mysqlbd = mysql.connector.connect(host="localhost",user="root",password="",database="base_de_datos")
      mycursor = mysqlbd.cursor()
      usuario = txt_usuario1.get()
      contrasena = txt_contraseña1.get()

      sql = "select * from registro where usuario = %s and contrasena = %s"
      mycursor.execute(sql,[(usuario),(contrasena)])
      result = mycursor.fetchall()


      if result:
        messagebox.showinfo("","login success")
        root.destroy()
        call[("python","index.py")]
        return True

      else:
        messagebox.showinfo("","incorrent Username and Password")
        return False

    def cancelar():
        txt_usuario1.delete(0,END)
        txt_contraseña1.delete(0,END)


#----------------------------ventana registro-------------------------------------------------------        
    j = Tk()
    j.title('Registro')
    j.geometry('800x300')
    j.resizable(0,0)
    j.config(bg='#B4C7E7')

    #global txt_contraseña1
    #global txt_usuario1
    #-------------------etiquesta login-------------------------------------------------------------------------
    etiquetas_usuario = Label (j,font=('century',18,'bold'),text='Usuario',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000").place(x=10,y=45)
    etiquetas_contraseña = Label (j,font=('century',18,'bold'),text='Contrasena',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000").place(x=1,y=150)
    #----------------------------txt login-------------------------------------------------------------------------------------------
    txt_usuario1 = Entry(j,font=('century',18,'bold'),width=20,bg="#D0CECE")
    txt_usuario1.place(x=240,y=50)
    txt_contraseña1 = Entry(j,font=('century',18,'bold'),width=20,bg="#D0CECE",show='*')
    txt_contraseña1.place(x=250,y=150)
    #----------------------------------------------------------------------
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="ingresar sistema",command=ingresar_sisitema).place(x=530,y=45)
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="cancelar",command=cancelar).place(x=540,y=145)
    #---------------------------ventana menu--------------------------------------------------

etiqueta=Label(v,font=("century",24,"bold"),text="REGISTRO",bg="#B4C7E7").place(x=125,y=25)

boton_inv=Button(v,font=("century",12,"bold"),text="registro", command=registro,width=15,height=5,bg="#FFFFFF").place(x=50,y=100)

boton_cli=Button(v,font=("century",12,"bold"),text="login", command=login,width=15,height=5,bg="#FFFFFF").place(x=300,y=100)


v.mainloop()

