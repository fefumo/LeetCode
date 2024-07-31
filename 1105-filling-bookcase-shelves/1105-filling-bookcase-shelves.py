class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = {}

        def dp(i, cur_h, rem_w):
            if (i, cur_h, rem_w) in memo:
                return memo[(i, cur_h, rem_w)]

            if i == len(books):
                return cur_h

            #next level
            ans = dp(i+1, books[i][1], shelfWidth-books[i][0]) + cur_h
            #same level
            if (books[i][0] <= rem_w):
                ans = min(ans, dp(i + 1, max(cur_h, books[i][1]), rem_w - books[i][0]))
            
            memo[(i, cur_h, rem_w)] = ans
            
            return ans

        return dp(0, 0, shelfWidth)