# Computational Intelligence Lab 02

In this laboratory we are trying to find an optimal solution to the Travelling Sales Person problem using an Evolutionary Algorithm. In order to so so we used the following data structures:
- <strong>solution</strong>: a named tuple associated with the list of nodes in same order the sales person is visiting them (genotype) and the cost of that path (weight).
- <strong>population</strong>: a list of individuals, each one associated with genotype and weight.
- <strong>offsprings</strong>: the list of offsprings for each new generation

The problem start by inizializing the population with greedy solutions:
- A <strong>standard</strong> greedy if the problem satisfies the triangular inequality. In this greedy algorithm we start building the solution from a random node and we choose the following one by picking the closest among the ones left.
- A greedy that tries to <strong>avoid leaving isolated nodes</strong> if the problem does not satisfy the triangular inequality. As before we start building the solution from a random node and each time we pick the following node by choosing the one that has the current node as the closest one

The Genetic Algorithm follows a modern approach, indeed at each generation, for each offspring it either:
1) <strong>Perform Mutation</strong> with probability p: the kind of mutation depends on the problem:
   - <strong>Inversion mutation </strong>if the problem matrix is symmetrical, since our goal is to minimize the changes in the edges, so that most neighbours stay neighbours, even though they are in the opposite order.
   - <strong>Insert mutation</strong> if the roblem matrix is asymmetrical, since our goal is to minimize the changes in the order, trying to preserve the relative order (since M[i][j] != M[j][i])
2) <strong>Perform Crossover</strong> with probability 1-p: the kind of mutation depends on the problem:
   - <strong>Edge Recombination Crossover (ERX)</strong>: if the problem matrix is symmetrical, since our goal is to minimize the changes in the edges
   - <strong>An alternative Crossover</strong> for asymmetrical problems, in which instead of minimizing the changes in edges we try to preserve the relative order 


### Results
#### G (problem_g)
| problem | result |
|---|---:|
| problem_g_10.npy | 1497.66 |
| problem_g_20.npy | 1755.51 |
| problem_g_50.npy | 2727.64 |
| problem_g_100.npy | 4167.37 |
| problem_g_200.npy | 5832.32 |
| problem_g_500.npy | 9422.04 |
| problem_g_1000.npy | 13659.81 |

#### R1 (problem_r1)
| problem | result |
|---|---:|
| problem_r1_10.npy | 184.27 |
| problem_r1_20.npy | 342.42 |
| problem_r1_50.npy | 578.79 |
| problem_r1_100.npy | 898.86 |
| problem_r1_200.npy | 1477.63 |
| problem_r1_500.npy | 3132.91 |
| problem_r1_1000.npy | 5850.80 |

#### R2 (problem_r2)
| problem | result |
|---|---:|
| problem_r2_10.npy | -411.70 |
| problem_r2_20.npy | -783.41 |
| problem_r2_50.npy | -2133.68 |
| problem_r2_100.npy | -4509.20 |
| problem_r2_200.npy | -8998.33 |
| problem_r2_500.npy | -22611.86 |
| problem_r2_1000.npy | -45553.85 |
