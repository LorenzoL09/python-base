def fattoriale(n):
    risultato=1
    for i in range(1, n+1):
        risultato*=i
    return risultato

n=int(input("inserisci un numero: "))
ris=fattoriale(n)
print(ris)