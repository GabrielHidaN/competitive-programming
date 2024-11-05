'''
Estrutura do CPF
Um CPF possui 11 dígitos no formato: XXX.XXX.XXX-YY, onde:

Os 9 primeiros dígitos (XXX.XXX.XXX) representam a base do CPF.
Os 2 últimos dígitos (YY) são dígitos verificadores, calculados a partir dos 9 primeiros.
Passos para Validar um CPF
Verifique se todos os dígitos são iguais: Um CPF com todos os dígitos iguais (como 111.111.111-11) é inválido.

Cálculo do Primeiro Dígito Verificador (penúltimo dígito do CPF):

Multiplique os 9 primeiros dígitos do CPF por uma sequência decrescente de números começando de 10 até 2.
Some todos os valores resultantes.
Calcule o módulo 11 da soma: R = soma % 11.
Se R for menor que 2, o primeiro dígito verificador é 0; caso contrário, ele será 11 - R.
Cálculo do Segundo Dígito Verificador (último dígito do CPF):

Inclua o primeiro dígito verificador calculado e multiplique os 10 primeiros dígitos por uma sequência decrescente de números, agora de 11 até 2.
Some todos os valores resultantes.
Calcule o módulo 11 da soma: R = soma % 11.
Se R for menor que 2, o segundo dígito verificador é 0; caso contrário, ele será 11 - R.
Verificação Final: Compare os dígitos verificadores calculados com os fornecidos no CPF. Se ambos coincidirem, o CPF é válido.
'''

class Validador_de_cpf:
    def __init__(self , cpf):
        self.cpf = cpf

    def verificar_modelo_enviado(self):
        self.cpf = cpf
        
        if cpf.isdigit():

            if len(self.cpf) != 11:
                print('@@@ CPF Inválido. Um CPF Válido Deve conter 11 Caracter!')
                return False
            return True
        print('@@@ Você Deve enviar Um digito!')
        return False


    def verificar_numeros(self ):
        self.cpf = str(cpf)
        if self.verificar_modelo_enviado() == True:
            cpf_valido = set(cpf)
            if len(cpf_valido) == 1:
                print('@@@ CPF Inválido, Você tentou me sacanear hahaha @@@')
                return False
            return True
        return False
    
    def validar_cpf(self):
        if self.verificar_numeros():
        # Cálculo do primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            primeiro_digito = (soma * 10) % 11
            primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

            if primeiro_digito != int(cpf[9]):
                print('@@@ CPF Inválido /1 digit @@@')
                return

        # Cálculo do segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            segundo_digito = (soma * 10) % 11
            segundo_digito = 0 if segundo_digito == 10 else segundo_digito

            if segundo_digito == int(cpf[10]):
                print(f'O CPF :  {cpf} é Válido.')
                return
            else:
                print('@@@ CPF Inválido /2 digit @@@')
                return
        





cpf= str(input('digite \n =>\t'))
cpf1= Validador_de_cpf(cpf)


#TODO resolver bug de metodo
cpf1.validar_cpf()