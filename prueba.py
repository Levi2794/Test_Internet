
#Importa la libreria speedtest
import speedtest

st = speedtest.Speedtest()

def Subida():
    #Velocidad de subida
    dw = st.download()/1000000
    print('Subida: {:.2f}'.format(dw) + ' Mb/s')

def Descarga():
    
    #Velocidad de descarga
    up = st.upload()/1000000
    print('Descarga: {:.2f}'.format(up) + ' Mb/s')

def Ping():
    pass


#Medición de ping
print(st.results.ping)

