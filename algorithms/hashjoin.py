
def hashjoin(hashcost, mergecost, nestloopcost):
    annotation = "This join is implemented using hash join operator as merge join and NL joins \
        increase the estimated cost by at least " + int(mergecost/hashcost) + " times and " \
            + int(nestloopcost/hashcost) + " times, respectively"
    
    return annotation