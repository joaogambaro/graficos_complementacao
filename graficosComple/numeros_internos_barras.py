
import seaborn as sns
import graficosComple.funcoes_auxiliares as faux
from graficosComple.contraste_texto_barra import cor_maior_contraste_branco_preto



#------------------------------------------------------------------
#   Escreve os textos dentro das barras
#------------------------------------------------------------------


def num_int_barras_verticais(ax,
                         f_texto_bar=0.025,
                         f_tam_letra=0.02,
                         cor_texto=None,
                         isTopo=True,
                         d=1,
                         rotation=0,
                         ds=None,
                         prefix='',
                         sufix=''
                           ):

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2

    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 rotation=rotation,
                 ha='center',  #alinhamento horizontal
                 )


    # escreve os textos nas barras
    for p in ax.patches:

        # coordenadas x
        x = p.get_center()[0]

        # define se texto é colocado no topo ou na base
        if isTopo == True:
            y = p.get_height()-ds  #altura do retangulo
            va='top'            #alinhamento vertical
        else:
            y = p.get_y()+ds
            va='bottom'         #alinhamento vertical



        # estima a cor da fonte
        cor_aux=cor_texto
        if cor_texto == None:

            # cor da barra
            c = p.get_facecolor()
            cor_aux = cor_maior_contraste_branco_preto(c)

            #(rotina ja usada)cor do texto a partir da luminescencia
            #l=rel_luminescence(c[0],c[1],c[2])
            #if l>0.4:
            #    cor_aux="#000000"
            #    cor_aux=ni.cor_maior_contraste_branco_preto(c)
            #else:
            #    cor_aux="#FFFFFF"


        # faz as anotações
        ax.annotate(f'{prefix}{round(p.get_height(),d)}{sufix}',
                    (x, y),
                    color=cor_aux,
                    va=va,
                    **kargs)

    return(ds)




def porc_int_barras_verticais(ax,
                          sum_tot=None,
                          f_texto_bar=0.025,
                          f_tam_letra=0.02,
                          cor_texto=None,
                          isTopo=True,
                          d=1,
                          rotation=0,
                          ds=None):

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_height()\
                     + ax.patches[-1].get_height())/2

    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 rotation=rotation,
                 ha='center')

    # escreve os textos nas barras
    for p in ax.patches:


        # coordenada x
        x = p.get_center()[0]

        # estima a cor do texto
        cor_aux=cor_texto
        if cor_texto == None:

            # cor da barra
            c = p.get_facecolor()

            # cor da texto
            cor_aux = cor_maior_contraste_branco_preto(c)


        # calcula a porcentagem
        porc= (p.get_height()/sum_tot)*100
        #Obs: não alterar o calculo da porcentagem, esta cálculo estave sendo
        #feito de forma errada, eu estava colocando y=p.get_height() no inicio do
        #código e estava usando y no calculo acima. Isto pode levar a erros pois
        #o valor de y pode ser alterada em rotinas anteriores



        # calcula a coordenada y do texto
        y = p.get_y()+ds
        va='bottom'         #alinhamento vertical

        if isTopo == True:
            y = p.get_height()-ds  #altura do retangulo
            va='top'            #alinhamento vertical



        # faz as anotações
        ax.annotate(f'{round(porc,d)}%',
                    (x, y),
                    color=cor_aux,
                    va=va,
                    **kargs)

    return(ds)






def num_int_barras_horizontais(ax,
                           f_texto_bar=0.025,
                           f_tam_letra=0.02,
                           cor_texto=None,
                           isRight=True,
                           d=1,
                           rotation=0,
                           ds=None,
                           prefix='',
                           sufix=''):

    '''
    Escreve os números equivalentes aos comprimentos das barras dentro
    das barras
    '''

   # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2


    # configurações texto
    kargs = dict(fontsize = f_tam_letra * faux._k(ax),
                 rotation=rotation,
                 va='center')     #va ->vertical aligment


    # escreve os textos nas barras
    for p in ax.patches:


        # coordenadas y
        y = p.get_center()[1]


        # define se texto é colocado no topo ou na base
        if isRight == True:
            x = p.get_width() - ds
            ha='right'            #alinhamento horizontal
        else:
            x = p.get_x()+ds
            ha=  'left'


        # estima a cor da fonte
        cor_aux=cor_texto
        if cor_texto == None:

            # cor da barra
            c = p.get_facecolor()
            cor_aux = cor_maior_contraste_branco_preto(c)


        # faz as anotações
        ax.annotate(f'{prefix}{round(p.get_width(),d)}{sufix}',
                    (x, y),
                    color=cor_aux,
                    ha= ha,
                    **kargs)

    return(ds)




def porc_int_barras_horizontais(ax,
                                sum_tot=None,
                                f_texto_bar=0.025,
                                f_tam_letra=0.02,
                                cor_texto=None,
                                isRight=True,
                                d=1,
                                rotation=0,
                                ds=None):
    '''
    Escreve as porcentagens dentro das barras'''

    # distancia do texto para a barra
    if(ds == None):
        ds = f_texto_bar*(ax.patches[0].get_width()\
                     + ax.patches[-1].get_width())/2


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * _k(ax),
                 rotation=rotation,
                 va='center')   #va ->vertical aligment

    # escreve os textos nas barras
    for p in ax.patches:


        # coordenadas y
        y = p.get_center()[1]

        # estima a cor da fonte
        cor_aux=cor_texto
        if cor_texto == None:

            # cor da barra
            c = p.get_facecolor()
            cor_aux = cor_maior_contraste_branco_preto(c)


        # calcula a porcentagem
        porc= (p.get_width()/sum_tot)*100
        #Obs: não alterar o calculo da porcentagem, este cálculo estava sendo
        #feito de forma errada. Eu estava colocando x=p.get_width() no inicio do
        #código e estava usando x no calculo acima. Isto pode levar a erros pois
        #o valor de x pode ser alterado em rotinas anteriores


        # calcula as coordenadas do x
        if isRight == True:
            x = p.get_width() - ds
            ha = 'right'            #alinhamento horizontal
        else:
            x = p.get_x() + ds
            ha = 'left'


        # faz as anotações
        ax.annotate(f'{round(porc, d)}%',
                    (x, y),
                    color=cor_aux,
                    ha= ha,
                    **kargs)

    return(ds)
