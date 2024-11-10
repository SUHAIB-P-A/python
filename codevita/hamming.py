def get_cost(s, a, b):
    
    cost = 0
    for i in range(len(s) - 1):
        if s[i] == "0" and s[i+1] == "1":
            cost += a
        elif s[i] == "1" and s[i+1] == "0":
            cost += b
    return cost


def minimize_cost(s, a, b):
    
    min_cost = float("inf")
    min_str = None
    min_ham_distance = float("inf")

    for i in range(len(s)):
        rotated_str = s[i:] + s[:i]
        curr_cost = get_cost(rotated_str, a, b)
        ham_distance = sum([a != b for a, b in zip(s, rotated_str)])
        if curr_cost < min_cost:
            min_cost = curr_cost
            min_str = rotated_str
            min_ham_distance = ham_distance
        elif curr_cost == min_cost:
            if ham_distance < min_ham_distance:
                min_ham_distance = ham_distance
                min_str = rotated_str

    return min_cost, min_str, min_ham_distance


def main():
    t = int(input())  # Number of test cases

    for _ in range(t):
        s = input()  # Binary string
        a, b = map(int, input().split())  # Cost of "01" and "10"

        if not all(c in "01" for c in s):
            print("INVALID")
        else:
            min_cost, min_str, ham_distance = minimize_cost(s, a, b)
            print(ham_distance)


if __name__ == "__main__":
    main()
