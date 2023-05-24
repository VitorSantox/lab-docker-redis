import redis
from datetime import datetime, timedelta

#Criando conexão com o Redis
r = redis.Redis(host='localhost', port=6379)


#informando o horario de inicio
horario_atual = datetime.now()
hora_atual = horario_atual.strftime("%H:%M")
print("Inicio de teste:", hora_atual)

# Realizando 1000 inserções
for i in range(100):
    r.set(f'key{i}', f'value{i}')

# informando o horario final
horario_atual2 = datetime.now()
hora_atual2 = horario_atual2.strftime("%H:%M")
print("Fim de teste:", hora_atual2)
