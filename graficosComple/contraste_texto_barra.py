

import seaborn as sns



#----------------------------------------------------
#   Luminosidade relativa e contraste entre cores
#----------------------------------------------------

def rel_luminescence(R_norm,G_norm,B_norm):

    '''
    Luminosidade relativa para uma cor.

    Este valor é umamedida da quão clara é uma cor e é
    usado no cálculo de contraste

    ref usada;
    https://contrastchecker.online/color-relative-luminance-calculator

    outras refs.:
    https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
    https://en.wikipedia.org/wiki/Relative_luminance
    https://alienryderflex.com/hsp.html
    https://www.w3schools.com/css/css_colors_rgb.asp
    https://medium.muz.li/the-science-of-color-contrast-an-expert-designers-guide-33e84c41d156
    https://stackoverflow.com/questions/22603510/is-this-possible-to-detect-a-colour-is-a-light-or-dark-colour
    '''

    RsRGB = R_norm   # R8bit normalizado (R8bit/255)
    GsRGB = G_norm   # G8bit normalizado (R8bit/255)
    BsRGB = B_norm   # B8bit normalizado (R8bit/255)


    # para red
    if RsRGB <= 0.03928:
        R = RsRGB/12.92
    else:
        R = ((RsRGB+0.055)/1.055)**2.4

    # para green
    if GsRGB <= 0.03928:
        G = GsRGB/12.92
    else:
        G = ((GsRGB+0.055)/1.055)**2.4

    # para blue
    if BsRGB <= 0.03928:
        B = BsRGB/12.92
    else:
        B = ((BsRGB+0.055)/1.055)**2.4

    # luminosidade relativa
    return(0.2126*R + 0.7152*G + 0.0722*B)



def contraste_cores(cor1=(0,0,0), cor2=(0,0,0)):

    '''
    Calcula o contraste entre duas cores:

    Contraste: (L1 + 0.05) / (L2 + 0.05)

    onde:
    L1 is the relative luminance of the lighter of the colors, and
    L2 is the relative luminance of the darker of the colors.

    L1 e L2 com menor valor-> mais dark

    Obs: o cntraste é um valor que pode ir de 1 até 21
    '''

    L1 = rel_luminescence(cor1[0],cor1[1],cor1[2])
    L2 = rel_luminescence(cor2[0],cor2[1],cor2[2])

    if L2<L1:
        contraste=(L1 + 0.05) / (L2 + 0.05)
    else:
        contraste=(L2 + 0.05) / (L1 + 0.05)

    return(contraste)







#----------------------------------------------------
#   Funções para escolher as cores do texto
#----------------------------------------------------


def cor_maior_contraste_intermed(cor=(0,0,0)):

    '''
    OBS:Esta função não foi usada no método do texto, seu resultado não
    ficou bom estéticamente.
    A função usada foi "cor_maior_contraste_branco_preto" esrita abaixo

    Descrição:
    cor de maior contraste para a barra com a barra pasnado por uma
    cor intermediária
    '''

    n=20
    contraste_lis=n*[0]
    cor_lis=n*[0]

    i=0
    for cor_cinza in ((1,1,1),(0.8, 0.8, 0.8),(0,0,0)):

        # calcula  o contraste e aloca no vetor
        contraste_lis[i]=contraste_cores((cor_cinza[0],cor_cinza[1],cor_cinza[2]),
                                  (cor[0],cor[1],cor[2]))

        # aloca cor no vetor
        cor_lis[i]=(cor_cinza[0],cor_cinza[1],cor_cinza[2])
        i=i+1


    # ordena as listas em ordem crescente dos contrastes
    zipped_lists = zip(contraste_lis, cor_lis)
    lis_oredenada = sorted(zipped_lists)

    tuples = zip(*lis_oredenada)
    contraste_lis, cor_lis = [ list(tuple) for tuple in  tuples]


    # maior e seg. maior contrastes
    contr_1=contraste_lis[-1]
    contr_2=contraste_lis[-2]

    if contr_1-contr_2>=2:
        #diferença dos contrastes é grande:
        # seleciona cor com maior contraste
        cor=cor_lis[-1]
    else:
        # diferença entre os contrastes é pequena:
        # seleciona a cor do terceiro contraste
        cor=cor_lis[-3]

    return(cor)





def cor_maior_contraste_branco_preto(cor_inp=(0,0,0)):
    '''
    Cor de maior contraste com a barra considerando somente 2 cores
    o branco e o preto
    '''

    contr_aux=0
    for cor_cinza in sns.color_palette("blend:#FFFFFF,#000000",5):

        # calcula  o contraste e aloca no vetor
        contraste = contraste_cores((cor_cinza[0],cor_cinza[1],cor_cinza[2]),
                                  (cor_inp[0],cor_inp[1],cor_inp[2]))
        #maior contraste
        if(contraste>contr_aux):
            contr_aux=contraste
            cor_output=(cor_cinza[0],cor_cinza[1],cor_cinza[2])

    return(cor_output)
