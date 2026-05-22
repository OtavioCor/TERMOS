from machine import Pin, time_pulse_us # mede tempo de pulsação em milisegundo
from time import sleep_us, sleep # lê o numero como milisegunda, sleep por segundos

trigger = Pin(5, Pin.OUT) # emite o som
echo = Pin(18, Pin.IN) # receber o som

def medir_distancia():
    trigger.off()
    sleep_us(2)
    
    trigger.on()
    sleep_us(10)
    trigger.off()
    
    duracao = time_pulse_us(echo, 1)
    
    distancia = (duracao * 0.0343) / 2 # O som pelo tempo, divido por 2 porque ele tem que ir e voltar
    
    return distancia

while True:
    distancia = medir_distancia()
    
    print("Distância: {:.2f} cm".format(distancia))
    sleep(1)
