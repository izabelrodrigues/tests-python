from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario,funcao):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        self._funcao = funcao

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_split = self._data_nascimento.split('/')
        ano_nascimento = data_split[-1]

        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário está em uma faixa não permitida para receber um bônus!')
        return valor

    def decrescer_salario(self):
        if self._salario >= 100000 and (self._is_diretor() or self._is_socio()):
            decrescimo = self._salario * 0.10
            self._salario = self._salario - decrescimo

    def _is_diretor(self):
        return self._funcao == 'DIRETOR'
    def _is_socio(self):
        return self._funcao == 'SOCIO'

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario}, {self._funcao})'
