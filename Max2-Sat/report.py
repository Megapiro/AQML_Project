import os
import re

B_SOL_PATH = 'testing_sat/Results/b_solutions.txt' # benchmarks solutions
Q_SOL_PATH = 'testing_sat/Results/q_solutions.txt' # quantum solutions
report = os.path.join(os.getcwd(), 'testing_sat/Results/report.md')

benchmarks = []

b_f = open(B_SOL_PATH, 'r')
q_f = open(Q_SOL_PATH, 'r')

# extract benchmarks solutions
b_lines = b_f.readlines()
b_data = []
for l in b_lines:
    b_data.append(l.split())
b_solutions = {}

for t in b_data:
    filename = t[0]
    benchmarks.append(filename)
    b_solutions[filename] = {}
    t.pop(0)
    for s in t:
        val = s.split('=')
        b_solutions[filename][val[0]] = val[1]

# extract quantum solutions
q_lines = q_f.readlines()
q_data = []
for l in q_lines:
    q_data.append(l.split())
q_solutions = {}

for t in q_data:
    filename = t[0]
    q_solutions[filename] = {}
    t.pop(0)
    for s in t:
        val = s.split('=')
        q_solutions[filename][val[0]] = val[1]

fr = open(report, 'w')

head_str = f'|Benachmark| S | O | T | O_SA | O_RA | total_time |\n'
init_str = f'|:--------:|:-:|:-:|:-:|:----:|:----:|:----------:|\n'

fr.write(head_str)
fr.write(init_str)

for b in benchmarks:
    # benchmarks results
    S = b_solutions[b]['S']
    O = b_solutions[b]['O']
    T = b_solutions[b]['T']

    # quantum results
    O_SA = q_solutions[b]['O_SA']
    O_RA = q_solutions[b]['O_RA']
    total_time = q_solutions[b]['total_time']

    str = f'|{b}|S={S} | O={O} | T={T} | O_SA={O_SA} | O_RA={O_RA} | total_time={total_time}|\n'
    fr.write(str)
    
        