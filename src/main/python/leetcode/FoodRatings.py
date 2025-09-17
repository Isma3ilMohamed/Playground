class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.foodRatings = {}
        self.foodCuisines = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodRatings[food] = rating
            self.foodCuisines[food] = cuisine
            heapq.heappush(self.cuisines[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRatings[food] = newRating
        cuisine = self.foodCuisines[food]
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines[cuisine]
        while self.foodRatings[heap[0][1]] != -heap[0][0]:
            heapq.heappop(heap)
        return heap[0][1]
