from flask import request
from Conexion.Conexion import ConexionBaseDatos


class MonitoreosVendedores():
    cone = ConexionBaseDatos()

    def getMonitoreoVededores(self):
        dicc = {'codigo': 0,
                'descripcion': '',
                'Monitoreo': ''}
        sql = """
            SELECT nombres, latitud,longitud FROM vendedores;"""
        execute = self.cone.ejecuta_query_all(sql)
        monitoreo = []
        if execute and execute != 1:
            for iten in execute:
                diccMonitoreo = {
                    "nombres": iten[0],
                    'latitud': iten[1],
                    'longitud': iten[2],
                }
                monitoreo.append(diccMonitoreo)

            dicc['codigo'] = 0
            dicc['descripcion'] = 'Success'
            dicc['contratos'] = monitoreo
        elif execute == 1:
            dicc = {'codigo': 1, 'descripcion': 'Error en consulta'}
        else:
            dicc['codigo'] = 2
            dicc['descripcion'] = 'No hay datos'
        return dicc
