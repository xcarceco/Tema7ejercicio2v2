#En este segundo ejercicios tendréis que crear un script que nos diga si es
# la hora de ir a casa. Tendréis que hacer uso del modulo time.
# Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y en
# caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time

horaactu=time.strftime("%I:%M:%S")
hora=int(time.strftime("%I"))
horafinal=int('6')
minuto=int(time.strftime("%M"))
minutofinal=int('60')
diferencia=horafinal-hora
diferenciaminuto=minutofinal-minuto
horadefin='07:00:00'

print('La fecha es:',time.strftime("%d/%m/%y"))
print('La hora es:',horaactu)
print('tu jornada se termina a las ', horadefin)

if horaactu>horadefin :
    print('Es hora de irse')
elif horaactu<horadefin :
    print('Aun te queda', diferencia, 'horas', diferenciaminuto, 'minutos')

