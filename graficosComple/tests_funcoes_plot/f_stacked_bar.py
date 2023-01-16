
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

# importa os módulos do pacote
import graficosComple.stacked_bar as st



# -------------------------------------------------
#    Funções    
# -------------------------------------------------

def fuc_teste_sctack_bar(isNorm, isVert, tipoTexto,tipoValor):
    '''
    Plota um gráfico stacked bar
    '''

    #gera os dados
    df_cross = pd.DataFrame(
        {'carro':    [0,0,3,5,7,6],
         'onibus':   [0,4,0,3,3,0],
         'bicicleta':[0,4,6,2,2,0]},
        index=['Joao', 'Karen', 'Lucas','Maria','Eduarda','Julia' ]
        )

    # define os eixos
    fig = plt.figure(constrained_layout=True, figsize=(5,4))
    gs = GridSpec(1,1, figure=fig)
    ax = fig.add_subplot(gs[0, 0])

    # plota o gráfico
    st.plotStacked(ax, df_cross, isNorm=isNorm, isVert=isVert)

    # escreve na figura
    st.escreveValores(ax,df_cross,color=None,
                      tipoTexto=tipoTexto,
                      tipoValor=tipoValor,
                      f_tam_letra=0.02)

    return(plt)
