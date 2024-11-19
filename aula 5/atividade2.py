#2) Crie uma função fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.

def par_impar(n):
    
    if n % 2 == 0:
        print("par ʕ•́ᴥ•̀ʔ")
    else:
        print("impar ʕ•́ᴥ•̀ʔ")

par_impar(int(input("Digite um numero: ")))
