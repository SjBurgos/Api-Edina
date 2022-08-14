from flask import Flask, request, jsonify

from Artista.Artista import Artista

class Servicios():
    global artista
    artista = Artista()
    app = Flask(__name__)
    @app.route("/Artista/Artista", methods=["GET"])
    def consulta_lista_menu():
        return jsonify (artista.getArtistaByEstado())
    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=False,port=8098) 