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



g = [{'a'},{'a','b'},{'a','b','c'}, {'a','b','c','d'}]
h = {'a','b','c','d'}
possible_ass_rules = None
print(possible_ass_rules)
def gen_ass_rules(list,itemset=None,left=None):
    if left is None: left = set()
    if list is None: list = []
    right = {i for i in itemset}
    for i in itemset:
        # print('start of loop:', left,right)
        add_left = {i for i in left} | {i}
        deduct_right = {i for i in right} - {i}
        # print("ADD",add_left, 'DEDUCT',deduct_right)
        # if len(deduct_right) == 0:
        #     two_itemset = [{i} for i in itemset]
        #     return list
        if len(right) > 1:
            if [add_left,deduct_right] in list:
                continue
            left = add_left
            right = deduct_right
            if [left,right] not in list:
                list += [[left,right]]
                list += [[right,left]]
        if len(right) == 1:
            if [right,left] not in list:
                list += [[right, left]]
            gen_ass_rules(list,left,right)
    return list
# j = gen_ass_rules(possible_ass_rules,h)
# z = []
# for i in j:
#     if i not in z:
#         z.append(i)
# print(j, len(j))
# print("\n\n\n\nZEE:\n",z)
# print(len(z))

# i = h | {'e'}
# j = gen_ass_rules(possible_ass_rules,i)
# z = []
# for i in j:
#     if i not in z:
#         z.append(i)
# print(j, len(j))
# print("\n\n\n\nZEE:\n",z)
# print(len(z))
# #


# o = {'a','b','c','d','e'}
# j = gen_ass_rules(possible_ass_rules,o)
# z = []
# for i in j:
#     if i not in z:
#         z.append(i)
# print(j, len(j))
# print("\n\n\n\nZEE:\n",z)
# print(len(z))

# e = {'a','b'}
# j = gen_ass_rules(possible_ass_rules,e)
# z = []
# for i in j:
#     if i not in z:
#         z.append(i)
# print("\n\n\n\nZEE:\n",z)
# print(len(z))

# i = {'e','f'}
# h.add(i.pop())
# geez = [{i for i in h}]
# print('geez',geez)
# print(h | i in geez)
# i-{'e'}
# print(h,i)


# newsy = []
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
# print(master)
# print("\n\nGENERATE",gen_combinations(h,newsy))
# print(h)

