
## 1. How does Object Oriented Programming differ from Process Oriented Programming?

The applications are created using both object-oriented programming(OOP) and Process Oriented Programming(POP). Before proceeding to the comparison, we will provide a brief summary of both approaches.. 

#### Process Oriented Programming

It is characterised as a programming language based on calling procedures that is derived from structural programming. Procedures are functions, routines, or subroutines that contain the computing steps that must be performed. It takes a step-by-step approach to breaking down a task into a set of variables and routines using a series of instructions. A procedure can be invoked at any time throughout the program's execution, either by other procedures or by itself.

Process Oriented Programming is less secure than object-oriented programming. During the design of a programme, Process Oriented Programming takes a top-down approach. It emphasises the concept of function and splits huge programmes into smaller components, which are referred to as functions. Process Oriented Programming is easy to understand. In contrast to object-oriented programming, Process Oriented Programming does not use access modifiers.


#### Object-oriented programming

Object-oriented programming is a technique for computer programming design that organizes software architecture around data or objects rather than functions and logic. It is a programming paradigm that revolves around an object or entity. A fully object-oriented programming language is one that uses the programming paradigm in which everything is represented as an object.  

It is best suited for large, sophisticated, and frequently updated or maintained projects. It simplifies programme creation and maintenance by introducing key ideas such as abstraction, inheritance, polymorphism, and encapsulation. These four characteristics are also the four pillars of an object-oriented programming system.

OOPs make it possible to imitate real-world occurrences much more effectively. Using the Object-Oriented Programming language, we may deliver solutions to real-world situations. OOPs hide data, but Procedure-oriented programming languages allow access to global data from everywhere.


Due to the above characteristics, the key differences are summarised as follows

1. Definition

POP: It is a programming language that is built on the concept of calling procedures and is derived from structural programming. It takes a step-by-step approach to breaking down a task into a set of variables and routines using a series of instructions.

OOP: Object-oriented programming is a technique for computer programming design that organizes/models software architecture around data or objects rather than functions and logic.

2. Security

POP is not as secure as OOPs. Because of abstraction, data hiding is possible in object-oriented programming. 

3. Approach

POP is approached from the top down. OOP is built from the ground up.

4. Data movement

Data travels freely within the system from one function to the next in Process Oriented Programmi. Objects in OOP can move and communicate with one another using member functions.

5. Orientation

POP is structured/procedural in nature whereas OOP is object-oriented in nature.

6. Access modifiers	

In POP, there are no access modifiers. In OOP, access modifiers are classified as private, public, or protected.

7. Inheritance	

There is a feature of inheritance in OOP only. 

8. Code reusability	

In POP, there is no code reusability. OOP provides code reusability by utilising the inheritance capability.

9. Overloading

Function overloading and operator overloading are concepts only in OOP.

10. Importance

OOP gives importance to data over functions.

11. Virtual class	

In OOP, there could be virtual classes in inheritance.

12. Complex problems	

OOP is more appropriate for complex systems.

13. Data hiding	

It is possible to hide data in OPP. 

14. Program division	

In OOP, a program is made of small parts that are referred to as objects, not lfunction like POP. 

15. languages Examples	

Process Oriented Programming languages : C, Fortran, Pascal, and VB
Object-oriented programming languages : .NET, C#, Python, Java, VB.NET, and C++.

Resource: https://www.javatpoint.com/procedural-programming-vs-object-oriented-programming	


## 2. What's polymorphism in OOP?

The meaning of ‘polymorphism’ is the condition of occurrence in different forms.

Polymorphism is a concept in OOP, which refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

Polymorphism appears in two type:Static and dynamic polymorphism

Here is an example of polymorphism with Classes: 

    class Adult:
        def move(self):
            print('walk')
    
        def greet(self):
            print('Hello!')


    class Baby:
        def move(self):
            print('crawl')
    
        def greet(self):
            print('smile :)')


    Keiko = Adult()
    Emma = Baby()
    
    for human in (Keiko, Emma):
        human.move()
        human.greet()
    
    # output
    # walk
    # Hello!
    # crawl
    # smile :)

Here, we have created two classes Adultand Baby. They share a similar structure and have the same method names move() and greet(). Although we have not created a common superclass or linked the classes together, we can pack these two different objects into a tuple and iterate through it using a common human variable. It is possible due to polymorphism. 


Source: https://www.programiz.com/python-programming/polymorphism

## 3. What's inheritance in OOP?

The ability to define a new class that is a modified version of an existing class is known as inheritance.

This feature's main benefit is that you can add new methods to classes without changing the ones that already exist. Because the new class inherits all of the existing class's methods, it is called "inheritance." Using this metaphor further, the current class may also be referred to as the parent class. The new class may be referred to as a "subclass" or its "child class."

Inheritance is a useful feature because inheritance can also help with code reuse without having to modify them. In some circumstances, the inheritance structure reflects the problem's natural nature, making the programme easier to understand.

