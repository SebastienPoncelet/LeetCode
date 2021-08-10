# Runtime: 68 ms, faster than 79.88% of Python3 online submissions for Relative Ranks.
# Memory Usage: 15.3 MB, less than 57.48% of Python3 online submissions for Relative Ranks.

from typing import List


def findRelativeRanks(score: List[int]) -> List[str]:
  max_heap = sorted(score, reverse=True)
  n = len(max_heap)

  rank = {}
  new_score = []

  for i in range(n):
    rank[max_heap[i]] = i

  for item in score:

    if rank[item] == 0:
      new_score.append('Gold Medal')

    elif rank[item] == 1:
      new_score.append('Silver Medal')

    elif rank[item] == 2:
      new_score.append('Bronze Medal')

    else:
      new_score.append(str(rank[item] + 1))
  print(new_score)

  return new_score

arr = [10,3,8,9,4]
findRelativeRanks(arr)
arr = [5,4,3,2,1]
findRelativeRanks(arr)
