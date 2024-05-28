no_of_elements = int(input("Enter the number of elements in sequence: "))
sequence = []
diff = []
flag = 1

print("Enter the elements in sequence:")
for i in range(no_of_elements):
    sequence.append(int(input()))

for i in range(no_of_elements - 1):
    difference = abs(sequence[i] - sequence[i + 1])
    diff.append(difference)

for i in range(no_of_elements - 2):
    if diff[i] == diff[i + 1] + 1:
        continue
    else:
        flag = 0
        break

if flag == 1:
    print("Sequence is jolly")
else:
    print("Sequence is not jolly")
