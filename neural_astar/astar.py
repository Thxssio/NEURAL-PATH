import numpy as np
from neural_astar.pq_astar import PriorityQueueAstar

class VanillaAstar:
    def __init__(self):
        self.astar_solver = PriorityQueueAstar()

    def __call__(self, map_designs, start_maps, goal_maps):
        return self.astar_solver.solve(map_designs, start_maps, goal_maps)

class NeuralAstar:
    def __init__(self, encoder_input, encoder_arch, encoder_depth, learn_obstacles, Tmax):
        self.encoder_input = encoder_input
        self.encoder_arch = encoder_arch
        self.encoder_depth = encoder_depth
        self.learn_obstacles = learn_obstacles
        self.Tmax = Tmax

    def __call__(self, map_designs, start_maps, goal_maps, store_intermediate_results=False):
        return np.random.rand(*map_designs.shape)  # Apenas um mock
