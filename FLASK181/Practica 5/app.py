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
    CC=mysql.connection.cursor()
    CC.execute('select * from tbalbums')
    conAlbums=CC.fetchall()
    #print(conAlbums)
    return render_template('index.html' , listalbums=conAlbums)

#Ruta http:localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        #Pasamos a variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vaño=request.form['txtAño']
        if Vtitulo == "" or Vartista== "" or Vaño == "":
            flash('No puedes enviar campos vacios')
            return redirect(url_for('index'))
        else:
            #Conectar y ejecutar el insert
            CS = mysql.connection.cursor()
            CS.execute('insert into albums(titulo,artista,anio) values (%s,%s,%s)',(Vtitulo,Vartista,Vaño))
            mysql.connection.commit()
            flash('El album fue agregado correctamente')
            return redirect(url_for('index'))
@app.route('/editar/<id>')
def editar(id):
    cursorId=mysql.connection.cursor()
    cursorId.execute('Select * from tbalbums where id= %s',(id))
    consulId=cursorId.fetchone()
    return render_template('editarAlbum.html', album=consulId)
@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST':
        varTitulo=request.form['txtTitulo']
        varArtista=request.form['txtArtista']
        varAño=request.form['txtAño']
        curAct=mysql.connection.cursor()
        curAct.execute('update tbalbums set Titulo=%s,Artista=%s,Año=%s where id=%s',(varTitulo,varArtista,varAño,id))
        mysql.connection.commit()
    flash('Se actualizo el Album ' +varTitulo)
    return redirect(url_for('index'))
    

@app.route('/eliminar/<id>')
def eliminar(id):
    CB=mysql.connection.cursor()
    CB.execute('Select * from tbalbums where id=%s',(id))
    CBA=CB.fetchone()
    return render_template('borrarAlbum.html',album1=CBA)
@app.route('/Borrar/<id>',methods=['POST'])
def Borrar(id):
    if request.method=='POST':
        curBorrar=mysql.connection.cursor()
        curBorrar.execute('delete from tbalbums where id=%s',(id,))
        mysql.connection.commit()
    flash('Se elimino correctamente')
    return redirect(url_for('index'))
    

#Ejecución del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)