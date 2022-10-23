from flask import Flask
 
#Creamos objeto Flask
app = Flask(_name_)
 
#Creamos nuestro primer servicio web
@app.route('/', methods=['GET'])
def test():
    return "hello world"


@app.route('/saludar/<string:name>', methods=['GET'])
def saludar(name: str):
    return "hola " + name
 
#Ejecutamos el servidor
if _name_ == '_main_':
    app.run()