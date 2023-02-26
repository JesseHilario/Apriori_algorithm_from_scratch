# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


l = ("deez", "nutz")
m = ("deez",)
print(set(sorted(l)))
p = [{5,7,8,9}, {5, 4, 6, 1}]
print(sorted(p))
def join(itemset_list, k=2):
    joined_list = []
    for i in itemset_list:
        for j in itemset_list:
            # if i[:-1] == j[:-1] and i[-1] < j[-1]:
            if i | j != i:
                joined_list.append(i | j)
            #     joined_list.append(i + (j[-1],))
        itemset_list.remove(j)
    return sorted(joined_list)

print(join(p))


q = (1,2,3,4)
r = (3,)
if r in q: print("yes")
s = {1,2,3,4}
t = {3,}
if t < s: print("yes")
for i in s:
    print(i)
for i in enumerate(s):
    print(i)

print({s.pop()})

g = [{'a'},{'a','b'},{'a','b','c'}, {'a','b','c','d'}]
master = []
for itemset in g:
    if len(itemset) < 1:
        continue
    for i in itemset:
        left = {i}
        right = itemset - left
        # if [left, right] in master:
        #     continue
        if len(right) == 0:
            break
        print([left,right])
        master += [[left,right]]
        print([right,left])
        master += [[right,left]]
        # print("\n\n\nmaster:",master)
        if len(right) > 1:
            for j in right:
                # print(left,right)
                # print(right, left)
                left.add(j)
                right = right - left
                if [left,right] in master:
                    continue
                if len(right) == 0:
                    break
                # master.append([left, right])
                # master.append([right, left])
                master += [[left,right]]
                master += [[right,left]]

                # print("\n\n\nmaster inner:",master)


h = {'a','b','c'}
newsy = []
# def gen_combinations(itemset, newsy, left=set()):
#     for i in itemset:
#         if len(newsy) == 0:
#             left = {i}
#         right = itemset - left
#         if len(right) == 0:
#             return newsy
#         if [left,right] not in newsy:
#             print("here",[left,right])
#             newsy += [[left, right]]
#         if len(right) > 1:
#             return newsy + gen_combinations(itemset,newsy,left=left)
    # if [left, right] in newsy:
    #     return newsy
    # if len(right) > 1:
    #     return gen_combinations(right, newsy,left=left) + newsy
        # if len(right) == 0:
        #     continue
        # print([left,right])
        # print([right,left])
        # newsy += [[right, left]]
        # while len(right) > 1:
        #     for j in right:
        #         left.add(j)
        #         right = right - left
        #         if [left,right] in newsy:
        #             continue
        #         if len(right) == 0:
        #             break
        #         print(left,right)
        #         print(right, left)
        #         # master.append([left, right])
        #         newsy.append([right, left])
        #         # print("\n\n\nmaster inner:",master)
print(master)
# print("\n\nGENERATE",gen_combinations(h,newsy))
# print(h)

