import string

index1 = ("abc")
index2 = ("aBc")
index3 = ("dog")

def is_sorted(string):
    if (all(string[x] <= string[x+1] for x in range(len(string)-1))):
        return True
    else:
        return False

print(is_sorted(index1))
print(is_sorted(index2))
print(is_sorted(index3))
