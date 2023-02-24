from data import items, db1, db2, db3, db4, db5
from timeit import default_timer


start = default_timer()




set_items = [{i} for i in items]

"""
Making each item in the items list a set:

Each list of frequent itemssets, L, is a list of 
sets, i.e., a list of itemsets. 

Each list of candidate itemsets, C, is a list of tuples.
This allows for comparing lexicographical order as a list
of sets cannot be sorted as a list of tuples can.
"""



def support(itemset, db):
    """
    Finds absolute and relative support of a
    k-itemset where k >= 0.

    :param itemset: a *single* set of k-itemset
    :param db: dictionary database of transactions
    :return: count, support
    """
    count = 0
    total_trans = 20
    for i in db.values():
        if itemset <= i:
            count += 1
    return count, count/total_trans



def is_frequent(itemset, db, supp_count=2):
    """
    Uses support() function to decide if any k-itemset
    meets desired support count. Here, minimum frequency
    must be 2.

    :param itemset: a single set of k-itemset
    :param db: dictionary database of transactions
    :param supp_count: set minimum count
    :return: boolean value
    """
    i = support(itemset, db)
    count = i[0]
    return count >= supp_count



def find_frequent_one_itemsets(db, supp_count=2):
    """
    Uses preset set_items set to return a new set
    of frequent lexicographically-ordered 1-itemsets.

    :param db: dictionary database of transactions
    :return: list of tuples of frequent 1-itemsets
    """
    itemset = []
    for i in set_items:
        if is_frequent(i, db, supp_count):
            itemset.append(tuple(i))
    itemset = sorted(itemset)
    return itemset



db1_L1 = find_frequent_one_itemsets(db1)
print(db1_L1)



def join(itemset_list, db):
    """
    Joins list of lexicographically sorted
    (k-1)-itemsets to create new list of k-itemsets.

    :param itemset: list of sorted itemset tuples
    :param db: dictionary database of transactions
    :return:list of k-itemset tuples
    """
    joined_list = []
    for i in itemset_list:
        for j in itemset_list:
            if i[:-1] == j[:-1] and i[-1] < j[-1]:
                joined_list.append(i + (j[-1],))
    return sorted(joined_list)


db1_C2 = join(db1_L1, db1)
print("CANDIDATES \n",db1_C2)


def prune(candidate_list, db, supp_count=2):
    """
    Prunes a candidate last and returns only itemsets
    that meet a specified minimum support level.

    :param candidate_list: list of joined itemset tuples
    :param db: dictionary database of transactions
    :return: list of frequent itemset tuples
    """
    pruned_list = []
    for i in candidate_list:
        if is_frequent(set(i),db,supp_count):
            pruned_list.append(i)
    return sorted(pruned_list)

db1_L2 = prune(db1_C2, db1)
print("PRUNED LIST: \n", db1_L2)



def gen_freq_itemsets(db, supp_count=2):
    """
    Generates frequent k-itemsets starting with 1-itemsets.
    The while loop stops when no more frequent k-itemsets
    can be generated.

    :param db: dictionary database of transactions
    :param supp_count: set support count, default 2
    :return: list of lists of tuples, where inner lists represent
    frequent 1-itemsets, 2-itemsets,...to k-itemsets. Each
    innermost tuple represents one frequent itemset.
    """
    freq_itemsets = []
    l = find_frequent_one_itemsets(db, supp_count)
    i = len(l)
    while i > 0:
        freq_itemsets.append(l)
        c = join(l, db)
        l = prune(c, db, supp_count)
        i = len(l)
    return freq_itemsets


print("Database 1:\n", gen_freq_itemsets(db1))
print("Database 2:\n", gen_freq_itemsets(db2))
print("Database 3:\n", gen_freq_itemsets(db3))
print("Database 4:\n", gen_freq_itemsets(db4))
print("Database 5:\n", gen_freq_itemsets(db5))


def generate_ass_rules(itemset_list, db):

    support()

# db1_C3 = join(db1_L2, db1)
# db1_L3 = join()

def brute_force(item_list, db):


    print("")


print(default_timer() - start)