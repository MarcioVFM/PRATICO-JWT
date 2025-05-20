from datetime import datetime

horario = datetime.now()
formatado = horario.strftime("%d/%m/%Y %H:%M:%S")
print(formatado)