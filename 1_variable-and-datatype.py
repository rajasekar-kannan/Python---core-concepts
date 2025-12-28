""" 
#1. Variable is a reference (not a box)
    Example
        a = 10
        b = a

        Output ->     a ──▶ 10  and b ──▶ 10

    What really happens
        Python creates one object: 10
        a points to that object a ──▶ 10
        Python does NOT create a new 10 (b = a)
        b now points to the same object as a
        So, This is reference copying, not value copying.

    Key idea
        Here, We did not copy the value. We copied the reference.

#2. Object has the type, not the variable
    Example
        x = 10
        x = "hello"
    What changed
        * Variable name x stayed the same
        * Object changed from 10 (number) to "hello" (text)

        x ──▶ 10        (earlier)
        x ──▶ "hello"  (now)

    Key idea
        Python variables are type-free.
        Objects are type-full.

#3. Immutable object behavior (safe)
    Example
        a = 10
        b = a
        a = 20

    What happens
        * 10 cannot change (immutable)
        * Python creates a new object 20
        * a now points to 20
        * b still points to 10
            a ──▶ 20
            b ──▶ 10

    Why this is safe
        Immutable objects never change.Reassignment always means new object.

#4. Mutable object behavior (danger zone)
    Example
        a = [1, 2, 3]
        b = a
        a.append(4)

    What happens
        * List object is mutable
        * append changes the same object
        * Both a and b see the change

        a ──▶ [1, 2, 3, 4]
        b ──▶ [1, 2, 3, 4]

    Key insight
        This is the most common Python bug in large systems.

#5. Why this surprises Java / Node developers
    Java
        * Variables have fixed types
        * Mutation rules are stricter
        * Compiler protects We

    Node.js
        * Objects are mutable
        * But Python is stricter about types

    Python
        * Dynamic
        * Reference-based
        * Strongly typed
        * Mutation must be explicitly managed 

"""