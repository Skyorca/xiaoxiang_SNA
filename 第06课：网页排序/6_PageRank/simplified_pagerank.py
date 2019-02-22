
PR = {}
# ------ init PR scores -------
PR['Yahoo'] = 1/3.0 
PR['Amazon'] = 1/3.0 
PR['Microsoft'] = 1/3.0

# ------- iteratively update PR scores ---------
num = 100
for i in range(num):
    PR_new = PR.copy()

    PR_new['Yahoo'] = (1/2)*PR['Yahoo'] + (1/2)*PR['Amazon']
    PR_new['Amazon'] = (1/2)*PR['Yahoo'] + PR['Microsoft']
    PR_new['Microsoft'] = (1/2)*PR['Amazon']
    PR = PR_new

print(PR)