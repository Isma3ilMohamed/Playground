package composition

interface Mouth {
    fun speak()
}

class CatMouth: Mouth{
    override fun speak() {
        println("Meaw")
    }

}

class SpecificCat: Mouth by CatMouth() {
    private val mouth: Mouth = CatMouth()

    fun meow(){
        mouth.speak()
    }

    fun specificFunction(){
        println("Specific")
    }
}

fun main() {
    val specificCat = SpecificCat()
    specificCat.speak() // meow
    specificCat.specificFunction() // specific
}