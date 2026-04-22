import sys

input = sys.stdin.readline
loop = True

while loop:

    questoes = int(input())

    if questoes == 0:
        break

    respostas = []

    for _ in range(questoes):

        A, B, C, D, E = map(int, input().split())

        alternativas = [(A, "A"), (B, "B"), (C, "C"), (D, "D"), (E, "E")]

        count = 0
        respostaAtual = ""

        for valor, letra in alternativas:
            if valor <= 127:
                count += 1
                respostaAtual = letra

        if count == 1:
            respostas.append(respostaAtual)
        else:
            respostas.append("*")

    for x in respostas:
        print(x)
