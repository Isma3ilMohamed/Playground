package flow

import leetcode.result
import java.util.concurrent.Executors
import java.util.concurrent.LinkedBlockingQueue
import java.util.concurrent.TimeUnit
import kotlin.coroutines.Continuation
import kotlin.coroutines.CoroutineContext
import kotlin.coroutines.EmptyCoroutineContext
import kotlin.coroutines.createCoroutine
import kotlin.coroutines.resume
import kotlin.coroutines.suspendCoroutine


suspend fun async() {
    println("ASYNC ${Thread.currentThread().name}")
    withContext(BackgroundDispatcher){
        println("Changed to ${Thread.currentThread().name}")
        withContext(MainDispatcher){
            println("Changed to ${Thread.currentThread().name}")
        }
    }
    println("Done in ${Thread.currentThread().name}")
}


fun main() {
    val coroutines = ::async.createCoroutine(Continuation(MainDispatcher) { result -> result.getOrThrow() })
    MainDispatcher.dispatch {
        coroutines.resume(Unit)
    }
    MainDispatcher.loop()
}

interface Dispatcher: CoroutineContext.Element{
    fun dispatch(block:()->Unit)
    override val key: CoroutineContext.Key<*> get()  = Key
    companion object Key: CoroutineContext.Key<Dispatcher>
}

object MainDispatcher: Dispatcher{
    private val queue= LinkedBlockingQueue<()->Unit>()
    override fun dispatch(block: () -> Unit) {
        queue.offer(block)
    }

    fun loop(){
        while (true){
            queue.poll(1, TimeUnit.SECONDS)?.invoke()?:return
        }
    }
}
object BackgroundDispatcher: Dispatcher{
    private val executors= Executors.newFixedThreadPool(4)

    override fun dispatch(block: () -> Unit) {
        executors.execute{block()}
    }

}

suspend fun<T> withContext(context: CoroutineContext,action:suspend ()->T):T{
    return suspendCoroutine { outerContinuation->
        val newContext=outerContinuation.context + context
        val newCoroutines=action.createCoroutine(Continuation(newContext){result->
            val dispatcher=outerContinuation.context[Dispatcher]?:error("No dispatcher found")

            dispatcher.dispatch {
                outerContinuation.resumeWith(result)
            }
        })

        val newDispatcher=newContext[Dispatcher]?:error("no dispatcher found")
        newDispatcher.dispatch {
            newCoroutines.resume(Unit)
        }

    }
}