'''
-> Plota o diagrama de Nyquist, LGR, Bode e a resposta ao degrau ao partir da função de transferência de malha aberta
'''


import control as ctrl
import numpy as np
import matplotlib.pyplot as plt


# Definição da função de transferência de malha aberta e malha fechada

#PSK

num = [1]
den = [1, 4, 5, 0]

G = ctrl.tf(num,den)
F = G/(1+G)


PMA = ctrl.pole(G)
ZMA = ctrl.zero(G)
PMF = ctrl.pole(F)
ZMF = ctrl.zero(F)

print("FTMA (G(S).H(S)): ", G)
print("FTMF (G/(1 + G.H)): ", F)
print("\n")

print("Polos de Malha Aberta:", np.around(PMA, 3))
print("Zeros de Malha Aberta:", np.around(ZMA, 3))
print("\n")

print("Polos de Malha Fechada:", np.around(PMF, 3))
print("Zeros de Malha Fechada:", np.around(ZMF, 3))
print("\n")
 
 
ctrl.nyquist(G)
plt.title('Diagrama de Nyquist')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')

plt.figure()
ctrl.root_locus(G)
plt.title('Lugar geométrico das raízes')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.grid(True)

plt.figure()
ctrl.bode(F, dB=True)

plt.figure()
t, y = ctrl.step_response(F)
plt.plot(t, y)
# plt.xlim(0, 20)
plt.title('Resposta ao degrau')
plt.xlabel('t[s]')
plt.ylabel('y(t)')
plt.grid(True)

# ctrl.sisotool(G)
