

'''
Funções neste módulo:

- anotacoes_box_texto()
- anotacoes_texto_box()
- anotacoes_texto_valor()
- anotacoes_valor_texto()

IMPORTANTE:
as coordenadas de imput "f_x" e "f_y" são frações dos eixos do
gráfico

'''




# importa parâmetro para definir tamanhos
import graficosComple.funcoes_auxiliares as faux



def anotacoes_box_texto(ax,texto1=None,
                        texto2=None,
                        f_x=None,
                        f_y=None,
                        numLetra=0.04,
                        c_FaceBox="#d8e6db",
                        c_EdgeBox="k",
                        c_LetraBox='#191970',
                        c_LetraTexto='gray',
                        boxstyle='round4',
                        f_textos=18):

    '''
    Faz anotações em gráficos dividindo as anotações em duas partes um quadro
    com um texto e um texto livre abaixo do quadro.

    Obs:
    -> As coordenadas de entrada são frações dos eixos. Ex: f_x=0.5 coordenda
       x do texto fica na metada do eixo x
    -> A função foi escrita de forma que aumentando o tamanho da letra, todos
       os compoenentes da anotação também aumentam mantendo todas as proporções

    ax: eixo do gráficos
    texto1: texto dentro da caixa
    texto2: texto fora da caixa
    f_x: fracao do eixo x
    f_y: coordenada y do texto
    numLetra: tamanho da letra
    c_FaceBox: cor interna da caixa
    c_EdgeBox: cor da borda da caixa
    c_LetraBox: cor da letra do texto da caixa
    c_LetraTexto: cor da letra do texto fora da caixa
    boxstyle: estilo da caixa. Dois valores ficam bons('square', 'round4')
    f_textos -> fração relacionada com as distâncias dos textos
                quanto maior este valor maior as distâncias
                entre os textos
    '''

    # configurações da caixa
    bbox=dict(boxstyle=boxstyle,  #"square" (outra opção)
              pad=1,              #define se quadro pe proximo ou distente do texto
              edgecolor = c_EdgeBox,
              facecolor = c_FaceBox,
              linewidth=0.0005* faux._k(ax))

    # escreve o primeiro texto (texto na caixa)
    ax.annotate(texto1,
                xy=(f_x, f_y),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = c_LetraBox,
                size=numLetra* faux._k(ax),
                bbox=bbox,
                ha = 'center',    #alinhamento horizontal
                va = 'bottom',    #alinhamento vertical
                )

    # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0]

    # coordenadas do segundo texto
    f_x = f_x
    f_y = f_y - (f_textos*(dy/ax.bbox.height))/dy

    # opções para o cálculi de f_y(não funcionam muito bem)
    #f_y = f_y - 0.04*dy              #invariável à escala
    #f_y = f_y - 100 /ax.bbox.height  #invariável a altura da fig

    # escreve o segundo texto
    ax.annotate(texto2,
                 xy = (f_x, f_y),
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = c_LetraTexto,
                 size = numLetra* faux._k(ax),
                 ha = 'center', #alinhamento horizontal
                 va = 'top',    #alinhamento vertical
               )



def anotacoes_texto_box(ax,
                        texto1=None,
                        texto2=None,
                        f_x=None,
                        f_y=None,
                        numLetra=0.04,
                        c_FaceBox="#d8e6db",
                        c_EdgeBox="k",
                        c_LetraBox='#191970',
                        c_LetraTexto='gray',
                        boxstyle='round4',
                        f_textos=18):
    '''
    Faz anotações em gráficos dividindo as anotações em duas partes um texto
    livre (sem caixa) e um texto abaixo dentro de uma caixa.

    Obs:
    -> As coordenadas de entrada são frações dos eixos. Ex: f_x=0.5 coordenda
       x do texto fica na metada do eixo x
    -> A função foi escrita de forma que aumentando o tamanho da letra, todos
       os compoenentes da anotação também aumentam mantendo todas as proporções

    ax: eixo do gráficos
    texto1: texto dentro da caixa
    texto2: texto fora da caixa
    f_x: coordenada x do texto
    f_y: coordenada y do texto
    numLetra: tamanho da letra
    c_FaceBox: cor interna da caixa
    c_EdgeBox: cor da borda da caixa
    c_LetraBox: cor da letra do texto da caixa
    c_LetraTexto: cor da letra do texto fora da caixa
    boxstyle: estilo da caixa. Dois valores ficam bons('square', 'round4')
    f_textos: fração relacionada com as distâncias dos textos
                quanto maior este valor maior as distâncias
                entre os textos
    '''

    # escreve o primeiro texto
    ax.annotate(texto1,
                 xy=(f_x, f_y),
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = c_LetraTexto,
                 size=numLetra * faux._k(ax),
                 ha='center',
                 va = 'bottom',  #alinhamento vertical
                 )

    # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0]

    # coordenadas do segundo texto
    f_x = f_x
    f_y = f_y - (f_textos*(dy/ax.bbox.height))/dy

    # configurações da caixa
    bbox=dict(boxstyle=boxstyle,
              pad=1,              #define se quadro pe proximo ou distente do texto
              edgecolor = c_EdgeBox,
              facecolor = c_FaceBox,
              linewidth=0.0005*faux._k(ax))

    # escreve o segundo texto
    ax.annotate(texto2,
                xy = (f_x, f_y),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = c_LetraBox,
                size = numLetra*faux._k(ax),
                ha = 'center', #alinhamento horizontal
                va = 'top',    #alinhamento vertical
                bbox=bbox)



