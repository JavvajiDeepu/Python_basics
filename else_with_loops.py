
cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("found faulty car, skipping...")
        break
    print(f"This car is {status}.")
else:
    print("All cars built sucessfully. No faulty cars!")