package generics


/**

out (Covariant):
This keyword means that the generic type can only be used as a return type, not as a function parameter.
It makes a type parameter covariant. This is safe when you only retrieve values of a specified type from a collection.
For example, a Producer<T> can produce Ts (like returning T), but it should not accept Ts.

in (Contravariant):
The in keyword means that the generic type can only be used as a function parameter, not as a return type.
This makes a type parameter contravariant. This is safe when you only put values into a collection.
For example, a Consumer<T> can consume Ts (like accepting T as a parameter) but should not return Ts.

where :
Kotlin allows you to apply multiple constraints to a generic type parameter using the where keyword.
This is useful when you need a type parameter to satisfy more than one type constraint.

 * */


class Box<in T, out K>(val value: K) {
    fun get(): K = value
    fun put(item: T) {
        println(item.toString())
    }
    fun <T> process(items:List<T>)where T:CharSequence,T:Comparable<T>{
        // T must be a CharSequence and must be Comparable to its own type.
        for (item in items) {
            // Do something with item, which you can treat as CharSequence and Comparable.
            println(item)
        }
    }
}

fun main() {
    val box=Box<Int,String>(value = "22")
    box.put(55)
    box.process(items = listOf("12","13"))

}