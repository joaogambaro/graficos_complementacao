
import seaborn as sns
import graficosComple.funcoes_auxiliares as faux




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


