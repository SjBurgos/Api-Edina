from flask import request
from Conexion.Conexion import ConexionBaseDatos


class Artista():
    cone = ConexionBaseDatos()

    def getArtistaByEstado(self):
        estado = request.json['estado']
        dicc={'codigo':0,
				'descripcion':'',
				'arte':''}
        sql = """
        SELECT nombres,descripcion,arte.estado FROM artista 
        JOIN arte ON artista.id_artista = arte.id_artista WHERE arte.estado='{0}'""".format(estado)
        execute = self.cone.ejecuta_query_all(sql)
        print(execute)
        arrayArte = []
        if execute and execute !=1:
            for iten in execute:
                diccArt={
                'nombres': iten[0],
                'descripcion': iten[1],
                'estado': iten[2],}
                arrayArte.append(diccArt)
            
            dicc['codigo']=0
            dicc['descripcion']='Success'
            dicc['arte']=arrayArte
        elif execute==1:
            dicc ={'codigo':1,'descripcion':'Error en consulta'}
        else:
            dicc['codigo']=2
            dicc['descripcion']='No se encuentra arte con respecto al estado ingresado'
        return dicc