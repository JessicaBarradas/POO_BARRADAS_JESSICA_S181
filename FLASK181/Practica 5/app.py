from flask import Flask,render_template,request,redirect,url_for, flash  #Importación del framework
from flask_mysqldb import MySQL  #Importación del MySQL 

app=Flask(__name__)   #Inicialización del APP o servidor
#configuración de la BD 
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Declaración de ruta http://localhost:5000
@app.route('/')
def index():
    return render_template('index.html')

#Ruta http:localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        #Pasamos a variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vaño=request.form['txtAño']
        print(Vtitulo,Vartista,Vaño)
        #Conectar y ejecutar el insert
        CS=mysql.connection.cursor()
        CS.execute('insert into tbalbums(Titulo,Artista,Año) values(%s,%s,%s)',(Vtitulo,Vartista,Vaño))
        mysql.connection.commit()
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la Base de Datos"

#Ejecución del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)