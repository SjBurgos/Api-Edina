from flask import Flask, request, jsonify

from Api.Artista import Artista
from Api.ContratoCerradoCapania import ContratoCerradoCampania
from Api.GestionPerdida import GestionPerdida
from Api.GestionVendedores import GestionVendedore
from Api.MonitoresVendedores import MonitoreosVendedores
from Api.PremiosSemanales import PremiosSemanales
from Api.Premios import Premios
from Api.RendimientoVendedores import RendimientoVendedores



class Servicios():
    global artista
    artista = Artista()
    global contrato
    contrato = ContratoCerradoCampania()
    global perdida
    perdida = GestionPerdida()
    global vendedores
    vendedores = GestionVendedore()
    global monitoreo 
    monitoreo = MonitoreosVendedores()
    global premio
    premio =  PremiosSemanales()  
    global premios
    premios =  Premios()
    global rendimiento
    rendimiento = RendimientoVendedores()    
    app = Flask(__name__)
    @app.route("/consulta/solicitudesArte", methods=["GET"])
    def consulta_lista_menu():
        return jsonify (artista.getArtistaByEstado())
    @app.route("/consulta/contratoCerradoPorCampana", methods=["GET"])
    def consultacontratoCerrados():
        return jsonify (contrato.getContratosCerrados())
    @app.route("/consulta/gestionPerdida", methods=["GET"])
    def consultaGestionPerdida():
        return jsonify (perdida.getGestionPerdia())
    @app.route("/consulta/getGestionVendedor", methods=["GET"])
    def consultaGestionVendedor():
        return jsonify (vendedores.getGestionVendedor())
    @app.route("/consulta/getMonitoreovendedores", methods=["GET"])
    def consultaMonitoreo():
        return jsonify (monitoreo.getMonitoreoVededores())
    @app.route("/consulta/getPremioSemanales", methods=["GET"])
    def consultaPremioSemanales():
        return jsonify (premio.getPremiosSemanales())
    @app.route("/consulta/getPremios", methods=["GET"])
    def consultaPremio():
        return jsonify (premios.getPremios())
    @app.route("/consulta/rendimientoVendedores", methods=["GET"])
    def consultaRendimientoVendedores():
        return jsonify (rendimiento.getRendimiento())
    
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=False,port=8098)