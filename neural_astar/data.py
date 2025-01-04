import numpy as np

def create_dataloader(dataset_path, mode, batch_size, shuffle):
    # Carrega o dataset a partir do arquivo .npz
    data = np.load(dataset_path)
    
    map_designs = data["map_designs"]
    start_maps = data["start_maps"]
    goal_maps = data["goal_maps"]

    # Retorna os mapas divididos em lotes (batch_size)
    num_samples = len(map_designs)
    indices = np.arange(num_samples)
    if shuffle:
        np.random.shuffle(indices)

    for i in range(0, num_samples, batch_size):
        batch_indices = indices[i:i + batch_size]
        yield map_designs[batch_indices], start_maps[batch_indices], goal_maps[batch_indices]
