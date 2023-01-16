

'''
    Este módulo possui funções diversas que são compartilhadas com
outros módulos

'''


def _k(ax):
    '''Retorna a lagura da caixa do gráfico em pixels. Este valor é usado
       para definir os tamnhos das letras,  largura das linhas, etc
    '''
    return(ax.bbox.width)



# casas decimais numeros
def num_dec(num, d=1):
    '''
    Escreve um número com 'd'' casas decimais
    '''
    if d==0:
        text = f'{int(num)}'
    elif d==1:
        text = '{:,.1f}'.format(num)
    elif d==2:
        text = '{:,.2f}'.format(num)
    elif d==3:
        text = '{:,.3f}'.format(num)
    elif d==4:
        text = '{:,.4f}'.format(num)
    return(text)




def porcent_dec(num, d=1):
    '''
    Escreve uma porcentagem com 'd'' casas decimais
    '''
    if d==0:
        text = '{:,.0f}%'.format(num)
    elif d==1:
        text = '{:,.1f}%'.format(num)
    elif d==2:
        text = '{:,.2f}%'.format(num)
    elif d==3:
        text = '{:,.3f}%'.format(num)
    elif d==4:
        text = '{:,.4f}%'.format(num)
    return(text)




def formato_num_porc(tipoTexto=0, numero=None, porcent=None, d=0):
    '''
    Define o formato que será escrito um "numero" com uma
    "porcentagem" dentro de uma barra.Quando somente um valor
    é fornecido somente aquele valor é escrito. Quando nenhum
    valor é fornecido é retornado ''. Se os dois valores forem
    informados existem 4 possibilidades de texto para o outoput
    que dependende de do input 'tipoTexto':

    tipoTexto=0  ->  numero
                    (porcent)

    tipoTexto=1  ->  porcent
                    (numero)

    tipoTexto=2  ->  numero(porcent)

    tipoTexto=3  ->  porcent(numero)

    '''

    if porcent != None and numero == None:
        # so a porcetagem possui valor
        texto = f'{num_dec(porcent,d=d)}%'

    elif porcent == None and numero != None:
        # so o numero possui valor
        texto = f'{num_dec(numero,d=d)}'

    elif porcent == None and numero == None:
        # o numero e a porcentagem nao possuem valores
        texto=''

    else:
        # quando a porcentagem e o número possuem valores

        # monta o texto
        if tipoTexto==0:
            texto = f'{num_dec(numero,d=d)}\n'\
                    f'{num_dec(porcent,d=d)}%'

        elif tipoTexto==1:
            texto = f'{num_dec(porcent,d=d)}%\n'\
                    f'{num_dec(numero,d=d)}'

        elif tipoTexto==2:
            texto = f"{num_dec(numero,d=d)} ("\
                    f"{num_dec(porcent, d=d)}%)"

        elif tipoTexto==3:
            texto = f"{num_dec(porcent, d=d)}% ("\
                    f"{num_dec(numero, d=d)})"

    return(texto)
