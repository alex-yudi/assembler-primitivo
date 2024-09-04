Este repositório contém a implementação de um `Assembler primitivo`, fazendo a conversão de código `Assembly MIPS32` para `Binário` ou `Hexadecimal` (o hexadecimal em formato compatível para implementação de imagem nas memórias utilizadas no Logisim).
Esse Assembler foi criado como um dos trabalhos da cadeira `Arquitetura e Organização de Computadores`, do curso de `Ciência da Computação` da `Ufersa`

Não ocorre tratamento de erros, então é necessário que o código Assembly utilizado possua sintaxe correta, bem como utilização dos registradores corretos.

## Para executar:
  Por se tratar de um código em python, é necessário que a máquina possua ele instalado.
  É necessário executar o arquivo `montador.py` com python e, via linha de comando, também passar qual arquivo será lido e convertido, bem como ser passado os argumentos `-b` ou `-h` para identificar se a conversão deve ser para binário ou hexadecimal.
  No terminal, o comando ficará parecido com isso: `/bin/python3 ./montador.py Teste.asm -h`
    A primeira parte sendo o comando para execução de código python, a segunda sendo qual o código para ser executado, a terceira qual o arquivo lido e a quarta qual o formato de saída.
