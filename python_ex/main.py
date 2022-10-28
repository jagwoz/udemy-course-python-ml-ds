print("My name is {}, I've {}".format('John', 20))
print("My name is {one}, I've {two}".format(two='John', one=20))

out = list(map(lambda x: x*2, range(0, 5)))
print(out)

out = list(filter(lambda x: x % 2 == 0, range(0, 5)))
print(out)

# str.split('#')  # split tweet hashtags for example
