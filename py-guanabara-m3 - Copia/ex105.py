#crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
#- quantidade de notas - a maior nota - a menor nota - a média da turma - a situação(opcional) - docstrigs

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    soma = maior = menor = media = cont = 0
    for c in n:
        if cont == 0:
            maior = c
            menor = c
        elif c > maior:
            maior = c
        elif c < menor:
            menor = c
        soma += c
        cont+=1
    media = soma / len(n)
    dicio = {'total': len(n), 'maior': maior, 'menor': menor, 'media': media}
    if sit == True:
        if media > 7:
            dicio['situacao'] = 'Boa'
        elif media > 5:
            dicio['situacao'] = 'Razoável'
        else:
            dicio['situacao'] = 'Ruim'
    return dicio


#resp = notas(5.5, 9.5, 10, 6.5, sit=True)
#resp = notas(5, 5, 5, 5, sit=True)
resp = notas(5, 7, sit=False)
print(resp)
help(notas)
