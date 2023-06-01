import redis

#Criando conexão com o Redis
r = redis.Redis(
  host='redis-14684.c114.us-east-1-4.ec2.cloud.redislabs.com',
  port=14684,
  password='SMvmjY73AMdcUlmh9KKMRxbYI6F2aC8e')

# Armazenar informações de eventos em hashes
r.hset('event:1', 'name', 'Login')
r.hset('event:1', 'timestamp', '2022-01-01T10:00:00')
r.hset('event:1', 'type', 'login')

print("Cadastro de user feito")

# Indexar o hash com o RedisSearch
r.execute_command('FT.ADD', 'events', 'event:1', '1.0', 'FIELDS', 'name', 'timestamp', 'type')

# Pesquisar eventos com base no tipo usando o RedisSearch
search_results = redis_client.execute_command('FT.SEARCH', 'events', '@type:login')
print(search_results)
