# https://www.beecrowd.com.br/judge/pt/problems/view/1089

while ((n := int(input())) != 0):
    peaks = 0
    magnitudes = list(map(int, input().split()))

    #adiciona os dois primeiros elementos para a lista ser circular quando chamar função zip
    magnitudes += magnitudes[0:2]

    for left, middle, right in zip(magnitudes, magnitudes[1:], magnitudes[2:]):
        
        # se as variações entre o meio e os vizinhos tiverem sinais iguais,
        # então significa que os dois pontos vizinhos estão no mesmo hemisfério
        # (acima ou abaixo de middle)
        # o produto dessas variações ser positivo indica que as variações têm sinais iguais
        if (middle - right) * (middle - left) > 0:
            peaks += 1
    
    print(peaks)
