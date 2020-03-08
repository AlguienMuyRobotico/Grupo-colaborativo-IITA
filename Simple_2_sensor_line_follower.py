# Librerias
import os, sys, inspect, time
# Cosadelprincipioquenoseloquehace
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Importa PiStorms
from PiStorms import PiStorms
# Crea instancia del objeto PiStorms
psm = PiStorms()

while True:
    # Lee valores de los sensores de luz del banco A y los almacena en variables
    sensor1 = psm.BAS1.reflectedLightSensorEV3()
    sensor2 = psm.BAS2.reflectedLightSensorEV3()

    # Si el sensor de luz detecta blanco, mueve su respectivo motor a 60 de velocidad. Si detecta negro lo para.
    if(sensor1 > 20):
        # Hace andar el motor 1 del banco B a 60 de velocidad infinitamente
        psm.BBM1.setSpeed(60)
    else:
        # Para el motor 1 del banco B
        psm.BBM1.brake()

    # Si el sensor de luz detecta blanco, mueve su respectivo motor a 60 de velocidad. Si detecta negro lo para.
    if(sensor2 >20):
        # Hace andar el motor 2 del banco B a 60 de velocidad infinitamente
        psm.BBM2.setSpeed(60)
    else:
        # Para el motor 2 del banco B
        psm.BBM2.brake()


