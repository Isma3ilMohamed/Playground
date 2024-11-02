package autocloseable_interface

import kotlin.contracts.ExperimentalContracts
import kotlin.contracts.InvocationKind
import kotlin.contracts.contract


interface AutoCloseable {
    fun close(t:Throwable?)
}

@OptIn(ExperimentalContracts::class)
inline fun <T: AutoCloseable?,R> T.use(block:(T) -> R):R{
    contract {
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    }

    var exception: Throwable? = null

    try {
        return block(this)
    }catch (e: Throwable){
        exception=e
        throw e
    }finally {
        this?.close(exception)
    }
}

class CSVWriter(fileName: String):AutoCloseable{
    init {
        println("Opening the $fileName file in write mode")
//        ...
    }

    fun writeCsvData(data: String) {
        println("Writing csv $data")
//        ...
    }

    override fun close(t: Throwable?) {
        println("Releasing resources")
    }

}


fun main() {
    CSVWriter(fileName = "example.csv").use { writer ->
        writer.writeCsvData("1")
        writer.writeCsvData("2")
        writer.writeCsvData("3 more data")
    }
}