
#Importa la libreria speedtest
import speedtest


def Subida():
    pass

def Descarga():
    pass

def Ping():
    #Medición de ping
    print(st.results.ping)

st = speedtest.Speedtest()

#Velocidad de subida
dw = st.download()/1000000
print('Subida: {:.2f}'.format(dw) + ' Mb/s')

#Velocidad de descarga
up = st.upload()/1000000
print('Descarga: {:.2f}'.format(up) + ' Mb/s')


