from flask import request
from Conexion.Conexion import ConexionBaseDatos
class RendimientoVendedores:
    cone = ConexionBaseDatos()
    contador = True
    def getRendimiento(self):
        # fechaInicial=request.json['fechaInicial']
        # fechaFin=request.json['fechaFin']
        
        dicc = {'codigo': 0,
                'descripcion': '',
                'Premios': ''}
        sql = """
           SELECT v.id_vendedores,v.nombres,r.`proceso`,r.`numero`,r.`valor`,r.`carteraPorTrabajar`,r.`ventaCargo`,r.`incrementoCargo` FROM `redimientoVendedores` r JOIN vendedores v ON r.`id_vendedores` = v.id_vendedores
           """
        execute = self.cone.ejecuta_query_all(sql)
        premios = []
        contador=''
        if execute and execute != 1:
            for iten in execute:
                if(iten[1]==contador):
                    diccpremios = {
                        "nombre": iten[1],
                        'numero': iten[2],
                        'carteraPorTrabajar': iten[3],
                        'ventaCargo': iten[4],
                        'incrementoCargo': iten[5],
                        }
                    premios.append(diccpremios)
                contador=iten[1]
            dicc['codigo'] = 0
            dicc['descripcion'] = 'Success'
            dicc['contratos'] = premios
        elif execute == 1:
            dicc = {'codigo': 1, 'descripcion': 'Error en consulta'}
        else:
            dicc['codigo'] = 2
            dicc['descripcion'] = 'No hay datos'
        return dicc    