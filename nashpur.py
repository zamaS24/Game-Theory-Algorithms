import numpy as np


# Trouver tous les équilibres de Nash en stratégies pures.
def nash_pure(matrix):
    num_rows, num_cols = matrix.shape[:-1]  

    equilibres = []

    for i in range(num_rows):
        for j in range(num_cols):

            # Vérification si la stratégie (i, j) est un équilibre de Nash pur
            est_equilibre = all(matrix[i, k][1] <= matrix[i, j][1] for k in range(num_cols)) and \
                      all(matrix[k, j][0] <= matrix[i, j][0] for k in range(num_rows))
            
            if est_equilibre:
                equilibres.append((i, j))

    return equilibres


matrix_example = np.array([[(4, 3), (5, 1), (6, 2)],
                            [(2, 1), (8, 4), (3, 6)],
                            [(3, 0), (9, 6), (2, 8)]])
equilibres_nash = nash_pure(matrix_example)

if not equilibres_nash:
    print("Aucun équilibre de Nash pur trouvé.")
else:
    print("Profils equilibre de nash : :", equilibres_nash)
    




