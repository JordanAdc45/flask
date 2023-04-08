from flask import Flask ,render_template,redirect,url_for,request
from config import *

con_bd = EstablecerConexion()
app = Flask(__name__)


@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM personas"
    cursor.execute(sql)  
    PersonasRegistradas = cursor.fetchall()
    return render_template('index.html', personas = PersonasRegistradas)

@app.route('/guardar_personas', methods=['POST'])
def AgregarPersonas():
    
    cursor = con_bd.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']

    if nombre and apellido and telefono:
        sql = "INSERT INTO personas (nombre,apellido,telefono) VALUES (%s,%s,%s)"
        cursor.execute(sql,(nombre,apellido,telefono))
        con_bd.commit()
        
        return redirect(url_for('index'))
    else:
     return "Error en la consulta"
    
@app.route('/eliminar_persona/<int:id_persona>')
def eliminar(id_persona):
    cursor = con_bd.cursor()
    sql = "DELETE FROM personas WHERE id = {0}".format(id_persona)
    cursor.execute(sql)
    con_bd.commit()
    Flask("Registro eliminar correctamente")
    return redirect((url_for('index')))


@app.route('/editar_persona/<int:id_persona>', methods=['POST'])
def ActualizarPersona(id_persona):
    cursor = con_bd.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    if nombre and apellido and telefono:
        sql = """
             UPDATE personas
	         SET nombre=%s, apellido=%s, telefono=%s
             WHERE id=%s;
        """
        cursor.execute(sql,(nombre,apellido,telefono,id_persona))
        con_bd.commit()
        #Grabar un mensaje al final de una solicitud y desplegar una ves se recarga la pagina
        Flask("Registro editado correctamente")
        return redirect((url_for('index')))
    else:
        return "Error en la consulta"

def crearTablaPersonas():
    cursor = con_bd.cursor()
    cursor.execute(""" 
         CREATE TABLE IF NOT EXISTS personas(
             Id serial NOT NULL,
             Nombre character varying(30),
             Apellido character varying(30),
             Telefono character varying,
             CONSTRAINT pk_personas_id PRIMARY KEY (id)
         );
         """)
    con_bd.commit()


if __name__ == '__main__':
    crearTablaPersonas()
    app.run(debug=True)


