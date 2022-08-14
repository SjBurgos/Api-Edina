from flask import request
from Conexion.Conexion import ConexionBaseDatos

class ContratoCerradoCampania():
    cone = ConexionBaseDatos()

    def getContratosCerrados(self):
        campania=request.json['campania']
        dicc={'codigo':0,
				'descripcion':'',
				'Contrato':''}
        sql = """
            select v.nombres, con.valor_venta
            from contrato con 
            inner join vendedores v
            on con.id_vendedores = v.id_vendedores
            inner join campanias cam
            on con.id_campanias = cam.id_campanias
            and con.id_campanias = '{0}'""".format(campania)
        execute = self.cone.ejecuta_query_all(sql)
        print(execute)
        arryContrato = []
        if execute and execute !=1:
            for iten in execute:
                diccContrato={
                'nombres': iten[0],
                'valor_ventas': iten[1],
                }
                arryContrato.append(diccContrato)
            
            dicc['codigo']=0
            dicc['descripcion']='Success'
            dicc['contratos']=arryContrato
        elif execute==1:
            dicc ={'codigo':1,'descripcion':'Error en consulta'}
        else:
            dicc['codigo']=2
            dicc['descripcion']='No se encuentra contrato con respecto al estado ingresado'
        return dicc