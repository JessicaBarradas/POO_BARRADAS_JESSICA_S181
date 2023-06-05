from tkinter import messagebox
import sqlite3 

class controladorBebi:

    def __init__(self):
        pass
#Preparamos la conexion a la BD para cuando sea necesario usarla
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/Jessy/Desktop/POO_BARRADAS_JESSICA_S181/POO_BARRADAS_JESSICA_S181/ALMACEN DE BEBIDAS/Almacen_bebidas.db")
            print("Conexion exitosa")
            return conexion

        except sqlite3.OperationalError:
            print("Conexion erronea")
#Metodo para insertar 
    def insertarBebida(self,Nom,Cla,Mar,Pre):
        conx=self.conexionBD()
        if(Nom == "" or Cla == "" or Mar == "" or Pre == ""):
            messagebox.showwarning("Error!","Llena todos los registros")
            conx.close()
        else:
            cursor = conx.cursor()
            datos =(Nom, Cla, Mar, Pre)
            qrInsert="insert into Bebidas(Nombre,Clasificacion,Marca,Precio) values(?,?,?,?)"
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!","Se guardo el material") 
    def consultaBebida(self,id):
        #1. Preparar la conexión
        conx=self.conexionBD()
        #2. Veificar que el ID no este vacio
        if(id==""):
            messagebox.showwarning("Cuidado","ID vacio escribe uno valido")
            conx.close()
        else:
                #proceder a buscar
            try:
                #4. Preparar lo necesario para el select
                cursor=conx.cursor()
                sqlSelect="Select * from Bebidas where ID="+id
                #5.Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                Bebida=cursor.fetchall()
                conx.close()
                return Bebida
            except sqlite3.OperationalError:
                print("Error consulta")
    def EliminarBebida(self,ID):
        conx=self.conexionBD()
        if(ID==""):
            messagebox.showwarning("CUIDADO","No puede estar ningun campo vacio")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                sqlEliminar="DELETE FROM Bebidas WHERE ID=?"
                cursor.execute(sqlEliminar,[ID])
                EliminarBed=cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("ENHORABUENA","El usuario se ha eliminado correctamente")
                return EliminarBed
            except sqlite3.OperationalError:
                messagebox.showerror("ERROR","Error en la consulta")
    def consultarB(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        try:
            sqlConsu="Select * from Bebidas"
            cursor.execute(sqlConsu)
            Consulta=cursor.fetchall()
            conx.close()
            return Consulta
        except sqlite3.OperationalError:
            messagebox.showwarning("Advertencia","No se encontro ningún usuario")
    def actualizarB(self,id,nomB,claB,MarB,PreB):
        conx=self.conexionBD()
        if (id=="" or nomB=="" or claB=="" or MarB=="" or PreB==""):
            messagebox.showwarning("Advertencia","Ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                nomb=nomB
                clas=claB
                Marca=MarB
                Precio=PreB
                sqlActu="UPDATE Bebidas SET Nombre=?, Clasifiacion=?, Marca=?, Precio=? WHERE ID=?"
                cursor.execute(sqlActu,[nomb,clas,Marca,Precio,id])
                BebActu=cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("ENHORABUENA","Datos actualizados correctamente")
                return BebActu
            except sqlite3.OperationalError:
                messagebox.showerror("ERROR","Error en la consulta")
    def cantidadBebidaMarca(self, CMar):
        conx = self.conexionBD()
        
        if (CMar == ""):
            messagebox.showwarning("Cuidado", "Campo vacio, escribe uno valido")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlCantidadMar = "SELECT COUNT(*) FROM Bebidas WHERE Marca =?"
                
                cursor.execute(sqlCantidadMar, [CMar])
                ResultMar = cursor.fetchall()
                conx.close()
                
                return ResultMar
            
            except sqlite3.OperationalError:
                print("Error de Consulta")    
    
    def cantidadBebidaClas(self, Cla):
        conx = self.conexionBD()
        
        if (Cla == ""):
            messagebox.showwarning("Cuidado", "Campo vacio, escribe uno valido")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlCantidadCla = "SELECT COUNT(*) FROM Bebidas WHERE Clasificacion =?"
                
                cursor.execute(sqlCantidadCla, [Cla])
                ResultCla = cursor.fetchall()
                conx.close()
                
                return ResultCla
            
            except sqlite3.OperationalError:
                print("Error de Consulta")    
        
    def Prome(self):
        conx = self.conexionBD()
        
        try:
                cursor = conx.cursor()
                sqlPro = "SELECT Precio FROM Bebidas"
                
                cursor.execute(sqlPro)
                ResultPro = cursor.fetchall()
                
                cantidaBeb = len(ResultPro)
                sumaPre = sum([precio[0] for precio in ResultPro])
                precioProm = sumaPre / cantidaBeb
                
                conx.close()
                
                return precioProm
            
        except sqlite3.OperationalError:
                print("Error de Consulta")