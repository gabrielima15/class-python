﻿# class-python

<br>

## explicação do uso do de class na disciplina de Estrtura de Dados.

<br>

### o que são classes.

<br>

## Em Python, uma classe é um "modelo" ou "plano" para criar objetos, que são entidades com dados (atributos) e comportamentos (métodos) específicos. Classes permitem que você organize seu código de forma modular, facilitando a criação de objetos reutilizáveis e a manutenção do código, onde cada um tem funções específico para.

<br>

## Elaboração de projetos a:

<br>

## Modelo para criação de objetos:
<br>

## Uma classe define a estrutura de um objeto, incluindo seus atributos (variáveis que armazenam informações) e métodos (funções que definem o que o objeto pode fazer).

<br> 

## Organização e modularidade:
## Classes permitem que você agrupe dados e funcionalidades relacionadas, tornando seu código mais organizado e fácil de entender. 
<br>

## Reutilização de código:
<br>

### Uma vez que você cria uma classe, você pode criar vários objetos a partir dela, cada um com seus próprios dados, mas todos compartilhando os mesmos métodos e comportamento. 
<br>

## Programação orientada a objetos (POO):
<br>

## Classes são um conceito fundamental da POO, um paradigma de programação que organiza o código em objetos e suas interações. 

<br>

```

# Definição da classe
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca  # Atributo
        self.cor = cor      # Atributo

    def acelerar(self):    # Método
        print("O carro está acelerando.")

    def frear(self):        # Método
        print("O carro está freando.")

# Criação de objetos (instâncias da classe)
meu_carro = Carro("Toyota", "Branco")  # Objeto
outro_carro = Carro("Honda", "Azul")   # Objeto

# Acessando atributos e chamando métodos
print(meu_carro.marca)      # Saída: Toyota
meu_carro.acelerar()        # Saída: O carro está acelerando.
outro_carro.frear()        # Saída: O carro está freando.

```
<br>

## Definição:

<br>

### (1) Serve para definir o nome da classe usamos a palavra reservado class.
<br>

### (2) Após o nome da classe devemos adicionar dois pontos.(:)

<br>

```
class pessoa:
```

<br>

### (3) Para criar um método usamos a palavra reservada 'def'.

<br>

### (4) O construtor é o método reservado chamado __init__.

<br>

### (5) O parâmetro self é obrigatório e os demais são definidos por nós.

<br>

```
def __init__(self,nome,idade):
```
<br>

### (6) Aqui está o corpo do método, sempre identado como manda a sintaxe da linguagem.

<br>

```
self.nome = nome
self.idade = idade

```

<br>
<br>

### Códico Completo:

<br>

```
class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def SetNome(nome):
        self.nome = nome
    
    def SetIdade(idade):
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
        
```
