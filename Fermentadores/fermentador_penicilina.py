
import numpy as np                   # Importa la libreria de funciones matemáticas
from scipy.integrate import odeint   # Importa el solucionador de ecuaciones diferenciales
import matplotlib.pyplot as plt      # Importa la libreria para graficar

def EcuacionesDif(y,t):
  X, P, S, Cl, V, H, T, CO2 = y
  # constantes
  '''Ea = 
  Ed = 
  mo = 
  mx = 
  kg = 
  kd = 
  K = 
  Kl = 
  Kox = 
  Kop = 
  Kp = 
  Kx = 
  K1 = 
  K2 = 
  p = 
  Sf = 
  Tf = 
  F = 
  Ypo = 
  Yps = 
  Yxo = 
  Yxs = 
  a = 
  beta = 
  





  ui=0.50       #Tasa máxima de crecimiento específica en ausencia de inhibidores
  Ks=6.10E-3    #Constante de saturación
  Ki=139.7      #Parámetro de inhibición para azúcar
  Pm=94.2       #Parametro de inhibición para etanol
  n=4.12        #Poder tóxico etanol
  Yps=0.40      
  a=4.87
  
  # Ecuaciones algebraicas auxiliares
  u = (ux/(1 + K1/H + H/K2))*(S/(Kx*X + S))*(Cl/(Kox*X + Cl))*(kg*np.exp(-Ea/(R*T)) - (kd*np.exp(-Ed(R*T))))
  upp = up*(S/(Kp + S + (S**2)/Kl))*(Clx/(Kop*X+Clx))
  Floss = V*x*(np.exp(5*((T - T0)/(Tv - T0)) - 1))
  Qrxn = u*X*delta_Hrxn*V
  K1a = a*(fg)**0.5(Pw/V)**beta
  B = (((10**(-14))/H - H)*V - (Ca*Fa - Cb*Fb)*delta_t) / (V + (Fa + Fb)*delta_t)
  UA = 34.996*Fc + 1071.5

  # Ecuaciones diferenciales
  dV = F + Fa + Fb - Floss      # Volumen en el reactor
  dX = u*X - (X/V)*dV           # Crecimiento de la biomasa
  dP = upp*X - K*P - (P/V)dV    #Producción de penicilina
  dS = (u/Yxs)*X - (upp/Yps)*X - mx*X + (F*Sf)/V - (S/V)*dV    # Consumo de sustrato
  dCl = -(u/Yxo)*X - (upp/Ypo)*X - mo*X + K1a*(Clx-Cl) - (Cl/V)*dV  # Perfil de oxígeno disuelto
  dH = ipsilon(u*X - (F*X)/V) + ((-B + (B**2+4*10**(-14))**0.5)/2 - H)*1/delta_t    # pH
  dT = (F/V)*(Tf - T) + (1/(V*p*Cp))*(Qrxn - Fc*pc*Cpc(T-Tc)(1 - np.exp(-(UA/(Fc*pc*Cpc)))))    # Perfil de temperatura
  dCO2 = a1*dX + a2*X + a3      # Emisión de CO2

  return [dX, dP, dS, dCl, dV, dH, dT, dCO2]
'''
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
