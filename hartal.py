no_of_days = int(input("Enter the number of days: "))
no_of_parties = int(input("Enter the number of parties: "))
diff_hartal = []
count = 0

for i in range(no_of_parties):
    diff = int(input("Enter the difference of hartal: "))
    diff_hartal.append(diff)

for i in range(1, no_of_days + 1):
    for j in diff_hartal:
        if (i % j == 0 and i % 7 != 0 and i % 7 != 6):
            count += 1
            break

print(count)