def anotacoes_texto_valor(ax,texto1=None,
                          texto2=None,
                          f_x=None,
                          f_y=None,
                          numLetra=0.04,
                          n_maior= 2,
                          cor_valor='#191970',
                          cor_texto='gray',
                          f_textos=5):
    """
    Escreve um texto com um valor abaixo

    Obs:
    -> As coordenadas de entrada são frações dos eixos. Ex: f_x=0.5 coordenda
       x do texto fica na metada do eixo x
    -> A função foi escrita de forma que aumentando o tamanho da letra, todos
       os compoenentes da anotação também aumentam mantendo todas as proporções

    texto1: texto de cima (neste caso é o texto maior,
            geralmente usado para colocar um valor)
    texto2: texto de baixo (neste caso é o texto menor,
            geralmente usado para colocar alguma inf. do valor)
    n_maior: numero de vezes a letra do texto maior (valor) é
            é maior que a letra do texto menor
    f_textos: ajuste para a distância entre as letras
    numLetra: ajuste para o tamanho da letra menor
    """

    # primeiro texto: texto maior
    ax.annotate(texto1,
                xy=(f_x, f_y),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = cor_valor,
                size=n_maior*numLetra*faux._k(ax),
                ha = 'center',    #alinhamento horizontal
                va = 'bottom',    #alinhamento vertical
                )

    # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0]

    # coordenadas do segundo texto
    f_x = f_x
    f_y = f_y - (f_textos*(dy/ax.bbox.height))/dy

    # segundo texto: texto menor
    ax.annotate(texto2,
                 xy = (f_x, f_y),
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = cor_texto,
                 size = numLetra*faux._k(ax),
                 ha = 'center', #alinhamento horizontal
                 va = 'top',    #alinhamento vertical
               )


def anotacoes_valor_texto(ax,texto1=None,
                          texto2=None,
                          f_x=None,
                          f_y=None,
                          numLetra=0.04,
                          n_maior= 2,
                          cor_valor='#191970',
                          cor_texto='gray',
                          f_textos=5):
    """
    Escreve um valor com uma anotação abaixo

    Obs:
    -> As coordenadas de entrada são frações dos eixos. Ex: f_x=0.5 coordenda
       x do texto fica na metada do eixo x
    -> A função foi escrita de forma que aumentando o tamanho da letra, todos
       os compoenentes da anotação também aumentam mantendo todas as proporções

    texto1: texto de cima (neste caso é o texto menor,
            eralmente usado para colocar alguma inf. do valor)
    texto2: texto de baixo (neste caso é o texto maior,
            geralmente usado para colocar um valor)
    n_maior: numero de vezes a letra do texto maior (valor) é
            é maior que a letra do texto menor
    f_textos: ajuste para a distância entre as letras
    numLetra: ajuste para o tamanho da letra menor
    """

    # primeiro texto: texto maior
    ax.annotate(texto1,
                xy=(f_x, f_y),
                xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                color = cor_texto,
                size=numLetra*faux._k(ax),
                ha = 'center',    #alinhamento horizontal
                va = 'bottom',    #alinhamento vertical
                )

    # limites dos eixos
    lim_y= ax.get_ylim()
    dy=lim_y[1]-lim_y[0]

    # coordenadas do segundo texto
    f_x = f_x
    f_y = f_y - (f_textos*(dy/ax.bbox.height))/dy

    # segundo texto: texto menor
    ax.annotate(texto2,
                 xy = (f_x, f_y),
                 xycoords='axes fraction',  #coordenadas definidas for frações dos eixos
                 color = cor_valor,
                 size = n_maior * numLetra*faux._k(ax),
                 ha = 'center', #alinhamento horizontal
                 va = 'top',    #alinhamento vertical
               )
