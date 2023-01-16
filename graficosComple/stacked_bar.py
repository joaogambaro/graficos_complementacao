
import graficosComple.funcoes_auxiliares as faux
from graficosComple.contraste_texto_barra import cor_maior_contraste_branco_preto
import math


# -----------------------------------------------
#   Monta o gráfico de stack bar
# ----------------------------------------------

def plotStacked(ax, df_cross, paleta='tab10',
                isNorm=True, isVert=True):
    '''
    Plota um gráfico de barras stacked a aprtir de uma
    tabela um cruzada
    '''

    # tipo de barras (verticais ou horizontais)
    kind='bar'
    if not isVert:
        kind='barh'


    if isNorm:
        # para barras normalizadas

        df_aux = df_cross.copy()

        # calcula o df com linhas normalizadas
        for x in ([*df_aux.index]):
            df_aux.loc[x]=df_aux.loc[x]/df_aux.loc[x].sum()

        # monta a figura
        df_aux.plot(kind=kind,
                    stacked=True,
                    colormap=paleta,
                    ax=ax
                )

    else:
        # para as barras não normalizadas

        # monta a figura
        df_cross.plot(kind=kind,
                      stacked=True,
                      colormap=paleta,
                      ax=ax
                )





# --------------------------------------------------
#   Escreve valores nas barras
# --------------------------------------------------

def escreveValores(ax, df_cross,color='k',
                   f_tam_letra=0.04,
                   d=2,
                   tipoTexto=0,tipoValor=None ):


    # configurações texto
    kargs = dict(fontsize=f_tam_letra * faux._k(ax),
                 rotation=0,
                 ha='center',
                 va='center')

    # obtem o valor total para cada barra
    sumColumns = list(df_cross.sum(axis=1))
    numLinhas= df_cross.shape[0]
    numColunas= df_cross.shape[1]


    # escreve os textos nas barras
    for i, p in enumerate(ax.patches):

        # coordenadas dos textos
        x = p.get_center()[0]
        y = p.get_center()[1]

        # obtem o numero a partir da linha e coluna da tabela
        iCol = int(i/numLinhas)
        iLinha = i%numLinhas
        numero = df_cross.iloc[iLinha][iCol]


        # obtem a porcentagem a partir da soma das colunas
        porc=0
        if sumColumns[iLinha] !=0:
            # quando pelo menos 1 das barras não é
            porc = (numero/ sumColumns[iLinha])*100

        if porc==0:
            porc=None
            numero=None
            #Obs: colocando os 2 como none nao será escrito nada
            # nesta barra. Isto deve ser feito quando:
            # - uma barra é 1 e a outra é 0. Os números da barra
            #   0 dever ser none para que nao seja escrito nada
            # - as 2 barras são zero, o que faz porc=Nan. A barra
            #   o texto na barra nao será escrito. A barra tbm
            #   não será desenhada



        # identifica quais valores devem ser escritos
        if(tipoValor=='porc'):
            numero=None
        if(tipoValor=='num'):
            porc=None


        # estima a cor da fonte
        cor_aux = color
        if color == None:
            # cor da barra
            c = p.get_facecolor()
            cor_aux = cor_maior_contraste_branco_preto(c)


        # faz as anotações
        ax.annotate(faux.formato_num_porc(tipoTexto, numero, porc),
                    (x, y),
                    color=cor_aux,
                    **kargs)
