#crie um programa que leia em metros e converta em centímetros e milímetros

m = int(input("Quantos metros?: "))

print("Em {:.0f} metros tem {:.2f} centímetros e {:.3f} milímetros".format(m, m, m))

print("Em {} metros tem {}00 centímetros e {}000 milímetros".format(m, m, m))

print("Em {} metros tem {} centímetros e {} milímetros".format(m, (m*100), (m*1000)))