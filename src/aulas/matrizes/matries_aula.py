import numpy as np
# from numpy.typing import NDArray

lista = [10, 20, 30, 40, 50]
vetor : np.ndarray = np.array(lista)

print(f'Tipo do obj: {type(vetor)}')
print(f'Num de dimensoes: {vetor.ndim}')
print(f'Formato do vetor: {vetor.shape}')
print(f'Tamanho: {vetor.size}')
print(f'Vetor do tipo: {vetor.dtype}')
print(f"Quem esta na posicao 2? {vetor[2]}")
vetor[2] = 100
print(f"Quem esta na posicao 2? {vetor[2]}")
terceira_dim = [1,2,3,4]
m = np.array(
    [
        [terceira_dim, terceira_dim, terceira_dim],
        [terceira_dim, terceira_dim, terceira_dim],
        [terceira_dim, terceira_dim, terceira_dim]
    ]
)
print(f'Num de dimensoes: {m.ndim}')
print(f'Formato do vetor: {m.shape}')
print(f'Tamanho: {m.size}')

nula = np.zeros((2,3))
print(nula)
um = np.ones((2,2))
print(um)
cheio = np.full((3, 2),7)
print(cheio)
identidade = np.eye((3))
print(identidade)

idades = np.array([18,22, 38], dtype=int)
print(idades.dtype)

d = np.dot(idades, cheio)
print(d)