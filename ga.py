import random from random

class GeneticAlgorithm:
  def __init__(self):
    print("GeneticAlgorithm()")
  
  def optimize(self, X, stop_iter=1000):
    def find_best_n(xs, n):
      return xs[0:n]

    def perform_mutation(solutions, best_solutions):
      for solution in solutions:
        if solution not in best_solutions:
          cur_iter = 0
          while cur_iter < 2:# or random() < 0.5:
            print("performing mutation")
        else:
          print("Hill Climbing not implemented yet")
    
    solutions = X[0:500]
    best_solutions = find_best_n(solutions, 5)
    cur_iter = 0
    while cur_iter < stop_iter:
      perform_mutation(solutions, best_solutions)
      solutions = find_best_n(solutions, 500)
      best_solutions = find_best_n(solutions, 5)
    return best_solutions[0]