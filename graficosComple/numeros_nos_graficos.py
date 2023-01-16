
'''
Funções neste módulo:

-> Para barras otizontais

    num_barras_verticais(ax, f_texto_bar=0.025,
                     f_tam_letra=0.25,
                     cor_texto='#000000',
                     d=1, rotation=0, ds=None)

    porc_barras_verticais(ax, sum_tot=None,
                      f_texto_bar=0.025, f_tam_letra=0.25,
                      cor_texto='#000000', d=1, rotation=0, ds=None)

    porc_num_bar_verticais(ax, sum_tot=None,  f_texto_bar=0.025,
                       f_tam_letra=0.25, d_porc=1,  d_num=1,
                       org_texto=1, cor_texto='#000000',
                       rotation=0, ds=None )


-> Para barras otizontais

    num_barras_horizontais(ax, f_texto_bar=0.025, f_tam_letra=0.25,
                       cor_texto='#000000', d=1, rotation=0, ds=None)

    porc_barras_horizontais(ax, sum_tot=None, f_texto_bar=0.025,
                        f_tam_letra=0.25, cor_texto='#000000', d=1,
                        rotation=0, ds=None)

    porc_num_bar_horizontal(ax, sum_tot=None, f_texto_bar=0.025,
                        f_tam_letra=0.25, d_porc=1, d_num=1,
                        org_texto=1, cor_texto='#000000',
                        rotation=0, ds=None)

-> Para linhas
    num_graf_linhas(ax,f_tam_letra=0.02,f_texto_linha=0.025,]
                cor_texto='#000000', d=1, rotation=0, ds=None):
'''









# importa parâmetro para definir tamanhos
import graficosComple.funcoes_auxiliares as faux

'''
faux.num_dec(num, d=1)

# casas decimais numeros
def num_dec(num, d=1):

    #Escreve um número com 'd'' casas decimais

    if d==0:
        text = '{:,.0f}'.format(num)
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

    #Escreve uma porcentagem com 'd'' casas decimais

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
'''



def num_barras_verticais(ax,
                         f_texto_bar=0.025,
                         f_tam_letra=0.02,
                         cor_texto='#000000',
                         d=0,
                         rotation=0,
                         ds=None,
                         prefix='',
                         sufix=''
                           ):
    '''
    Escreve os números em cima das barras

    Args:
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra.
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd': número de casas decimais do numero das barras
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos
    '''

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()+ds

        ax.annotate(f'{prefix}{faux.num_dec(p.get_height(), d=d)}{sufix}',
                    (x, y),
                    rotation=rotation,
                    **kargs)
        #Obs: nas anotações não colocar 'y', mas sim "p.get_height()"
        #isto ppor que o valor de y está acrescido de 'ds' e seria
        #escrito um valor errado

    return(ds)



def porc_barras_verticais(ax,
                          sum_tot=None,
                          f_texto_bar=0.025,
                          f_tam_letra=0.02,
                          cor_texto='#000000',
                          d=1,
                          rotation=0,
                          ds=None):

    '''
    Escreve as porcentagens em cima das barras

    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra.
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd': número de casas decimais da porcentagem
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos
    '''



    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2




    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()

        porc= (y/sum_tot)*100

        ax.annotate(porcent_dec(porc, d=d),
                    (x, y+ds),
                    rotation=rotation,
                    **kargs)

    return(ds)



def porc_num_bar_verticais(ax, sum_tot=None,  f_texto_bar=0.025,  f_tam_letra=0.02,
                      d_porc=1,  d_num=1,  org_texto=0, cor_texto='#000000',
                      rotation=0, ds=None):
    '''
    Escreve os números e as porcentagens em cima das barras

    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra.
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd_porc': número de casas decimais da porcentagem
    'd_num': número de casas decimais do numero das barras
    'org_texto': numero que define a organização das anotações:
        0-> escreve numero em cima e porcentagem a baixo
        1-> escreve porcentagem em cima e número a baixo
    'rotation': rotação das anotações
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos
    '''


    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        x = p.get_center()[0]
        y = p.get_height()

        # calcula a porcentagem
        porc= (y/sum_tot)*100


        # monta o texto
        if org_texto==0:
            texto=  faux.num_dec(p.get_height(),d=d_num)+'\n'+\
                    faux.porcent_dec(porc, d=d_porc)
        elif org_texto==1:
            texto=  faux.porcent_dec(porc, d=d_porc)+'\n'+\
                    faux.num_dec(p.get_height(),d=d_num)


        # escreve na figura
        ax.annotate(texto,
                    (x, y+ds),
                    rotation=rotation,
                    **kargs)

    # retorna 'dh' para graficos correlaciondados
    return(ds)




def num_barras_horizontais(ax,
                           f_texto_bar=0.025,
                           f_tam_letra=0.02,
                           cor_texto='#000000',
                           d=1,
                           rotation=0,
                           ds=None,
                           prefix='',
                           sufix=''):

    '''
    Escreve os números equivalentes aos comprimentos das barras no canto
    das barras
    '''

   # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2


    # configurações texto
    kargs = dict(fontsize = f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 va='center')     #va ->vertical aligment


    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width() + ds

        ax.annotate(f'{prefix}{faux.num_dec(p.get_width(),d=d)}{sufix}',
                    (x, y),
                    rotation=rotation,
                    **kargs)
        #Obs: nas anotações não colocar 'x', mas sim "p.get_width()"
        #isto ppor que o valor de x está acrescido de 'ds' e seria
        #escrito um valor errado

    return(ds)



