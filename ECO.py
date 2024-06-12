'''
%___________________________________________________________________________________________________________________________________________________%

% Educational Competition Optimizer (ECO) source codes (version 1.0)

% Website and codes of Educational Competition Optimizer(ECO):

% http://www.aliasgharheidari.com/ECO.html

% https://github.com/junbolian/ECO

% Junbo Lian, Ting Zhu, Ling Ma, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen, Guohua Hui

% Last update: May 21 2024

% E-Mail: junbolian@qq.com, as_heidari@ut.ac.ir, aliasghar68@gmail.com, chenhuiling.jlu@gmail.com

%----------------------------------------------------------------------------------------------------------------------------------------------------%

% Authors: Junbo Lian (junbolian@qq.com), Ali Asghar Heidari(as_heidari@ut.ac.ir, aliasghar68@gmail.com), Huiling Chen(chenhuiling.jlu@gmail.com)

%----------------------------------------------------------------------------------------------------------------------------------------------------%

% After use of code, please users cite to the main paper on Educational Competition Optimizer (ECO):
% Junbo Lian, Ting Zhu, Ling Ma, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen*, Guohua Hui*
% The Educational Competition Optimizer
% INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE, Taylor & Francis Online - 2024
% https://doi.org/10.1080/00207721.2024.2367079

%----------------------------------------------------------------------------------------------------------------------------------------------------%

% You can use and compare with other optimization methods developed by the same authors:
% (AO) - 2024: http://www.aliasgharheidari.com/AO.html
% (PO) - 2024: http://www.aliasgharheidari.com/PO.html
% (RIME) - 2023: http://www.aliasgharheidari.com/RIME.html
% (INFO) - 2022: http://www.aliasgharheidari.com/INFO.html
% (RUN) - 2021: http://www.aliasgharheidari.com/RUN.html
% (HGS) - 2021: http://www.aliasgharheidari.com/HGS.html
% (SMA) - 2020: http://www.aliasgharheidari.com/SMA.html
% (HHO) - 2019: http://www.aliasgharheidari.com/HHO.html

%____________________________________________________________________________________________________________________________________________________%
'''

import numpy as np


def ECO(N, Max_iter, lb, ub, dim, fobj):
    H = 0.5
    G1 = 0.2
    G2 = 0.1

    G1Number = round(N * G1)
    G2Number = round(N * G2)

    if np.isscalar(ub):
        ub = np.ones(dim) * ub
        lb = np.ones(dim) * lb

    # Initialization
    X0 = initializationLogistic(N, dim, ub, lb)
    X = np.copy(X0)

    fitness = np.zeros(N)
    for i in range(N):
        fitness[i] = fobj(X[i, :])

    fitness, index = np.sort(fitness), np.argsort(fitness)
    GBestF = fitness[0]
    AveF = np.mean(fitness)

    X = X[index, :]

    curve = np.zeros(Max_iter)
    avg_fitness_curve = np.zeros(Max_iter)

    GBestX = X[0, :]
    GWorstX = X[-1, :]
    X_new = np.copy(X)

    search_history = np.zeros((N, Max_iter, dim))
    fitness_history = np.zeros((N, Max_iter))

    # Start search
    for i in range(Max_iter):
        if i % 100 == 0:
            print(f'At iteration {i}, the fitness is {curve[i-1]}')

        avg_fitness_curve[i] = AveF
        R1 = np.random.rand()
        R2 = np.random.rand()
        P = 4 * np.random.randn() * (1 - i / Max_iter)
        E = (np.pi * i) / (P * Max_iter)
        w = 0.1 * np.log(2 - (i / Max_iter))

        for j in range(N):
            if i % 3 == 1:
                if j < G1Number:
                    X_new[j, :] = X[j, :] + w * (np.mean(X[j, :]) - X[j, :]) * Levy(dim)
                else:
                    X_new[j, :] = X[j, :] + w * (close(X[j, :], 1, X, G1Number) - X[j, :]) * np.random.randn()
            elif i % 3 == 2:
                if j < G2Number:
                    X_new[j, :] = X[j, :] + (GBestX - np.mean(X, axis=0)) * np.exp(i / Max_iter - 1) * Levy(dim)
                else:
                    if R1 < H:
                        X_new[j, :] = X[j, :] - w * close(X[j, :], 2, X, G2Number) - P * (
                                    E * w * close(X[j, :], 2, X, G2Number) - X[j, :])
                    else:
                        X_new[j, :] = X[j, :] - w * close(X[j, :], 2, X, G2Number) - P * (
                                    w * close(X[j, :], 2, X, G2Number) - X[j, :])
            else:
                if j < G2Number:
                    X_new[j, :] = X[j, :] + (GBestX - X[j, :]) * np.random.randn() - (
                                GBestX - X[j, :]) * np.random.randn()
                else:
                    if R2 < H:
                        X_new[j, :] = GBestX - P * (E * GBestX - X[j, :])
                    else:
                        X_new[j, :] = GBestX - P * (GBestX - X[j, :])

            # Boundary control
            X_new[j, :] = np.clip(X_new[j, :], lb, ub)

            fitness_new = fobj(X_new[j, :])
            if fitness_new > fitness[j]:
                fitness_new = fitness[j]
                X_new[j, :] = X[j, :]

            if fitness_new < GBestF:
                GBestF = fitness_new
                GBestX = X_new[j, :]

        X = np.copy(X_new)
        fitness = np.array([fobj(X[k, :]) for k in range(N)])

        curve[i] = GBestF
        Best_pos = GBestX
        Best_score = curve[-1]
        search_history[:, i, :] = X
        fitness_history[:, i] = fitness

        fitness, index = np.sort(fitness), np.argsort(fitness)
        X = X[index, :]

    return avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history


def Levy(d):
    beta = 1.5
    sigma = (np.math.gamma(1 + beta) * np.sin(np.pi * beta / 2) / (
                np.math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    u = np.random.randn(1, d) * sigma
    v = np.random.randn(1, d)
    step = u / np.power(np.abs(v), (1 / beta))
    return step


def close(t, G, X, GNumber):
    m = X[0, :]
    for s in range(GNumber):
        school = X[s, :]
        if np.sum(np.abs(m - t)) > np.sum(np.abs(school - t)):
            m = school
    return m


def initializationLogistic(pop, dim, ub, lb):
    Positions = np.zeros((pop, dim))
    for i in range(pop):
        for j in range(dim):
            x0 = np.random.rand()
            a = 4
            x = a * x0 * (1 - x0)
            if len(ub) == 1:
                Positions[i, j] = (ub - lb) * x + lb
            else:
                Positions[i, j] = (ub[j] - lb[j]) * x + lb[j]
            x0 = x
    return Positions



def test_function(x):
    # this is a simple test function
    return sum(x**2)

# parameter set
N = 50  
Max_iter = 1000 
lb = -10 
ub = 10  
dim = 10  

avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history = ECO(N, Max_iter, lb, ub, dim, test_function)

print("Best Position：", Best_pos)
print("Best Score：", Best_score)

