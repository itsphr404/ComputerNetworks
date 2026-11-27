
cap = int(input("Enter the bucket size: "))
process = int(input("Enter the processing rate: "))
nsec = int(input("Enter the number of seconds: "))

inp = []

for i in range(nsec):
    inp.append(int(input(f"Enter packets at {i+1} sec: ")))

count = 0

print("\nSecond | Received | Sent | Left | Dropped")
print("------------------------------------------")

for i in range(nsec):
    count += inp[i]
    drop = 0

    if count > cap:
        drop = count - cap
        count = cap

    mini = min(count, process)
    count -= mini

    print(i+1, "\t", inp[i], "\t", mini, "\t", count, "\t", drop)

i = nsec

while count > 0:
    mini = min(count, process)
    count -= mini

    print(i+1, "\t", 0, "\t", mini, "\t", count, "\t", 0)
    i += 1
