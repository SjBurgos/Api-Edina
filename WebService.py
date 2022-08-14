from flask import Flask, request, jsonify

from Api.Artista import Artista
from Api.ContratoCerradoCapania import ContratoCerradoCampania
from Api.GestionPerdida import GestionPerdida
from Api.GestionVendedores import GestionVendedore

class Servicios():
    global artista
    artista = Artista()
    global contrato
    contrato = ContratoCerradoCampania()
    global perdida
    perdida = GestionPerdida()
    global vendedores
    vendedores = GestionVendedore()
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
    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=False,port=8098) 