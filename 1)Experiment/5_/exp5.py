def generate_candidates(itemset, k):
    candidates = []
    n = len(itemset)
    for i in range(n):
        for j in range(i + 1, n):
            L1 = itemset[i][:k - 2]
            L2 = itemset[j][:k - 2]
            if L1 == L2:
                candidates.append(itemset[i] + [itemset[j][-1]])
    return candidates

def prune(itemset, candidates, min_support):
    pruned_itemset = []
    support_count = {}
    for candidate in candidates:
        for item in itemset:
            if set(candidate).issubset(set(item)):
                if tuple(candidate) in support_count:
                    support_count[tuple(candidate)] += 1
                else:
                    support_count[tuple(candidate)] = 1
    for item, count in support_count.items():
        support = count / len(itemset)
        if support >= min_support:
            pruned_itemset.append(list(item))
    return pruned_itemset

def apriori(itemset, min_support):
    k = 2
    frequent_itemsets = []
    while True:
        candidates = generate_candidates(itemset, k)
        pruned_itemset = prune(itemset, candidates, min_support)
        if not pruned_itemset:
            break
        frequent_itemsets.extend(pruned_itemset)
        itemset = pruned_itemset
        k += 1
    return frequent_itemsets

# Example usage
itemset = [['A', 'B', 'C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'D'], ['B', 'D']]
min_support = 0.4
frequent_itemsets = apriori(itemset, min_support)
print(frequent_itemsets)


from prettytable import PrettyTable
from itertools import combinations
def calculate_frequency(itemset, frequent_itemsets):
    frequency = {}
    for item in frequent_itemsets:
        for transaction in itemset:
            if set(item).issubset(set(transaction)):
                if tuple(item) in frequency:
                    frequency[tuple(item)] += 1
                else:
                    frequency[tuple(item)] = 1
    return frequency

def generate_rules(frequent_itemsets, frequency, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        n = len(itemset)
        for i in range(1, n):
            for subset in combinations(itemset, i):
                subset = list(subset)
                left = subset
                right = list(set(itemset) - set(subset))
                confidence = frequency[tuple(itemset)] / frequency[tuple(left)]
                if confidence >= min_confidence:
                    rules.append((left, right, confidence))
    return rules

def print_table(frequency, rules):
    # Print frequency table
    freq_table = PrettyTable(['Itemset', 'Frequency'])
    for item, freq in frequency.items():
        freq_table.add_row([list(item), freq])
    print(freq_table)

    # Print rules table
    rules_table = PrettyTable(['Antecedent', 'Consequent', 'Confidence'])
    for left, right, confidence in rules:
        rules_table.add_row([left, right, confidence])
    print(rules_table)

# Example usage
itemset = [['A', 'B', 'C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'D'], ['B', 'D']]
min_support = 0.4
min_confidence = 0.6
frequent_itemsets = apriori(itemset, min_support)
frequency = calculate_frequency(itemset, frequent_itemsets)
rules = generate_rules(frequent_itemsets, frequency, min_confidence)
print_table(frequency, rules)