import sys
from itertools import product

def generate_rule_dict(identifier):
    rule_bin = format(identifier, '08b')[::-1]
    return {pattern: rule_bin[i] for i, pattern in enumerate(product('01', repeat=3))}

def can_generate(target_state, rule_dict, N, partial_state, index):
    if index == N:
        new_state = ''.join(rule_dict[(partial_state[(i-1) % N], partial_state[i], partial_state[(i+1) % N])] for i in range(N))
        return new_state == target_state

    for bit in "01":
        if can_generate(target_state, rule_dict, N, partial_state + bit, index + 1):
            return True
    
    return False

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 3:
        continue
    
    identifier = int(parts[0])
    N = int(parts[1])
    target_state = parts[2]

    rule_dict = generate_rule_dict(identifier)

    if can_generate(target_state, rule_dict, N, "", 0):
        print("REACHABLE")
    else:
        print("GARDEN OF EDEN")
