# conversor-bases-python

Conversor de números da base decimal para bases de 2 até 16, desenvolvido em Python.

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de aplicar na prática um conceito estudado na faculdade: **conversão de bases numéricas**.

A ideia foi implementar, em Python, o algoritmo clássico que utiliza **divisão inteira e resto da divisão** para obter os dígitos da nova base.

O programa também realiza validação das entradas do usuário e suporta conversão para bases que utilizam caracteres hexadecimais (A, B, C, D, E e F).

---

## Funcionalidades

- Conversão de decimal para bases de 2 a 16
- Validação de entradas inválidas
- Suporte a representação hexadecimal
- Implementação manual do algoritmo de conversão

---

## Como funciona

O algoritmo segue os seguintes passos:

1. Divide o número pela base desejada
2. Armazena o resto da divisão
3. Atualiza o número com a divisão inteira
4. Repete até o número chegar em 0
5. Exibe os dígitos na ordem inversa

---

## Exemplo

Entrada:

```
Digite um número em base decimal: 255
Para qual base o 255 será convertido? (Max. 16) 16
```

Saída:

```
FF
```

---

## Como executar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo:

```bash
python ConvertorBases.py
```

3. Insira o número decimal e a base desejada.

---
