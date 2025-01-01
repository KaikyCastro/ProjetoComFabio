import re

class CPF:
    def __init__(self, cpf):
        self.__cpf = cpf

    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpf):
        self.__cpf = cpf

    def validate(self, cpf) -> bool:

    # Verifica a formata��o do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Obt�m apenas os n�meros do CPF, ignorando pontua��es
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 n�meros ou se todos s�o iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Valida��o do primeiro d�gito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Valida��o do segundo d�gito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True
    