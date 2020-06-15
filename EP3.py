from random import randint

m1='''
010
111
000
101'''.split() # Separa os elementos através do parâmetro do espaço vazio

m2='''
10101
10101
11111'''.split()

m3 = '''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''.split()

matriz = [m1, m2, m3] # Lista com as matrizes de possibilidades

m = matriz[randint(0,2)] # Faz sorteio das matrizes de possibilidades
print ("Entrada:")
print (m)
print ()

m = [list(x) for x in m] # Separa cada unidade da linha da matriz

print ("Matriz de Entrada:")
for x in m:
    print (' '.join(x)) # Fazendo com que se pareca mais com uma matriz
                        # Mostra a matriz do parametro de entrada
print() 


regioes = []

lin = len(m) # A quantidade de linhas na matriz
             # eh a quantidade de elementos que nela contem

col = len(m[0]) # A quantidade de colunas
                # eh o tamanho de um dos elementos da matriz


def cima(x, y): # O parametro sao as coordenadas do elemento na matriz
  if x == -1: # Se ele é um elemento de posicao na 1º linha
              # Porque ele não teria um antecessor
      return False
  return m[x][y] == '1'



def esq(x, y):
  if y == -1: # Se ele é um elemento de posicao na 1º coluna
      return False
  return m[x][y] == '1'


def regindex(x, y):
  for k in range(len(regioes)):
    for coord in regioes[k]:
      if (x, y) == coord:
        return k
  else:
    return -1


for j in range(lin):
  for k in range(col):

    if m[j][k] == '1':
      rcima = resq = -1

      if cima(j-1, k):
          rcima = regindex(j-1, k) 

      if esq(j, k-1):
          resq = regindex(j, k-1)

      if rcima != -1:
        regioes[rcima].append((j, k))

      if resq != -1:

        if rcima != -1:

          if rcima == resq:
              continue

          regioes[rcima].extend(regioes[resq])
          del regioes[resq]

        else:
          regioes[resq].append((j, k))

      if rcima == resq == -1:
        regioes.append([(j, k)])

cont = ord('1')

for r in regioes:
  for j, k in r:
    m[j][k] = chr(cont)
  cont = cont + 1

print ("Matriz de Saída:")
for linha in m:
  print (' '.join(linha))
