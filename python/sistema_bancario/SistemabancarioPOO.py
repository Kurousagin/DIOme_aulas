from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def efetuar_transacao(self, conta, transacao):
        transacao.registar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica:
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico - Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls( numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        saldo_excedido = valor > saldo

        if saldo_excedido:
            print("Falha!! Saldo insuficiente")

        elif valor > 0:
            self.saldo -= valor
            print("saque realizaado com sucesso!!")
            return True

        else:
            print("Falha!! Valor inválido")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso!")

        else:
            print("Falha! Valor inválido")
            return False
        
        return True
    

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limte = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        nro_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        limite_excedido = valor > self.limite
        saque_excedido = nro_saques > self.limite_saque

        if limite_excedido:
            print("Operação Falhou!! Limite excedido!" )

        elif saque_excedido:
            print("Operação falhou!! Limite de sques excedido!!")

        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"\ Agência: \t{self.agencia} C/C\t\t {self.numero}Titular\t{self.cliente.nome} "


class Historico:
    def __init__(self):
        self.transacoes = []

    # @property

class Transacao:
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass