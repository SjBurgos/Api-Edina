from flask import request
from Conexion.Conexion import ConexionBaseDatos
class PremiosSemanales:
    cone = ConexionBaseDatos()
    contador = True
    def getPremiosSemanales(self):
        fechaInicial=request.json['fechaInicial']
        fechaFin=request.json['fechaFin']
        
        dicc = {'codigo': 0,
                'descripcion': '',
                'Premios': ''}
        sql = """
            SELECT v.`nombres`,SUM(p.`total_venta`)  AS total 
            FROM premiosSemanales p INNER JOIN vendedores v ON p.`id_vendedores`=v.`id_vendedores` 
            AND p.`fecha` BETWEEN '{0}'AND'{1}' GROUP BY v.`nombres` ORDER BY 2 DESC;""".format(fechaInicial,fechaFin)
        execute = self.cone.ejecuta_query_all(sql)
        premios = []
        if execute and execute != 1:
            for iten in execute:
                if self.contador:
                    diccpremios = {
                        "nombres": iten[0],
                        'total': iten[1],
                        'status':"Premiado"
                    }
                    self.contador = False                   
                else:           
                    for iten in execute:
                        diccpremios = {
                            "nombres": iten[0],
                            'total': iten[1],
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