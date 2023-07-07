from flask import Flask,render_template,request,redirect,url_for, flash 
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_fruteria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Declaración de ruta http://localhost:5000
@app.route('/')
def index():
    return render_template('index.html' )

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        #Pasamos a variables el contenido de los inputs
        VFruta=request.form['txtFruta']
        VTemporada=request.form['txtTemporada']
        VPrecio=request.form['txtPrecio']
        VStock=request.form['txtStock']
        print(VFruta,VTemporada,VPrecio,VStock)
        #Conectar y ejecutar el insert
        CS=mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(VFruta,VTemporada,VPrecio,VStock))
        mysql.connection.commit()
    flash('La Fruta fue agregada correctamente')
    return redirect(url_for('index'))
@app.route('/consultar')
def consultar():
    CC=mysql.connection.cursor()
    CC.execute('select * from tbfrutas')
    conFrutas=CC.fetchall()
    print(conFrutas)
    return render_template('consultar_fruta.html',listFruta=conFrutas)
@app.route('/editar/<id>')
def editar(id):
    cursorId=mysql.connection.cursor()
    cursorId.execute('Select * from tbfrutas where id= %s',(id))
    conlId=cursorId.fetchone()
    return render_template('editarFruta.html', frut=conlId)
@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST':
        varFruta=request.form['txtFruta']
        varTemporada=request.form['txtTemporada']
        varPrecio=request.form['txtPrecio']
        varStock=request.form['txtStock']
        curAct=mysql.connection.cursor()
        curAct.execute('update tbfrutas set fruta=%s,temporada=%s,precio=%s,stock=%s where id=%s',(varFruta,varTemporada,varPrecio,varStock,id))
        mysql.connection.commit()
    flash('Se actualizo la fruta correctamente')
    return redirect(url_for('consultar'))
@app.route('/eliminar/<id>')
def eliminar(id):
    CB=mysql.connection.cursor()
    CB.execute('Select * from tbfrutas where id=%s',(id))
    CBA=CB.fetchone()
    return render_template('borrar_fruta.html',frut1=CBA)
@app.route('/Borrar/<id>',methods=['POST'])
def Borrar(id):
    if request.method=='POST':
        curBorrar=mysql.connection.cursor()
        curBorrar.execute('delete from tbfrutas where id=%s',(id,))
        mysql.connection.commit()
    flash('Se elimino correctamente la Fruta')
    return redirect(url_for('index'))
@app.route('/Consultar_fruta')
def Consultar_fruta():
    return render_template('buscar_fruta.html')
@app.route('/ConsultaNombre',methods=['POST'])
def consultaNombre():
    varBuscar=request.form['txtBuscarFruta']
    print(varBuscar)
    CUR=mysql.connection.cursor()
    CUR.execute('select * from tbfrutas where fruta LIKE %s', (f'%{varBuscar}%',))
    conFrutas=CUR.fetchall()
    print(conFrutas)
    return render_template('buscar_fruta.html',listFruta=conFrutas)


#Ejecución del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)