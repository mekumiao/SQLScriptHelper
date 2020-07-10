#
# 有一个背包，它的容量为C（Capacity），现在有n种不同的物品编号分别为0...n-1，其中每一件物品的重量为w(i)，价值为v(i)。问可以向这个背包中盛放哪些物品，使得在不超过背包容量的基础上，物品的总价值最大
#  #


class Solution:
    def __init__(self):
        self.memo = []

    def knapsack(self, w, v, C):
        assert len(w) == len(v)

        if len(w) == 0 or len(v) == 0:
            return 0

        # 初始化二维数组
        self.memo = [[0 for i in range(C+1)] for _ in range(len(w))]

        # 初始化第一行
        for i in range(C+1):
            self.memo[0][i] = v[0] if i >= w[0] else 0

        # 找出最优解
        for i in range(len(w)):
            for j in range(C+1):
                self.memo[i][j] = self.memo[i-1][j]
                if j >= w[i]:
                    self.memo[i][j] = max(
                        self.memo[i][j], self.memo[i-1][j-w[i]]+v[i])

        for i in range(len(w)):
            line = ''
            for j in range(C+1):
                line += '{}    '.format(self.memo[i][j])
            print(line)

        return self.memo[-1][-1]


# solution = Solution()
# w = [2, 3, 4, 2]
# v = [10, 12, 15, 15]

# price = solution.knapsack(w, v, 7)
# print(price)


class Opt:

    def dp_opt(self, arr):
        if len(arr) == 0:
            return 0
        memo = [0 for i in range(len(arr))]
        memo[0] = arr[0]
        memo[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            memo[i] = max(memo[i-1], memo[i-2]+arr[i])
        return memo[-1]


opt = Opt()
arr = [1, 2, 4, 1, 7, 8, 3]
nbr = opt.dp_opt(arr)
print(nbr)
