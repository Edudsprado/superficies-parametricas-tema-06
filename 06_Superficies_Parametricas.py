# SEMINÁRIO 3D — TEMA 6: SUPERFÍCIES PARAMÉTRICAS
# Objetivo: gerar esfera, cilindro ou cone a partir de parâmetros.
import numpy as np
import matplotlib.pyplot as plt

# Selecione: 'esfera', 'cilindro' ou 'cone'.
objeto = 'esfera'
segmentos = 36  # altere para 12, 24, 60...

u = np.linspace(0, 2*np.pi, segmentos)
v = np.linspace(0, np.pi, segmentos//2)
U, V = np.meshgrid(u, v)

if objeto == 'esfera':
    X = np.cos(U) * np.sin(V)
    Y = np.sin(U) * np.sin(V)
    Z = np.cos(V)
elif objeto == 'cilindro':
    altura = np.linspace(-1, 1, segmentos//2)
    U, H = np.meshgrid(u, altura)
    X, Y, Z = np.cos(U), np.sin(U), H
elif objeto == 'cone':
    altura = np.linspace(0, 1, segmentos//2)
    U, H = np.meshgrid(u, altura)
    X, Y, Z = (1-H)*np.cos(U), (1-H)*np.sin(U), H
else:
    raise ValueError('Escolha esfera, cilindro ou cone')

fig = plt.figure(figsize=(8,6)); ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='black', linewidth=.2, alpha=.9)
ax.set_title(f'Superfície: {objeto} | segmentos: {segmentos}')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_box_aspect((1,1,1)); plt.tight_layout(); plt.show()

# DESAFIOS INDIVIDUAIS:
# 1. Compare 8, 16, 36 e 72 segmentos.
# 2. Gere pelo menos duas superfícies diferentes.
# 3. Explique a relação entre quantidade de segmentos e aparência da malha.
