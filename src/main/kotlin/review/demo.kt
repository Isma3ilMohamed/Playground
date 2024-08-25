package review

fun main() {

    2 addFive 2

    val demo = Demo()
    demo + 5

    val counter=Counter()


    val list= listOf(1,2,3,4,5,6,7,8)
    val count= countElements(list)
}


fun add(a: Int, b: Int): Int {
    return a + b
}

fun returnMeAddFunction(): ((Int, Int) -> Int) = ::add


class Demo {
    var x = 10
    infix fun minus(num: Int) = this.x - num

    operator fun plus(num: Int): Int {
        return x + num
    }
}

infix fun Int.addFive(num: Int) = this + num

 fun <T> countElements(input:Collection<T>):MutableMap<T,Int>{
     val counterMap= mutableMapOf<T,Int>()

     for (element in input){
         counterMap[element] = counterMap.getOrDefault(element,0)+1
     }

     return counterMap
 }

class Counter {
    @Volatile
    var flag: Boolean = false

    @Synchronized
    fun increment() = {}
    @Synchronized
    fun decrement() = {}
    @Synchronized
    fun getCount() = {}
}