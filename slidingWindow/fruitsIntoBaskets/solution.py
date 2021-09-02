class Solution:
    def fruits_into_baskets(self, fruits):
        max_fruits = 0
        start_index = 0
        end_index = 0
        unique = dict()

        for fruit in fruits:
            end_index += 1
            unique[fruit] = unique.get(fruit, 0) + 1
            while len(unique) > 2:
                first_fruit = fruits[start_index]
                unique[first_fruit] -= 1
                if unique[first_fruit] == 0:
                    unique.pop(first_fruit)
                start_index += 1
            max_fruits = max(max_fruits, end_index - start_index)
        return max_fruits
