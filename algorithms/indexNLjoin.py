
def indexnestloopjoin(hashcost, mergecost, nestloopcost):
    annotation = "This join is implemented using index NL joins operator as hash join and merge join \
        increase the estimated cost by at least " + int(hashcost/nestloopcost) + " times and " \
            + int(mergecost/nestloopcost) + " times, respectively"

    return annotation