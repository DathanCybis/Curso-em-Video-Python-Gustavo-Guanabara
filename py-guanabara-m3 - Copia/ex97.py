#crie um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(txt):
    f = len(txt) + 4
    print("~" * f)
    print(f"{f"{txt}":^{f}}")
    print("~" * f)

escreva("teste")
escreva("basquete")
escreva("Curso em Vídeo")
escreva("Evolução")
