package coroutines_flow

import kotlinx.coroutines.*
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.channels.trySendBlocking
import kotlinx.coroutines.flow.*


@OptIn(ExperimentalCoroutinesApi::class, FlowPreview::class)
fun main() = runBlocking {

    /**
     *The map operator is used to transform each emitted value into a new value. It's like applying a function to each item in the flow.
     * */
    flowOf("apple", "banana", "cherry")
        .map { fruit -> "I love $fruit" }
        .collect { /*println(it)*/ }

    /**
     * The filter operator allows you to select elements that meet a specific condition. It's useful for filtering data within a flow.
     * */
    flowOf(1, 2, 3, 4, 5)
        .filter { number -> number % 2 == 0 }
        .collect { /*println(it)*/ }


    /**
     * The flatMapConcat operator transforms each value into a new flow and merges them sequentially.
     * It's particularly useful for creating sub-flows within a flow.
     * */
    flowOf(1, 2, 3)
        .flatMapConcat { value -> flowOf(value, value * 2) }
        .collect { /*println(it)*/ }

    /**
     * The debounce operator is used to emit only the last value in a specified time window. It's handy for handling user input or real-time events.
     * */
    flowOf(1, 2, 3)
        .debounce(200) // Emits the last value after a 200ms pause
        .collect { /*println(it)*/ }


    /**
     * The zip operator combines values from multiple flows into pairs or tuples. It's useful for synchronizing data from different sources
     * */
    val flow1 = flowOf("A", "B", "C")
    val flow2 = flowOf(1, 2, 3)
    flow1.zip(flow2) { letter, number -> "$letter$number" }
        .collect { /*println(it)*/ }

    /**
     * The scan operator is used to accumulate values and emit the result at each step. It's like a running total of values in the flow.
     * */

    flowOf(1,2,3,4)
        .scan(0){accumulator, value -> accumulator+value }
        .collect{ /*println(it)*/ }

    /**
     * The distinctUntilChanged operator suppresses repeated consecutive values. It ensures that only distinct values are emitted.
     * */
    flowOf(1, 1, 2, 2, 3)
        .distinctUntilChanged()
        .collect {/* println(it)*/ }

    flowOf(1, 1, 2, 2, 3).transform { value->
        emit(value)
    } .collect { println(it) }
}