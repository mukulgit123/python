# Python3
# Constraints for checking the second Highest Score
# 2 <= n <= 10
# -100 <= A[i] <= 100

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sortArr = list(sorted(arr))
    secondHighest = -100  # Had to initialize
    if n >= 2 and n <= 10 and sortArr[n - 1] <= 100 and sortArr[n -
                                                                1] >= -100:  # Exit when constraints are not met for the
        # highest score
        highestScore = sortArr[n - 1]
    else:
        exit()
    for score in sortArr:
        if score >= 100 and score <= - \
                100:  # Exit when constraints are not met for remaining scores
            exit()
        if score < highestScore and score > secondHighest:
            secondHighest = score
    print(secondHighest)
