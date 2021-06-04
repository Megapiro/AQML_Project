For the practical part you have been assigned the Max 2-Sat problem.
You will find the QUBO formulation on the Glover 2019 paper which we also briefly saw during one of the lectures. Details on the type of analysis you should do have been sent some time ago via BeeP.

In your project you should implement the generation of the BQM given that QUBO formulation and a set of clauses.
In order to generate SAT instances to test you can generate them at random (no need to guarantee they are satisfiable) or use a portion of instances you may find as part of online benchmarking repositories, but those may be too big for the purposes of this project. Keep it simple.

To generate SAT instances that are guaranteed to be satisfiable you can also use a factory method. This has the advantage of allowing you to check if the solver has found the ground state (one of the satisfiable assignments that are guaranteed to exist). In this case you should use the "manual" BQM construction from the QUBO formulation for some initial examples and then you can use the factory method for bigger instances. See:
https://docs.ocean.dwavesys.com/projects/binarycsp/en/latest/reference/generated/dwavebinarycsp.factories.csp.sat.random_2in4sat.html#dwavebinarycsp.factories.csp.sat.random_2in4sat

You can find a very simple code snippet in this document at pag 5
https://docs.ocean.dwavesys.com/_/downloads/binarycsp/en/latest/pdf/

Compared to other types of problems SAT has a structure which is more prone to noise, so it could be that the quality of solutions you get from the QPU is lower than those of SA. This can be mitigated with the annealing duration and schedule but it is not required of you to do an extensive study.
