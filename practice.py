a ="ab"+"122"
print(a)


lst=[1, 2, 3]

for item in lst:
    print(item)

list1=[1, 2, [3,5,6],[7,8,9]]
for item in list1:
    if isinstance(item, list):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)