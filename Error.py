import numpy as np
import matplotlib.pyplot as plt
print(f"Delta Z = {0.01/6563}")
t = 5.8
Zs = [0.009802, 0.009901, 0.009843, 0.009853]
Summ = 0
SummSqr = 0
N = len(Zs)
for i in range(len(Zs)):
    Summ = Summ + Zs[i]
print(Summ/N)
for i in range(len(Zs)):
    SummSqr = SummSqr + (Zs[i] - Summ/N)**2

sigma = (1/N*(N-1)*SummSqr)**0.5
print(f"Z = 0.00985 +- {sigma*t}")