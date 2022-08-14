from flask import request
from Conexion.Conexion import ConexionBaseDatos

class GestionPerdida():
    cone = ConexionBaseDatos()
    def getGestionPerdia(self):
        campania=request.json['campania']
        vendedor=request.json['vendedor']
        
        dicc={'codigo':0,
				'descripcion':'',
				'Contrato':''}
        sql = """
            select v.nombres, -con.valor_venta,con.estado_cargo
            from contrato con 
            inner join vendedores v
            on con.id_vendedores = v.id_vendedores
            inner join campanias cam
            on con.id_campanias = cam.id_campanias
            WHERE con.estado_cargo = 'PERDIDA' AND CAM.id_campanias = '{0}' AND V.id_vendedores = '{1}';""".format(campania,vendedor)
        execute = self.cone.ejecuta_query_all(sql)
        print(execute)
        arrayPerdida = []
        if execute and execute !=1:
            for iten in execute:
                diccPerdida={
                'nombres': iten[0],
                'valor_ventas': iten[1],
                'estado': iten[2],
                }
                arrayPerdida.append(diccPerdida)
            
            dicc['codigo']=0
            dicc['descripcion']='Success'
            dicc['contratos']=arrayPerdida
        elif execute==1:
            dicc ={'codigo':1,'descripcion':'Error en consulta'}
        else:
            dicc['codigo']=2
            dicc['descripcion']='No se encuentra gestion Perdida con respecto a los valores ingresado'
        return dicc