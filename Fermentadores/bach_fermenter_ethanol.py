# Este código describe la concentraciones de Etanol, Azúcar y Biomasa 
# y puede ser empleado para simular un fermentador

# Las ecuaciones ordianrias que describen este proceso está descrito por:
# Wang, Er-Qiang & Li, Shi-Zhong & Tao, Ling & Geng, Xin & Li, Tian-Cheng, 2010. 
# "Modeling of rotating drum bioreactor for anaerobic solid-state fermentation,"
# Applied Energy, Elsevier, vol. 87(9), pages 2839-2845, September, doi: 10.1016/j.apenergy.2009.05.032.

import numpy as np                     # Importa la libreria de funciones matematicas
from scipy.integrate import odeint     # Importa el solucionador de ecuaciones diferenciales
import matplotlib.pyplot as plt        # Importa la libreria para graficar

def EcuacionesDif(y,t):
  Cx, Cp, Cs = y
  # constantes
  um=0.330          # Tasa específica máxima de crecimiento
  cxm=0.0297        # Máxima concentración de biomasa posible
  yxs=0.0702        # Coeficiente de rendimiento celular
  yps=338.4         # Coeficiente de rendimiento de etanol en el sustrato
  m=0.00078         # Constante de mantenimiento celular
  alpha=4.378       # Coeficiente de producción de etanol
  beta=0.0388       # Coeficiente de producción de etanol
  
    
  # Ecuaciones diferenciales
  dCx = Cx*um*(1-Cx/cxm)            # Balance de crecimiento y muerte de la biomasa
  dCp = alpha*dCx + beta * Cx       # Tasa de producción de etanol
  dCs = -(1/yxs)*(dCx)-(m*Cx)+((1/yps)*(dCp))   # Tasa de consumo del sustrato
  
  return [dCx, dCp, dCs]

# Valores iniciales de las variables:
Cx0=  0.002          # g/100g 
Cp0=  0.01           # g/g
Cs0=  0.425          # g/g   

t=np.linspace(0,50,50)
#print(t) 
y0=[Cx0, Cp0, Cs0] 
sol=odeint(EcuacionesDif, y0, t)

# Para graficar:
fig,ejes1=plt.subplots()
ejes1.plot(t,sol[:,0],'r-',label='[Cx] Contenido de biomasa')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Concentracion biomasa (g/100g)')
plt.title('Fermentador')
plt.legend(loc=1)
plt.grid()

fig,ejes3=plt.subplots()
ejes3.plot(t,sol[:,2],'g--',label='[Cs] Consumo de azúcar')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Consumo total azúcar (g/g)')
plt.title('Fermentador')
plt.legend(loc=1)
plt.grid()


fig2,ejes2=plt.subplots()
ejes2.plot(t,sol[:,1],'b:',label='[Cp] Contenido de etanol')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Contenido de etanol (g/g)')
plt.title('Fermentador')
plt.legend(loc=1)
plt.grid()
plt.show()

print('Después de %s días de fermentación las concentraciones son: \n\n Biomasa: %s g/100g \n Etanol: %s g/g \n Azúcar: %s g/g' %(round(t[-1]/24,2), round(sol[-1,0],5), round(sol[-1,1],5), round(sol[-1,2],5)))
