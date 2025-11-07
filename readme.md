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

The population at each generation is "deduplicated", so the duplicated individuals are removed, in order to have a better differentiation.


### Results
#### G (problem_g)
| problem | result |
|---|---:|
| problem_g_10.npy | 1497.66 |
| problem_g_20.npy | 1755.51 |
| problem_g_50.npy | 2673.65.64 |
| problem_g_100.npy | 4158.75 |
| problem_g_200.npy | 5802.58 |
| problem_g_500.npy | 9065.08 |
| problem_g_1000.npy | 13373.95 |

#### R1 (problem_r1)
| problem | result |
|---|---:|
| problem_r1_10.npy | 184.27 |
| problem_r1_20.npy | 340.86 |
| problem_r1_50.npy | 548.72 |
| problem_r1_100.npy | 923.09 |
| problem_r1_200.npy | 1485.31 |
| problem_r1_500.npy | 3013.48 |
| problem_r1_1000.npy | 5648.55 |

#### R2 (problem_r2)
| problem | result |
|---|---:|
| problem_r2_10.npy | -411.70 |
| problem_r2_20.npy | -820.16 |
| problem_r2_50.npy | -2219.38 |
| problem_r2_100.npy | -4428.14 |
| problem_r2_200.npy | -9099.35 |
| problem_r2_500.npy | -23045.06 |
| problem_r2_1000.npy | -45566.02 |


### Notes
The code for plotting the solution of the test problem on the map has been written thanks to the help of copilot.