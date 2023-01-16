
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd
import seaborn as sns

# importa os módulos do pacote
import graficosComple.numeros_nos_graficos as ng
import graficosComple.limites_dos_graficos as li



# -------------------------------------------------
#    Funções: para barras verticais
# -------------------------------------------------

# escreve números
def fuc_num_barras_verticais():


    #gera os dados
    df1= pd.DataFrame({'x':list(range(10)),
                      'y':3*[10]+2*[9.5]+3*[9]+2*[8]  })
    df2= pd.DataFrame({'x':list(range(10)),
                      'y':3*[5]+2*[4]+3*[3]+2*[2]  })

    # define os eixos
    fig = plt.figure(constrained_layout=True, figsize=(10, 5))
    gs = GridSpec(1, 2, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    # paleta
    pal_1= sns.color_palette("blend:#e8c8ce,#2019f7",5)

    # grafico 1
    # plota barras
    sns.barplot(ax=ax1, data=df1, x='x', y='y', palette=pal_1)
    ax1.set_title("Primeiros valores")
    # muda os limites/ faz antações
    ylims1 = li.muda_limites_eixo_y(ax1, frac=0.1)
    ds1=ng.num_barras_verticais(ax1,
                     f_texto_bar=0.10,
                     f_tam_letra=0.02,
                     d=1,
                     prefix="R$",
                     sufix="",
                     rotation=0)
    #eixos
    ax1.spines[['right','top']].set_visible(False)
    ax1.set_yticks([])
    ax1.set_ylabel('')

    # grafico 2
    # plota barras
    sns.barplot(ax=ax2, data=df2, x='x', y='y', palette=pal_1)
    ax2.set_title("Ultimos valores")
    # muda os limites/ faz antações
    ylims1 = li.muda_limites_eixo_y(ax2, ylims=ylims1)
    ds1=ng.num_barras_verticais(ax2,
                     f_texto_bar=0.025,
                     f_tam_letra=0.03,
                     d=2,
                     ds=ds1,
                     prefix="R$",
                     sufix=" (real)",
                     rotation=80)
    #eixos
    ax2.spines[['right','top']].set_visible(False)
    ax2.set_yticks([])
    ax2.set_ylabel('')

    return(plt)


# escreve números e porcentagens
def fuc_porc_num_bar_verticais(org_texto):
    '''
    Obs: incluir no input todas as opções para "org_texto"
    '''

    #gera os dados
    df1= pd.DataFrame({'x':list(range(10)),
                      'y':3*[10]+2*[9.5]+3*[9]+2*[8]  })
    df2= pd.DataFrame({'x':list(range(10)),
                      'y':3*[5]+2*[4]+3*[3]+2*[2]  })

    # define eixos
    fig = plt.figure(constrained_layout=True, figsize=(10, 5))
    gs = GridSpec(1, 2, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    # paleta
    pal_1= sns.color_palette("blend:#e8c8ce,#2019f7",5)

    # --- grafico 1 ---
    # plota barras
    sns.barplot(ax=ax1, data=df1, x='x', y='y', palette=pal_1)
    ax1.set_title("Primeiros valores")
    # muda os limites/ faz antações
    ylims1 = li.muda_limites_eixo_y(ax1, frac=0.1)
    ds1= ng.porc_num_bar_verticais(ax1, sum_tot=df1['y'].sum(),
                               d_porc=2,  org_texto=org_texto)
    #eixos
    ax1.spines[['right','top']].set_visible(False)
    ax1.set_yticks([])
    ax1.set_ylabel('')

    # --- grafico 2
    # plota barras
    sns.barplot(ax=ax2, data=df2, x='x', y='y', palette=pal_1)
    ax2.set_title("Ultimos valores")
    # muda os limites/ faz antações
    ylims1 = li.muda_limites_eixo_y(ax2, ylims=ylims1)
    ng.porc_num_bar_verticais(ax2, sum_tot=df1['y'].sum(),
                              org_texto=org_texto, d_porc=2,  rotation=20, ds=ds1)
    #eixos
    ax2.spines[['right','top']].set_visible(False)
    ax2.set_yticks([])
    ax2.set_ylabel('')
    return(plt)



# -------------------------------------------------
#    Funções: para barras horizontais
# -------------------------------------------------

def fuc_num_barras_horizontais():

    #gera os dados
    df1= pd.DataFrame({'x':list(range(10)),
                      'y':3*[10]+2*[9.5]+3*[9]+2*[8]  })
    df2= pd.DataFrame({'x':list(range(10)),
                      'y':3*[5]+2*[4]+3*[3]+2*[2]  })

    # define os eixos
    fig = plt.figure(constrained_layout=True, figsize=(10, 5))
    gs = GridSpec(2, 1, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])

    # paleta
    pal_1= sns.color_palette("blend:#e8c8ce,#2019f7",5)

    # gráfico 1
    sns.barplot(ax=ax1, data=df1.head(5), x='y', y='x',
             orient='h',palette =pal_1)
    # limites e antações
    ds1 = ng.num_barras_horizontais(ax1,prefix='R$',sufix=' (real)',
                                d=2,f_tam_letra=0.015)
    xlims = li.muda_limites_eixo_x(ax1, frac=0.2, tipo_aumento=0)
    # eixos
    ax1.spines[['right','top']].set_visible(False)
    ax1.set_yticks([])
    ax1.set_ylabel('')


    # grafico_2
    sns.barplot(ax=ax2, data=df2.head(5), x='y', y='x',
             orient='h',palette =pal_1)
    # limites e antações
    ds1 = ng.num_barras_horizontais(ax2,prefix='R$',sufix='(real)',
                               d=2,f_tam_letra=0.015, rotation=10,ds=ds1)
    li.muda_limites_eixo_x(ax2, xlims=xlims)
    # eixos
    ax2.spines[['right','top']].set_visible(False)
    ax2.set_yticks([])
    ax2.set_ylabel('')

    return(plt)



def fuc_porc_num_bar_horizontais(org_texto):

    '''
    Obs: incluir no input todas as opções para "org_texto"
    '''

    #gera os dados
    df1= pd.DataFrame({'x':list(range(10)),
                      'y':3*[10]+2*[9.5]+3*[9]+2*[8]  })
    df2= pd.DataFrame({'x':list(range(10)),
                      'y':3*[5]+2*[4]+3*[3]+2*[2]  })

    # define os eixos
    fig = plt.figure(constrained_layout=True, figsize=(10, 5))
    gs = GridSpec(2, 1, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])

    # paleta
    pal_1= sns.color_palette("blend:#e8c8ce,#2019f7",5)


    # gráfico 1
    sns.barplot(ax=ax1, data=df1.head(5), x='y', y='x',
             orient='h',palette =pal_1)
    # limites e antações
    ds1= ng.porc_num_bar_horizontais(ax1, sum_tot=df1['y'].sum(),
                               d_porc=2,f_tam_letra=0.01,  org_texto=org_texto)
    xlims = li.muda_limites_eixo_x(ax1, frac=0.2, tipo_aumento=0)
    # eixos
    ax1.spines[['right','top']].set_visible(False)
    ax1.set_yticks([])
    ax1.set_ylabel('')


    # grafico_2
    sns.barplot(ax=ax2, data=df2.head(5), x='y', y='x',
             orient='h',palette =pal_1)
    # limites e antações
    ng.porc_num_bar_horizontais(ax2, sum_tot=df2['y'].sum(),
                               d_porc=2,
                            f_tam_letra=0.01,ds=ds1,  org_texto=org_texto)
    li.muda_limites_eixo_x(ax2, xlims=xlims)
    # eixos
    ax2.spines[['right','top']].set_visible(False)
    ax2.set_yticks([])
    ax2.set_ylabel('')

    return(plt)
