data = ["Python", "C", "Java", "C++", "Object-C", "R"]

print(data)

posob = data.index("Object-C")
print("Odject-C:",posob)

data[posob] = "Swift"

posja = data.index("Java")
print("Java:",posja)

data.insert(posja,"C#")

data.remove("R")

print(data)
