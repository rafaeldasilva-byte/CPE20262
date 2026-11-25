# Importa o molde (classe) da biblioteca
from argon2 import PasswordHasher

# Cria a instância da máquina de hash com os custos padrão
ph = PasswordHasher()

dado_sensivel = "minha string secreta"
dado_sensivel1 = "minha string secrta"

# O método .hash() aceita APENAS uma str (ou bytes) por vez
# e devolve uma nova str no formato PHC
resultado_phc = ph.hash(dado_sensivel)
resultado1_phc = ph.hash(dado_sensivel1)

print("O que vai para o arquivo:",resultado_phc, resultado1_phc)
