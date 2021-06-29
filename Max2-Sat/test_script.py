from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from neal import SimulatedAnnealingSampler
from tqdm import tqdm

import os
import numpy as np
import dimod
import itertools 
import networkx as nx

# parameters

TOKEN = 'DEV-2cc3acd9d7df48a4fcad58db19dc214c174b74e5' # API dwave
#BENCHMARK_PATH = 'Max2-Sat/testing_sat/benchmarks'
BENCHMARK_PATH = 'testing_sat/benchmarks'
NUM_READS_SQA = 20
NUM_READS_QPU = 20

time_labels = [
'qpu_sampling_time', 
'qpu_anneal_time_per_sample', 
'qpu_readout_time_per_sample', 
'qpu_access_time', 
'qpu_access_overhead_time', 
'qpu_programming_time', 
'qpu_delay_time_per_sample', 
'total_post_processing_time', 
'post_processing_overhead_time'
]

# functions

# parse the clauses from file in DIMACS format
def extract_clauses(path):
    with open(path, "r") as f:
        # retrieve data from file
        sat = f.readlines()
        data = sat[2].split(" ")

    n_variables = int(data[2]) 

    sat = sat[3:]
    clauses = [x.replace(' 0\n', '') for x in sat]
    
    return clauses, n_variables

# build matrix Q and c of the QUBO formulation and construct the respective QUBO_graph
def gen_q(clauses, n_variables):
    Q = np.zeros(shape=(n_variables, n_variables))
    c = 0
    QUBO_graph = nx.Graph()
    for clause in clauses:
        clause = clause.split(' ')
        int_clause = [int(c) for c in clause]

        s1, s2 = int_clause[0], int_clause[1]
        v1, v2 = abs(s1)-1, abs(s2)-1
        QUBO_graph.add_edge(abs(s1), abs(s2))

        if s1 > 0 and s2 > 0: # True True
            # 1 - x1 - x2 + x1x2
            c += 1
            Q[v1][v1] += -1 
            Q[v2][v2] += -1
            Q[v1][v2] += 1/2 
            Q[v2][v1] += 1/2
        elif s1 > 0 and s2 < 0: # True False
            # x2 - x1x2
            Q[v2][v2] += 1
            Q[v1][v2] += -1/2 
            Q[v2][v1] += -1/2

        elif s1 < 0 and s2 > 0: # False True
            # x1 - x1x2
            Q[v1][v1] += 1
            Q[v1][v2] += -1/2 
            Q[v2][v1] += -1/2

        elif s1 < 0 and s2 < 0: # False False
            # x1x2
            Q[v1][v2] += 1/2 
            Q[v2][v1] += 1/2

        else:
            pass # throw error
            
    return Q, c, QUBO_graph

# solve with simulated annealing
def simulated_annealing(bqm, num_reads_sa=NUM_READS_SQA):
    sampler = SimulatedAnnealingSampler()
    response_SQA = sampler.sample(bqm, num_reads=num_reads_sa)
    return response_SQA

# solve on the real QPU
def real_annealing(bqm, num_reads_qpu=NUM_READS_QPU, token=TOKEN):
    # Run the QUBO on the solver from your config file
    sampler = EmbeddingComposite(DWaveSampler(token=token))

    response_QPU = sampler.sample(bqm, num_reads=num_reads_qpu)
    return response_QPU

# return the solution found given the response and the respective QUBO
def return_solution(response, Q, c):
    count = 0
    for i in range(len(response)):
        new_count = response[i][2]
        if  new_count > count:
            best = response[i][0]
            count = new_count
    
    y = c + np.matmul(np.matmul(best.T, Q), best) 

    return y, best


# script for finding the optimum obtained both with simulated and real annealing

from time import strftime, gmtime
timestamp = strftime("%d-%m-%Y-%H:%M:%S", gmtime())

cwd = os.getcwd()
benchmarks = os.listdir(os.path.join(cwd, BENCHMARK_PATH))
#results = os.path.join(cwd, 'Max2-Sat/testing_sat/Results/Benchmarks_' + os.path.splitext(benchmarks[0])[0] + '_' + os.path.splitext(benchmarks[len(benchmarks)-1])[0] + '.txt')
results = os.path.join(cwd, 'testing_sat/Results/Benchmarks_'+ timestamp +'.txt')

fr = open(results, 'w')

for test in tqdm(benchmarks):
    clauses, n_variables = extract_clauses(os.path.join(cwd, BENCHMARK_PATH, test))
    Q, c, QUBO_graph = gen_q(clauses, n_variables)

    # Create BQM
    variable_order = ["x_{}".format(n) for n in range(1, n_variables+1)]
    BQM = dimod.BinaryQuadraticModel.from_numpy_matrix(Q, variable_order = variable_order)

    response_SQA = simulated_annealing(BQM)
    response_QPU = real_annealing(BQM)

    Oy_SA, _ = return_solution(response_SQA.aggregate().record, Q, c)
    Oy_RA, _ = return_solution(response_QPU.aggregate().record, Q, c)

    # time string + total time sum
    time_str = ''
    total_time = 0
    for t in time_labels:
        time = response_QPU.info["timing"][t]
        time_str += f'{t}={time} '
        total_time += time
    time_str += f'total_time={total_time}'

    fr.write(f'{test} O_SA={str(Oy_SA)} O_RA={str(Oy_RA)} {time_str}\n')

fr.close()