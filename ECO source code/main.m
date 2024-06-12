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

close all
clear
clc
N = 40; % Number of search agents
Function_name='F5'; % Name of the test function that can be from F1 to F23 (Table 1,2,3 in the paper)
Max_iteration = 500; % Maximum numbef of iterations

% Load details of the selected benchmark function
[lb,ub,dim,fobj] = Get_Functions_details(Function_name);
[avg_fitness_curve, Best_pos, Best_score, Convergence1, search_history, fitness_history] = ECO(N,Max_iteration,lb,ub,dim,fobj);

figure('Position',[454 445 1600 300])
%Draw search space
subplot(1,4,1);
func_plot(Function_name);
title('Parameter space')
xlabel('x_1');
ylabel('x_2');
zlabel([Function_name,'( x_1 , x_2 )'])


%
subplot(1,4,2);
hold on
for k1 = 1:size(search_history, 1)
    for k2 = 1:size(search_history, 2)
        plot(search_history(k1, k2, 1), search_history(k1, k2, 2), '.', 'markersize', 1, 'MarkerEdgeColor', 'k', 'markerfacecolor', 'k');
    end
end
title('ECO (x1 and x2 only)')
xlabel('x1')
ylabel('x2')
box on
axis tight




%
subplot(1,4,3);
hold on
plot(mean(fitness_history),'Linewidth', 1.5);
title('Average fitness')
xlabel('Iteration')
box on
axis tight



%Draw objective space
subplot(1,4,4);
semilogy(Convergence1,'Color','k','Linewidth', 1.5)
hold on
title('Objective space')
xlabel('Iteration');
ylabel('Best score obtained so far');
axis tight
grid on
box on
legend('ECO')



