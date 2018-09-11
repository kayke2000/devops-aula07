import jogovelha
import sys

erroValidacao = FALSE

jogovelha.inicializar()
jogovelha.jogada()
valid = jogovelha.validacao()

SE valid == FALSE:
  erroValidacao = TRUE
SENAO: 
    PARA cada jogada FACA: 
      SE jogada não for concluida FACA:
        erroValidacao = TRUE
      ELSE
          PARA cada posicao FACA:
             SE jogada concluida e marcação em cima de outra marcação FACA:
                erroValidacao = TRUE
SE erroValidacao FACA:
  Mensagem : ERRO!
SENAO:
  sys.exit(0)
          
                
                
             
        
      