Inheritance, on the other hand, can make programmes harder to read. When a method is called, it is not always obvious where to look for its definition. The relevant code may be spread over numerous modules. Furthermore, many of the things that may be done using inheritance may be done just as neatly without inheritance. 

Following is an example of inheritance where a class named Car inherited properties and methods from a class named Vehicle.

Create a class named Vehicle, with brand and name properties, and a printname method:

    class Vehicle:
      def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    
      def printname(self):
        print(self.brand, self.name)
    
    x = Vehicle("Toyota", "Sora Bus")
    x.printname()

    # Create a class named Car, which will inherit the properties and methods from the Vehicle class:
    class Car(Vehicle):
      pass
    
    # Now the Car class has the same properties and methods as the Vehicle class.
    x = Car("Ford", "F-Series")
    x.printname()

Source : https://openbookproject.net/thinkcs/python/english3e/inheritance.html#:~:text=Inheritance%20is%20the%20ability%20to,methods%20of%20the%20existing%20class.

## 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?

Given the limited information provide, I will make the following assumptions
- Funny people are already nominated
- People selects one person from the nominated people
- The person who has the most votes are considered to be the funniest
- We don’t need to consider a tie
- Vote eligibility check is not required. 

I would make it possible to vote on those people by creating a website, which presents the options, maybe buttons with nominated people's name. When a voter clicks the button, the website will send the vote and the data is stored in an appropriate storage, database or a file depending on the number of voters.

For the backend, I would use a lightweight framework such as Flask if the number of voters are small. Otherwise, I would consider other frameworks such as Django.  

If it is stored in a file, I would use an array to store the vallots and use Counter from collections to count the votes. The results will be sorted and the top three people with highest votes are the top three funniest people.  

If it is stored in a database such as sql, I would run a query COUNT(vote) and return top 3 people for the results. 

Since there is no requirement to display the result, I would probably just print the results after the voting has completed. 


## 5. What's the software development cycle?

The software development cycle refers to the complete process of developing software from beginning to end. When beginning a new software project, it is critical to consider how it will be created and maintained. 

The process is called as a cycle because even after completing a piece of software, it may be essential to return to the beginning. For example, it may be possible to upgrade the programme in response to the availability of new technologies. You might be able to make significant modifications to how the software operates and restart the development cycle.

The essential stages of the cycle are as follows:

- Planning

The planning stage is the first stage of the software development cycle. During this stage, developers identify the project's goals and objectives. They also determine the resources required, such as time, money, and manpower. This is a crucial step since it establishes the foundations for the entire project.

- Collecting requirements

The requirement gathering stage is the second stage of the software development cycle. Developers gather information on what the user wants and needs from the software programme during this stage. They also collect data about the existing system, if one exists. This stage is critical since it assists developers in understanding what they need to produce.

- Design

Design is the third stage of the software development cycle. Developers construct a blueprint for the software application during this stage. They decide how the programme will look and feel, as well as how it will function. This stage is critical since it guarantees that the software programme satisfies the needs of the user.

- Prototyping

Prototyping is frequently regarded a part of the design stage, although it can also be considered its own stage. Developers produce a working model of the software application during prototyping. Users can then try the application and provide comments.

- Implementation

Implementation is the fourth stage of the software development cycle. During this stage, developers write the software application's code and then build it. This is a critical stage because it brings the software programme to life.

- Testing

Testing is the fifth and last stage of the software development cycle. Developers test the software application at this stage to confirm that it operates as intended. They also patch any issues they discover. This stage is critical because it guarantees that the software application is ready for use by users.

- Deployment

The software development cycle does not end until the programme is deployed. Deployment can be performed in-house or outsourced to a third-party vendor.

- Maintenance and operation

It's the last stage of the software development process. Following the deployment of the software application, it must be monitored and maintained. There are three kinds of maintenance:

corrective - repair any faults found in the programme
perfective - add new features
Adaptive - make adjustments to the software to accommodate for new situations, allowing it to run on new operating systems and hardware.

Source: https://www.bbc.co.uk/bitesize/guides/z8n3d2p/revision/1
https://rooche.net/software-development-cycle/

## 6. What's the difference between agile and waterfall?

Agile is a collection of principles and values established in 2001 by 17 technology leaders. Scrum, Lean, Six Sigma, and Kanban are among the frameworks and product delivery methods that fall under the Agile umbrella. Agile frameworks and approaches, in general, do not govern the project lifecycle, but rather give a flexible and iterative solution that allows you to change as needed.

Waterfall, on the other hand, is far more linear, focused on upfront preparation with well stated requirements before a project begins. Work cascades across several project phases, much like a waterfall, as the term implies. Each phase must be completed before moving on to the next.

The primary distinctions between agile and waterfall techniques are as follows.

- Customer involvement over contract negotiations
- People and engagement take precedence over process and tools.
- Adapting to change rather than sticking to a routine
- Overcoming extensive documentation by developing/testing solutions

