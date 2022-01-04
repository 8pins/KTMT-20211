from matplotlib import pyplot as plt

fig, axs = plt.subplots(1,2)
fig.suptitle('Bộ lọc trung vị')
a = plt.imread("https://media.geeksforgeeks.org/wp-content/uploads/20190520115432/Screenshot-1110.png")
b = plt.imread("https://media.geeksforgeeks.org/wp-content/uploads/20190520115504/Screenshot-1210.png")
axs[0].imshow(a)
axs[1].imshow(b)
fig.show()
print()
