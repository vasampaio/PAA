dp = {}
# Função que calcula se o troco é possível
def troco(valor, moedas):
    if(valor < 0): # Se o valor for negativo, não é possível
        return False
    if(valor == 0): # Se o valor for 0, é possível
        return True
    try :
        if dp[valor] >= 0: # Se o valor já foi calculado, retorna o valor
            return dp[valor]
    except:
        pass
    for i in moedas:
        if troco(valor - i, moedas): # Se o troco for possível, retorna True
            return True
    dp[valor] = False
    return False

def main():
    valor = 15 # Valor a ser trocado
    moedas = [10, 5] # Moedas disponíveis
    print(troco(valor, moedas))

if __name__ == "__main__":
    main()