def porc_barras_horizontais(ax,
                                 sum_tot=None,
                                 f_texto_bar=0.025,
                                 f_tam_letra=0.02,
                                 cor_texto='#000000',
                                 d=1,
                                 rotation=0,
                                 ds=None):

    '''
    Escreve as porcentagens em cima das barras

    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'h_texto_bar': fracao para calcular a posicao do texto a partir da barra.
        A posicao é calculada com a média da maior e da menor barra vezes esta
        fração
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd': número de casas decimais da porcentagem
    'dh':(USADO PARA UNIR GRAFICOS CORRELACIONADOS). É a altura de estabelecida para as
        anotações em cima da barra. Para unir dois ou mais gráficos este valor é estabelecido
        por um gráfico enterior

    Outputs:
    'dh': distância das anotações para as barras. Este retorno é usado para unir 2
        ou mais gráficos
    '''



    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 va='center')   #va ->vertical aligment

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width()

        porc= (x/sum_tot)*100

        ax.annotate(porcent_dec(porc, d=d),
                    (x+ds, y),
                    rotation=rotation,
                    **kargs)

    return(ds)



def porc_num_bar_horizontais(ax,
                       sum_tot=None,
                       f_texto_bar=0.025,
                       f_tam_letra=0.02,
                       d_porc=1,
                       d_num=1,
                       org_texto=1,
                       cor_texto='#000000',
                       rotation=0,
                       ds=None,):
    '''
    Escreve os números e as porcentagens ao lado das barras

    Args:
    'sum_tot': número equivalente a soma dos valores de todas as barras.
        Este valor deve ser calculado previamenete e passada para a função
    'f_texto_bar': fracao para calcular a posição do texto a partir da barra.
        A posicao é calculada com a média da maior e da menor barra multiplicada
        por esta fração
    'f_tam_letra': fração usada para calcular o tamnho da fonte das anotações.
        O tamanho da fonte é esta fração vezes o tamanho da maior barra
    'd_porc': número de casas decimais da porcentagem
    'd_num': número de casas decimais do numero das barras
    'org_texto': numero que define a organização das anotações:
        0-> escreve numero em cima e porcentagem a baixo
        1-> escreve porcentagem em cima e número a baixo
        2-> escreve numero e porcentagem na mesma linha como: num(porc)
        3-> escreve numero e porcentagem na mesma linha como: porc(num)
    'rotation': rotação das anotações
    'ds': distância entre as barras e o texto. É usado para unir 2 ou mais gráficos

    Outputs:
    'ds': distância entre as barras e o texto. É usado para unir 2 ou mais gráficos
    '''

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 color=cor_texto,
                 va='center')   #va-> vertical aligment

    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas do texto
        y = p.get_center()[1]
        x = p.get_width()

        porc= (x/sum_tot)*100


        # monta o texto
        if org_texto==0:
            # formato 0: num
            #            porc
            texto = faux.num_dec(p.get_width(),d=d_num)+'\n'+\
                    faux.porcent_dec(porc, d=d_porc)

        elif org_texto==1:
            # formato 1: porc
            #            num
            texto = faux.porcent_dec(porc, d=d_porc)+'\n'+\
                    faux.num_dec(p.get_width(),d=d_num)

        elif org_texto==2:
            #formato 2: num(porc)
            texto = faux.num_dec(p.get_width(),d=d_num)+' ('+\
                    faux.porcent_dec(porc, d=d_porc)+')'

        elif org_texto==3:
            #formato 3: porc(num)
            texto = faux.porcent_dec(porc, d=d_porc)+' ('+\
                    faux.num_dec(p.get_width(),d=d_num)+')'


        # escreve na figura
        ax.annotate(texto,
                    (x+ds, y),
                    rotation=rotation,
                    **kargs)


    # retorna 'dh' para graficos correlaciondados
    return(ds)




def num_graf_linhas(ax,
                    f_tam_letra=0.02,
                    f_texto_linha=0.025,
                    cor_texto='#000000',
                    d=1,
                    rotation=0,
                    ds=None,
                    prefix='',
                    sufix=''):

    '''Escreve os valores numéricos de um gráficos de linha como anotação
       em cima das linhas
    '''

    # distancia da texto para a linha
    if ds==None:
        # coordenadas y dos pontos da linha
        coordY = ax.lines[0].get_data()[1]
        # calcula o ds
        ds= f_texto_linha*(coordY.max()+coordY.min())/2


    # configurações texto
    kargs = dict(fontsize= f_tam_letra * faux._k(ax),        #f_tam_letra * _dl(ax),
                 color=cor_texto,
                 ha='center',
                 rotation=rotation)


    # escrever as anotações
    for p in ax.lines:

        # coordenadas dos pontos
        [x_pts,y_pts]= p.get_data()

        # escreve os numeros
        for x, y in zip(x_pts,y_pts):
            ax.annotate(f'{prefix}{faux.num_dec(y, d)}{sufix}',
                        xy=(x, y+ds),
                        **kargs
                       )

    return(ds)
