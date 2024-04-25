# 1-Recursion

### In a typical recursive function, each call to the function makes a new entry on the call stack, which stores information about the function's execution context
### such as its variables and the place in the code where it should return after executing. 
### This can lead to a problem known as "stack overflow" if the recursion goes too deep, because there is a limit to the size of the stack.

### For example, a recursive function to calculate the factorial of a number would look something like this:

```kotlin
fun recursiveFactorial(n: Int) : Int {
    return if (n <= 1) {
        1
    } else {
        n * recursiveFactorial(n - 1)
    }
}
```
### In this function, each call to factorial waits for the result of another call to factorial, building up a chain of unresolved operations on the stack.

# 2-Tail Recursion
### Tail recursion is a special case of recursion where the recursive call is the last operation performed by the function. This allows for an optimization called "tail call optimization" (TCO), where the stack frame of the current function call can be reused for the next function call, significantly reducing the memory overhead and avoiding stack overflow.

### However, it's important to note that not all programming languages automatically optimize tail recursive calls. Languages like Scheme and Haskell support this optimization, while languages like Python and Java do not by default.

### A tail recursive version of the factorial function might look like this:

```kotlin
fun factorial(n:Long,accum:Long=1):Long{
    val result = n * accum
    return if (n <= 1) {
        result
    } else {
        factorial(n - 1, result)
    }
}
```
### Here, the last operation is the recursive call itself, and there are no pending operations after it. If the programming language supports tail call optimization, this version of the function can run with constant stack space.

## 3- in kotlin we have a keyword called ```tailrec``` that marks a function as tail-recursive  (allowing the compiler to replace recursion with iteration)

```kotlin
tailrec fun factorial(n:Long,accum:Long=1):Long{
    val soFar = n * accum
    return if (n <= 1) {
        soFar
    } else {
        factorial(n - 1, soFar)
    }
}

```
### so if we see the compilation output, we will see this result

```java
public final long factorial(long n, long accum) {
   while(n > (long) 1) {
      long var10000 = n - (long)1;
      accum = n * accum;
      n = var10000;
   }

   return n * accum;
}
```

# 4-Performance Improvements
#### We can occasionally see performance improvements using this optimization, as well as safety gains. These benefits depend on some other factors – such as how deep the recursion is, and how complicated the calculations are.

### The improvements come from the fact that method calls are more expensive than simply looping.

#### Using our factorial example again, we can measure how long it takes to execute and compare:

#### Calculating factorial(50) 1,000,000 times without tail recursion takes ~70ms
#### Calculating factorial(50) 1,000,000 times with tail recursion takes ~45ms
#### Using the naive benchmark, we got a speedup of 36%, which is significant just for allowing the compiler to re-work our implementation.

#### Note that these measurements are from very simple benchmarking of a simple function. Actual performance changes will vary based on circumstances, and should always be measured before making any decisions