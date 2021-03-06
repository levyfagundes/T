# -*- coding: utf-8 -*-

from random import choice

#gera a palavra a partir da categoria escolhida
def gera_palavra(idx):

  animal = ['PATO','GATO','BALEIA']
  fruta = ['BANANA','LIMAO','MANGA']
  objeto = ['DADO','CANETA', 'PINCEL']

  lista = animal,fruta,objeto

  palavra = choice(lista[idx])

  return palavra

#exibe a dica da palavra na tela
def dica(sorteio):
  if sorteio == 0:
    print('\nDICA: A palavra e um(a): ANIMAL\n')
  elif sorteio == 1:
    print('\nDICA: A palavra e um(a): FRUTA\n')
  else:
    print('\nDICA: A palavra e um(a): OBJETO\n')
      
#imprime a string com as palavras que o jogador chutou      
def imprimeChutes(str_chutes):
  print("Chutes:", end=" ")
  for s in str_chutes:
    print("%c"%s, end=" ")

  print("")

def atualizaForca(chute, oldForca, palavra):
  newForca = str()

  for j in range(len(oldForca)):

    if(chute == palavra[j]):
      newForca += chute
    else:
      newForca += oldForca[j]

  return newForca
        
#Programa Principal
print('='*50)
print('{:^50}'.format('JOGO DA FORCA'))
print('='*50)
print('Tente descobrir qual a palavra !!\n')

num = choice([0,1,2]) #escolhe em qual categoria a palavra será gerada

escolhe = gera_palavra(num) #palavra que foi gerada para o jogo
tam_palavra = len(escolhe)  #tamanho da palavra que foi gerada para o jogo

saida = "_"*(tam_palavra) #irá guardar a string que aparece as letras que o jogador acertou
chutes_letras = str() #armazena as letras que o jogador chutou

tentativas = 6 #quantidade de tentativas que o jogador tem
i=0

dica(num)
print('A palavra tem {} letras.\n'.format(tam_palavra))
print(saida)

while(i<tentativas):

  print('\nVocê ainda tem {} tentativas !\n'.format(tentativas - i))

  chute = input('\nLetra: ').upper()

  aux = str()

  if ( (chute in chutes_letras) or (chute in saida) ):
    print("Você já escolheu essa letra, tente de novo")
  
  else:
    i+=1

    if(chute in escolhe):
    #   for j in range(tam_palavra):
    #     if(chute == escolhe[j]):
    #       aux += chute
    #       acertos+=1
    #     else:
    #       aux += saida[j]

      saida = atualizaForca(chute, saida, escolhe)

    else:
      print("Não existe a letra", chute)
      chutes_letras+=chute


    imprimeChutes(chutes_letras)
    print(saida)

    if(saida == escolhe):
      print('Você GANHOU !!\nA palavra era: {}'.format(escolhe))
      break

if(saida != escolhe):
  print('\n\nVocê PERDEU!')
  print('\nA palavra era: {}\n\n'.format(escolhe))
  
  
