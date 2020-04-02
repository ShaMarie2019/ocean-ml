import matplotlib.pyplot as plt
import matplotlib.image as mpimg

<<<<<<< HEAD
#pic = mpimg.imread('/Users/brownscholar/Desktop/Intern_Git/ocean-ml/session-3-26/excitement.jpeg')
=======
pic = mpimg.imread('./images/excitement.jpeg')
>>>>>>> 43d737d6877dd505a998425e546733ce6e3280d1

plt.imshow(pic)
plt.show(block=False)
plt.pause(3)
plt.close()
