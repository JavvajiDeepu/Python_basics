# continue 
cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("found faulty car, skipping...")
        continue
    print(f"This car is {status}.")

# break is used to break the current working 
cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("found faulty car, skipping...")
        break
    print(f"This car is {status}.")
