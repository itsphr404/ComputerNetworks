
data = input("Enter data bits: ")
gen = "10001000000100001"

def divide(data):
    temp = list(data)

    for i in range(len(data) - 16):
        if temp[i] == '1':
            for j in range(len(gen)):
                temp[i + j] = str(int(temp[i + j]) ^ int(gen[j]))

    return ''.join(temp[-16:])

crc = divide(data + "0" * 16)

print("CRC:", crc)

transmitted = data + crc
print("Transmitted data:", transmitted)

received = input("Enter received data: ")

remainder = divide(received)

if remainder == "0" * 16:
    print("No error detected")
else:
    print("Error detected")
