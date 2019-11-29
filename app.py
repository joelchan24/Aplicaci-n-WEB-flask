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

@app.route('/AddUsuario/<idUsuario>')
def AddUsuario(idUsuario):
    idUsuarioUs = idUsuario

    URL = "https://api-beesoft.herokuapp.com/perfil" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
    PARAMS = {'idUsuario':idUsuarioUs}
    r = requests.post(url = URL, json= PARAMS,headers=headers)    
    data = r.json()
    #print(data)
    return render_template('AddUsuario.html',idUsuario=idUsuario,data=data)

@app.route('/CrontrolUsuarios.html')
def CrontrolUsuarios():
    URL = "https://api-beesoft.herokuapp.com/listAllUsers"   
   
    r = requests.get(url = URL)    
   
    data = r.json()    
    return render_template('CrontrolUsuarios.html',data=data)


#######Cuidado######
#cajasapiaerio
@app.route('/<id>')
def CajasApiario2(id):
    apiario=id
    URL = "https://api-beesoft.herokuapp.com/caja" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
    PARAMS = {'idApiario':apiario}
    r = requests.post(url = URL, json= PARAMS,headers=headers) 
    data = r.json()
    return render_template('CajasApiario.html',data=data,apiario=apiario)
    
    
#Control Panales
@app.route('/CrontrolApiario.html')
def CrontrolApiario():
    URL = "https://api-beesoft.herokuapp.com/apiario"   
   
    r = requests.get(url = URL)    
   
    data = r.json()        
      
    return render_template('CrontrolApiario.html',data=data)


    #Agrera  addAPIARIO
@app.route('/AddApiario/<idusuario>/<nom>/<idapiario>/<nomApiario>')
def AddApiario(idusuario,nom,idapiario,nomApiario):
    return render_template('AddApiario.html',usuario=idusuario,nomusu=nom,apiario=idapiario,nombreapi=nomApiario)

 #GuardarCaja
@app.route('/GuardarCaja', methods=['POST', 'GET'])  
def GuardarCaja():  
    
    if request.method == 'POST':
        idapiario=request.form['txtidApiario']
        nom=request.form['txtdueñoApiario']
        nomapiario=request.form['txtnapiario']
        idcaja=request.form['txtidCaja']

        
        
        URLLast = "https://api-beesoft.herokuapp.com/ultimaCaja" 
        headersLast = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
        PARAMS = {'idApiario':idapiario}
        rl = requests.post(url = URLLast, json= PARAMS,headers=headersLast)    
    
        data = rl.json() 
        numeroCaja=data[0]['NumCaja']     
        
        numCuadros=request.form['txtNumCuadros']
        fechareg =str(date.today()) 
        URL = ""
        PARAMS={}
        if(idcaja=="0"):
            URL='https://api-beesoft.herokuapp.com/insertCaja'
            PARAMS={'numeroCaja':numeroCaja,'idApiario':idapiario,'fechaReg':fechareg,'numeroCuadros':numCuadros}
        else:
            URL='https://api-beesoft.herokuapp.com/updateCaja'
            PARAMS={"idCaja":idcaja,"numeroCuadros":numCuadros}
        headers = {'Content-type': 'application/json'}  
        
     
        r = requests.post(url = URL, json= PARAMS,headers=headers) 
        if(r.status_code==200):
            apiario=idapiario
            URL = "https://api-beesoft.herokuapp.com/caja" 
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
            PARAMS = {'idApiario':apiario}
            r = requests.post(url = URL, json= PARAMS,headers=headers)    
   
            data = r.json()
            return render_template('CajasApiario.html',data=data,apiario=apiario,nombre=nom,napiario=nomapiario)

    return render_template('CajasApiario.html')

    
   
    

        
        
   
               

@app.route('/ApiarioUsuario')
def ApiarioU():  
    

    return render_template('ApiarioUsuario.html')

#update Apiario - 2 parametros
@app.route('/apiario/<usuario>/<nombre>')
def ApiarioUm(usuario,nombre):
    usu=usuario
    URL = "https://api-beesoft.herokuapp.com/apiariosUser" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  
    PARAMS = {'usuarioid':usu}
    r = requests.post(url = URL, json= PARAMS,headers=headers)    
    print(r.json())
    data = r.json()
    

    return render_template('ApiarioUsuario.html',data=data,nombre=nombre,usuarioid=usu)
#Cajas 3 parametros
@app.route('/cajas/<idapiario>/<nombre>/<nomapiario>')
def ApiarioCajas(idapiario,nombre,nomapiario):
    apiario=idapiario
    nom=nombre
    nomapiario=nomapiario
    URL = "https://api-beesoft.herokuapp.com/caja" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
    PARAMS = {'idApiario':apiario}
    r = requests.post(url = URL, json= PARAMS,headers=headers)
    data = r.json()
    return render_template('CajasApiario.html',data=data,apiario=apiario,nombre=nom,napiario=nomapiario)

#Caja con 1 parametros
@app.route('/CajaInfo/<idcaja>')
def CajaInfo(idcaja):
    idCaja=idcaja
    #nom=nombre
    #nomapiario=nomapiario
    URL = "https://api-beesoft.herokuapp.com/monitoreo" 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
    PARAMS = {'idCaja':idCaja}
    r = requests.post(url = URL, json= PARAMS,headers=headers)
    data = r.json()
    #return render_template('CajasApiario.html',data=data,apiario=apiario,nombre=nom,napiario=nomapiario)
    return render_template('CajaInfo.html',caja=idcaja, data=data)


######Cuidado#######


if __name__ == '__main__':
    #app.debug = True
    app.run()
