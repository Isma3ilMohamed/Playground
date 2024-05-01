package dp

import kotlin.math.min

fun coinChangeTopDown(coins:List<Int>,target:Int):Int{
    val dp= hashMapOf<Int,Int>()

     fun count(n:Int):Int{
         //setup base case
         if (n==0) return 0
         if (n <0) return Int.MAX_VALUE
         //check if value is sorted
         if (dp.containsKey(n)) return dp[n]!!

         //variable to store min values from coin list
         var  minCoins=Int.MAX_VALUE
         for (coin in coins){

             val res=count(n-coin)
             if (res !=Int.MAX_VALUE){
                 minCoins=min(minCoins,res+1)
             }
         }
         dp[n]= minCoins
         return dp[n]!!
     }

    val result=count(target)

     return result
 }

fun coinChangeBottomUp(coins: List<Int>, target: Int):Int{
    val dp=IntArray(target+1){
        Int.MAX_VALUE
    }

    dp[0]=0

    for (i in 1..target){
        for (coin in coins){
           if (i >= coin && dp[i-coin] != Int.MAX_VALUE){
               dp[i]= min(dp[i],dp[i-coin]+1)
           }
        }

    }

    return dp[target]
}


fun main() {
    println(coinChangeBottomUp(coins = listOf(2,4,5), target = 10))
}





