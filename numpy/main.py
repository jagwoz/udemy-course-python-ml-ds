import numpy as np

myList = np.array([0, 1, 2, 3])
print(myList)

print(np.arange(0, 10))
print(np.zeros(5))
print(np.zeros((4, 4)))  # or ones()

linear = np.linspace(0, 10, 5)  # line values
print(linear)

print(np.eye(3))

rand = np.array(np.random.randint(0, 10, 25))
rand = rand.reshape(5, 5)
print(rand)
print(rand.argmax())
print(rand.shape)

random = rand
random[2:5, 2:3] = 20
print(random)  # rand is the same

print(rand[0, 0])
print(rand[0][0])

print(rand[rand < 4])

print(rand + rand)
print(rand.sum(axis=0))

