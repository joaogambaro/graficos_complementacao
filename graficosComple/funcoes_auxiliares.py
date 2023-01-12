

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
