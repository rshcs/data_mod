from skimage import data
from matplotlib import pyplot as plt

coins = data.coins()

plt.imshow(coins, cmap='gray')