#Lists stores multiple values in single variable
names = (["sai,24"], "ram")
print(names[0])

# types of lists
# 1,append
nam = ["sai", "ram"]
nam.append("max")
print(nam)

# 2,list.remove(elmnt)
name = ["sai", "ram"]
name.remove("sai")
print(name)

# 3, list.length(elmnt)
name = ["om", "sai", "ram"]
print(len(name))

# 4, list.insert(position, elmnt)
name = ["sai", "ram"]
name.insert(3,"om")
print(name)