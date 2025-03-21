from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        reverse_graph = defaultdict(list)
        in_degree = {}
        for recipe, reqs in zip(recipes, ingredients):
            in_degree[recipe] = len(reqs)
            for ing in reqs:
                reverse_graph[ing].append(recipe)
        queue = deque(supplies)
        result = []

        while queue: 
            supply = queue.popleft()
            for recipe in reverse_graph[supply]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0: 
                    result.append(recipe)
                    queue.append(recipe)
        return result