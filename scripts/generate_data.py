import numpy as np
import os

# Configurações do dataset
NUM_MAPS = 100         # Quantidade de mapas gerados
MAP_SIZE = (64, 64)    # Tamanho do mapa (aumentado de 32x32 para 64x64)
OBSTACLE_DENSITY = 0.4 # Percentual de obstáculos (40%)

# Diretório de saída
DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)

# Criando mapas aleatórios com mais obstáculos
map_designs = np.random.choice(
    [0, 1], size=(NUM_MAPS, *MAP_SIZE), p=[1 - OBSTACLE_DENSITY, OBSTACLE_DENSITY]
)

# Criando mapas de início e destino
start_maps = np.zeros((NUM_MAPS, *MAP_SIZE))
goal_maps = np.zeros((NUM_MAPS, *MAP_SIZE))

for i in range(NUM_MAPS):
    # Define a posição inicial no canto superior esquerdo
    start_x, start_y = np.random.randint(0, 10, size=2)
    goal_x, goal_y = np.random.randint(54, 64, size=2)
    start_maps[i, start_x, start_y] = 1
    goal_maps[i, goal_x, goal_y] = 1

# Salvando o dataset no formato `.npz`
dataset_path = os.path.join(DATA_DIR, "dataset.npz")
np.savez(dataset_path, map_designs=map_designs, start_maps=start_maps, goal_maps=goal_maps)

print(f"✅ Dataset salvo em {dataset_path}")
