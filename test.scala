#!/usr/bin/env scala
//
//2n
//println("Hello " + name + "!")
val msg = "Hello, world!"
val msg2: java.lang.String = "Hello again, world!"
println(msg)
println(msg2)
val multiLine =
  "jkjkjk"
println(multiLine)

def max(x: Int, y: Int): Int = {
           if (x > y)
             x
           else 
             y
         }

println(max(9,10))
var i = 0
//args.foreach(arg => println(arg))
val big = new java.math.BigInteger("12345")

val greetStrings = new Array[String](3)
  
    greetStrings(0) = "Hello"
    greetStrings(1) = ", "
    greetStrings(2) = "world!\n"
  
    for (i <- 0 to 2)
      print(greetStrings(i))
val x = (1).+(2)

val numNames = Array("zero", "one", "two")
numNames.foreach(name => println(name))
Console println 10
