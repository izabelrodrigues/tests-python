from datetime import date
from domain.funcionario import Funcionario


class TestFuncionario:
    def test_valida_calculo_idade(self):
        # given
        ano_nascimento = 1980
        ano_atual = date.today().year
        idade_esperada = ano_atual - ano_nascimento

        funcionario_mock = self.build_mock_funcionario(10000)

        # when
        idade_calculada = funcionario_mock.idade()

        # then
        assert idade_calculada == idade_esperada

    def test_valida_calculo_bonus_salario_maior_dez_mil_deve_retornar_zero(self):
        # given
        funcionario_mock = self.build_mock_funcionario(11000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 0

    def test_valida_calculo_bonus_salario_menor_dez_mil_deve_retornar_bonus_dez_porcento(self):
        # given
        funcionario_mock = self.build_mock_funcionario(9000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 900

    def test_valida_calculo_bonus_salario_igual_dez_mil_deve_retornar_bonus_mil_reais(self):
        # given
        funcionario_mock = self.build_mock_funcionario(10000)

        # when
        bonus_calculado = funcionario_mock.calcular_bonus()

        # then
        assert bonus_calculado == 1000

    def test_quando_salario_igual_cem_mil_deve_realizar_decrescimo_dez_porcento(self):
        # given
        salario = 100000
        funcionario_mock = self.build_mock_funcionario(salario, 'DIRETOR')
        novo_salario_esperado = 90000

        # when
        funcionario_mock.decrescer_salario()
        novo_salario_calculado = funcionario_mock._salario

        # then
        assert novo_salario_calculado == novo_salario_esperado

    def test_quando_salario_maior_cem_mil_deve_realizar_decrescimo_dez_porcento(self):
        # given
        salario = 150000
        funcionario_mock = self.build_mock_funcionario(salario,'SOCIO')
        novo_salario_esperado = 135000

        # when
        funcionario_mock.decrescer_salario()
        novo_salario_calculado = funcionario_mock._salario

        # then
        assert novo_salario_calculado == novo_salario_esperado

    def test_quando_salario_menor_cem_mil_nao_deve_realizar_decrescimo_dez_porcento(self):
        # given
        salario = 90000
        funcionario_mock = self.build_mock_funcionario(salario)
        novo_salario_esperado = 90000

        # when
        funcionario_mock.decrescer_salario()
        novo_salario_calculado = funcionario_mock._salario

        # then
        assert novo_salario_calculado == novo_salario_esperado

    def test_quando_diretor_salario_menor_cem_mil_nao_deve_realizar_decrescimo_dez_porcento(self):
        # given
        salario = 90000
        funcionario_mock = self.build_mock_funcionario(salario, 'DIRETOR')
        novo_salario_esperado = 90000

        # when
        funcionario_mock.decrescer_salario()
        novo_salario_calculado = funcionario_mock._salario

        # then
        assert novo_salario_calculado == novo_salario_esperado

    def test_quando_socio_salario_menor_cem_mil_nao_deve_realizar_decrescimo_dez_porcento(self):
        # given
        salario = 90000
        funcionario_mock = self.build_mock_funcionario(salario, 'SOCIO')
        novo_salario_esperado = 90000

        # when
        funcionario_mock.decrescer_salario()
        novo_salario_calculado = funcionario_mock._salario

        # then
        assert novo_salario_calculado == novo_salario_esperado

    def build_mock_funcionario(self, salario, funcao='TEAM'):
        return Funcionario('Func-Test', '01/03/1980', salario, funcao)

