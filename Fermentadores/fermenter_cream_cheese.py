# Este modelo no quedó igual al del artículo, se asume que
# las ecuaciones no son correctas
# https://onlinelibrary.wiley.com/doi/10.1002/jctb.6517 

import numpy as np                     # Importa la libreria de funciones matematicas
from scipy.integrate import odeint     # Importa el solucionador de ecuaciones diferenciales
import matplotlib.pyplot as plt        # Importa la libreria para graficar

def EcuacionesDif(y,t):
  X, S, P = y
  # constantes
  umax = 3.1
  Ksx = 199.9
  Kix = 5777.1
  Pix = 2
  Pmx = 4.8
  qsmax = 30.5
  Kss = 1081.9
  Kis = 99.9
  Pis = 295.1
  Pms = 992.8
  a = 0.6
  qpmax = 1
  Ksp = 1.5
  Kip = 8.6
  Pip = 555.5
  Pmp = 3067.2

  # Ecuaciones algebraicas auxiliares
  ux =  umax*(S/(Ksx + S))*(1-((P-Pix)/(Pmx-Pix)))*(Kix/(Kix+S))
  us = qsmax*(S/(Kss + S))*(1-((P-Pis)/(Pms-Pis)))*(Kis/(Kis+S))
  up = qpmax*(S/(Ksp + S))*(1-((P-Pip)/(Pmp-Pip)))*(Kip/(Kip+S))
  # Ecuaciones diferenciales
  dX= ux*X     # balance  de crecimiento y muerte 
  dS= us*X    # balance de azúcar 
  dP= a*dX + up*X    # balance de etanol
  
  return [dX, dS, dP]

# Valores iniciales de las variables:
X0=  0.035                # g/L
S0=  40.350               #g/L 
P0=  0.012                 # g/L
                

t=np.linspace(0,10,100)
#print(t) 
y0=[X0, S0, P0] 
sol=odeint(EcuacionesDif, y0, t)

# Para graficar:
fig,axes=plt.subplots()
axes.plot(t,sol[:,0],'r-',label='[X] Crecrimiento y muerte')
axes.plot(t,sol[:,1],'b-+',label='[S] Azúcar ')
axes.plot(t,sol[:,2],'g--',label='[P] Etanol ')

plt.xlabel('tiempo (horas)')
plt.ylabel('Concentracion (g/L)')
plt.title('Fermentador - Etanol')
plt.legend(loc=1)
 
plt.grid()
plt.show()
