from flask import request
from Conexion.Conexion import ConexionBaseDatos


class GestionVendedore():
    cone = ConexionBaseDatos()

    def getGestionVendedor(self):
        vendedor = request.json['vendedor']
        fechaInicio = request.json['fechaInicio']
        fechaFin = request.json['fechaFin']

        dicc = {'codigo': 0,
                'descripcion': '',
                'Gestion_vendedor': ''}
        sql = """
            SELECT ven.`nombres` AS vendedor, cl.`nombres`,cl.`apellidos`,pl.`descripcion`,pl.`hora_planificacion` ,pl.`fecha_planificacion` ,pl.`estado` AS estado_planificacion,cl.`estado` AS 'cliente/reseva'
            FROM planificacion pl 
            INNER JOIN cliente cl ON pl.`id_cliente`=cl.`id_cliente`
            INNER JOIN vendedores ven ON ven.`id_vendedores`=pl.`id_vendedores`
            WHERE ven.`id_vendedores` ='{0}' AND pl.`fecha_planificacion` BETWEEN '{1}' AND '{2}'""".format(vendedor,fechaInicio,fechaFin)
        execute = self.cone.ejecuta_query_all(sql)
        gestionVendedor = []
        if execute and execute != 1:
            for iten in execute:
                diccvendedor = {
                    'vendedor': iten[0],
                    'nombre_cliente': iten[1]+iten[2],
                    'descripcion':iten[3],
                    'hora':iten[4],
                    'fecha':iten[5],
                    'estado_planificacion':iten[6],
                    'cliente/reserva':iten[7],
                    
                    
                }
                gestionVendedor.append(diccvendedor)

            dicc['codigo'] = 0
            dicc['descripcion'] = 'Success'
            dicc['contratos'] = gestionVendedor
        elif execute == 1:
            dicc = {'codigo': 1, 'descripcion': 'Error en consulta'}
        else:
            dicc['codigo'] = 2
            dicc['descripcion'] = 'No se encuentra datos con los parametros ingresados.'
        return dicc
