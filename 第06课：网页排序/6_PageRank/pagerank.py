
PR = {}
# ------ init PR scores -------
PR['Yahoo'] = 1/3.0 
PR['Amazon'] = 1/3.0 
PR['Microsoft'] = 1/3.0
# ------ set the random jump probabilities
c1 = 0.8
c2 = 0.2
Eu = 1/3.0
# ------- iteratively update PR scores ---------
num = 100
for i in range(num):
    PR_new = PR.copy()
    # ---------- example 1 ----------
    #PR_new['Yahoo'] = c1*((1/2)*PR['Yahoo'] + (1/2)*PR['Amazon']) + c2*Eu
    #PR_new['Amazon'] = c1*((1/2)*PR['Yahoo'] + PR['Microsoft']) + c2*Eu
    #PR_new['Microsoft'] = c1*(1/2)*PR['Amazon'] + c2*Eu

    # ----------- example 2 ----------
    PR_new['Yahoo'] = c1*((1/2)*PR['Yahoo'] + (1/2)*PR['Amazon']) + c2*Eu
    PR_new['Amazon'] = c1*((1/2)*PR['Yahoo']) + c2*Eu
    PR_new['Microsoft'] = c1*((1/2)*PR['Amazon']+PR['Microsoft']) + c2*Eu

    PR = PR_new

print(PR)