The main distinction between these techniques is that, whereas Agile completes projects iteratively in a cycle of sprints, Waterfall plans and follows a sequence. Waterfall forecasts how the ultimate product will turn out, whereas Agile envisions it. Agile, in a sense, leaves nothing to chance. Despite having planned everything from the start, it nonetheless allows for and adjusts to changes and unforeseen challenges that may develop as the project cycle progresses.

Before the next sprint can begin, Agile relies on client collaboration and feedback, whereas Waterfall methodologies do not value customer collaboration until the final build is ready for testing. As each Agile sprint is completed and consumer feedback is received, the team is able to make quick changes.

Source: https://www.aipm.com.au/blog/agile-vs-waterfall-whats-the-difference
https://www.nilc.co.uk/agile-v-waterfall-project-management-methodology-what-are-the-differences-and-how-it-applies-to-the-im-a-celebrity-2020-show/


## 7. What is a reduced function used for?

When a function is applied on an iterable, the reduce() function returns an aggregated value as a result. Applying the function to the first pair of items in the iterable and using the resulting value with the following item in the sequence is repeated until item n.

To compute the sum of a list of numbers, here is an example.

So one of the ways in python is using a basic for loop:

    total = 0
    numbers = [1, 2, 3, 4]
    for num in numbers:
        total += num
    
    print(total)  # Output: 10
    
Here is another approach using reduce() now:
    
    from functools import reduce
    total = reduce((lambda x, y: x + y), [1, 2, 3, 4])
    
    print(total) # Output: 10


Source : https://python-reference.readthedocs.io/en/latest/docs/functions/reduce.html
https://book.pythontips.com/en/latest/map_filter.html


## 8. How does merge sort work

Merge Sort algorithm is based on the Divide and Conquer paradig. This algorithm divides the array into two equal parts, which are then combined in a sorted way.

The array is repeatedly divided in half until it can no longer be divided, which is how the merge sort algorithm operates. This indicates that the splitting will stop if the array runs out of space or has just one element left, which is the base case for stopping the recursion. If an array contains many elements, divide it in half and use the merge sort iteratively on each half. After sorting both halves, the merge operation is then used. 

This is an example how it works. 

    array = [ 55, 15, 33, 100, 1, 2, 8] 
    
    Step 1 : [55, 15, 33, 100] , [1, 2, 8]  First divided into two arrays of size 4 and 3 respectively
    
    Step 2 : [55] / [15] / [33] / [100] / [1] / [2] / [8] Now, keep dividing these two arrays into smaller and smaller parts until more division is impossible.
    
    Step 3 :[15, 55] / [33, 100] / [1, 2] / [8] Start merging the items once more based on comparison.
    
    Step 4 :[15, 33, 55, 100] /  [1, 2, 8] In order to combine the elements from two lists into one, you must first compare each list's elements.
    
    Step 5 :[1, 2, 8, 15, 33, 55, 100] Following the final merging, the list appears like this
Source : https://www.geeksforgeeks.org/merge-sort/

## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?


Generator is useful when a machine’s memory is incapable of working a large dataset or when you have a complex function that needs to keep an internal state, but the function is too small to create a class. 

#### Example 1 : Reading Large Files

For example, Working with huge files, such as CSV files, or data streams is a frequent application for generators to avoid MemoryError. 

    def csv_reader(file_name):
        for row in open(file_name, "r"):
            yield row
    
    # Rows are 64186394.

The file is opened, iterated over, and a row is produced. The output from this code ought to be generated without any memory errors. So, in a sense, this program has converted csv reader() into a generator function. In this variation, a file is opened, each line is iterated through, and each row is yielded rather than returned.

#### Example 2:  Generating an Infinite Sequence

Infinite sequences can also be produced using a generator. Again, since memory is limited, yield over return will prevent a computer crash as you work through an infinite sequence.

    def infinite_sequence():
        num = 0
        while True:
            yield num
            num += 1

#### Example 3: Detecting Palindromes

Generators can cycle through an unlimited series of numbers and determine whether the number created is the same forwards and backwards, making them excellent tools for palindrome detection.

Please note that the code examples are taken from the source below.

Source: https://realpython.com/introduction-to-python-generators/


## 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?

The function returns another function, usually applied as a function transformation using the @wrapper syntax. 

#### Useful use of decorators include:

Timing Functions : It will measure the time a function takes to run and print the time.
Debugging Code:  It will print the arguments and its return value every time the function is called
Slowing Down Code : It will sleep one second before it calls the decorated function. It may be useful when you want to rate-limit a function that continuously checks whether a resource, such as a web page, has changed
User Logged In: Often used with a web framework, a web page can only be visible to logged in users

#### Harmful decorators idea:

 hide a backdoor : Hiding a backdoor and a module that collects users credentials and sends the data to a remote server

Source: https://docs.python.org/3/glossary.html
https://realpython.com/primer-on-python-decorators/#timing-functions
https://www.bleepingcomputer.com/news/security/backdoored-python-library-caught-stealing-ssh-credentials/




