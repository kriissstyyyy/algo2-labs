import os

def solve_words(words_list):
    if not words_list:
        return 0
    max_len = max(len(w) for w in words_list)
    buckets = [[] for _ in range(max_len + 1)]
    for word in words_list:
        buckets[len(word)].append(word)
    words = []
    for bucket in buckets:
        words.extend(bucket)

    dp = {}
    max_overall = 0

    for word in words:
        current_max = 1
        for i in range(len(word)):
            prev_word = word[:i] + word[i + 1:]
            if prev_word in dp:
                current_max = max(current_max, dp[prev_word] + 1)
        dp[word] = current_max
        if current_max > max_overall:
            max_overall = current_max

    return max_overall


def solve():
    try:
        with open('wchain.in', 'r') as f:
            data = f.read().split()
    except FileNotFoundError:
        return

    if not data:
        return

    result = solve_words(data[1:])

    with open('wchain.out', 'w') as f:
        f.write(str(result) + '\n')


if __name__ == "__main__":
    solve()

 