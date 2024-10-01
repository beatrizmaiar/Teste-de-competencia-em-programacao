def conta_pares(n, lista_de_botas):
    pares = 0
    tamanhos_direito = {}
    for bota in lista_de_botas:
        tamanho, pe = bota
        if pe == "D":
            if tamanho in tamanhos_direito:
                tamanhos_direito[tamanho] += 1
            else:
                tamanhos_direito[tamanho] = 1
        else:
            if tamanho in tamanhos_direito:
                pares += 1
                tamanhos_direito[tamanho] -= 1
    return pares

def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            lista_de_botas = []
            for _ in range(n):
                tamanho, pe = input().split()
                lista_de_botas.append((int(tamanho), pe))
            pares = conta_pares(n, lista_de_botas)
            print(pares)
        except EOFError:
            break

if __name__ == "__main__":
    main()