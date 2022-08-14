"""
Función: Conexion
Descripcion: Es la que realiza la conexcion a la base de datos, 
esta función es llamada en cada uno de los py para realizar la conexion
Fucnión: Ejecuta_query 
Descripcion: Realizada para ejecutar los query de los servicios 
al igual que la función conexión es llamada en todos los py 

"""

from __future__ import print_function
import MySQLdb as my

class ConexionBaseDatos:

	def conexion(self): 
		bd='edina'
		user='root'
		passwd=''
		host='localhost'
		puerto='3306'
		try:
			db = my.connect(host="127.0.0.1",
                    user="root",
                    passwd="",
                    db="edina"
                    )
			return db
		except Exception as e: 
		 
			print ("Error en conexion: ",str(e))

	def ejecuta_query_one(self, query):
		try:
			conn = self.conexion()
			cursor = conn.cursor()
			cursor.execute(query)
			result = cursor.fetchone()
		except Exception as e:
			print(str(e),'estr')
			result=1
		finally:
			conn.close()

		return result

	def ejecuta_query_all(self, query):
		try:
			conn = self.conexion()
			cursor =conn.cursor()

			cursor.execute(query)
			result = cursor.fetchall()
			
			
		except Exception as e:
			print(str(e),'estr')
			result=1

		finally:
			
			conn.close()

		return result

	def ejecuta_query(self, query):
		
		try:
			conn = self.conexion()
			cursor =conn.cursor()

			cursor.execute(query)
			conn.commit()
			result=0
			
		except Exception as e:
			print(str(e),'estr')
			result = 1

		finally:
			
			conn.close()
		return result