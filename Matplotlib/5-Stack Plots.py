from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

# minutes of the game
minutes = [1,2,3,4,5,6,7,8,9]

# player 1 scored 1 point in first minute, 5 points in total at the end of the game
player1 = [1,2,3,3,4,4,4,4,5]
# player 2 scored 1 point till 4th minutes of the game, 4 point in total
player2 = [1,1,1,1,2,2,2,3,4]
# player 3 scored 1 point till 3d minute, 3 points in total
player3 = [1,1,1,2,2,2,3,3,3]
labels = ['player1','player2','player3']
colors = ['Black','Blue','Yellow']

plt.stackplot(minutes,player1,player2,player3, labels = labels, colors = colors)
plt.legend(loc='upper left')
plt.title('Pie Chart')
plt.tight_layout()
plt.savefig('StackPlots')
plt.show()
