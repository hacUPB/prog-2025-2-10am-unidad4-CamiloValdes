# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]
# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Indexación (comienza en 0)
print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa), con los negativos solo se puede dar una sola vuelta

# Slicing (rebanado)
print(componentes[1:3])  # ["fuselaje", "motores"] , muestra desde el primero hasta el otro-1
print(componentes[:2])   # ["alas", "fuselaje"]
print(componentes[2:])   # ["motores", "tren de aterrizaje"]