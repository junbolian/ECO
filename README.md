# Educational Competition Optimizer (ECO)

Abstract: In recent research, metaheuristic strategies stand out as powerful tools for complex optimization, capturing widespread attention. This study proposes the Educational Competition Optimizer (ECO), an algorithm created for diverse optimization tasks. ECO draws inspiration from the competitive dynamics observed in real-world educational resource allocation scenarios, harnessing this principle to refine its search process. To further boost its efficiency, the algorithm divides the iterative process into three distinct phases: elementary, middle, and high school. Through this stepwise approach, ECO gradually narrows down the pool of potential solutions, mirroring the gradual competition witnessed within educational systems. This strategic approach ensures a smooth and resourceful transition between ECO's exploration and exploitation phases. The results indicate that ECO attains its peak optimization performance when configured with a population size of 40. Notably, the algorithm's optimization efficacy does not exhibit a strictly linear correlation with population size. To comprehensively evaluate ECO's effectiveness and convergence characteristics, we conducted a rigorous comparative analysis, comparing ECO against nine state-of-the-art metaheuristic algorithms. ECO's remarkable success in efficiently addressing complex optimization problems underscores its potential applicability across diverse real-world domains. The additional resources and open-source code for the proposed ECO can be accessed at https://aliasgharheidari.com/ECO.html

## Overview

Welcome to the Educational Competition Optimizer (ECO) repository! The ECO is an innovative optimization algorithm inspired by the competitive nature of educational systems. This repository contains the source code for ECO, along with comprehensive documentation to help you understand and utilize this powerful optimization tool.

### Inspiration

The ECO algorithm draws inspiration from the intense competition observed in educational settings. As students strive to meet the rigorous admission criteria of educational institutions, their pursuit mirrors the process of navigating complex optimization problems. By simulating this educational competition, ECO employs greedy selection and balanced exploration and exploitation principles to retain elite solutions and find the optimal solution.

### Mathematical Model

The ECO algorithm models the educational competition process through three distinct stages: primary school, middle school, and high school. Each stage represents different levels of competitive intensity and strategies:

1. **Primary School Stage**: Schools select optimal locations based on the population's average location, and students compete for the nearest school.
2. **Middle School Stage**: The number of schools decreases, and schools consider both the population's mean and best positions. Students' motivation and patience in learning are taken into account.
3. **High School Stage**: Schools adopt a meticulous approach, considering the population's mean, best, and worst positions. Students converge toward the current best location, competing for superior educational opportunities.

### Population Initialization

ECO uses logistic chaos mapping to simulate the absence of education leading to societal chaos. The initialization formula ensures the population is spread across the search space, enhancing the exploration capabilities of the algorithm.

### Stages of ECO

#### Primary School Stage

During this stage, schools determine suitable teaching locations based on the average population location, and students aim for the nearest school. The top 20% of the population are designated as schools, while the remaining 80% are students.

#### Middle School Stage

In this stage, schools adopt a more sophisticated approach by considering both the average and optimal population locations. The top 10% of the population are designated as schools, while the remaining 90% are students. Students' learning patience and motivation are considered.

#### High School Stage

At the high school level, schools consider the average, best, and worst population locations to determine their educational location. The top 10% of the population are designated as schools, and the remaining 90% are students, all striving for the best location.

### Pseudo-code of the ECO Algorithm

```python
Algorithm 1: Pseudo-code of the ECO algorithm
1: Initialize the ECO parameters
2: Initialize the solutions' positions randomly (Logistic Chaos Mapping)
3: For i = 1:Max_iter do
4:    Calculate the fitness function
5:    Find the best position and worst position
6:    Calculate R1, R2, P, E
7:    For j = 1:N do
8:        Stage 1: Primary school competition
9:        If mod(i, 3) == 1 Then
10:           If j = 1:G1Number Then
11:               Update schools position by Eq. (3)
12:           Elseif j = G1Number+1:N Then
13:               Update students position by Eq. (4)
14:           End
15:       Stage 2: middle school competition
16:       Elseif mod(i, 3) == 2 Then
17:           If j = 1:G2Number Then
18:               Update schools position by Eq. (10)
19:           Elseif j = G2Number+1:N Then
20:               Update students position by Eq. (11)
21:           End
22:       Stage 3: High school competition
23:       Elseif mod(i, 3) == 0 Then
24:           If j = 1:G2Number Then
25:               Update schools position by Eq. (12)
26:           If j = G2Number+1:N Then
27:               Update students position by Eq. (13)
28:           End
29:       End
30:       If X_i^(t+1)>X_i^t Then
31:           Select the optimal solution using the positive greedy selection mechanism
32:       End
33:   End
34:   Return the best solution
35: End
```

- **Website and codes of Educational Competition Optimizer (ECO):**
  - [ECO Website](http://www.aliasgharheidari.com/ECO.html)

- **Authors:**
  - Junbo Lian: [junbolian@qq.com](mailto:junbolian@qq.com)
  - Ali Asghar Heidari: [as_heidari@ut.ac.ir](mailto:as_heidari@ut.ac.ir), [aliasghar68@gmail.com](mailto:aliasghar68@gmail.com)
  - Huiling Chen: [chenhuiling.jlu@gmail.com](mailto:chenhuiling.jlu@gmail.com)

- **Contributors:**
  - Ting Zhu
  - Ling Ma
  - Xincan Wu
  - Yi Chen
  - Guohua Hui

- **Last update:** May 21, 2024

## Citation

After using the code, please cite the main paper on Educational Competition Optimizer (ECO):

**Junbo Lian, Ting Zhu, Ling Ma, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen*, Guohua Hui*.**  
*The Educational Competition Optimizer.*  
International journal of systems science, Taylor & Francis Online - 2024

## Comapre with other optimization methods

You can use and compare ECO with other optimization methods developed recently:

- **AO (2024):** [Link](http://www.aliasgharheidari.com/AO.html)
- **PO (2024):** [Link](http://www.aliasgharheidari.com/PO.html)
- **RIME (2023):** [Link](http://www.aliasgharheidari.com/RIME.html)
- **INFO (2022):** [Link](http://www.aliasgharheidari.com/INFO.html)
- **RUN (2021):** [Link](http://www.aliasgharheidari.com/RUN.html)
- **HGS (2021):** [Link](http://www.aliasgharheidari.com/HGS.html)
- **SMA (2020):** [Link](http://www.aliasgharheidari.com/SMA.html)
- **HHO (2019):** [Link](http://www.aliasgharheidari.com/HHO.html)
