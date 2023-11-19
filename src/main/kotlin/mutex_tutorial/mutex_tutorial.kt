package mutex_tutorial

import jdk.tools.jlink.plugin.ResourcePool
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock


//1. Protecting Shared Data in Multi-threaded Applications\
//2. Implementing Rate Limiting

val mutex= Mutex()
val sharedList= mutableListOf<Int>()
suspend fun addItem(item:Int){
    mutex.withLock {
        sharedList.add(item)
    }
}


//3. Managing Resource Pools
/*val resourceMutex = Mutex()
val resourcePool = ResourcePool()

suspend fun useResource() {
    resourceMutex.withLock {
        val resource = resourcePool.acquire()
        // Use the resource
        resourcePool.release(resource)
    }
}*/

//5. Implementing Atomic Operations


fun main() {


}