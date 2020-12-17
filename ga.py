import random
import numpy as np

class GeneticAlgorithm:
  def __init__(self, stop_iter=1000):
    self.stop_iter = stop_iter
    print("GeneticAlgorithm(stop_iter={})".format(stop_iter))
  
  def optimize(self, workers, tasks):
    def fitness(solution):
      return sum([skill * time for ((worker, skill), (task, time)) in solution])

    def find_best_n(solutions, n):
      eval_solutions = sorted(solutions, key=lambda solution: fitness(solution), reverse=True)
      return eval_solutions[0:n]

    def perform_mutation(solutions, best_solutions):
      for solution in solutions:
        if solution not in best_solutions:
          cur_iter = 0
          while cur_iter < 2:# or random.random() < 0.5:
            cur_iter = cur_iter + 1
            # find worst element in solution
            # 2do: make dependent on fitness function
            # 2do: don't swap element with itself
            def eval_solution_el(solution_element):
              ((worker, skill), (task, time)) = solution_element
              return skill * time

            index1 = solution.index(min(solution, key=eval_solution_el))
            index2 = solution.index(random.choice(solution))
            solution[index1], solution[index2] = solution[index2], solution[index1]
        else:
          pass # print("Hill Climbing not implemented yet")
    
    solutions = []
    for i in range(500):
      # 2do: delete reserved_workers
      reserved_workers = []
      solution = []
      for task in tasks:
        worker = random.choice(workers)
        while worker in reserved_workers:
          worker = random.choice(workers)
        solution.append((worker, task))
        reserved_workers.append(worker)
      solutions.append(solution)

    best_solutions = find_best_n(solutions, 5)
    cur_iter = 0
    while cur_iter < self.stop_iter:
      if cur_iter % 100 == 0:
        print("Iter {} of {}".format(cur_iter, self.stop_iter))
      perform_mutation(solutions, best_solutions)
      solutions = find_best_n(solutions, 500)
      best_solutions = find_best_n(solutions, 5)
      cur_iter = cur_iter + 1
    return best_solutions[0]