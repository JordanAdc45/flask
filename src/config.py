from psycopg2 import connect 


HOST ='containers-us-west-107.railway.app'
PORT= 7347
BD = 'railway'
USUARIO ='postgres'
PASS = 'NvGn0nmFSQzDTq0rP6ZY'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PORT, dbname=BD, user=USUARIO, password=PASS)
    except ConnectionError:
        print( "ERROR EN LA CONEXION")

    return conexion