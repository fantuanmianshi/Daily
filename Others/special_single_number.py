# solution 1
def special_single_number_1(lst):
    ht = {}                          # a hash map
    ht = defaultdict(lambda: 0, ht)  # with default value 0
    for i in lst:
        ht[i] += 1
    ret = []
    for k, v in ht.iteritems():
        if v == 1:
            ret.append(k)
    return ret