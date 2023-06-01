import redis

#Criando conexão com o Redis
r = redis.Redis(
  host='redis-14684.c114.us-east-1-4.ec2.cloud.redislabs.com',
  port=14684,
  password='SMvmjY73AMdcUlmh9KKMRxbYI6F2aC8e')

# Armazenar informações de eventos em hashes(chave)
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', 'age', 25)
r.hset('user:1', 'city', 'New York')

print("Cadastro de user feito")

#criando um novo hash(chave)
r.hset('user:2', 'name', 'torvi')

#alterando valor de um hash(chave)
r.hset('user:1', 'name', 'torvidois')

#extraindo informação de uma chave valor
name = r.hget('user:1', 'name')

print(name)