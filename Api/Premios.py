from flask import request
from Conexion.Conexion import ConexionBaseDatos
class Premios:
    cone = ConexionBaseDatos()
    contador = True
    def getPremios(self):
        # fechaInicial=request.json['fechaInicial']
        # fechaFin=request.json['fechaFin']
        
        dicc = {'codigo': 0,
                'descripcion': '',
                'Premios': ''}
        sql = """
           select descripcion,total_minimo,estado from premios
           """
        execute = self.cone.ejecuta_query_all(sql)
        premios = []
        if execute and execute != 1:
            for iten in execute:
                diccpremios = {
                    "descripcion": iten[0],
                    'total_minimo': iten[1],
                    'estado': iten[2]
                    }
                premios.append(diccpremios)
            dicc['codigo'] = 0
            dicc['descripcion'] = 'Success'
            dicc['contratos'] = premios
        elif execute == 1:
            dicc = {'codigo': 1, 'descripcion': 'Error en consulta'}
        else:
            dicc['codigo'] = 2
            dicc['descripcion'] = 'No hay datos'
        return dicc    