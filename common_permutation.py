from collections import Counter

def common_permutation(str1, str2):
    # Count characters in both strings
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)

    # Find common characters by intersecting both counters
    common_chars = count_str1 & count_str2

    # Sort the common characters and join them to form the result string
    result = ''.join(sorted(common_chars.elements()))

    return result

# Input strings
str1 = "pretty"
str2 = "women"

# Calculate and print the common permutation
print(common_permutation(str1, str2))
