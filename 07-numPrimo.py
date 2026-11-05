def primo(n):
    if n < 2:
        return False 
    for i in range(2, n):
        if n%i==0:
            return False
    return True

n=int(input("inserisci un numero: "))
if primo(n):
    print("il numero è primo")
else:
    print("il numero non è primo")