from yate import Yate
from deportivo import Deportivo
from alquilerBarcos import Alquiler
class main:
    barco1=Deportivo('AA3A',15,2018,200)
    barco2=Yate('ss3s',24,2020,2)

    alquilada=Alquiler('juancho',123,20,22,'--',barco1)

    print(alquilada.calcPrecioAlquiler())
