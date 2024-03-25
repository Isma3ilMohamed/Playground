package flow

import kotlinx.coroutines.*
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.channels.trySendBlocking
import kotlinx.coroutines.flow.*

// todo Buffer
fun main()= runBlocking {

/*    var sendData: suspend (data: Int) -> Unit = { }
    var closeChannel: () -> Unit = { }

    launch {
        channelFlow {
            for (i in 1..5) send(i)
            sendData = { data -> send(data) }
            closeChannel = { close() }
            awaitClose {
                sendData = {}
                closeChannel = {}
            }
        }.collect { println(it) }
    }

    delay(10)
    println("Sending 6")
    sendData(6)
    closeChannel()*/
    var sendData: (data: Int) -> Unit = { } // Not suspending
    var closeChannel: () -> Unit = { }

    launch {
        channelFlow {
            for (i in 1..5) trySendBlocking(i)
            sendData = { data -> trySendBlocking(data) }
            closeChannel = { close() }
            awaitClose {
                sendData = {}
                closeChannel = {}
            }
        }.collect { println(it) }
    }

    delay(10)
    println("Sending 6")
    sendData(6)
    closeChannel()
    sendData(7)

    callbackFlow {
        send(1)

    }
}

fun <T> Flow<T>.flowMerge(other: Flow<T>): Flow<T> = channelFlow {
    launch {
        collect { send(it) }
    }
    other.collect { send(it) }
}
