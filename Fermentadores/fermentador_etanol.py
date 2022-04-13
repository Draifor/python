# Modelado de un fermentador tomado del artículo
# Kinetic Modeling and Optimization of a Batch Ethanol Fermentation.
# Samuel C Oliveira, Romulo C Oliveira, Mariana V Tacin and Edwil AL Gattás.
# Se solucionará empleando el método numérico de Runge Kutta 
# de 4to orden. Este metodo se importa en la función odeint de python.


import numpy as np                     # Importa la libreria de funciones matematicas
from scipy.integrate import odeint     # Importa el solucionador de ecuaciones diferenciales
import matplotlib.pyplot as plt        # Importa la libreria para graficar

def EcuacionesDif(y,t):
  X, P, S = y
  # constantes
  ui=0.50       #Tasa máxima de crecimiento específica en ausencia de inhibidores
  Ks=6.10E-3    #Constante de saturación
  Ki=139.7      #Parámetro de inhibición para azúcar
  Pm=94.2       #Parametro de inhibición para etanol
  n=4.12        #Poder tóxico etanol
  Yps=0.40      
  a=4.87
  
  # Ecuaciones algebraicas auxiliares
  gP=(1-(P/Pm))**n
  u=(ui*S/(Ks+S+((S**2)/Ki)))*gP    # Tasa de crecimiento del microorganismo
  pi=a*u                            # Tasa específica de formación de producto
  o=pi/Yps                         # Tasa específica de consumo de sustrato
  
  # Ecuaciones diferenciales
  dX=u*X     # balance  de crecimiento y muerte 
  dP=pi*X     # balance de etanol
  dS=-o*X    # balance de azúcar 
  return [dX, dP, dS]

# Valores iniciales de las variables:
X0=  25.0                # g/L
P0=  0.0                 # g/L
S0=  111.5               #g/L   

t=np.linspace(0,8,100)
#print(t) 
y0=[X0, P0, S0] 
sol=odeint(EcuacionesDif, y0, t)

# Para graficar:
fig,axes=plt.subplots()
axes.plot(t,sol[:,0],'r-',label='[X] Crecrimiento y muerte')
axes.plot(t,sol[:,1],'g--',label='[P] Etanol ')
axes.plot(t,sol[:,2],'b-+',label='[S] Azúcar ')


plt.xlabel('tiempo (horas)')
plt.ylabel('Concentracion (g/L)')
plt.title('Fermentador - Etanol')
plt.legend(loc=1)
 
plt.grid()
plt.show()
