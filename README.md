# 👩🏻‍💻 Identificando Imagens Binarias 

## 👨🏽‍🏫 Professor Orientador: [Fernando Masanori](https://github.com/fmasanori)

## 📋  Enunciado

Dada uma imagem binária identifique suas regiões conexas utilizando estruturas de dados do Python. A conexão não ocorre na diagonal, somente na horizontal e vertical. Os programas devem passar pelos três testes abaixo:

* Não ler arquivos;
* Atribuir as matrizes como um texto multilinha e,
* Converter para matriz de zeros e uns.

⚠  **OBS:** É recomendado testar com outras matrizes de entrada.

Há várias aplicações interessantes para este problema, tais como: aplicações militares (reconhecimento de instalações ou objetos em imagens de satélite), aplicações da agroindústria (previsão de safras) ou na medicina (identificação de regiões cancerígenas em imagens de tomografia). 

É dada uma imagem através de uma matriz de “pixels”, onde cada pixel pode assumir o valor 0 (branco) ou 1 (preto). Desejamos identificar os objetos conexos da imagem, ou seja, dada a matriz da imagem, seu programa deverá rotular os “pixels” da matriz de forma a identificar os objetos conexos nela contidos. Seu programa deverá ser bastante eficiente, evitando percorrer toda a matriz de entrada várias vezes. Uma estratégia que deverá ser implementada é a que descrevemos a seguir. A matriz é varrida de cima para baixo e da esquerda para a direita. Se um “pixel” tem valor 1, verificamos seu vizinho de cima e o da esquerda. Se ambos são 0, um novo objeto começa neste pixel. Se um deles é 1, este pixel pertence ao objeto anterior. Finalmente, se ambos os vizinhos têm rótulos diferentes, a matriz deverá ser corrigida para que ambos tenham o mesmo rótulo (ou seja, um dos rótulos vai desaparecer e todos os pixels daquele rótulo vão passar a ter o outro). A fim de realizar eficientemente esta última operação cada objeto deverá manter uma lista com as coordenadas dos pixels associados com seu rótulo.

**Entrada:** 📥 
 ~~~
 010
 111
 000
 101
 ~~~
  
**Saída:** 📤 
 ~~~
 010
 111
 000
 203
 ~~~
  
-------------------

**Entrada:** 📥 
 ~~~
 10101
 10101
 11111
 ~~~
  
**Saída:** 📤 
 ~~~
 10101
 10101
 11111
 ~~~
  
------------------
  
**Entrada:** 📥 
 ~~~
 0011001010
 0110001010
 0011001110
 0000000000
 0010001010
 0010011111
 1111100000
 0010001110
 0010001110
 ~~~
  
**Saída:** 📤 
~~~
0011002020
0110002020
0011002220
0030004040
0030044444
3333300000
0030005550
0030005550
~~~
