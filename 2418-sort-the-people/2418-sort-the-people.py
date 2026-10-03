class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        ans = []
        people = {}
        for name , height in zip(names,heights):
                people[height] = name
        heights.sort(reverse = True)
        for height in heights:
            for k , v in people.items():
                if height == k:
                    ans.append(v)
        return ans