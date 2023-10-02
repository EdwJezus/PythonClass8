print('Lista de Exercícios por Eduardo Jesus')

def cab(n):
  print('')
  print('='*50)
  print('')
  print('Atividade', n)
  print('')
  print('-'*30)
  print('')

################################
##Atividade 1
cab(1)

def nested_sum(lista):
    soma = 0
    for k in lista:
        for c in k:
            soma += c
    return soma
    

t = [[1], [1, 2], [2, 3]]

print(nested_sum(t))

################################
##Atividade 2
cab(2)

def cumsum(lista):
    soma = 0
    soma_cum = []
    for k in lista:
        soma += k
        soma_cum.append(soma)
    return soma_cum

print(cumsum([1, 2, 3]))

################################
##Atividade 3
cab(3)

def middle(lista):
    lista_middle = []
    for k in range(0, len(lista)):
        if k != 0 and k != len(lista):
            lista_middle.append(lista[k])
    return lista_middle

lista = [1, 2, 3, 4]
print(middle(lista))

################################
##Atividade 4
cab(4)

def chop(lista):
    lista.pop()
    lista.pop(0)
    return lista

lista = [1, 2, 3, 4]
chop(lista)
print(lista)

################################
##Atividade 5
cab(5)

def is_sorted(lista):
    lista_sorted = lista[:]
    lista_sorted.sort()
    return lista == lista_sorted

lista = [1, 2, 3]
lista2 = ['b', 'a']
print(is_sorted(lista))
print(is_sorted(lista2))

################################
##Atividade 6
cab(6)

def is_anagram(palavra1, palavra2):
    novapalavra = ''
    if len(palavra1) != len(palavra2):
        print('a')
        return False
    for k in range(0, len(palavra1)):
        for c in range(0, len(palavra2)):
            if palavra1[k] == palavra2[c]:
                novapalavra += palavra2[c]
                palavra2.replace(palavra2[c], '')
                break
    return palavra1 == novapalavra

a = 'abc'
b = 'cba'
c = 'ppp'
print(is_anagram(a, b))
print(is_anagram(a, c))

################################
##Atividade 7
cab(7)

def has_duplicates(lista, lista1):
    for k in lista:
        contador = 0
        for c in lista1:
            if k == c:
                contador += 1
        if contador > 1:
            return True
    return False

a = [1, 2, 3, 4, 5]
b = [3, 4, 5]
c = [3, 3]
print(has_duplicates(a, b))
print(has_duplicates(a, c))

################################
##Atividade 8
cab(8)

def birthday(a):
    prob = 1
    for k in range(0, a):
        prob *= (365 - k) / 365
    return f'{100 - (prob * 100)}%'


print(birthday(23))

################################
##Atividade 9
cab(9)

def lista_append():
    lista = []
    arq = open('words.txt')
    for k in arq:
        lista.append(k.strip())
    return lista

def lista_sum():
    lista = []
    arq = open('words.txt')
    for k in arq:
        lista += [k.strip()]
    return lista

print(lista_append())
print(lista_sum())

################################
##Atividade 10
cab(10)

def in_bisect(lista_ordenada, valor_alvo):
    if len(lista_ordenada) == 0:
        return False
    else:
        meio = len(lista_ordenada) // 2
        if lista_ordenada[meio] == valor_alvo:
            return meio
        elif lista_ordenada[meio] > valor_alvo:
            return in_bisect(lista_ordenada[:meio], valor_alvo)
        else:
            i = in_bisect(lista_ordenada[meio+1:], valor_alvo)
            if i == None:
                return None
            else:
                return meio+1+i

################################
##Atividade 11
cab(11)

def reverse_pair(word_list):
    for word1 in word_list:
        for word2 in word_list:
            if word1 == word2[::-1]:
                print(word1, word2)
