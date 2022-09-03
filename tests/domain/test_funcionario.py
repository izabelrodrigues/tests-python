from datetime import date
from domain.funcionario import Funcionario


class TestFuncionario:
    def test_valida_calculo_idade(self):

        # given
        ano_nascimento = 1980
        ano_atual = date.today().year
        idade_esperada = ano_atual - ano_nascimento

        funcionario_mock = Funcionario('Func-Test', '01/03/1980', 10000)

        # when
        idade_calculada = funcionario_mock.idade()

        # then
        assert idade_calculada == idade_esperada

    def test_valida_calculo_bonus_salario_maior_dez_mil_deve_retornar_zero(self):

        # given
        funcionario_mock = Funcionario('Func-Test', '01/03/1980', 11000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 0

    def test_valida_calculo_bonus_salario_menor_dez_mil_deve_retornar_bonus_dez_porcento(self):

        # given
        funcionario_mock = Funcionario('Func-Test', '01/03/1980', 9000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 900

    def test_valida_calculo_bonus_salario_igual_dez_mil_deve_retornar_bonus_mil_reais(self):

        # given
        funcionario_mock = Funcionario('Func-Test', '01/03/1980', 10000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 1000


