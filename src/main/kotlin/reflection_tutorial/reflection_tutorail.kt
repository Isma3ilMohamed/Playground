package reflection_tutorial

import kotlin.reflect.full.memberProperties
import kotlin.reflect.full.valueParameters

data class Person(val name: String, val age: Int)


fun foo(x: Int) = println(x)
var counter = 0
fun main() {
    //   val person=Person("Boody",30)
    //Java reflection
//    val properties=person.javaClass.declaredFields
//    for (property in properties){
//        //By setting the isAccessible property to true, we ensure that we can access private fields as well.
//        property.isAccessible=true
//
//        val value=property.get(person)
//        println("${property.name}: $value")
//    }

    //Kotlin's reflection
//    val kClass=person.javaClass.kotlin
//    println(kClass.simpleName)
//    kClass.memberProperties.forEach { println(it.name) }


    //KCallable
    /**
    KCallable is a super interface for functions and properties, and it declares the call method, which allows you to invoke the corresponding function or property getter.
     * */

//    val kFunction=::foo
//    /*If you try to call the function with an incorrect number of arguments, such as function.call(),
//     it will throw a runtime exception with the message "IllegalArgumentException: Callable expects 1 argument, but 0 were provided."*/
//    kFunction.call(60)
//    //if we need To provide better type safety and enforce the correct number of arguments, you can use a more specific method called invoke
//    kFunction.invoke(60)

    //KProperty
    /**
    The KProperty interface provides methods to achieve this, with different interfaces for top-level properties and member properties.
     * */
//    val kProperty=::counter
//    kProperty.setter.call(21)
//    println(kProperty.get())
//
//
//    val memberProperty = Person::age
//    println(memberProperty.get(person))

    /**
    Please keep in mind that reflection can only be used to access properties defined at the top level or within a class,
    and not local variables within a function. If you try to obtain a reference to a local variable using::x,
    you will encounter a compilation error stating that "References to variables aren't supported yet".
     * */
    val person = Person("John Doe", 30)

    // Serialization using reflection
    val serializedData = Person::class.memberProperties
        .associateBy({ it.name }, { it.getter.call(person) })
    println(serializedData) // Output: {name=John Doe, age=30}
// Deserialization using reflection
    val deserializedPerson = Person::class.constructors.first()
        .call(serializedData["name"], serializedData["age"])
    println(deserializedPerson) // Output: Person(name=John Doe, age=30)

        val clientClass = Client::class
        val constructors = clientClass.constructors

        if (constructors.isNotEmpty()) {
            val constructor = constructors.first()
            val parameters = constructor.parameters

            // Dependency injection using reflection
            val serviceA = ServiceA()
            val serviceB = ServiceB()
            val client = constructor.callBy(mapOf(parameters[0] to serviceA, parameters[1] to serviceB))

            client.performActions()
        }

}

class ServiceA {
    fun doSomething() {
        println("Service A is doing something.")
    }
}

class ServiceB {
    fun doSomethingElse() {
        println("Service B is doing something else.")
    }
}

class Client(private val serviceA: ServiceA, private val serviceB: ServiceB) {
    fun performActions() {
        serviceA.doSomething()
        serviceB.doSomethingElse()
    }
}


