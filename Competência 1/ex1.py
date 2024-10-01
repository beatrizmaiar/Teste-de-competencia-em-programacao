pecas = []

while True:
  num = int(input())
  if 2 <= num <= 1000:
    break
  else:
    print("insira um número entre 2 e 1000.")

entrada = input()
pecas = list(map(int, entrada.split()))

sequencia_completa = set(range(1, num + 1))

pecas_presentes = set(pecas)

pecas_faltantes = sequencia_completa - pecas_presentes

print(pecas_faltantes.pop())
