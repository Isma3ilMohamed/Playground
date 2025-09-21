from sortedcontainers import SortedSet


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.rented_movies = SortedSet()
        self.available_movies = {}
        self.movie_price = {}

        for shop, movie, cost in entries:
            if movie not in self.available_movies:
                self.available_movies[movie] = SortedSet()

            self.available_movies[movie].add((cost, shop))

            if movie not in self.movie_price:
                self.movie_price[movie] = {}
            self.movie_price[movie][shop] = cost

    def search(self, movie: int) -> List[int]:
        result = []
        if movie in self.available_movies:
            for cost, shop in self.available_movies[movie]:
                result.append(shop)
                if len(result) == 5:
                    break
        return result

    def rent(self, shop: int, movie: int) -> None:
        cost = self.movie_price[movie][shop]
        self.available_movies[movie].remove((cost, shop))
        self.rented_movies.add((cost, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        cost = self.movie_price[movie][shop]
        self.rented_movies.remove((cost, shop, movie))
        self.available_movies[movie].add((cost, shop))

    def report(self) -> List[List[int]]:
        result = []
        for cost, shop, movie in self.rented_movies:
            result.append([shop, movie])
            if len(result) == 5:
                break
        return result


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
