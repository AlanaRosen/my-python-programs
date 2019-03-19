the_list = [76, 92.3, "hello", True, 4, 76]

the_list.append("apple")
the_list[3:3]=["cat"]
the_list[0:0] = [99]
print(the_list.index("hello"))
print(the_list.count(76))
the_list.remove(76)
the_list.pop(4)

print(the_list)