import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
jobs=[100,80,60]
domains=["Java","Python","Android"]
plt.pie(jobs, labels=domains)
