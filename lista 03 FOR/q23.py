def main():
    n = int(input('Quantidade de funcionários: '))

    for i in range(n):
        print(f'\nFuncionário {i + 1}')
        codigo = int(input('Código: '))
        horas = int(input('Horas trabalhadas: '))
        dependentes = int(input('Quantidade de dependentes: '))

        valor_horas = horas * 12
        valor_dependentes = dependentes * 40
        salario = valor_horas + valor_dependentes
        inss = salario * 0.085 
        ir = salario * 0.05 
        total = salario - (inss + ir)

        tela = f'''
    Informações do código:  {codigo}
    Valor descontado(INSS): R$ {inss:.2f}
    Valor descontado(IR):   R$ {ir:.2f}
    Salário líquido:        R$ {total:.2f}
    '''
        print(tela)


main()
