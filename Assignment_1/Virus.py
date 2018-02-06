#Some libraries we are going to need
import matplotlib.pyplot as plt

#First we initialize the number of viruses and the number of bacteria
nv = 1
nb = 1000
steps = 0

varr = [nv]
barr = [nb]
n = [1]

while nb>nv:
 nb = 2*(nb-nv)
 nv = 2*nv
 varr.append(nv)
 barr.append(nb)
 n.append(steps)
 steps = steps+1

print('Number of steps: %i' %steps)

plt.semilogy(n,varr, 'k--',n,barr,'k:')
plt.title('Bacteria-Virus growth (semilogx)')
plt.xlabel('Number of steps')
plt.ylabel('Virus or bacteria count')
plt.legend(('Number of viruses', 'Number of bacteria'), loc = 'upper center', shadow = False)
plt.show()
