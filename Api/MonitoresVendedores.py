from flask import request
from Conexion.Conexion import ConexionBaseDatos

class MonitoreosVendedores():
    cone = ConexionBaseDatos()

    def getMonitoreoVededores(self):
        vendedor=request.json['vendedor']
        pass