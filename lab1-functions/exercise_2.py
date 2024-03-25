## place for exercise 2
import numpy as np
import matplotlib.pyplot as plt

# chessboard

x = np.arange(1, 9, 1)
y = np.arange(1, 9, 1)

data = np.zeros((len(y), len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0) :
            data[j, i] = 1


plt.imshow(data, cmap='binary')

plt.title("Chessboard")
x_labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
plt.xticks(np.arange(len(x_labels)), x_labels)
plt.yticks(np.arange(len(y)), y)


plt.show()