def maximize_gems(dish_data):
    
    # Sort dishes by id
    dish_data.sort(key=lambda x: x[0])

    # Calculate prefix minimum and maximum ratings
    min_ratings = [dish_data[0][1]]
    max_ratings = [dish_data[0][1]]
    for i in range(1, len(dish_data)):
        min_ratings.append(min(min_ratings[-1], dish_data[i][1]))
        max_ratings.append(max(max_ratings[-1], dish_data[i][1]))

    # Initialize variables for dynamic programming
    dp = [0] * len(dish_data)
    max_gem_idx = [-1] * len(dish_data)

    # Calculate maximum gems for each dish
    for i in range(len(dish_data)):
        # Consider grouping this dish alone
        dp[i] = max_ratings[i]

        # Consider grouping this dish with previous dishes
        for j in range(i - 1, -1, -1):
            if dish_data[j][0] < dish_data[i][0]:
                # Combine max rating from current group with min rating from previous group
                curr_gem = max_ratings[i] + min_ratings[j]
                if curr_gem > dp[i]:
                    dp[i] = curr_gem
                    max_gem_idx[i] = j
                break

    # Get the final maximum gems
    max_gems = max(dp)

    # Backtrack to find the grouping that gives maximum gems
    grouping = []
    i = len(dish_data) - 1
    while i >= 0:
        if max_gem_idx[i] == -1:
            grouping.append(str(dish_data[i][0]) + ":" + str(dish_data[i][1]))
        else:
            grouping.append("(" + ",".join([str(dish_data[j][0]) + ":" + str(
                dish_data[j][1]) for j in range(max_gem_idx[i], i + 1)]) + ")")
        i = max_gem_idx[i] - 1

    return max_gems, grouping[::-1]


def main():
    n = int(input())  # Number of dishes
    dish_data = []

    for _ in range(n):
        id, rating = map(int, input().split(":"))
        dish_data.append((id, rating))

    max_gems, grouping = maximize_gems(dish_data)
    print(max_gems)
    print(",".join(grouping))


if __name__ == "__main__":
    main()
