from calendar import month
from datetime import date, datetime, timedelta
import locale
from threading import local
from datetime import time


while True:
    agora = datetime.now()
    t = agora.strftime('%H:%M')
    t2 = agora.replace(hour=10, minute=31)
    t_simplificado = t2.strftime('%H:%M')

    if t >= t_simplificado:
        print('Se acabou')
        break