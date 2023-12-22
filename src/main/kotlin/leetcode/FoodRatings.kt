package leetcode

import java.util.*
import java.util.function.Function


data class Food(val foodRating:Int,val foodName:String) : Comparable<Food>{
    override fun compareTo(other: Food): Int {
        if (foodRating==other.foodRating){
            return foodName.compareTo(other.foodName)
        }
        return -1 * foodRating.compareTo(other.foodRating)
    }

}
class FoodRatings(foods: Array<String>, cuisines: Array<String>, ratings: IntArray) {
    val foodRatingMap= mutableMapOf<String,Int>()
    val foodCuisineMap= mutableMapOf<String,String>()
    val cuisineFoodMap= mutableMapOf<String,PriorityQueue<Food>>()

    init {
        for (i in foods.indices) {
            // Store 'rating' and 'cuisine' of the current 'food' in 'foodRatingMap' and 'foodCuisineMap' maps.
            foodRatingMap[foods[i]] = ratings[i]
            foodCuisineMap.put(foods[i], cuisines[i])
            // Insert the '(rating, name)' element into the current cuisine's priority queue.
            cuisineFoodMap.computeIfAbsent(
                cuisines[i]
            ) { _ -> PriorityQueue<Food>() }.add(
                Food(
                    ratings[i],
                    foods[i]
                )
            )
        }
    }
    fun changeRating(food: String, newRating: Int) {
        foodRatingMap[food] = newRating
        val cuisineName= foodCuisineMap[food]
        cuisineFoodMap[cuisineName]?.add(Food(newRating,food))
    }

    fun highestRated(cuisine: String): String {
        var cuisineHighRate= cuisineFoodMap[cuisine]?.peek()

        while (foodRatingMap[cuisineHighRate?.foodName?:""] != cuisineHighRate?.foodRating){
            cuisineFoodMap.getValue(cuisine).poll()
            cuisineHighRate=cuisineFoodMap[cuisine]?.peek()
        }
        return cuisineHighRate?.foodName?:""
    }

}