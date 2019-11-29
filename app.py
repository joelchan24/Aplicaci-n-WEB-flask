from flask import Blueprint, Flask, render_template,request, redirect, url_for, flash
import requests
from datetime import datetime, date



#Para crear nuestras rutas del servidor o url
app = Flask(__name__,instance_relative_config=True)
# settings
app.secret_key = "mysecretkey"
#Decolorador
#Metodo route recibe un nombre para poder crear una url
@app.route('/', methods = ['GET'])
def Login():
    return render_template('Login.html')


@app.route('/index.html')
def home():
    URL = "https://api-beesoft.herokuapp.com/GetAllUsers"   
    r = requests.get(url = URL)    
    data = r.json()

    URL = "https://api-beesoft.herokuapp.com/GetAllTables"   
    r = requests.get(url = URL)    
    data2 = r.json()

    URL = "https://api-beesoft.herokuapp.com/GetAllCajas"   
    r = requests.get(url = URL)    
    data3 = r.json()

    URL = "https://api-beesoft.herokuapp.com/GetAllUsers"   
    r = requests.get(url = URL)    
    data4 = r.json()    
    return render_template('index.html',data=data, data2=data2, data3=data3, data4=data4)


@app.route('/Perfil.html')
def profile():
    return render_template('Perfil.html')  
@app.route('/Perfil/<idusuario>')
def Perfil(idusuario):
    URL = "https://api-beesoft.herokuapp.com/perfil" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
    PARAMS = {'idUsuario':idusuario}
    r = requests.post(url = URL, json= PARAMS,headers=headers)    
    data = r.json()
    print(data)
    return render_template('Perfil.html',data=data)  

@app.route('/CrontrolUsuarios.html')
def CrontrolUsuarios():
    URL = "https://api-beesoft.herokuapp.com/listAllUsers"   
   
    r = requests.get(url = URL)    
   
    data = r.json()    
    return render_template('CrontrolUsuarios.html',data=data)


if __name__ == '__main__':
    #app.debug = True
    app.run()
