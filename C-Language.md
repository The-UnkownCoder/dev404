#include <stdio.h>
#include <string.h>
#include <math.h>

// Concepts of C Language
/*
1. Basic Concepts
Introduction to C Language: History, features, and applications of C.
Structure of a C Program: Functions, variables, constants, and the main() function.
Basic Input and Output: printf, scanf, file handling.
Data Types: Primitive types (int, char, float, double), user-defined types (struct, enum), and void type.

2. Variables and Constants
Variable Declaration: Naming rules, data types.
Constants: #define, const, and enum.

3. Operators
Arithmetic Operators: +, -, *, /, %.
Relational Operators: ==, !=, >, <, >=, <=.
Logical Operators: &&, ||, !.
Bitwise Operators: &, |, ^, <<, >>, ~.
Assignment Operators: =, +=, -=, *=, /=.
Increment/Decrement Operators: ++, --.
Conditional Operator: ?:.
Comma Operator: ,.
4. Control Flow Statements
Decision Making: if, else, else if, switch.
Loops: for, while, do-while.
Jump Statements: break, continue, return, goto.

5. Functions
Function Declaration and Definition: Function prototypes, function definition, and function calls.
Passing Arguments: Call by value, call by reference (using pointers).
Recursive Functions: Definition and examples.
Function Overloading (not directly supported in C but achievable via macros or different function names).

6. Arrays
One-dimensional Arrays: Declaration, initialization, and access.
Multi-dimensional Arrays: 2D arrays, 3D arrays.
String Handling: Strings as character arrays, functions from <string.h>.

7. Pointers
Pointer Basics: Declaration, initialization, dereferencing, and accessing values.
Pointer Arithmetic: Incrementing, decrementing, and comparing pointers.
Pointer to Pointer: Multi-level pointers.
Dynamic Memory Allocation: malloc(), calloc(), realloc(), free().
Function Pointers: Declaring and using pointers to functions.

8. Structures and Unions
Structures: Definition, declaration, initialization, and access to members.
Unions: Definition, difference between structures and unions.
Enums: Enumeration types and usage.
Typedef: Simplifying type names using typedef.

9. File Handling
File Operations: Opening, reading, writing, closing files.
File Pointers: fopen(), fclose(), fread(), fwrite(), fseek().
Text vs Binary Files: Difference and handling.
Error Handling: Checking for errors during file operations.

10. Memory Management
Dynamic Memory Allocation: malloc(), calloc(), realloc(), free().
Memory Leaks: How to avoid memory leaks.
Memory Access and Errors: Pointer dereferencing errors, segmentation faults.

11. Preprocessor Directives
Macros: #define, #ifdef, #ifndef, #endif.
Conditional Compilation: #if, #else, #elif.
Include Files: #include for header files.
File Inclusion: Using external libraries and custom header files.

12. Error Handling and Debugging
Error Handling: Using errno, perror(), and strerror().
Assertions: assert() for runtime checks.
Debugging Tools: Using gdb or lldb for debugging.
Logging: Basic logging mechanisms.

13. Advanced Concepts
Bit Fields: Using bit-level operations to define variables that hold specific bits of data.
Memory-Mapped I/O: Using pointers for direct memory access in embedded systems.
Concurrency and Multithreading: Basics of multithreading in C using pthread.
Linked Lists: Singly and doubly linked lists, basic operations like insertion, deletion, and traversal.
Stack and Queue: Implementations of stack and queue using arrays or linked lists.
Trees: Binary trees, binary search trees, tree traversal algorithms (in-order, pre-order, post-order).
Graphs: Representation of graphs using adjacency matrix/list, graph traversal (BFS, DFS).

14. Compiler and Linking
Compilation Process: Preprocessing, compilation, assembly, and linking.
Linking: Static linking and dynamic linking.
Header Files: How to create and use custom header files.

15. Algorithms
Sorting Algorithms: Bubble sort, selection sort, insertion sort, quicksort, mergesort.
Searching Algorithms: Linear search, binary search.
Graph Algorithms: BFS, DFS, Dijkstra’s algorithm, Bellman-Ford.
Dynamic Programming: Solving problems using dynamic programming techniques (e.g., Fibonacci series, knapsack problem).
Divide and Conquer: Examples and techniques for solving problems using divide and conquer.
Greedy Algorithms: Approach for optimization problems (e.g., coin change problem, activity selection).

16. Miscellaneous Topics
Command-Line Arguments: How to process command-line arguments using argc and argv.
Preprocessor Macros: Usage of macros for code optimization, conditional compilation, and inline functions.
Volatile Keyword: When and why to use volatile for variables.
Const Keyword: Using const for read-only variables and pointer constness.

17. Best Practices
Code Optimization: Efficient coding practices, minimizing time and space complexity.
Code Readability: Writing clean, understandable, and maintainable code.
Memory Management: Proper allocation and deallocation of memory, avoiding memory leaks.
Modular Programming: Using functions, header files, and libraries to organize code.

18. C Standard Library
Standard I/O Library: stdio.h functions like printf(), scanf(), fopen(), etc.
String Library: Functions for string manipulation from string.h.
Math Library: Functions for mathematical operations from math.h.
Time Library: Functions to work with time from time.h.
Standard Library Utilities: Functions from stdlib.h like malloc(), free(), qsort(), atoi(), etc.

19. C Programming in Embedded Systems
Embedded Systems Basics: Introduction to programming for microcontrollers and embedded systems using C.
Interrupts: Basics of interrupts handling in C for embedded programming.
Real-time Operating Systems (RTOS): Basics of RTOS, task scheduling, and real-time programming in C.
*/

//1.Variables and Identifiers
/*
A variable in C is a storage location identified by a name and can store data. It must be declared with a specific type before being used. The declaration tells the compiler what kind of data the variable will store, so it can allocate the necessary amount of memory.
Syntax for Variable Declaration:
data_type variable_name;
Naming Rules for Variables:
A variable name must start with a letter (A-Z or a-z) or an underscore (_).
After the first character, the name can include digits (0-9), letters, and underscores.
Variable names are case-sensitive (variable is different from Variable).
Reserved keywords (e.g., int, return, if) cannot be used as variable names.
Variable names cannot contain spaces.
The length of the variable name can be arbitrarily long, but some compilers may impose limits.

Examples of valid variable names:
int age;
float salary;
char name[50];

Examples of invalid variable names:
int 1stName;  // Starts with a digit
int my-name;  // Contains hyphen (-)
int int;

Types of Variables

Local Variables:
Declared inside a function or a block.
Accessible only within the function or block.
Not initialized by default.
void func() {
    int num = 5; // Local variable
    printf("%d", num);
}

Global Variables:
Declared outside all functions.
Accessible throughout the program.
Initialized to zero by default if not explicitly initialized.
int count = 0; // Global variable
void func() {
    printf("%d", count);
}

Static Variables:
Retain their value across multiple function calls.
Declared with the static keyword.
void func() {
    static int counter = 0; // Static variable
    counter++;
    printf("%d", counter);
}

Automatic Variables:
Default type for local variables.
Declared with the auto keyword (rarely used explicitly).
void func() {
    auto int num = 10; // Automatic variable
    printf("%d", num);
}

External Variables:
Declared with the extern keyword to reference global variables defined in another file or location.
extern int count; // Reference to a global variable

Identifiers in C
Definition
Identifiers are the names used to identify variables, functions, arrays, or other user-defined elements in a C program.

Rules for Naming Identifiers
Can consist of letters (A-Z, a-z), digits (0-9), and underscores (_).
Must begin with a letter or an underscore.
Cannot use C reserved keywords (e.g., int, return, if).
Case-sensitive (count and Count are different).
Cannot include spaces or special characters (e.g., @, $, %).

Examples of Valid Identifiers
int age;
float total_salary;
char _grade;

Examples of Invalid Identifiers
int 1age;       // Starts with a digit
float total-salary; // Contains hyphen
char char;      // 'char' is a keyword
*/

//2.Constants
/*
1.#define
The #define preprocessor directive is used to define constants or macros. It is commonly used for defining constants that are used throughout a program.
#define CONSTANT_NAME value
CONSTANT_NAME is the name of the constant.
value is the value that the constant represents.
Example:
#define PI 3.14159
#define MAX_SIZE 100

float area = PI * radius * radius;
int arr[MAX_SIZE];
Advantages:

#define constants are replaced by the preprocessor before the actual compilation starts.
It allows for more readable code by using meaningful names for constants.

Limitations:
No type safety (the constant is just replaced by its value).
Cannot be debugged as easily as const.

2.const
The const keyword is used to define variables whose values cannot be changed after initialization. Unlike #define, const can be used with data types and allows for type checking.
Syntax:
const data_type CONSTANT_NAME = value;
Example:
const float pi = 3.14159;
const int maxSize = 100;
pi = 3.14; // Error: cannot modify a constant

Advantages:
Type-safe, as it is associated with a specific data type.
Supports debugging and can be used for any variable, not just simple constants.

Limitations:
Its value cannot be changed once set, but unlike #define, it is still a variable, and memory is allocated for it.

3.enum
An enum (short for "enumeration") defines a set of named integer constants. It is used when you want to assign symbolic names to a set of values.
Syntax:
enum enum_name {
    CONSTANT1,
    CONSTANT2,
    CONSTANT3,
    ...
};
By default, the first constant in an enum has a value of 0, and each subsequent constant is incremented by 1.

Example:
enum Week { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
enum Week today = Wednesday;
if (today == Wednesday) {
    printf("Today is Wednesday\n");
}

Advantages:
Provides a more readable and meaningful way to represent integers with symbolic names.
Can be used for flags and state machine implementations.
You can manually set the value of constants within the enum.
Example with manual values:
enum ErrorCode { OK = 0, WARNING = 1, ERROR = 2 };

Limitations:
In C, enum constants are always treated as integer values.

Key Differences:
#define: Used for simple constants or macros. No type checking.
const: Defines a constant with a specific data type. Type-safe and debuggable.
enum: Defines a set of named constants, mainly used for handling sets of related values.

//3.Keywords
/*
auto  
break  
case  
char  
const  
continue  
default  
do  
double  
else  
enum  
extern  
float  
for  
goto  
if  
inline  
int  
long  
register  
restrict  
return  
short  
signed  
sizeof  
static  
struct  
switch  
typedef  
union  
unsigned  
void  
volatile  
while  
_Bool  
_Complex  
_Imaginary  
*/

//4.Data Types
/*
Basic Data Types:
int: Used to store integers (whole numbers).
Example: int age = 25;

char: Used to store a single character.
Example: char letter = 'A';

float: Used to store single-precision floating-point numbers (decimals).
Example: float height = 5.75;

double: Used to store double-precision floating-point numbers (decimals with more precision).
Example: double pi = 3.14159;

void: Represents the absence of a value (used for functions that do not return a value).

Modifiers:
short: A shorter version of int, usually occupying 2 bytes.
Example: short int num = 10;

long: A longer version of int, usually occupying 4 bytes or more.
Example: long int population = 1000000000;

unsigned: An unsigned version of integer types (does not allow negative numbers).
Example: unsigned int positiveNum = 100;

signed: The default for integers, can hold both negative and positive values.

char - 1  
signed char - 1  
unsigned char - 1  
short - 2  
signed short - 2  
unsigned short - 2  
int - 4  
signed int - 4  
unsigned int - 4  
long - 4 or 8  
signed long - 4 or 8  
unsigned long - 4 or 8  
long long - 8  
signed long long - 8  
unsigned long long - 8  
float - 4  
double - 8  
long double - 8, 12, or 16  
_Bool - 1
*/

//5.Operators
/*
1. Arithmetic Operators:
+ - * / %

2. Relational Operators:
== != > < >= <=

3. Logical Operators:
&& || !

4. Bitwise Operators:
& | ^ ~ << >>

5. Assignment Operators:
= += -= *= /= %= &= |= ^= <<= >>=

6. Increment and Decrement Operators:
++ --

7. Conditional (Ternary) Operator:
? :
Definition
The ternary operator, also known as the conditional operator, is a shorthand way of writing an if-else statement in a single line. It is represented by the symbols ? :.
condition ? expression1 : expression2;
condition: An expression that evaluates to true or false.
expression1: Executed if the condition is true.
expression2: Executed if the condition is false.
#include <stdio.h>
int main() {
    int a = 10, b = 20;
    int max;

    // Using the ternary operator
    max = (a > b) ? a : b;

    printf("The maximum value is: %d\n", max);
    return 0;
}

Output:
The maximum value is: 20

How It Works
The condition (a > b) is evaluated.
If a > b is true, the value of a is assigned to max.
If a > b is false, the value of b is assigned to max.

Use Cases
Finding the maximum or minimum of two numbers:
int min = (x < y) ? x : y;

Checking even or odd:
printf("%d is %s\n", num, (num % 2 == 0) ? "even" : "odd");

Assigning values conditionally:
int eligibility = (age >= 18) ? 1 : 0;

Advantages
Concise and readable for simple conditions.
Reduces the need for multiple lines of code for basic conditional operations.

Disadvantages
Can become hard to read if overused or nested.

Nested Ternary Operators
You can nest ternary operators, but it may reduce readability:
int result = (x > y) ? ((x > z) ? x : z) : ((y > z) ? y : z);

Explanation:
Checks if x > y:
If true, compares x with z.
If false, compares y with z.

8. Comma Operator:
,

9. Sizeof Operator:
sizeof

10. Pointer Operators:
* &

11. Member and Structure Operators:
. ->

12. Type Cast Operator:
(type)

13. Special Operators:
[] () {}
*/

//4.Conditional Statements
/*
1. if Statement
if (condition) {
    // code to execute if condition is true
}

2. if-else Statement
if (condition) {
    // code to execute if condition is true
} else {
    // code to execute if condition is false
}


3. if-else if-else Ladder
if (condition1) {
    // code to execute if condition1 is true
} else if (condition2) {
    // code to execute if condition2 is true
} else {
    // code to execute if none of the conditions are true
}


4. Nested if Statement
if (condition1) {
    if (condition2) {
        // code to execute if both condition1 and condition2 are true
    }
}


5. switch Statement
switch (expression) {
    case value1:
        // code to execute if expression == value1
        break;
    case value2:
        // code to execute if expression == value2
        break;
    // add more cases as needed
    default:
        // code to execute if none of the cases match
}
*/

//6.Loop Control Statements
/*
1. for Loop
for (initialization; condition; increment/decrement) {
    // Code to execute
}

2. while Loop
while (condition) {
    // Code to execute
}

3. do-while Loop
do {
    // Code to execute
} while (condition);

4. break Statement (to exit a loop)
if (condition) {
    break;
}

5. continue Statement (to skip the current iteration and continue with the next)
if (condition) {
    continue;
}
*/

//7.Functions
/*
1. Based on Return Type
Functions with No Return Type (void)
These functions do not return any value.
void functionName(parameters) {
    // Function body
}
void printMessage() {
    printf("Hello, World!");
}

Functions with Return Type
These functions return a specific value of a defined type (e.g., int, float, char).
returnType functionName(parameters) {
    // Function body
    return value;
}
int add(int a, int b) {
    return a + b;
}

2. Based on Parameters
Functions with No Parameters
These functions do not take any arguments.
returnType functionName() {
    // Function body
}
void greet() {
    printf("Good morning!");
}

Functions with Parameters
These functions take one or more arguments as input.
returnType functionName(type parameter1, type parameter2, ...) {
    // Function body
}

float multiply(float a, float b) {
    return a * b;
}

3. Based on Call Method
Call by Value
Only a copy of the argument is passed to the function; changes do not affect the original value.
void update(int x) {
    x = x + 10;
}

Call by Reference
The address of the argument is passed to the function; changes affect the original value.
void update(int *x) {
    *x = *x + 10;
}

4. Based on Function Type
Library Functions
Predefined functions provided by C libraries, e.g., printf, scanf, strlen.
printf("Hello, World!");

User-defined Functions
Functions created by the user for specific tasks.
int square(int n) {
    return n * n;
}

5. Recursive Functions
A function that calls itself directly or indirectly.
int factorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}

6. Inline Functions
Functions that are expanded in place of a call during compilation (suggested with inline keyword).
inline int max(int a, int b) {
    return (a > b) ? a : b;
}

*/

//8.Types Of Scopes
/*
1. Block Scope
Definition: A variable declared inside a block (typically inside a pair of curly braces {}) has block scope.
Access: The variable is only accessible within the block in which it is declared. Once the block ends, the variable is destroyed.
#include <stdio.h>
int main() {
    int a = 5;  // a has block scope
    if (a > 0) {
        int b = 10;  // b has block scope inside the if statement
        printf("b = %d\n", b);
    }
    // printf("b = %d\n", b); // This would cause an error because b is out of scope
    return 0;
}

2. Function Scope
Definition: A variable declared inside a function has function scope.
Access: The variable is only accessible within the function, even if declared outside of any block in the function (but still inside the function body).
#include <stdio.h>
void myFunction() {
    int a = 5;  // a has function scope
    printf("a = %d\n", a);
}
// printf("a = %d\n", a); // This would cause an error because a is out of scope of the function

3. File Scope (Global Scope)
Definition: A variable declared outside of all functions (typically at the top of the file) has file (or global) scope.
#include <stdio.h>
int a = 5;  // a has file (global) scope
void myFunction() {
    printf("a = %d\n", a);  // Can access a because it's in file scope
}
int main() {
    myFunction();
    return 0;
}

4. Function Prototype Scope
Definition: Variables declared within a function prototype or function declaration are only valid within the prototype, and their scope is limited to the declaration.
Access: They are not accessible in the function body.
#include <stdio.h>
void myFunction(int a);  // a has function prototype scope

int main() {
    myFunction(5);
    return 0;
}

void myFunction(int a) {  // a is accessible here
    printf("a = %d\n", a);
}

5. Parameter Scope
Definition: Function parameters have their own scope, and they are only accessible within the function in which they are declared.
Access: They are local to the function and cannot be accessed outside of the function.
#include <stdio.h>
void myFunction(int x) {  // x has parameter scope
    printf("x = %d\n", x);
}

int main() {
    int a = 10;
    myFunction(a);  // Passing argument to function
    return 0;
}

6. Extern (Global) Scope
Definition: Variables declared with the extern keyword are used to refer to variables defined outside the current file or function. They are typically used in multi-file projects.
Access: The variable is accessible across files, but it must be defined elsewhere in the program.
// File 1 (file1.c)
#include <stdio.h>
extern int a;  // a is declared as an external variable
void printA() {
    printf("a = %d\n", a);
}

int main() {
    printA();
    return 0;
}

// File 2 (file2.c)
int a = 10;  // a is defined in another file
*/

// Searching and Sorting
/*

*/

//9.Pointers : A variable that stores the memory address of another variable
/*
1. Declaring Pointers
To declare a pointer, use the * symbol to indicate it is a pointer.
int *ptr;  // Pointer to an integer
char *ptr2;  // Pointer to a character

2. Initializing Pointers
A pointer is usually initialized with the address of a variable using the & operator.
int num = 10;
int *ptr = &num;  // Pointer ptr holds the address of num

3. Dereferencing a Pointer
Dereferencing means accessing the value at the address stored by the pointer using the * operator.
int num = 10;
int *ptr = &num;
printf("%d\n", *ptr);  // Output: 10

4. Pointer Arithmetic
Incrementing: When a pointer is incremented, it moves to the next memory location of the data type it points to.
int arr[] = {10, 20, 30};
int *ptr = arr;  // ptr points to arr[0]
ptr++;  // Now ptr points to arr[1]
Decrementing: Similarly, decrementing a pointer moves it to the previous memory location.
ptr--;  // Now ptr points to arr[0]

Pointer Arithmetic Example:
int arr[] = {10, 20, 30};
int *ptr = arr;
printf("%d\n", *ptr);  // Output: 10
ptr++;
printf("%d\n", *ptr);  // Output: 20

5. Pointer Comparison
Pointers can be compared using relational operators. This compares the memory addresses they store.
int a = 5, b = 10;
int *ptr1 = &a, *ptr2 = &b;

if(ptr1 == ptr2) {
    printf("Pointers are the same\n");
} else {
    printf("Pointers are different\n");
}

6. Passing Pointers to Functions
Pointers can be passed to functions to modify the original variable's value (pass-by-reference).
void modify(int *ptr) {
    *ptr = 20;  // Modify the value of the original variable
}

int main() {
    int num = 10;
    modify(&num);
    printf("%d\n", num);  // Output: 20
    return 0;
}

7. Pointer to Pointer
A pointer to a pointer is used when you need to store the address of another pointer.
int num = 10;
int *ptr = &num;
int **ptr2 = &ptr;  // Pointer to pointer
printf("%d\n", **ptr2);  // Output: 10

8. Array of Pointers
You can create an array where each element is a pointer to a variable.
int num1 = 10, num2 = 20, num3 = 30;
int *arr[] = {&num1, &num2, &num3};
printf("%d\n", *arr[1]);  // Output: 20 (points to num2)

9. Dynamic Memory Allocation with Pointers
malloc():
Allocates a block of memory of a specified size and returns a pointer to it.
int *ptr = (int*) malloc(sizeof(int));  // Allocate memory for one integer
if(ptr == NULL) {
    printf("Memory allocation failed\n");
}
*ptr = 10;  // Set the value at the allocated memory

free():
Frees the dynamically allocated memory.
free(ptr);  // Frees the memory pointed to by ptr

calloc():
Allocates memory for an array of elements and initializes all bytes to zero.
int *ptr = (int*) calloc(5, sizeof(int));  // Allocate memory for 5 integers

realloc():
Resizes a previously allocated memory block.
int *ptr = (int*) realloc(ptr, 10 * sizeof(int));  // Resize to hold 10 integers

10. NULL Pointer
A NULL pointer is a pointer that does not point to any valid memory address. It is typically used to initialize pointers.
int *ptr = NULL;  // Pointer is initialized to NULL
if(ptr == NULL) {
    printf("Pointer is NULL\n");
}

11. Function Pointers
A function pointer points to a function instead of a data variable. This is used in callbacks and dynamic function calls.
void myFunction(int x) {
    printf("Value: %d\n", x);
}

int main() {
    void (*funcPtr)(int) = &myFunction;  // Function pointer
    funcPtr(10);  // Call the function through the pointer
    return 0;
}

void calculate(int a, int b, int c, int *sum, int *product, int *average) {
    *sum = a + b + c;
    *product = a * b * c;
    *average = (a + b + c)/3;
}

int main() {
    int age=22;
    int *ptr = &age;
    int **pptr = &ptr;
    int _age = *ptr;
    int __age = **pptr;

    printf("%d %d %d %d\n", age, ptr, _age, __age);

    int i = 5;
    int *iptr = &i;
    int **ipptr = &iptr;

    printf("%d", **ipptr);

    int a = 3, b = 5, c = 6;
    int sum, product, average;
    calculate(a, b, c, &sum, &product, &average);
    printf("%d %d %d", sum, product, average);
    return 0;
}
*/

//10.DMA
/*
Dynamic Memory Allocation in C allows programs to allocate memory at runtime (while the program is running) rather than at compile-time. This flexibility is useful when you don't know the exact amount of memory you will need until the program is running, or when the memory size is dependent on user input, system conditions, or other factors.

In C, dynamic memory allocation is managed via the standard library functions defined in <stdlib.h>. These functions allow you to request, free, and resize memory blocks during program execution.

Key Functions for Dynamic Memory Allocation:
malloc(): Allocates a block of memory of a specified size.
calloc(): Allocates a block of memory for an array of elements and initializes all bytes to zero.
realloc(): Resizes an already allocated memory block.
free(): Deallocates memory previously allocated by malloc(), calloc(), or realloc().
1. malloc() - Memory Allocation
malloc() (Memory Allocation) allocates a specified number of bytes in memory. It returns a pointer to the allocated memory, or NULL if the allocation fails.

Syntax:

c
Copy code
void* malloc(size_t size);
size: The number of bytes to allocate.
Example:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    // Allocating memory for 5 integers
    arr = (int*) malloc(n * sizeof(int));

    // Check if malloc was successful
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Assign values to the allocated memory
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    // Print the values
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Free the allocated memory
    free(arr);

    return 0;
}
2. calloc() - Contiguous Memory Allocation
calloc() (Contiguous Allocation) allocates memory for an array of num elements of size size and initializes all bits to zero. It is often used when you need an array and want the elements to be initialized to zero.

Syntax:

c
Copy code
void* calloc(size_t num, size_t size);
num: The number of elements.
size: The size of each element.
Example:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    // Allocating memory for 5 integers and initializing to 0
    arr = (int*) calloc(n, sizeof(int));

    // Check if calloc was successful
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Print the values (all will be initialized to 0)
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Free the allocated memory
    free(arr);

    return 0;
}
3. realloc() - Reallocation of Memory
realloc() is used to resize a previously allocated memory block. If there is already a block of memory, realloc() will change its size while keeping the original data intact (if the size increases).

Syntax:

c
Copy code
void* realloc(void* ptr, size_t new_size);
ptr: Pointer to the previously allocated memory block.
new_size: New size in bytes for the memory block.
Example:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    // Allocating memory for 5 integers
    arr = (int*) malloc(n * sizeof(int));

    // Check if malloc was successful
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Assign values to the allocated memory
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    // Print the values
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Resize the memory block to hold 10 integers
    n = 10;
    arr = (int*) realloc(arr, n * sizeof(int));

    // Check if realloc was successful
    if (arr == NULL) {
        printf("Memory reallocation failed\n");
        return 1;
    }

    // Assign new values to the reallocated memory
    for (int i = 5; i < n; i++) {
        arr[i] = i + 1;
    }

    // Print all the values
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Free the allocated memory
    free(arr);

    return 0;
}
4. free() - Memory Deallocation
The free() function is used to deallocate memory that was previously allocated with malloc(), calloc(), or realloc(). It takes the pointer to the allocated memory as an argument.

Syntax:

c
Copy code
void free(void* ptr);
ptr: Pointer to the memory to be freed.
Example of Memory Leak Prevention:
Not freeing memory can lead to a memory leak, where the program consumes more and more memory over time. To prevent this, always free dynamically allocated memory after you're done using it.

Example of Freeing Memory:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    // Allocating memory
    arr = (int*) malloc(n * sizeof(int));

    // Use the memory...

    // Free the memory once done
    free(arr);

    return 0;
}
Notes on Dynamic Memory Allocation:
Memory Allocation Failure: Always check if the memory allocation was successful. If malloc(), calloc(), or realloc() fails, they return NULL.
Accessing Freed Memory: After freeing a pointer, do not use it unless it has been reallocated. This can cause undefined behavior.
Memory Leaks: If dynamically allocated memory is not freed, it leads to memory leaks, which may cause the program or system to run out of memory.
Pointer Validity: After using realloc(), the pointer returned might be different from the original one, so always use the result of realloc() for subsequent memory accesses.
*/

//11.File Handling
/*
File handling in C allows you to read from, write to, and manipulate files on your system. In C, the standard library provides functions for performing file operations, such as opening, closing, reading, writing, and more. These functions are defined in the <stdio.h> header file.

Here's a breakdown of the essential file-handling operations in C:

1. Opening a file
To open a file, you use the fopen() function. This function takes two parameters: the filename and the mode in which you want to open the file.

c
Copy code
FILE *fopen(const char *filename, const char *mode);
Common modes:

"r": Read mode (opens for reading, file must exist).
"w": Write mode (opens for writing, creates a new file or truncates an existing one).
"a": Append mode (opens for appending, creates a new file if it doesn't exist).
"r+": Read/Write mode (opens for both reading and writing, file must exist).
"w+": Write/Read mode (opens for both writing and reading, creates or truncates the file).
"a+": Append/Read mode (opens for both appending and reading, creates the file if it doesn't exist).
2. Reading from a file
There are several functions for reading data from a file:

fgetc(FILE *stream): Reads a single character from the file.
fgets(char *str, int n, FILE *stream): Reads a line (up to n-1 characters) from the file.
fread(void *ptr, size_t size, size_t count, FILE *stream): Reads count elements of size size into the buffer ptr.
Example of reading a file:

c
Copy code
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("Could not open file\n");
        return 1;
    }

    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch); // Print character to console
    }

    fclose(file); // Always close the file
    return 0;
}
3. Writing to a file
To write data to a file, you can use the following functions:

fputc(int char, FILE *stream): Writes a single character to the file.
fputs(const char *str, FILE *stream): Writes a string to the file.
fwrite(const void *ptr, size_t size, size_t count, FILE *stream): Writes count elements of size size from ptr to the file.
Example of writing to a file:

c
Copy code
#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Could not open file for writing\n");
        return 1;
    }

    fprintf(file, "Hello, World!\n"); // Write formatted data
    fputs("This is another line.\n", file); // Write a string

    fclose(file); // Close the file after writing
    return 0;
}
4. Closing a file
Once you are done working with a file, you should always close it using the fclose() function:

c
Copy code
int fclose(FILE *stream);
5. Error Handling
To check for errors during file operations, you can use ferror() and feof():

ferror(FILE *stream): Returns a non-zero value if an error occurs on the stream.
feof(FILE *stream): Returns a non-zero value if the end of the file has been reached.
Example: Reading and writing with error checking
c
Copy code
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "r");
    if (file == NULL) {
        perror("Error opening file"); // Prints the error message
        return 1;
    }

    char buffer[100];
    if (fgets(buffer, 100, file) != NULL) {
        printf("Read from file: %s", buffer);
    } else {
        if (feof(file)) {
            printf("End of file reached\n");
        } else if (ferror(file)) {
            perror("Error reading from file");
        }
    }

    fclose(file); // Always close the file
    return 0;
}
6. Random Access File Operations
To perform random access (seek and move within a file), you can use the following functions:

fseek(FILE *stream, long offset, int whence): Moves the file pointer to a new position.
ftell(FILE *stream): Returns the current position of the file pointer.
rewind(FILE *stream): Moves the file pointer back to the beginning.
Example: Random Access
c
Copy code
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("Could not open file\n");
        return 1;
    }

    fseek(file, 5, SEEK_SET); // Move the file pointer 5 bytes from the beginning
    char ch = fgetc(file);    // Read the character at the current position
    printf("Character at position 5: %c\n", ch);

    fclose(file);
    return 0;
}
7. File Existence Check
Before opening a file, you can check if it exists using the access() function from <unistd.h> (in UNIX-like systems):

c
Copy code
#include <unistd.h>

if (access("example.txt", F_OK) != -1) {
    // File exists
} else {
    // File doesn't exist
}
*/

//12.Array
/*
1. Definition
An array is a collection of variables of the same data type that are accessed using a single name and an index.

2. Syntax
data_type array_name[size];
data_type: Type of elements (e.g., int, float, char).
array_name: Name of the array.
size: Number of elements in the array.

3. Types of Arrays
One-Dimensional Array
Stores a list of elements.
Example:
int numbers[5] = {1, 2, 3, 4, 5};
Access elements using the index:
printf("%d", numbers[0]); // Outputs 1

Two-Dimensional Array
Represents a table or matrix.
Example:
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

Access elements using row and column indices:
printf("%d", matrix[1][2]); // Outputs 6

Multi-Dimensional Array
Represents more complex structures like 3D data.
Example:
int cube[2][2][2] = {
    {{1, 2}, {3, 4}},
    {{5, 6}, {7, 8}}
};

Character Array (String)
Used to store sequences of characters.
Example:
char str[10] = "Hello";
Strings are null-terminated in C.

4. Array Initialization
During Declaration
int arr[3] = {1, 2, 3};

Partial Initialization
Uninitialized elements are set to 0.
int arr[5] = {1, 2}; // Rest are set to 0
Using Loops
for (int i = 0; i < 5; i++) {
    arr[i] = i + 1;
}

5. Operations on Arrays

Accessing Elements
printf("%d", arr[2]); // Accesses the third element

Traversing
Use loops to iterate over all elements.
for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
}

Insertion
Assign a value to an index.
arr[2] = 10; // Inserts 10 at the third position

Searching
Linear or binary search can be used.
for (int i = 0; i < size; i++) {
    if (arr[i] == value) {
        printf("Found at index %d", i);
    }
}

Sorting
Sort elements using algorithms like Bubble Sort, Quick Sort, etc.
for (int i = 0; i < size - 1; i++) {
    for (int j = i + 1; j < size; j++) {
        if (arr[i] > arr[j]) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}

Deletion
Set an element to 0 or shift remaining elements.
for (int i = pos; i < size - 1; i++) {
    arr[i] = arr[i + 1];
}
size--;

6. Advantages of Arrays
Efficient memory usage.
Allows random access to elements using indices.
Simplifies code for operations like sorting and searching.

7. Limitations of Arrays
Fixed size: Cannot change size dynamically.
Stores elements of the same data type.
Inefficient for insertion and deletion (requires shifting).

8. Important Concepts
Indexing
Array indices start from 0.
For arr[n], valid indices are 0 to n-1.

Pointer Relation
The name of the array is a pointer to its first element.
printf("%p", arr); // Address of the first element

Passing Arrays to Functions
Pass by reference using pointers.
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

Dynamic Arrays
Use malloc or calloc for dynamic memory allocation.
int* arr = (int*)malloc(size * sizeof(int));

9. Applications of Arrays
Storing data in bulk (e.g., scores, marks, names).
Implementing data structures like stacks, queues, and matrices.
Used in algorithms like sorting, searching, and graph traversal.

*/

//13.String
/*
1. Declaring Strings
Syntax: char string_name[size];
size: The maximum number of characters the string can hold, including the null character (\0).
char name[20]; // Declares a string of size 20
char greeting[] = "Hello"; // Declares and initializes a string
Notes:
Strings must always include space for the null character (\0).
Strings can also be defined using a pointer: char *name = "John"; // Stored in read-only memory

2. Input and Output with Strings
Using scanf and printf:
char name[50];
printf("Enter your name: ");
scanf("%s", name);
printf("Hello, %s\n", name);
Limitation: Stops reading at whitespace.

Using fgets:
fgets(name, sizeof(name), stdin); // Reads a string, including spaces

Using puts:
puts(name); // Prints the string and adds a newline

3. String Initialization
char str1[] = "Hello"; // Automatically includes \0
char str2[6] = "Hello"; // Includes \0
char str3[10] = {'H', 'e', 'l', 'l', 'o', '\0'}; // Explicit \0

4. String Functions in <string.h>
strlen: Returns the length of a string (excluding \0). Example: int len = strlen(str);
strcpy: Copies one string into another. Example: strcpy(dest, src);
strncpy: Copies a limited number of characters. Example: strncpy(dest, src, n);
strcmp: Compares two strings (0 if equal). Example: if (strcmp(str1, str2) == 0)
strncmp: Compares the first n characters of two strings. Example: strncmp(str1, str2, n);
strcat: Concatenates two strings. Example: strcat(dest, src);
strncat: Concatenates up to n characters. Example: strncat(dest, src, n);
strchr: Finds the first occurrence of a character. Example: char *pos = strchr(str, 'a');
strrchr: Finds the last occurrence of a character. Example: char *pos = strrchr(str, 'a');
strstr: Finds the first occurrence of a substring. Example: char *pos = strstr(str, "sub");
strtok: Tokenizes a string based on delimiters. Example: token = strtok(str, " ");
memset: Sets all bytes in a string to a specific character. Example: memset(str, '-', strlen(str));

5. String Manipulation Without <string.h>
Length Calculation:
int length = 0;
while (str[length] != '\0') {
    length++;
}

String Comparison:
int compareStrings(char *str1, char *str2) {
    while (*str1 && *str1 == *str2) {
        str1++;
        str2++;
    }
    return *str1 - *str2;
}

String Copy:
void copyString(char *dest, char *src) {
    while ((*dest++ = *src++));
}

6. String Concatenation
char str1[50] = "Hello";
char str2[] = " World";
strcat(str1, str2); // str1 becomes "Hello World"

7. Tokenizing Strings (strtok)
Used to split strings into tokens based on delimiters.
char str[] = "Hello,World,C";
char *token = strtok(str, ",");
while (token != NULL) {
    printf("%s\n", token);
    token = strtok(NULL, ",");
}

8. Multidimensional Strings
Used to store multiple strings.
char names[3][20] = {"Alice", "Bob", "Charlie"};
printf("First name: %s\n", names[0]);

9. Common String Errors
Buffer Overflow: Ensure the array is large enough to hold the string and \0.
Dangling Pointers: Avoid using pointers to strings that are out of scope.
Null Character Handling: Always terminate strings with \0.

10. String and Pointer Relationship
Strings can be accessed and manipulated using pointers.
char str[] = "Hello";
char *ptr = str;
while (*ptr != '\0') {
    printf("%c", *ptr);
    ptr++;
}

11. Strings vs Character Arrays
Null Termination: Strings must be terminated by \0. Character arrays may or may not be.
Initialization: Strings can be directly initialized, while arrays need explicit initialization.
Library Functions: <string.h> functions apply to strings only.

12. Advanced Topics
Dynamic String Allocation:
char *str = malloc(100 * sizeof(char));
strcpy(str, "Dynamic Memory");
free(str);
Immutable String Literals:
Strings like char *str = "Hello"; are stored in read-only memory and should not be modified.

int main() {
    char choice, ch;
    choice = getchar();
    printf("%c\n", choice);

    while(getchar() != '\n');

    scanf(" %c", &ch);
    printf("%c\n", ch);

    char name[] = {'S', 'H', 'I', 'V', 'A', 'M', '\0'};
    printf("%s\n", &name);
    
    char Name[20];
    scanf(" %s", &Name);
    printf("%s\n", &Name);
    getchar();

    char FullName[20];
    fgets(FullName, 20, stdin);
    
    // Remove newline character if present
    FullName[strcspn(FullName, "\n")] = '\0';
    printf("%s", FullName);
    return 0;''
}
*/

//14.Recursion
/*
Syntax
return_type function_name(parameters) {
    if (base_case_condition) {
        // Base case: directly return a value.
        return base_case_value;
    } else {
        // Recursive case: call the function itself.
        return function_name(modified_parameters);
    }
}
*/

//15.Structure
/*
1. What is a Structure in C?
A structure in C is a user-defined data type that allows you to combine data items of different types into a single unit. Structures are commonly used to represent real-world entities that have multiple attributes.

Structure Syntax:
c
Copy code
struct StructureName {
    dataType member1;
    dataType member2;
    // ... other members
};

2. Declaring and Using Structures:
You can define a structure and declare a variable of that structure type in the following way:

Example 1: Simple Structure Declaration and Access
#include <stdio.h>

// Define a structure to hold a point with x and y coordinates
struct Point {
    int x;
    int y;
};

int main() {
    // Declare a structure variable
    struct Point p1;

    // Assign values to members of the structure
    p1.x = 10;
    p1.y = 20;

    // Accessing the structure members and printing them
    printf("Point p1: (%d, %d)\n", p1.x, p1.y);

    return 0;
}
Explanation:
Structure Definition: struct Point defines a structure with two members x and y, both of type int.
Structure Variable: p1 is a variable of type struct Point.
Accessing Members: p1.x and p1.y are used to assign values and print them.

3. Structure Initialization
Structures can be initialized at the time of declaration, just like arrays.

Example 2: Initializing a Structure at Declaration
#include <stdio.h>

// Define a structure to hold student information
struct Student {
    char name[50];
    int age;
    float gpa;
};

int main() {
    // Declare and initialize a structure variable
    struct Student s1 = {"Alice", 20, 3.8};

    // Access and print the structure members
    printf("Name: %s\n", s1.name);
    printf("Age: %d\n", s1.age);
    printf("GPA: %.2f\n", s1.gpa);

    return 0;
}
Explanation:
Initialization: The structure s1 is initialized with "Alice", 20, and 3.8 for name, age, and gpa, respectively.
Accessing Members: The values are then printed out using s1.name, s1.age, and s1.gpa.

4. Structures with Nested Structures
A structure can contain another structure as a member. This is called a nested structure.

Example 3: Using Nested Structures
#include <stdio.h>

// Define a structure to hold address information
struct Address {
    char street[100];
    char city[50];
    int postalCode;
};

// Define a structure for Person with a nested Address structure
struct Person {
    char name[50];
    int age;
    struct Address address;  // Nested structure
};

int main() {
    // Declare and initialize a Person structure
    struct Person p1 = {"John Doe", 30, {"123 Main St", "Springfield", 12345}};

    // Access and print the structure members
    printf("Name: %s\n", p1.name);
    printf("Age: %d\n", p1.age);
    printf("Address: %s, %s, %d\n", p1.address.street, p1.address.city, p1.address.postalCode);

    return 0;
}
Explanation:
Nested Structure: The Person structure contains an instance of the Address structure as a member (address).
Accessing Nested Members: You access the nested structure members using p1.address.street, p1.address.city, and p1.address.postalCode.

5. Structure with Pointers
You can also have pointers to structures. This is helpful when passing structures to functions efficiently.

// Define a structure to represent a rectangle
struct Rectangle {
    int width;
    int height;
};

// Function to calculate area of the rectangle (using structure pointer)
int calculateArea(struct Rectangle *rect) {
    return rect->width * rect->height;
}

int main() {
    // Declare and initialize a structure variable
    struct Rectangle rect = {10, 20};

    // Pass the structure variable to the function using a pointer
    printf("Area of rectangle: %d\n", calculateArea(&rect));

    return 0;
}
Explanation:
Pointer to Structure: The function calculateArea() receives a pointer to a struct Rectangle.
Accessing Members: The -> operator is used to access members of the structure through the pointer (rect->width, rect->height).

6. typedef and Structures
You can use typedef to define a shorthand for a structure, making it easier to declare structure variables.

Example 5: Using typedef with Structures
#include <stdio.h>

// Define a structure with typedef
typedef struct {
    char title[100];
    char author[50];
    int year;
} Book;

int main() {
    // Declare and initialize a structure variable
    Book book1 = {"C Programming", "Dennis Ritchie", 1978};

    // Access and print the structure members
    printf("Book Title: %s\n", book1.title);
    printf("Author: %s\n", book1.author);
    printf("Year: %d\n", book1.year);

    return 0;
}
Explanation:
typedef: The typedef allows you to use Book directly instead of struct Book.
Simplified Declaration: Book book1 is easier to read and write than struct Book book1.

7. Arrays of Structures
You can create arrays of structures to store multiple instances of the same structure.

Example 6: Array of Structures
#include <stdio.h>

// Define a structure for a student
struct Student {
    char name[50];
    int age;
};

int main() {
    // Declare an array of structures (for 3 students)
    struct Student students[3] = {
        {"Alice", 20},
        {"Bob", 22},
        {"Charlie", 21}
    };

    // Access and print each student's information
    for (int i = 0; i < 3; i++) {
        printf("Name: %s, Age: %d\n", students[i].name, students[i].age);
    }

    return 0;
}
Explanation:
Array of Structures: students[3] is an array of 3 struct Student instances.
Accessing Array Members: You can loop through the array to access each student's information.

8. Common Errors with Structures:
Uninitialized Structures: Always initialize structures before using them.
Memory Allocation Issues: If using dynamic memory for structures, make sure you allocate and free memory properly.
Accessing Undefined Members: Accessing a structure member before initialization can lead to unexpected behavior.
*/

//16.Union
/*
Union in C
A union in C is a special data type that allows storing different types of data in the same memory location. It is similar to a struct, but with one key difference: in a union, all members share the same memory location. This means only one member can hold a value at a time.

Key Features of Union
Memory Sharing:

All members of a union share the same memory space.
The size of a union is determined by the size of its largest member.
Mutual Exclusivity:

Only one member of a union can contain a valid value at any time.
Assigning a value to one member will overwrite the value of other members.
Declaration Syntax: Similar to structures:

c
Copy code
union UnionName {
    memberType1 memberName1;
    memberType2 memberName2;
    ...
};
Accessing Members:

Union members are accessed using the dot operator (.) or arrow operator (-> for pointers).
Declaration and Initialization
Example of Declaration:
c
Copy code
union Data {
    int i;
    float f;
    char str[20];
};
Initialization:
c
Copy code
union Data data;  // Declaring a union variable

data.i = 10;      // Assigning to integer member
data.f = 3.14;    // This will overwrite the value of `i`
strcpy(data.str, "Hello, World!"); // Overwrites the float value
Memory Layout of Union
Example:
c
Copy code
union Data {
    int i;       // 4 bytes
    float f;     // 4 bytes
    char str[20]; // 20 bytes
};
The size of the union will be the size of its largest member: 20 bytes.
All members share the same memory, so:
data.i, data.f, and data.str point to the same location.
Differences Between union and struct
Feature	Union	Structure
Memory	All members share the same memory space.	Each member has its own memory space.
Size	Size is determined by the largest member.	Size is the sum of all members' sizes.
Member Access	Only one member can be used at a time.	All members can be used simultaneously.
Usage	Useful for memory-efficient storage.	Useful for grouping related data.
Usage of Unions
Memory Efficiency:

When only one of the members is needed at a time, unions save memory.
Example: Storing sensor data that could be in different formats.
Type-Punning:

Unions can interpret the same memory in multiple ways (used in embedded systems).
Example: Interpreting raw bytes as integers or floats.
Variant Data Types:

Unions are useful in implementing variant types or data that can take on multiple forms.
Example: A tagged union to handle different data types.
Example Programs
Basic Union Example:
c
Copy code
#include <stdio.h>
#include <string.h>

union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    union Data data;

    data.i = 10;
    printf("data.i: %d\n", data.i);

    data.f = 3.14;
    printf("data.f: %f\n", data.f);

    strcpy(data.str, "Hello");
    printf("data.str: %s\n", data.str);

    // Note: Accessing `data.i` or `data.f` after modifying `data.str` is undefined behavior
    return 0;
}
Union for Type-Punning:
c
Copy code
#include <stdio.h>

union TypePunning {
    int i;
    float f;
};

int main() {
    union TypePunning data;

    data.f = 3.14; // Assigning a float value
    printf("Float value: %f\n", data.f);

    // Interpreting the same memory as an integer
    printf("Interpreted as int: %d\n", data.i);

    return 0;
}
Tagged Union Example:
A tagged union is a union combined with a discriminator to identify which member is currently valid.

c
Copy code
#include <stdio.h>

enum DataType { INT, FLOAT, STRING };

union Data {
    int i;
    float f;
    char str[20];
};

struct TaggedUnion {
    enum DataType type;
    union Data data;
};

int main() {
    struct TaggedUnion var;

    var.type = INT;
    var.data.i = 42;
    printf("Integer: %d\n", var.data.i);

    var.type = FLOAT;
    var.data.f = 3.14;
    printf("Float: %f\n", var.data.f);

    var.type = STRING;
    strcpy(var.data.str, "Hello");
    printf("String: %s\n", var.data.str);

    return 0;
}
Advanced Concepts of Unions
Bitfields in Unions:
Bitfields can be combined with unions to pack multiple flags or small values efficiently.

c
Copy code
#include <stdio.h>

union PackedData {
    struct {
        unsigned int flag1 : 1; // 1-bit field
        unsigned int flag2 : 1; // 1-bit field
        unsigned int flag3 : 1; // 1-bit field
        unsigned int value : 29; // Remaining bits
    };
    unsigned int rawData; // Access as raw 32-bit data
};

int main() {
    union PackedData data;

    data.rawData = 0; // Initialize to 0
    data.flag1 = 1;
    data.value = 100;

    printf("Raw Data: %u\n", data.rawData);
    printf("Flag1: %u, Value: %u\n", data.flag1, data.value);

    return 0;
}
Advantages and Disadvantages of Union
Advantages:
Saves memory by sharing space among members.
Useful for handling variant data types.
Enables efficient type-punning and bit-level operations.
Disadvantages:
Only one member is valid at a time.
Misuse or incorrect assumptions about member usage can lead to undefined behavior.
Debugging can be challenging when multiple types share the same memory.
Common Problems Using Unions
Undefined Behavior:

Accessing a member of a union that was not the last one written can cause undefined behavior in C.
Type Safety:

Unions do not enforce type safety, so it’s the programmer’s responsibility to track which member is valid.
Practical Problems
1. Use Union to Store Data of Different Types
Create a union to store integer, float, and string values dynamically based on user input.

2. Create a Bitfield with Union
Store multiple flags efficiently in a union with bitfields.

3. Implement a Variant Type
Use a tagged union to create a variant type that can hold different types of data safely.
*/

//17.Linked List
/*
Linked List in C
A linked list is a linear data structure where each element (node) contains two parts:

Data: Stores the actual data.
Pointer/Reference: A pointer to the next node in the sequence.
Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each node points to the next node, forming a chain of elements.

Basic Terminology
Node: The building block of a linked list. Each node typically contains:

Data
A pointer to the next node (next or link).
Head: A pointer to the first node in the linked list.

Tail: A pointer to the last node, which points to NULL.

NULL: The special value indicating the end of the list (i.e., the last node's next pointer).

Types of Linked Lists
Singly Linked List:

Each node points to the next node in the sequence, and the last node points to NULL.
Doubly Linked List:

Each node contains two pointers: one pointing to the next node and one pointing to the previous node.
Circular Linked List:

The last node points back to the first node, creating a circular structure.
Singly Linked List - Structure and Operations
Basic Node Structure:
c
Copy code
struct Node {
    int data;           // Data of the node
    struct Node* next;  // Pointer to the next node
};
Creating a Linked List:
Node Creation: Allocate memory for a new node.
Insert a Node: Add a node to the beginning, end, or at a specific position.
Traversal: Traverse the list from the head to print or process data.
Deletion: Remove a node from the list.
Functions for Linked List Operations
Insert at the Beginning:
Adds a new node at the start.
Insert at the End:
Adds a new node at the end of the list.
Insert at a Specific Position:
Insert a new node after a specific node.
Delete a Node:
Removes a node from the list (either by value or position).
Traversal:
Prints the list elements.
Example of Singly Linked List in C
1. Basic Node Structure:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;           // Store data
    struct Node* next;  // Pointer to the next node
};
2. Insert at the Beginning:
c
Copy code
// Function to insert a node at the beginning
void insertAtBeginning(struct Node** head, int newData) {
    // Allocate memory for new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    // Set data and next pointer
    newNode->data = newData;
    newNode->next = *head;  // Make next of new node the old head

    // Move the head to point to the new node
    *head = newNode;
}
3. Insert at the End:
c
Copy code
// Function to insert a node at the end
void insertAtEnd(struct Node** head, int newData) {
    // Allocate memory for new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head;

    // Set data and next pointer
    newNode->data = newData;
    newNode->next = NULL;

    // If the list is empty, make the new node the head
    if (*head == NULL) {
        *head = newNode;
        return;
    }

    // Traverse to the last node
    while (last->next != NULL) {
        last = last->next;
    }

    // Change the next of the last node to point to the new node
    last->next = newNode;
}
4. Traversal:
c
Copy code
// Function to traverse and print the linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}
5. Delete a Node (by value):
c
Copy code
// Function to delete a node by value
void deleteNode(struct Node** head, int key) {
    struct Node* temp = *head;
    struct Node* prev = NULL;

    // If the node to be deleted is the head node
    if (temp != NULL && temp->data == key) {
        *head = temp->next; // Change head
        free(temp);          // Free the old head
        return;
    }

    // Search for the node to be deleted
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If the key is not found
    if (temp == NULL) {
        printf("Node with data %d not found.\n", key);
        return;
    }

    // Unlink the node from the linked list
    prev->next = temp->next;
    free(temp); // Free the memory
}
Complete Example - Singly Linked List
c
Copy code
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to insert a node at the beginning
void insertAtBeginning(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = *head;
    *head = newNode;
}

// Function to insert a node at the end
void insertAtEnd(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head;
    newNode->data = newData;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }

    last->next = newNode;
}

// Function to print the linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

// Function to delete a node by value
void deleteNode(struct Node** head, int key) {
    struct Node* temp = *head;
    struct Node* prev = NULL;

    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Node with data %d not found.\n", key);
        return;
    }

    prev->next = temp->next;
    free(temp);
}

int main() {
    struct Node* head = NULL;

    insertAtBeginning(&head, 10);
    insertAtBeginning(&head, 20);
    insertAtEnd(&head, 30);
    insertAtEnd(&head, 40);

    printf("Linked List: ");
    printList(head);

    printf("Deleting node with data 20\n");
    deleteNode(&head, 20);

    printf("Updated Linked List: ");
    printList(head);

    return 0;
}
Output:
rust
Copy code
Linked List: 20 -> 10 -> 30 -> 40 -> NULL
Deleting node with data 20
Updated Linked List: 10 -> 30 -> 40 -> NULL
Advantages of Linked Lists:
Dynamic Size: Unlike arrays, linked lists can dynamically grow or shrink in size.
Efficient Insertions/Deletions: Inserting or deleting nodes does not require shifting elements (as with arrays).
Disadvantages:
Memory Usage: Each node requires extra memory for storing the pointer.
Sequential Access: Accessing elements requires traversing the list, which can be slower than arrays (which provide random access).
Complexity: Linked lists can be more complex to implement and manage than arrays.
Applications of Linked Lists:
Implementing dynamic memory management.
Used in data structures like stacks, queues, graphs, etc.
Managing memory in operating systems.
Efficiently managing collections of data where the size is not fixed.
*/

//18.Stack
/*
Stack in C
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed.

In simple terms:

Push: Add an element to the stack.
Pop: Remove the top element from the stack.
Peek/Top: View the top element of the stack without removing it.
IsEmpty: Check if the stack is empty.
IsFull: Check if the stack is full (applicable to arrays or fixed-size stacks).
Stacks are widely used in many applications such as:

Function calls (call stack in recursion).
Undo functionality in text editors.
Expression evaluation (infix, prefix, postfix notation).
Backtracking algorithms (like maze-solving).
Basic Operations of Stack
Push: Adds an element to the stack.
Pop: Removes the top element from the stack.
Peek/Top: Returns the top element without removing it.
IsEmpty: Returns 1 if the stack is empty, otherwise returns 0.
IsFull: (For fixed-size stacks) Returns 1 if the stack is full, otherwise returns 0.
Stack Implementation
In C, a stack can be implemented using two primary methods:

Using Arrays: Stack size is fixed.
Using Linked List: Stack size is dynamic.
Here, we'll focus on the array-based implementation of a stack.

Array-Based Stack Implementation
Basic Structure of Stack Using Arrays:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define maximum size of the stack

// Stack structure
struct Stack {
    int arr[MAX];  // Array to hold stack elements
    int top;       // Index of the top element
};

// Function to initialize the stack
void initStack(struct Stack* stack) {
    stack->top = -1;  // Stack is initially empty
}

// Function to check if the stack is full
int isFull(struct Stack* stack) {
    return stack->top == MAX - 1;
}

// Function to check if the stack is empty
int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

// Function to push an element onto the stack
void push(struct Stack* stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow\n");
    } else {
        stack->arr[++(stack->top)] = value;
        printf("Pushed %d onto stack\n", value);
    }
}

// Function to pop an element from the stack
int pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow\n");
        return -1;  // Return an error code
    } else {
        int value = stack->arr[(stack->top)--];
        return value;
    }
}

// Function to peek at the top element of the stack
int peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is Empty\n");
        return -1;  // Return an error code
    } else {
        return stack->arr[stack->top];
    }
}

// Function to display the elements of the stack
void display(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is Empty\n");
    } else {
        printf("Stack elements are: \n");
        for (int i = 0; i <= stack->top; i++) {
            printf("%d ", stack->arr[i]);
        }
        printf("\n");
    }
}

int main() {
    struct Stack stack;   // Create a stack
    initStack(&stack);     // Initialize the stack

    push(&stack, 10);      // Push 10 onto the stack
    push(&stack, 20);      // Push 20 onto the stack
    push(&stack, 30);      // Push 30 onto the stack

    display(&stack);       // Display stack elements

    printf("Peek: %d\n", peek(&stack));  // Peek the top element

    printf("Popped: %d\n", pop(&stack));  // Pop an element

    display(&stack);       // Display stack after pop

    return 0;
}
Explanation of the Code:
Stack Structure:

arr[MAX]: Array used to store stack elements.
top: Index that keeps track of the top element. Initially, it's set to -1 (empty stack).
Functions:

initStack(): Initializes the stack by setting top to -1.
isFull(): Checks if the stack is full by comparing top with MAX-1.
isEmpty(): Checks if the stack is empty by checking if top is -1.
push(): Adds an element to the stack by incrementing top and placing the value in the arr[top].
pop(): Removes the top element by returning the value and decrementing top.
peek(): Returns the value at the top of the stack without modifying the stack.
display(): Prints all elements of the stack.
Sample Output:
yaml
Copy code
Pushed 10 onto stack
Pushed 20 onto stack
Pushed 30 onto stack
Stack elements are:
10 20 30 
Peek: 30
Popped: 30
Stack elements are:
10 20
Operations Time Complexity:
Push: O(1) – Adding an element takes constant time.
Pop: O(1) – Removing an element takes constant time.
Peek: O(1) – Getting the top element takes constant time.
IsEmpty/IsFull: O(1) – Checking if the stack is empty or full takes constant time.
Display: O(n) – Printing all elements requires traversing the stack.
Advantages of Stack:
Fast Operations: Stack operations (push, pop, peek) are very fast (constant time, O(1)).
Memory Efficiency: Especially when using dynamic memory (linked list-based stacks), the stack grows and shrinks as needed.
Useful in Various Algorithms: Stacks are crucial in recursion, parsing expressions, function calls, backtracking, etc.
Disadvantages:
Fixed Size (Array-Based): If using an array-based stack, the size is fixed and can lead to overflow if the stack exceeds the array's size.
Memory Usage (Linked List-Based): Linked list implementations of stacks have overhead due to the need for additional memory to store the pointers.
No Random Access: You can only access the top element, so it doesn't support random access like arrays.
Applications of Stack:
Function Calls (Call Stack): When a function is called, the return address and local variables are stored in a stack.
Expression Evaluation: Stacks are used to evaluate expressions in postfix and prefix notation.
Undo Mechanisms: Most text editors use stacks to manage the "undo" and "redo" functionality.
Backtracking Algorithms: Algorithms that involve making a series of choices, such as solving mazes or puzzles, use stacks to store choices and backtrack when needed.
*/

//19.Queue
/*
Queue in C
A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

In simple terms:

Enqueue: Adds an element to the queue (insert operation).
Dequeue: Removes the front element from the queue (remove operation).
Front: Views the element at the front of the queue without removing it.
Rear: Views the element at the rear of the queue.
IsEmpty: Checks if the queue is empty.
IsFull: Checks if the queue is full (only for a fixed-size queue).
Types of Queues
Simple Queue:

Elements are inserted at the rear and removed from the front.
Can be implemented using arrays or linked lists.
Circular Queue:

A variation of the queue where the last position is connected back to the first position, making it circular.
Helps avoid unused space in an array-based queue when the front and rear elements are far apart.
Priority Queue:

A type of queue where each element is assigned a priority, and elements with higher priority are dequeued before those with lower priority.
Double Ended Queue (Deque):

Elements can be inserted or removed from both ends (front and rear).
Queue Operations
Enqueue (Insert): Adds an element at the rear of the queue.
Dequeue (Remove): Removes the front element from the queue.
Front: Returns the front element without removing it.
Rear: Returns the rear element.
IsEmpty: Returns 1 if the queue is empty; otherwise, 0.
IsFull: (For fixed-size queues) Returns 1 if the queue is full; otherwise, 0.
Queue Implementation (Array-Based)
In C, a queue can be implemented using an array. Here is an example implementation:

Basic Structure of Queue Using Arrays:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define maximum size of the queue

// Queue structure
struct Queue {
    int arr[MAX];  // Array to store queue elements
    int front;     // Index of the front element
    int rear;      // Index of the rear element
};

// Function to initialize the queue
void initQueue(struct Queue* queue) {
    queue->front = -1;
    queue->rear = -1;
}

// Function to check if the queue is full
int isFull(struct Queue* queue) {
    return (queue->rear == MAX - 1);
}

// Function to check if the queue is empty
int isEmpty(struct Queue* queue) {
    return (queue->front == -1 || queue->front > queue->rear);
}

// Function to enqueue (add) an element to the queue
void enqueue(struct Queue* queue, int value) {
    if (isFull(queue)) {
        printf("Queue Overflow\n");
    } else {
        if (queue->front == -1) {
            queue->front = 0;  // Set the front to 0 if the queue is empty
        }
        queue->arr[++(queue->rear)] = value;  // Insert at rear
        printf("Enqueued %d\n", value);
    }
}

// Function to dequeue (remove) an element from the queue
int dequeue(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue Underflow\n");
        return -1;  // Return error code if queue is empty
    } else {
        int value = queue->arr[queue->front];
        queue->front++;  // Move the front pointer to the next element
        return value;
    }
}

// Function to get the front element of the queue
int front(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
        return -1;
    } else {
        return queue->arr[queue->front];
    }
}

// Function to get the rear element of the queue
int rear(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
        return -1;
    } else {
        return queue->arr[queue->rear];
    }
}

// Function to display the queue elements
void display(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
    } else {
        printf("Queue elements: ");
        for (int i = queue->front; i <= queue->rear; i++) {
            printf("%d ", queue->arr[i]);
        }
        printf("\n");
    }
}

int main() {
    struct Queue queue;
    initQueue(&queue);  // Initialize the queue

    // Enqueue elements
    enqueue(&queue, 10);
    enqueue(&queue, 20);
    enqueue(&queue, 30);
    enqueue(&queue, 40);
    enqueue(&queue, 50);

    // Display the queue
    display(&queue);

    // Dequeue elements
    printf("Dequeued: %d\n", dequeue(&queue));

    // Display the queue after dequeue
    display(&queue);

    // Check front and rear elements
    printf("Front: %d\n", front(&queue));
    printf("Rear: %d\n", rear(&queue));

    return 0;
}
Explanation of the Code:
Queue Structure:

arr[MAX]: Array used to store the elements of the queue.
front: Pointer/index to the front of the queue.
rear: Pointer/index to the rear of the queue.
Functions:

initQueue(): Initializes the queue by setting both front and rear to -1.
isFull(): Checks if the queue is full by comparing rear with MAX - 1.
isEmpty(): Checks if the queue is empty by checking if front is -1 or front is greater than rear.
enqueue(): Adds an element at the rear of the queue. If the queue is empty, it sets front to 0. If full, it prints an overflow message.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, it prints an underflow message.
front(): Returns the front element of the queue without removing it.
rear(): Returns the rear element of the queue.
display(): Prints the elements from front to rear.
Sample Output:
yaml
Copy code
Enqueued 10
Enqueued 20
Enqueued 30
Enqueued 40
Enqueued 50
Queue elements: 10 20 30 40 50
Dequeued: 10
Queue elements: 20 30 40 50
Front: 20
Rear: 50
Queue Operations Time Complexity:
Enqueue: O(1) – Adding an element takes constant time.
Dequeue: O(1) – Removing an element takes constant time.
Front: O(1) – Returning the front element takes constant time.
Rear: O(1) – Returning the rear element takes constant time.
Display: O(n) – Displaying all elements takes linear time.
Advantages of Queue:
Order Preservation: Ensures elements are processed in the order they are inserted (FIFO).
Efficient: Operations such as enqueue and dequeue are efficient (O(1)).
Simple Concept: Easy to implement and use in various real-world scenarios (e.g., task scheduling, handling requests, etc.).
Disadvantages:
Fixed Size (Array-Based): If using an array-based queue, the size is fixed, which may lead to overflow if the queue becomes full.
Memory Overhead (Linked List-Based): Linked list-based queues incur memory overhead due to additional pointers for each node.
No Random Access: You cannot access elements randomly in a queue; elements must be dequeued in FIFO order.
Applications of Queue:
Task Scheduling: Queues are widely used in scheduling tasks, like print jobs in a printer queue or task scheduling in operating systems.
Breadth-First Search (BFS): A graph traversal algorithm that uses a queue to explore nodes level by level.
Buffering: Used in situations where data needs to be stored temporarily before processing, such as streaming or IO operations (e.g., keyboard input buffering).
Inter-process Communication: Queues are used in message passing between processes in multi-threaded or multi-processing environments.Queue in C
A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

In simple terms:

Enqueue: Adds an element to the queue (insert operation).
Dequeue: Removes the front element from the queue (remove operation).
Front: Views the element at the front of the queue without removing it.
Rear: Views the element at the rear of the queue.
IsEmpty: Checks if the queue is empty.
IsFull: Checks if the queue is full (only for a fixed-size queue).
Types of Queues
Simple Queue:

Elements are inserted at the rear and removed from the front.
Can be implemented using arrays or linked lists.
Circular Queue:

A variation of the queue where the last position is connected back to the first position, making it circular.
Helps avoid unused space in an array-based queue when the front and rear elements are far apart.
Priority Queue:

A type of queue where each element is assigned a priority, and elements with higher priority are dequeued before those with lower priority.
Double Ended Queue (Deque):

Elements can be inserted or removed from both ends (front and rear).
Queue Operations
Enqueue (Insert): Adds an element at the rear of the queue.
Dequeue (Remove): Removes the front element from the queue.
Front: Returns the front element without removing it.
Rear: Returns the rear element.
IsEmpty: Returns 1 if the queue is empty; otherwise, 0.
IsFull: (For fixed-size queues) Returns 1 if the queue is full; otherwise, 0.
Queue Implementation (Array-Based)
In C, a queue can be implemented using an array. Here is an example implementation:

Basic Structure of Queue Using Arrays:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define maximum size of the queue

// Queue structure
struct Queue {
    int arr[MAX];  // Array to store queue elements
    int front;     // Index of the front element
    int rear;      // Index of the rear element
};

// Function to initialize the queue
void initQueue(struct Queue* queue) {
    queue->front = -1;
    queue->rear = -1;
}

// Function to check if the queue is full
int isFull(struct Queue* queue) {
    return (queue->rear == MAX - 1);
}

// Function to check if the queue is empty
int isEmpty(struct Queue* queue) {
    return (queue->front == -1 || queue->front > queue->rear);
}

// Function to enqueue (add) an element to the queue
void enqueue(struct Queue* queue, int value) {
    if (isFull(queue)) {
        printf("Queue Overflow\n");
    } else {
        if (queue->front == -1) {
            queue->front = 0;  // Set the front to 0 if the queue is empty
        }
        queue->arr[++(queue->rear)] = value;  // Insert at rear
        printf("Enqueued %d\n", value);
    }
}

// Function to dequeue (remove) an element from the queue
int dequeue(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue Underflow\n");
        return -1;  // Return error code if queue is empty
    } else {
        int value = queue->arr[queue->front];
        queue->front++;  // Move the front pointer to the next element
        return value;
    }
}

// Function to get the front element of the queue
int front(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
        return -1;
    } else {
        return queue->arr[queue->front];
    }
}

// Function to get the rear element of the queue
int rear(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
        return -1;
    } else {
        return queue->arr[queue->rear];
    }
}

// Function to display the queue elements
void display(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is Empty\n");
    } else {
        printf("Queue elements: ");
        for (int i = queue->front; i <= queue->rear; i++) {
            printf("%d ", queue->arr[i]);
        }
        printf("\n");
    }
}

int main() {
    struct Queue queue;
    initQueue(&queue);  // Initialize the queue

    // Enqueue elements
    enqueue(&queue, 10);
    enqueue(&queue, 20);
    enqueue(&queue, 30);
    enqueue(&queue, 40);
    enqueue(&queue, 50);

    // Display the queue
    display(&queue);

    // Dequeue elements
    printf("Dequeued: %d\n", dequeue(&queue));

    // Display the queue after dequeue
    display(&queue);

    // Check front and rear elements
    printf("Front: %d\n", front(&queue));
    printf("Rear: %d\n", rear(&queue));

    return 0;
}
Explanation of the Code:
Queue Structure:

arr[MAX]: Array used to store the elements of the queue.
front: Pointer/index to the front of the queue.
rear: Pointer/index to the rear of the queue.
Functions:

initQueue(): Initializes the queue by setting both front and rear to -1.
isFull(): Checks if the queue is full by comparing rear with MAX - 1.
isEmpty(): Checks if the queue is empty by checking if front is -1 or front is greater than rear.
enqueue(): Adds an element at the rear of the queue. If the queue is empty, it sets front to 0. If full, it prints an overflow message.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, it prints an underflow message.
front(): Returns the front element of the queue without removing it.
rear(): Returns the rear element of the queue.
display(): Prints the elements from front to rear.
Sample Output:
yaml
Copy code
Enqueued 10
Enqueued 20
Enqueued 30
Enqueued 40
Enqueued 50
Queue elements: 10 20 30 40 50
Dequeued: 10
Queue elements: 20 30 40 50
Front: 20
Rear: 50
Queue Operations Time Complexity:
Enqueue: O(1) – Adding an element takes constant time.
Dequeue: O(1) – Removing an element takes constant time.
Front: O(1) – Returning the front element takes constant time.
Rear: O(1) – Returning the rear element takes constant time.
Display: O(n) – Displaying all elements takes linear time.
Advantages of Queue:
Order Preservation: Ensures elements are processed in the order they are inserted (FIFO).
Efficient: Operations such as enqueue and dequeue are efficient (O(1)).
Simple Concept: Easy to implement and use in various real-world scenarios (e.g., task scheduling, handling requests, etc.).
Disadvantages:
Fixed Size (Array-Based): If using an array-based queue, the size is fixed, which may lead to overflow if the queue becomes full.
Memory Overhead (Linked List-Based): Linked list-based queues incur memory overhead due to additional pointers for each node.
No Random Access: You cannot access elements randomly in a queue; elements must be dequeued in FIFO order.
Applications of Queue:
Task Scheduling: Queues are widely used in scheduling tasks, like print jobs in a printer queue or task scheduling in operating systems.
Breadth-First Search (BFS): A graph traversal algorithm that uses a queue to explore nodes level by level.
Buffering: Used in situations where data needs to be stored temporarily before processing, such as streaming or IO operations (e.g., keyboard input buffering).
Inter-process Communication: Queues are used in message passing between processes in multi-threaded or multi-processing environments.
*/

// Bit Manipulation
/*
Bit Manipulation in C
Bit manipulation refers to the process of performing operations on individual bits of a number. It is a low-level operation that allows for fast computation by directly manipulating the binary representations of numbers. This is often used in scenarios where performance and memory efficiency are crucial, such as in embedded systems, cryptography, networking, and competitive programming.

Bitwise operations work at the bit level and are faster than arithmetic operations. In C, bit manipulation can be done using the following bitwise operators:

Bitwise Operators in C
AND (&):
The AND operator performs a bitwise AND operation. It sets the bit to 1 if both corresponding bits are 1; otherwise, it sets it to 0.

c
Copy code
a & b
OR (|):
The OR operator performs a bitwise OR operation. It sets the bit to 1 if at least one of the corresponding bits is 1; otherwise, it sets it to 0.

c
Copy code
a | b
XOR (^):
The XOR (exclusive OR) operator sets the bit to 1 if exactly one of the corresponding bits is 1. If both are 0 or both are 1, it sets the bit to 0.

c
Copy code
a ^ b
NOT (~):
The NOT operator is a unary operator that flips the bits. It inverts each bit of the operand (0 becomes 1, and 1 becomes 0).

c
Copy code
~a
Left Shift (<<):
The left shift operator shifts the bits of a number to the left by a specified number of positions. It inserts 0s on the right side and discards bits that overflow.

c
Copy code
a << n
Right Shift (>>):
The right shift operator shifts the bits of a number to the right by a specified number of positions. It inserts 0s on the left side for unsigned numbers and the sign bit for signed numbers.

c
Copy code
a >> n
Common Applications of Bit Manipulation
Setting a Bit To set a specific bit to 1, use the OR operator (|).

c
Copy code
num = num | (1 << i); // Set the ith bit of num to 1
Clearing a Bit To clear a specific bit (set it to 0), use the AND operator (&) with the complement of the bit mask.

c
Copy code
num = num & ~(1 << i); // Clear the ith bit of num
Toggling a Bit To toggle a specific bit (flip it from 0 to 1 or from 1 to 0), use the XOR operator (^).

c
Copy code
num = num ^ (1 << i); // Toggle the ith bit of num
Checking a Bit To check if a specific bit is set (1) or not (0), use the AND operator (&).

c
Copy code
if (num & (1 << i)) {
    // The ith bit is set (1)
} else {
    // The ith bit is not set (0)
}
Counting Set Bits (Hamming Weight) To count the number of 1s in the binary representation of a number, iterate through all bits and use the AND operation.

c
Copy code
int countSetBits(int num) {
    int count = 0;
    while (num) {
        count += (num & 1); // If the least significant bit is 1
        num >>= 1;  // Shift num to the right
    }
    return count;
}
Power of 2 Check A number is a power of 2 if it has exactly one bit set. You can check this using the property num & (num - 1) == 0.

c
Copy code
int isPowerOfTwo(int num) {
    return (num > 0) && (num & (num - 1)) == 0;
}
Examples of Bit Manipulation
Swapping Two Numbers Using XOR

You can swap two numbers without using a temporary variable by using the XOR operator.

c
Copy code
void swap(int *a, int *b) {
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}
This works because XORing the same value twice cancels out the effect:
a = a ^ b
b = a ^ b (which becomes the original value of a)
a = a ^ b (which becomes the original value of b)
Extracting Specific Bits (Bit Masking)

You can extract a specific bit from a number by ANDing the number with a mask that has the bit you want to extract set to 1 and all other bits set to 0.

c
Copy code
int getBit(int num, int i) {
    return (num >> i) & 1; // Right shift num to get the ith bit and mask it with 1
}
Setting Multiple Bits

You can set multiple bits in a number by ORing the number with a mask that has all the bits set to 1.

c
Copy code
int setBits(int num, int mask) {
    return num | mask; // Set bits where mask has 1s
}
Clearing Lower Bits

To clear all bits below a certain bit (e.g., setting the lowest n bits to 0), you can create a mask and apply the AND operation.

c
Copy code
int clearLowerBits(int num, int n) {
    int mask = ~((1 << n) - 1);  // Create a mask with the lowest n bits set to 0
    return num & mask;
}
Finding the Highest Set Bit

To find the position of the most significant bit (highest set bit) in an integer, you can use the following trick. It works by shifting the number left until the number becomes zero.

c
Copy code
int highestSetBit(int num) {
    int position = -1;
    while (num) {
        position++;
        num >>= 1;
    }
    return position;
}
Common Bit Manipulation Problems
Reverse Bits of a Number Given a number, you can reverse the order of its bits.

c
Copy code
unsigned int reverseBits(unsigned int num) {
    unsigned int reversed = 0;
    while (num > 0) {
        reversed = (reversed << 1) | (num & 1); // Shift reversed left and append the LSB of num
        num >>= 1; // Right shift num to process the next bit
    }
    return reversed;
}
Find the Two Non-Repeated Elements in an Array Given an array where every element appears twice except for two elements, find the two elements that appear only once.

Approach: XOR all elements. The result will be the XOR of the two unique elements. Then, find the rightmost set bit in the result and use it to divide the elements into two groups.

c
Copy code
void findTwoUniqueElements(int arr[], int n) {
    int xorResult = 0;
    for (int i = 0; i < n; i++) {
        xorResult ^= arr[i];  // XOR all elements together
    }

    // Find the rightmost set bit in xorResult
    int rightmostSetBit = xorResult & -xorResult;

    int num1 = 0, num2 = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] & rightmostSetBit) {
            num1 ^= arr[i];  // XOR elements with the rightmost set bit
        } else {
            num2 ^= arr[i];  // XOR elements without the rightmost set bit
        }
    }

    printf("The two unique elements are: %d and %d\n", num1, num2);
}
Maximize XOR of Two Numbers in an Array Given an array of numbers, find two numbers that produce the maximum XOR result.

Approach: Use a trie or bitwise operations with prefixes to efficiently find the maximum XOR pair.
*/

// 20.Tree
/*
Tree in C
A tree is a non-linear data structure that consists of nodes connected by edges. A tree represents hierarchical relationships, where each node stores a value and has references to its child nodes.

In a tree:

Root: The topmost node in a tree. There is only one root in a tree.
Parent: A node that has one or more children.
Child: A node that is connected to a parent node.
Leaf: A node that does not have any children.
Subtree: A tree formed by a node and its descendants.
Height of a node: The number of edges on the longest path from that node to a leaf.
Depth of a node: The number of edges from the root to the node.
Types of Trees
Binary Tree:

A tree in which each node has at most two children (left and right).
Binary Search Tree (BST):

A binary tree where the left child of a node contains a value less than the node, and the right child contains a value greater than the node.
Balanced Tree:

A tree where the height of the left and right subtrees of any node differ by at most 1 (e.g., AVL tree).
Heap:

A special tree-based data structure that satisfies the heap property. Max heaps and min heaps are common examples.
Trie (Prefix Tree):

A tree used to store a dynamic set of strings, where each node represents a character of a string.
Basic Terminology
Node: An element that holds data and references to its children.
Edge: A connection between two nodes.
Root: The topmost node of the tree.
Leaf: A node with no children.
Parent: A node that has one or more children.
Child: A node connected to a parent node.
Subtree: A portion of the tree that includes a node and all of its descendants.
Tree Representation in C
A tree can be represented in C using a struct. Each node typically stores data and pointers to its left and right child (for binary trees). For general trees, it may store pointers to multiple children.

Binary Tree Node Structure:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Structure for a Binary Tree Node
struct Node {
    int data;           // Data to be stored in the node
    struct Node* left;  // Pointer to the left child
    struct Node* right; // Pointer to the right child
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Preorder Traversal (Root, Left, Right)
void preorderTraversal(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

// Inorder Traversal (Left, Root, Right)
void inorderTraversal(struct Node* root) {
    if (root == NULL) return;
    inorderTraversal(root->left);
    printf("%d ", root->data);
    inorderTraversal(root->right);
}

// Postorder Traversal (Left, Right, Root)
void postorderTraversal(struct Node* root) {
    if (root == NULL) return;
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    printf("%d ", root->data);
}

// Main function to demonstrate tree operations
int main() {
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    printf("Preorder Traversal: ");
    preorderTraversal(root);
    printf("\n");

    printf("Inorder Traversal: ");
    inorderTraversal(root);
    printf("\n");

    printf("Postorder Traversal: ");
    postorderTraversal(root);
    printf("\n");

    return 0;
}
Explanation of the Code:
Node Structure:

Each node in the tree has three parts: data, left, and right.
data: Holds the value of the node.
left: A pointer to the left child.
right: A pointer to the right child.
createNode() Function:

Dynamically allocates memory for a new node, initializes the data, and sets both left and right pointers to NULL.
Tree Traversals:

Preorder Traversal: Visit the root first, then traverse the left subtree, and finally the right subtree.
Inorder Traversal: Traverse the left subtree first, then visit the root, and finally the right subtree.
Postorder Traversal: Traverse the left and right subtrees first, then visit the root.
Example Tree: The tree created in the code has the following structure:

markdown
Copy code
       1
      / \
     2   3
    / \
   4   5
Output:

yaml
Copy code
Preorder Traversal: 1 2 4 5 3 
Inorder Traversal: 4 2 5 1 3 
Postorder Traversal: 4 5 2 3 1 
Operations on Binary Trees:
Insertion:

In a binary tree, insertion can be done by placing the node in the first available position at the bottom (incomplete tree), typically using a level-order traversal.
Deletion:

Deletion involves finding the node and removing it. For a node with two children, the node's data is replaced with the largest node in the left subtree or the smallest node in the right subtree.
Searching:

Binary Search Tree (BST) allows fast searching. The search starts from the root, and if the value to be found is less than the current node's data, we move to the left child. Otherwise, we move to the right child.
Height of a Tree:

The height of a tree is the number of edges in the longest path from the root to a leaf. A recursive approach can be used to calculate the height by comparing the heights of the left and right subtrees.
Applications of Trees:
Expression Parsing: Trees are used in the evaluation of mathematical expressions (e.g., syntax trees).
Hierarchical Data Representation: Filesystems, organization charts, etc., are naturally represented as trees.
Search Trees (BST): Used to store data in a way that allows efficient searching, insertion, and deletion.
Balancing: AVL trees, Red-Black trees are used to ensure balanced structures for efficient operations.
Network Routing: Trees are used in routing algorithms (e.g., spanning tree for a network).
Binary Search Tree (BST)
A Binary Search Tree (BST) is a binary tree with the following properties:

For any node, all elements in its left subtree are smaller.
All elements in its right subtree are greater.
BST Operations:
Insertion: Insert nodes in such a way that the BST property is maintained.
Search: Search for an element by comparing with the root and traversing left or right based on the value.
Deletion: Deleting a node requires handling three cases:
Node with no children (leaf node): Simply remove it.
Node with one child: Replace the node with its child.
Node with two children: Replace the node with the minimum element from the right subtree or maximum from the left subtree.
Example of Binary Search Tree:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a BST node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

// Function to insert a new node in the BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) {
        return newNode(data); // If the tree is empty, create a new node
    }

    // Otherwise, recur down the tree
    if (data < root->data) {
        root->left = insert(root->left, data);  // Insert in the left subtree
    } else if (data > root->data) {
        root->right = insert(root->right, data); // Insert in the right subtree
    }

    return root;  // Return the (unchanged) node pointer
}

// Inorder Traversal (Left, Root, Right)
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// Main function
int main() {
    struct Node* root = NULL;

    // Insert nodes
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    printf("Inorder traversal: ");
    inorderTraversal(root);
    printf("\n");

    return 0;
}
*/

// Binary Tree
/*
Binary Tree in C
A binary tree is a hierarchical data structure in which each node has at most two children, typically referred to as the left and right child. The topmost node is called the root, and the nodes with no children are called leaves.

Key Terminologies in a Binary Tree:
Node: A basic unit of a tree that contains data and pointers to its left and right children.
Root: The topmost node in the binary tree.
Leaf Node: A node that has no children.
Internal Node: A node that has at least one child.
Parent Node: A node that has one or more children.
Child Node: A node that is a descendant of a parent node.
Subtree: A tree formed by any node and its descendants.
Depth: The number of edges from the root to a node.
Height: The number of edges on the longest path from a node to a leaf.
Level: The level of a node is the number of edges from the root to the node.
Binary Tree Representation in C
A binary tree can be represented using structures and dynamic memory allocation. We will define a structure for each node in the tree, which will store its data and pointers to the left and right child nodes.

Basic Structure of a Binary Tree Node:
c
Copy code
struct Node {
    int data;               // Data part
    struct Node* left;      // Pointer to left child
    struct Node* right;     // Pointer to right child
};
Binary Tree Operations:
Some common operations on binary trees are:

Insertion: Adding a new node to the tree.
Traversal: Visiting all nodes in a specific order.
Pre-order Traversal (Root, Left, Right)
In-order Traversal (Left, Root, Right)
Post-order Traversal (Left, Right, Root)
Searching: Searching for a particular element in the tree.
Deletion: Removing a node from the tree.
Finding the height of the tree.
1. Binary Tree Insertion in C:
In this example, we will insert nodes to create a simple binary tree.

Code for Binary Tree Creation and Traversal:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Define a binary tree node
struct Node {
    int data;               // Data part
    struct Node* left;      // Pointer to left child
    struct Node* right;     // Pointer to right child
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Pre-order traversal (Root, Left, Right)
void preOrder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);   // Visit the root
        preOrder(root->left);        // Traverse left subtree
        preOrder(root->right);       // Traverse right subtree
    }
}

// In-order traversal (Left, Root, Right)
void inOrder(struct Node* root) {
    if (root != NULL) {
        inOrder(root->left);         // Traverse left subtree
        printf("%d ", root->data);   // Visit the root
        inOrder(root->right);        // Traverse right subtree
    }
}

// Post-order traversal (Left, Right, Root)
void postOrder(struct Node* root) {
    if (root != NULL) {
        postOrder(root->left);       // Traverse left subtree
        postOrder(root->right);      // Traverse right subtree
        printf("%d ", root->data);   // Visit the root
    }
}

// Function to calculate the height of a binary tree
int height(struct Node* root) {
    if (root == NULL) {
        return -1;  // Height of an empty tree is -1
    } else {
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
    }
}

int main() {
    // Creating nodes
    struct Node* root = createNode(1);
    struct Node* n1 = createNode(2);
    struct Node* n2 = createNode(3);
    struct Node* n3 = createNode(4);
    struct Node* n4 = createNode(5);

    // Linking nodes to create a binary tree
    root->left = n1;
    root->right = n2;
    n1->left = n3;
    n1->right = n4;

    // Traversals
    printf("Pre-order Traversal: ");
    preOrder(root);
    printf("\n");

    printf("In-order Traversal: ");
    inOrder(root);
    printf("\n");

    printf("Post-order Traversal: ");
    postOrder(root);
    printf("\n");

    // Height of the tree
    printf("Height of the tree: %d\n", height(root));

    return 0;
}
Explanation:
Node Structure:

Each node in the binary tree contains an integer data and two pointers, left and right, which point to the left and right child nodes, respectively.
createNode() Function:

This function dynamically allocates memory for a new node, initializes the data, and sets the left and right pointers to NULL.
Traversal Functions:

Pre-order Traversal: First visits the root, then recursively visits the left subtree and the right subtree.
In-order Traversal: First recursively visits the left subtree, then visits the root, and finally the right subtree.
Post-order Traversal: First recursively visits the left subtree, then the right subtree, and finally the root.
Height Function:

This function computes the height of the tree by recursively determining the height of the left and right subtrees and returning the larger of the two heights plus 1.
Sample Output:
yaml
Copy code
Pre-order Traversal: 1 2 4 5 3
In-order Traversal: 4 2 5 1 3
Post-order Traversal: 4 5 2 3 1
Height of the tree: 2
Binary Tree Types:
Full Binary Tree: Every node has either 0 or 2 children.
Complete Binary Tree: All levels are completely filled except possibly the last level, which is filled from left to right.
Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level.
Balanced Binary Tree: The height of the left and right subtrees of every node differ by at most 1.
Binary Tree Applications:
Expression Parsing: Used in the evaluation of arithmetic expressions (expression trees).
Huffman Coding Tree: Used in data compression algorithms.
Binary Search Tree (BST): A special type of binary tree where left children are smaller and right children are larger than the parent node, supporting efficient searching, insertion, and deletion operations.
*/

// Maximum Spanning Tree
/*
Minimum Spanning Tree (MST)
A Minimum Spanning Tree (MST) of a connected, undirected graph is a tree that spans all the vertices of the graph, where the total weight of the edges in the tree is minimized. In simpler terms, it connects all nodes with the minimum possible total edge weight.

Key Characteristics of MST:
Spanning: The tree includes all the vertices of the graph.
Minimum Weight: The sum of the weights of the edges in the tree is the smallest possible.
Tree: The MST is a tree, meaning it has no cycles and contains exactly V - 1 edges, where V is the number of vertices.
Common Algorithms for Finding MST:
Kruskal's Algorithm
Prim's Algorithm
Let’s go over these algorithms and their implementation.

1. Kruskal's Algorithm
Kruskal's Algorithm is a greedy algorithm that finds the minimum spanning tree by sorting all the edges in the graph by weight and then adding edges one by one to the MST, ensuring no cycles are formed. It uses Disjoint Set (Union-Find) to keep track of cycles.

Steps of Kruskal’s Algorithm:
Sort all the edges of the graph in ascending order by their weight.
Initialize a Disjoint Set (Union-Find) structure for all vertices to track connected components.
Iterate through the sorted edges and for each edge:
If the edge connects two different components (i.e., it doesn't form a cycle), add it to the MST.
If it forms a cycle, discard it.
Repeat until V-1 edges are added to the MST (where V is the number of vertices).
Kruskal's Algorithm Code:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Structure to represent a graph edge
struct Edge {
    int src, dest, weight;
};

// Structure to represent a subset for union-find
struct Subset {
    int parent, rank;
};

// Function to find the subset of an element (using path compression)
int find(struct Subset subsets[], int i) {
    if (subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);  // Path compression
    return subsets[i].parent;
}

// Function to do union of two subsets (using union by rank)
void Union(struct Subset subsets[], int x, int y) {
    int xroot = find(subsets, x);
    int yroot = find(subsets, y);

    if (subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if (subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
    else {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}

// Comparator function to sort edges based on their weight
int compare(const void *a, const void *b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

// Function to construct MST using Kruskal's algorithm
void KruskalMST(struct Edge edges[], int V, int E) {
    struct Edge result[V - 1];  // To store the final MST
    int e = 0;  // Count of edges in MST
    int i = 0;  // Initial index of sorted edges
    struct Subset *subsets = (struct Subset*)malloc(V * sizeof(struct Subset));

    // Step 1: Sort all the edges in the graph
    qsort(edges, E, sizeof(edges[0]), compare);

    // Step 2: Initialize subsets for union-find
    for (int v = 0; v < V; v++) {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    // Step 3: Pick the smallest edge and check if it forms a cycle
    while (e < V - 1) {
        struct Edge next_edge = edges[i++];
        int x = find(subsets, next_edge.src);
        int y = find(subsets, next_edge.dest);

        // If including this edge does not cause a cycle, include it in the result
        if (x != y) {
            result[e++] = next_edge;
            Union(subsets, x, y);
        }
    }

    // Step 4: Print the MST
    printf("Edges in the Minimum Spanning Tree:\n");
    for (int i = 0; i < e; i++) {
        printf("%d -- %d == %d\n", result[i].src, result[i].dest, result[i].weight);
    }

    free(subsets);
}

int main() {
    int V = 4; // Number of vertices
    int E = 5; // Number of edges

    // Define the edges of the graph (src, dest, weight)
    struct Edge edges[] = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    KruskalMST(edges, V, E);

    return 0;
}
Explanation:
find(): This function finds the parent of a node using path compression (to speed up future queries).
Union(): This function combines two sets using union by rank (to keep the tree flat).
KruskalMST(): This is the main function that implements Kruskal's algorithm. It sorts the edges, processes them, and adds edges to the MST without forming cycles.
Sample Output:
lua
Copy code
Edges in the Minimum Spanning Tree:
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
2. Prim's Algorithm
Prim's Algorithm is another greedy algorithm for finding the MST. It starts with an arbitrary node and grows the MST one edge at a time by always choosing the minimum weight edge that connects a vertex in the MST to a vertex outside the MST.

Steps of Prim’s Algorithm:
Start with an arbitrary node and mark it as part of the MST.
Find the minimum weight edge that connects a node in the MST to a node outside the MST.
Add the chosen edge to the MST and mark the new node as part of the MST.
Repeat until all vertices are included in the MST.
Prim's Algorithm Code:
c
Copy code
#include <stdio.h>
#include <limits.h>

#define V 5 // Number of vertices in the graph

// Find the vertex with the minimum key value
int minKey(int key[], int mstSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++) {
        if (mstSet[v] == 0 && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

// Function to implement Prim's algorithm for MST
void primMST(int graph[V][V]) {
    int parent[V]; // Array to store the constructed MST
    int key[V];    // Key values used to pick minimum weight edge
    int mstSet[V]; // To represent the set of vertices included in the MST

    // Initialize all keys as infinite and mstSet as false
    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = 0;
    }

    // Always include the first vertex in the MST
    key[0] = 0;
    parent[0] = -1; // First node has no parent

    // Find the MST for all vertices
    for (int count = 0; count < V - 1; count++) {
        // Pick the minimum key vertex that is not yet included in MST
        int u = minKey(key, mstSet);

        // Add the picked vertex to the MST set
        mstSet[u] = 1;

        // Update key and parent values of adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && mstSet[v] == 0 && graph[u][v] < key[v]) {
                key[v] = graph[u][v];
                parent[v] = u;
            }
        }
    }

    // Print the constructed MST
    printf("Edge   Weight\n");
    for (int i = 1; i < V; i++) {
        printf("%d - %d    %d\n", parent[i], i, graph[i][parent[i]]);
    }
}

int main() {
    // Adjacency matrix representation of the graph
    int graph[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    primMST(graph);

    return 0;
}
Explanation:
minKey(): This function finds the vertex with the smallest key value that hasn’t been included in the MST yet.
primMST(): This function implements Prim's algorithm to build the MST using the adjacency matrix representation of the graph.
Sample Output:
Copy code
Edge   Weight
0 - 1    2
0 - 3    6
1 - 2    3
1 - 4    5
*/

// Fenwick Trees
/*
Fenwick Tree (Binary Indexed Tree)
A Fenwick Tree, also known as a Binary Indexed Tree (BIT), is a data structure that efficiently supports the following operations:

Prefix Sum Query: Query the sum of the first i elements.
Point Update: Update a single element in the array.
Both operations can be done in O(log n) time, making the Fenwick Tree an efficient structure for handling dynamic cumulative frequency tables.

Key Features:
Efficient: Fenwick Tree provides logarithmic time complexity for both updates and queries, making it much faster than a simple array.
Compact: The tree uses an array and performs operations directly on the array in a way that mimics a tree structure but without using actual nodes.
Prefix sum support: It allows us to compute the prefix sum of an array efficiently.
Operations:
Update Operation: Modify an element in the array and propagate the change efficiently to the tree.
Query Operation: Compute the sum of elements in a range, typically the prefix sum up to a certain index.
Fenwick Tree Structure:
A Fenwick Tree is usually represented as an array. For a given index i:

The parent of i can be computed as i + (i & -i).
The parent-child relationships and the update mechanism rely on binary representations.
Fenwick Tree Example:
Let’s assume an array arr[] with n elements. The Fenwick Tree bit[] will be constructed to provide the sum of elements efficiently.

Operations in Fenwick Tree:
Query (sum(i)): This function returns the sum of the array from arr[0] to arr[i] (prefix sum).
Update (update(i, delta)): This function updates the value of arr[i] by adding delta to it.
Fenwick Tree Construction:
For an array arr[] of size n, the Fenwick Tree bit[] is built using the following:

bit[i] stores the sum of the last i & -i elements of the original array. This allows efficient updates and queries.
Fenwick Tree Operations:
1. Query Operation:
c
Copy code
int query(int bit[], int index) {
    int sum = 0;
    while (index > 0) {
        sum += bit[index];
        index -= index & (-index);  // Move to the parent
    }
    return sum;
}
2. Update Operation:
c
Copy code
void update(int bit[], int n, int index, int delta) {
    while (index <= n) {
        bit[index] += delta;  // Update the current index
        index += index & (-index);  // Move to the next element to update
    }
}
Complete Example in C:
Let’s look at a full example of implementing and using a Fenwick Tree to handle updates and range queries.

c
Copy code
#include <stdio.h>

#define MAX 100

// Function to update the BIT with delta at index
void update(int BIT[], int n, int index, int delta) {
    while (index <= n) {
        BIT[index] += delta;
        index += index & (-index);  // Move to the next node in the tree
    }
}

// Function to get the prefix sum from BIT[1] to BIT[index]
int query(int BIT[], int index) {
    int sum = 0;
    while (index > 0) {
        sum += BIT[index];
        index -= index & (-index);  // Move to the parent node in the tree
    }
    return sum;
}

int main() {
    int n = 8; // Size of the array
    int arr[MAX] = {0};  // Original array (indexed from 1)
    int BIT[MAX] = {0};  // Fenwick Tree (indexed from 1)

    // Initialize the array with some values
    arr[1] = 1;
    arr[2] = 3;
    arr[3] = 2;
    arr[4] = 5;
    arr[5] = 7;
    arr[6] = 6;
    arr[7] = 8;
    arr[8] = 4;

    // Build the Fenwick Tree from the array (initialize BIT)
    for (int i = 1; i <= n; i++) {
        update(BIT, n, i, arr[i]);
    }

    // Query the sum from index 1 to 4
    printf("Sum of elements from 1 to 4: %d\n", query(BIT, 4));

    // Query the sum from index 3 to 6
    printf("Sum of elements from 3 to 6: %d\n", query(BIT, 6) - query(BIT, 2));

    // Update the value at index 4 (add 3 to arr[4])
    update(BIT, n, 4, 3);

    // Query the sum after the update
    printf("Sum of elements from 1 to 4 after update: %d\n", query(BIT, 4));

    return 0;
}
Explanation of the Code:
update(): This function adds a delta value to the index element in the BIT array and updates its parent nodes accordingly.
query(): This function calculates the prefix sum from 1 to the given index. It moves upward in the BIT array by subtracting the least significant bit (index -= index & (-index)).
Sample Output:
vbnet
Copy code
Sum of elements from 1 to 4: 11
Sum of elements from 3 to 6: 21
Sum of elements from 1 to 4 after update: 14
Advantages of Fenwick Tree:
Efficient:
The query and update operations both run in O(log n) time.
For frequent updates and queries, Fenwick Trees are highly efficient compared to brute-force methods.
Space Complexity:
The Fenwick Tree requires O(n) space, which is space-efficient compared to segment trees (which require O(4n) space).
Simple to Implement:
Fenwick Trees are easier to implement than segment trees and often provide enough efficiency for competitive programming tasks.
Applications of Fenwick Tree:
Dynamic Prefix Sum Calculation: It allows efficient computation of prefix sums for problems like cumulative frequency tables.
Range Queries and Updates: In problems where we need to perform range queries (sum, min, max, etc.) with frequent updates.
Counting Inversions: Can be used to count the number of inversions in an array during sorting.
Solving Range Sum Queries: Common in problems involving dynamic datasets where the elements change frequently.
Complexity:
Time Complexity:
Query: O(log n)
Update: O(log n)
Space Complexity: O(n)
*/

// Trie
/*
Trie (Prefix Tree)
A Trie, also known as a Prefix Tree, is a special type of tree used to efficiently store and retrieve strings, particularly when there is a need for searching words or prefixes in a dictionary. It is commonly used in tasks like:

Autocomplete suggestions
Spell checkers
IP routing
Storing large sets of strings efficiently
Key Characteristics:
Nodes: Each node in the Trie represents a character in the string. A Trie starts with a root node and branches out for every character of a string.
String Storage: Unlike regular trees, which store data in the nodes, the Trie stores strings along the path from the root to the leaves.
Prefix-based Search: It is efficient for storing words with common prefixes and performing operations like prefix search, insertion, and deletion in a way that reduces redundant storage.
Time Complexity: Each operation (insert, search) takes O(L) time, where L is the length of the string being processed. This is better than searching for strings in a simple list or array.
Basic Operations on Trie:
Insert: Add a string to the Trie.
Search: Check if a string exists in the Trie.
Prefix Search: Check if there are any strings in the Trie that start with a given prefix.
Trie Data Structure Representation:
A Trie is typically represented using nodes. Each node has:

A list of child nodes (each representing a character).
A boolean flag isEndOfWord to mark whether the current node is the end of a word.
Trie Node Structure:
c
Copy code
struct TrieNode {
    struct TrieNode *children[26];  // For lowercase English letters
    bool isEndOfWord;               // To mark if the current node is the end of a word
};
Basic Trie Operations:
Insert Operation: Insert a word into the Trie character by character, creating new nodes as necessary.

Search Operation: Search for a word by traversing the Trie nodes based on each character in the word.

Prefix Search Operation: Check if there exists any word in the Trie that starts with a given prefix.

Trie Implementation in C:
c
Copy code
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define ALPHABET_SIZE 26  // For lowercase English letters

// Trie node structure
struct TrieNode {
    struct TrieNode *children[ALPHABET_SIZE];  // Children array
    bool isEndOfWord;  // True if the node represents the end of a word
};

// Function to create a new Trie node
struct TrieNode* createNode() {
    struct TrieNode* newNode = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    newNode->isEndOfWord = false;

    for (int i = 0; i < ALPHABET_SIZE; i++) {
        newNode->children[i] = NULL;
    }

    return newNode;
}

// Function to insert a word into the Trie
void insert(struct TrieNode *root, const char *word) {
    struct TrieNode *current = root;
    int index;

    // Traverse through the word and insert characters one by one
    for (int i = 0; i < strlen(word); i++) {
        index = word[i] - 'a';  // Convert character to index (0 for 'a', 1 for 'b', ...)
        
        if (current->children[index] == NULL) {
            current->children[index] = createNode();
        }

        current = current->children[index];
    }

    // Mark the end of the word
    current->isEndOfWord = true;
}

// Function to search for a word in the Trie
bool search(struct TrieNode *root, const char *word) {
    struct TrieNode *current = root;
    int index;

    for (int i = 0; i < strlen(word); i++) {
        index = word[i] - 'a';

        if (current->children[index] == NULL) {
            return false;  // Word not found
        }

        current = current->children[index];
    }

    // Return true if the current node marks the end of the word
    return current != NULL && current->isEndOfWord;
}

// Function to search for a prefix in the Trie
bool startsWith(struct TrieNode *root, const char *prefix) {
    struct TrieNode *current = root;
    int index;

    for (int i = 0; i < strlen(prefix); i++) {
        index = prefix[i] - 'a';

        if (current->children[index] == NULL) {
            return false;  // No word starts with this prefix
        }

        current = current->children[index];
    }

    return true;  // Prefix found
}

int main() {
    // Create a root node
    struct TrieNode *root = createNode();

    // Insert words into the Trie
    insert(root, "hello");
    insert(root, "world");
    insert(root, "hell");

    // Search for words
    printf("Search 'hello': %s\n", search(root, "hello") ? "Found" : "Not Found");
    printf("Search 'hell': %s\n", search(root, "hell") ? "Found" : "Not Found");
    printf("Search 'world': %s\n", search(root, "world") ? "Found" : "Not Found");
    printf("Search 'word': %s\n", search(root, "word") ? "Found" : "Not Found");

    // Check for prefixes
    printf("Prefix 'he': %s\n", startsWith(root, "he") ? "Exists" : "Does not exist");
    printf("Prefix 'wo': %s\n", startsWith(root, "wo") ? "Exists" : "Does not exist");

    return 0;
}
Explanation of Code:
TrieNode Structure:

Each node of the Trie has an array children[] that stores pointers to its child nodes. The array size is 26 for lowercase English letters (a to z).
isEndOfWord is a boolean that marks whether the current node represents the end of a word.
createNode:

This function creates a new Trie node and initializes the children[] array to NULL and isEndOfWord to false.
insert:

This function inserts a word into the Trie. It iterates through each character of the word, checking if the corresponding child node exists; if not, it creates a new node.
After processing all characters, it marks the last node as isEndOfWord = true to signify that the word ends there.
search:

This function checks if a given word exists in the Trie by traversing through the nodes for each character of the word.
If the traversal reaches the end of the word and the isEndOfWord is true, the word exists in the Trie.
startsWith:

This function checks if there is any word in the Trie that starts with the given prefix. It performs a similar search as search, but it doesn't need to check for the isEndOfWord flag. If it can traverse all the characters of the prefix, it returns true.
Sample Output:
sql
Copy code
Search 'hello': Found
Search 'hell': Found
Search 'world': Found
Search 'word': Not Found
Prefix 'he': Exists
Prefix 'wo': Exists
Time and Space Complexity:
Time Complexity:

Insert: O(L), where L is the length of the string being inserted.
Search: O(L), where L is the length of the word being searched.
Prefix Search: O(L), where L is the length of the prefix.
Here, L is the length of the string or prefix, so the operations are very efficient as each operation depends on the length of the string, not the number of strings in the Trie.

Space Complexity:

The space complexity is O(N * L), where N is the number of strings inserted, and L is the average length of the strings.
The Trie stores each character of the string at each level, so its space complexity is proportional to the total number of characters in all the words inserted.
Applications of Tries:
Autocomplete: Tries are widely used in applications such as autocomplete or suggestion engines, where you can quickly find words that start with a given prefix.
Dictionary Search: Tries can efficiently store dictionaries and help with tasks such as spell checking or word searches.
IP Routing: Tries can be used in networks for efficient IP routing and IP lookup.
Search Engines: Search engines use Trie-like structures to store and retrieve indexed terms efficiently.
*/

// Heap
/*
Heap in C
A heap is a special tree-based data structure that satisfies the heap property. It is primarily used to implement efficient priority queues. There are two main types of heaps:

Max-Heap: In a max-heap, the value of the parent node is greater than or equal to the values of its children. The root node contains the maximum value.
Min-Heap: In a min-heap, the value of the parent node is less than or equal to the values of its children. The root node contains the minimum value.
Heap Properties:
Complete Binary Tree: A heap is always a complete binary tree, meaning all levels of the tree are completely filled except possibly the last level, which is filled from left to right.
Heap Order Property:
In a max-heap, the key of each node is greater than or equal to the keys of its children.
In a min-heap, the key of each node is less than or equal to the keys of its children.
Applications of Heap:
Priority Queue: A heap is used to implement a priority queue, where each element is associated with a priority. The heap allows efficient retrieval of the element with the highest (max-heap) or lowest (min-heap) priority.
Heap Sort: A sorting algorithm that builds a heap from the input data and then repeatedly extracts the maximum (for max-heap) or minimum (for min-heap) element to produce a sorted list.
Graph Algorithms: Used in algorithms like Dijkstra's algorithm for shortest path and Prim's algorithm for minimum spanning tree, where a priority queue is needed to extract the smallest (or largest) element efficiently.
Binary Heap Operations:
Insert: Insert a new element into the heap.
Extract (Remove): Remove the root element (maximum or minimum depending on the heap type) and reheapify the tree.
Peek: Return the root element without removing it.
Heapify: Convert an unsorted array into a heap, ensuring that the heap property is maintained.
Basic Structure of a Heap Node:
A heap is usually implemented as an array, where for a node at index i, the left child is located at 2i + 1, and the right child is located at 2i + 2. The parent of a node at index i is located at index (i - 1) / 2.

Max-Heap in C
Code to Implement a Max-Heap:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to heapify a subtree rooted at index i
void heapify(int arr[], int n, int i) {
    int largest = i;   // Initialize largest as root
    int left = 2 * i + 1;  // Left child index
    int right = 2 * i + 2; // Right child index

    // Check if left child exists and is greater than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Check if right child exists and is greater than root
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root, swap and recursively heapify the affected subtree
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Function to build a max-heap from the given array
void buildHeap(int arr[], int n) {
    // Start from the last non-leaf node and heapify each node
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}

// Function to extract the maximum element from the heap
int extractMax(int arr[], int* n) {
    if (*n <= 0) return -1; // Heap is empty

    // The root is the maximum element
    int max = arr[0];

    // Move the last element to the root and heapify
    arr[0] = arr[*n - 1];
    (*n)--;  // Reduce the heap size
    heapify(arr, *n, 0);

    return max;
}

// Function to insert a new element into the heap
void insert(int arr[], int* n, int key) {
    (*n)++;
    int i = *n - 1;
    arr[i] = key;

    // Move the new element up to maintain the heap property
    while (i != 0 && arr[(i - 1) / 2] < arr[i]) {
        swap(&arr[i], &arr[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// Function to print the heap array
void printHeap(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {4, 10, 3, 5, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Build the heap
    buildHeap(arr, n);
    printf("Max-Heap: ");
    printHeap(arr, n);

    // Insert a new element
    insert(arr, &n, 15);
    printf("After inserting 15: ");
    printHeap(arr, n);

    // Extract the maximum element
    int max = extractMax(arr, &n);
    printf("Extracted max: %d\n", max);
    printf("Heap after extraction: ");
    printHeap(arr, n);

    return 0;
}
Explanation of the Code:
swap(): Swaps two elements in the array.
heapify(): Ensures that the subtree rooted at index i satisfies the max-heap property. If the left or right child is larger than the root, it swaps them and recursively heapifies the affected subtree.
buildHeap(): Builds a max-heap by calling heapify() on all non-leaf nodes (from the bottom-up).
extractMax(): Removes and returns the maximum element (root of the heap). It replaces the root with the last element, decreases the heap size, and calls heapify() on the root.
insert(): Inserts a new element into the heap. It first adds the new element at the end of the heap, then moves it up to restore the heap property.
printHeap(): Prints the elements of the heap.
Sample Output:
yaml
Copy code
Max-Heap: 10 5 3 4 1
After inserting 15: 15 10 3 4 1 5
Extracted max: 15
Heap after extraction: 10 5 3 4 1
Heap Sort Algorithm
Heap Sort is a comparison-based sorting algorithm that uses a heap to sort the elements. It first builds a heap from the input data and then extracts the maximum (or minimum) element from the heap and places it at the end of the array.

Heap Sort Code:
c
Copy code
#include <stdio.h>

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements from the heap one by one
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        heapify(arr, i, 0);
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
Heap Sort Output:
c
Copy code
Sorted array: 5 6 7 11 12 13
*/

// 21.Graph
/*
Graph in C
A graph is a collection of nodes (also called vertices) and edges that connect pairs of nodes. Graphs are fundamental data structures used to represent various real-world problems, such as network connections, social networks, or paths in maps.

Key Terminologies in Graphs:
Vertex (Node): A point in the graph representing an entity.
Edge: A connection between two vertices, which may be directed or undirected.
Weighted Graph: A graph where each edge has a weight or cost associated with it.
Directed Graph (Digraph): A graph in which the edges have a direction (i.e., an edge from vertex A to vertex B does not imply an edge from B to A).
Undirected Graph: A graph in which the edges do not have a direction (i.e., an edge from vertex A to vertex B implies an edge from B to A).
Adjacency List: A representation of a graph where each vertex has a list of adjacent vertices (nodes that are directly connected).
Adjacency Matrix: A 2D array representation where the cell at (i, j) is true if there's an edge between vertex i and vertex j.
Degree: The number of edges connected to a vertex.
Graph Representation in C
There are two main ways to represent a graph in C:

Adjacency Matrix: Using a 2D array to store graph connections.
Adjacency List: Using an array of linked lists (more space-efficient for sparse graphs).
1. Graph Representation Using Adjacency Matrix
In an adjacency matrix, if there is an edge from vertex i to vertex j, the matrix at position i, j is set to 1 (or the weight of the edge, in the case of a weighted graph). Otherwise, it is 0.

Adjacency Matrix Example (Undirected Graph):
css
Copy code
   0  1  2  3  4
0 [ 0  1  1  0  0 ]
1 [ 1  0  0  1  0 ]
2 [ 1  0  0  0  1 ]
3 [ 0  1  0  0  1 ]
4 [ 0  0  1  1  0 ]
Here, vertices 0 and 1 are connected, 0 and 2 are connected, and so on.

Code for Graph Representation Using Adjacency Matrix:
c
Copy code
#include <stdio.h>

#define MAX_VERTICES 5

// Graph represented as an adjacency matrix
int adjMatrix[MAX_VERTICES][MAX_VERTICES];

// Function to initialize the graph
void initGraph() {
    for (int i = 0; i < MAX_VERTICES; i++) {
        for (int j = 0; j < MAX_VERTICES; j++) {
            adjMatrix[i][j] = 0; // Initialize with no edges
        }
    }
}

// Function to add an edge to the graph
void addEdge(int u, int v) {
    adjMatrix[u][v] = 1;  // For undirected graph, also set adjMatrix[v][u] = 1
    adjMatrix[v][u] = 1;
}

// Function to print the adjacency matrix
void printGraph() {
    printf("Adjacency Matrix Representation of the Graph:\n");
    for (int i = 0; i < MAX_VERTICES; i++) {
        for (int j = 0; j < MAX_VERTICES; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    initGraph();

    // Adding edges
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(3, 4);
    addEdge(2, 4);

    printGraph();

    return 0;
}
Output:

mathematica
Copy code
Adjacency Matrix Representation of the Graph:
0 1 1 0 0 
1 0 0 1 0 
1 0 0 0 1 
0 1 0 0 1 
0 0 1 1 0 
2. Graph Representation Using Adjacency List
In an adjacency list, each vertex has a list of adjacent vertices. This method is more space-efficient, especially for sparse graphs, as it only stores the edges that exist.

Adjacency List Example (Undirected Graph):
makefile
Copy code
0: 1 -> 2
1: 0 -> 3
2: 0 -> 4
3: 1 -> 4
4: 2 -> 3
Code for Graph Representation Using Adjacency List:
c
Copy code
#include <stdio.h>
#include <stdlib.h>

// Define the node structure for the adjacency list
struct Node {
    int vertex;
    struct Node* next;
};

// Define the graph structure (array of adjacency lists)
struct Graph {
    int numVertices;
    struct Node** adjList;
};

// Function to create a new graph
struct Graph* createGraph(int vertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;
    graph->adjList = (struct Node**)malloc(vertices * sizeof(struct Node*));

    // Initialize each adjacency list as NULL
    for (int i = 0; i < vertices; i++) {
        graph->adjList[i] = NULL;
    }

    return graph;
}

// Function to create a new node
struct Node* createNode(int vertex) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

// Function to add an edge to the graph (undirected)
void addEdge(struct Graph* graph, int src, int dest) {
    // Add edge from src to dest
    struct Node* newNode = createNode(dest);
    newNode->next = graph->adjList[src];
    graph->adjList[src] = newNode;

    // Add edge from dest to src (for undirected graph)
    newNode = createNode(src);
    newNode->next = graph->adjList[dest];
    graph->adjList[dest] = newNode;
}

// Function to print the adjacency list representation of the graph
void printGraph(struct Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        struct Node* temp = graph->adjList[i];
        printf("Vertex %d: ", i);
        while (temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

int main() {
    int vertices = 5;
    struct Graph* graph = createGraph(vertices);

    // Adding edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 3, 4);
    addEdge(graph, 2, 4);

    printGraph(graph);

    return 0;
}
Output:

rust
Copy code
Vertex 0: 2 -> 1 -> NULL
Vertex 1: 3 -> 0 -> NULL
Vertex 2: 4 -> 0 -> NULL
Vertex 3: 4 -> 1 -> NULL
Vertex 4: 3 -> 2 -> NULL
Types of Graphs
Undirected Graph: The edges have no direction. If there is an edge between vertices A and B, you can traverse it both ways.
Directed Graph (Digraph): The edges have a direction. If there is an edge from vertex A to vertex B, you cannot traverse it from B to A unless there is another edge.
Weighted Graph: Each edge has an associated weight or cost.
Unweighted Graph: The edges do not have weights associated with them.
Graph Traversal Algorithms
Breadth-First Search (BFS):

Explores all the neighbors of a vertex before moving on to the next level of vertices.
Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Depth-First Search (DFS):

Explores as far as possible along each branch before backtracking.
Time Complexity: O(V + E).
Graph Traversal Using BFS (Breadth-First Search)
Here’s an implementation of BFS in C:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 5

// Graph structure and adjacency matrix
int graph[MAX_VERTICES][MAX_VERTICES];

// Function to implement BFS
void bfs(int start) {
    int visited[MAX_VERTICES] = {0};
    int queue[MAX_VERTICES], front = 0, rear = 0;
    
    // Mark the start node as visited and enqueue it
    visited[start] = 1;
    queue[rear++] = start;

    while (front != rear) {
        int current = queue[front++];
        printf("%d ", current);

        // Enqueue all adjacent unvisited nodes
        for (int i = 0; i < MAX_VERTICES; i++) {
            if (graph[current][i] == 1 && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    // Initialize graph (example)
    for (int i = 0; i < MAX_VERTICES; i++) {
        for (int j = 0; j < MAX_VERTICES; j++) {
            graph[i][j] = 0;
        }
    }

    // Add edges (undirected graph)
    graph[0][1] = graph[1][0] = 1;
    graph[0][2] = graph[2][0] = 1;
    graph[1][3] = graph[3][1] = 1;
    graph[3][4] = graph[4][3] = 1;
    graph[2][4] = graph[4][2] = 1;

    // Perform BFS starting from vertex 0
    printf("BFS Traversal: ");
    bfs(0);
    
    return 0;
}
Output:

yaml
Copy code
BFS Traversal: 0 1 2 3 4 
*/

// Graph Algorithm
/*
Graph Algorithms
Graphs are a fundamental data structure used to represent networks, relationships, and connections between entities. In a graph, vertices (also called nodes) represent entities, and edges represent the connections between them. Graphs can be directed or undirected, and can contain weighted or unweighted edges.

Graph algorithms are designed to process graphs, find specific information, and solve problems such as shortest paths, connectivity, and traversal.

Types of Graphs
Directed Graph (Digraph): The edges have a direction, i.e., they go from one vertex to another.
Undirected Graph: The edges do not have a direction. If there is an edge between vertex A and vertex B, you can go in both directions.
Weighted Graph: Each edge has a weight or cost associated with it.
Unweighted Graph: The edges do not have any associated weights or costs.
Common Graph Algorithms
1. Depth-First Search (DFS)
Depth-First Search (DFS) is an algorithm for traversing or searching a graph. It starts at a source vertex and explores as far as possible along each branch before backtracking.

Time Complexity: 
𝑂
(
𝑉
+
𝐸
)
O(V+E), where 
𝑉
V is the number of vertices, and 
𝐸
E is the number of edges.
Space Complexity: 
𝑂
(
𝑉
)
O(V), due to the recursion stack or visited array.
Implementation:
c
Copy code
#include <stdio.h>
#include <stdbool.h>

#define MAX 100

int adj[MAX][MAX];  // Adjacency matrix
bool visited[MAX];  // Visited array

void dfs(int node, int V) {
    visited[node] = true;
    printf("%d ", node);

    for (int i = 0; i < V; i++) {
        if (adj[node][i] == 1 && !visited[i]) {
            dfs(i, V);
        }
    }
}

int main() {
    int V, E, u, v;
    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);
    
    // Initializing the adjacency matrix
    for (int i = 0; i < E; i++) {
        printf("Enter edge (u v): ");
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;  // Directed graph (u -> v)
        adj[v][u] = 1;  // Undirected graph (v -> u)
    }
    
    printf("DFS traversal starting from node 0: ");
    dfs(0, V);  // Starting DFS from node 0
    return 0;
}
2. Breadth-First Search (BFS)
Breadth-First Search (BFS) is an algorithm for traversing or searching a graph. It starts at a source vertex and explores all neighbors at the present depth level before moving on to nodes at the next depth level.

Time Complexity: 
𝑂
(
𝑉
+
𝐸
)
O(V+E), where 
𝑉
V is the number of vertices, and 
𝐸
E is the number of edges.
Space Complexity: 
𝑂
(
𝑉
)
O(V), due to the queue and visited array.
Implementation:
c
Copy code
#include <stdio.h>
#include <stdbool.h>
#include <queue>

#define MAX 100

int adj[MAX][MAX];  // Adjacency matrix
bool visited[MAX];  // Visited array

void bfs(int start, int V) {
    std::queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        printf("%d ", node);

        for (int i = 0; i < V; i++) {
            if (adj[node][i] == 1 && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main() {
    int V, E, u, v;
    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    // Initializing the adjacency matrix
    for (int i = 0; i < E; i++) {
        printf("Enter edge (u v): ");
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;  // Directed graph (u -> v)
        adj[v][u] = 1;  // Undirected graph (v -> u)
    }

    printf("BFS traversal starting from node 0: ");
    bfs(0, V);  // Starting BFS from node 0
    return 0;
}
3. Dijkstra's Algorithm (Shortest Path)
Dijkstra's Algorithm is a famous algorithm used to find the shortest paths from a source vertex to all other vertices in a weighted graph. The algorithm works by iteratively selecting the vertex with the smallest tentative distance.

Time Complexity: 
𝑂
(
𝑉
2
)
O(V 
2
 ) with an adjacency matrix or 
𝑂
(
𝐸
log
⁡
𝑉
)
O(ElogV) with a priority queue.
Space Complexity: 
𝑂
(
𝑉
)
O(V).
Implementation:
c
Copy code
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF INT_MAX

int adj[MAX][MAX];  // Adjacency matrix

void dijkstra(int src, int V) {
    int dist[V];
    bool sptSet[V];  // Shortest path tree set

    // Initialize distances and sptSet
    for (int i = 0; i < V; i++) {
        dist[i] = INF;
        sptSet[i] = false;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++) {
        // Find the vertex with minimum distance
        int minDist = INF, u;
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && dist[v] <= minDist) {
                minDist = dist[v];
                u = v;
            }
        }

        sptSet[u] = true;

        // Update the distances of adjacent vertices
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && adj[u][v] != 0 && dist[u] != INF && dist[u] + adj[u][v] < dist[v]) {
                dist[v] = dist[u] + adj[u][v];
            }
        }
    }

    // Print the result
    printf("Vertex\tDistance from Source\n");
    for (int i = 0; i < V; i++) {
        printf("%d\t%d\n", i, dist[i]);
    }
}

int main() {
    int V, E, u, v, w;
    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    // Initializing the adjacency matrix
    for (int i = 0; i < E; i++) {
        printf("Enter edge (u v w): ");
        scanf("%d %d %d", &u, &v, &w);
        adj[u][v] = w;  // Directed graph (u -> v with weight w)
        adj[v][u] = w;  // Undirected graph (v -> u with weight w)
    }

    dijkstra(0, V);  // Find shortest paths from node 0
    return 0;
}
4. Bellman-Ford Algorithm (Shortest Path)
Bellman-Ford is an algorithm for finding the shortest paths in a graph with negative weights. It works by repeatedly relaxing the edges and can detect negative weight cycles.

Time Complexity: 
𝑂
(
𝑉
×
𝐸
)
O(V×E).
Space Complexity: 
𝑂
(
𝑉
)
O(V).
Implementation:
c
Copy code
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF INT_MAX

typedef struct {
    int u, v, weight;
} Edge;

Edge edges[MAX];
int dist[MAX];

void bellmanFord(int V, int E, int src) {
    for (int i = 0; i < V; i++) dist[i] = INF;
    dist[src] = 0;

    // Relax all edges V-1 times
    for (int i = 1; i < V; i++) {
        for (int j = 0; j < E; j++) {
            if (dist[edges[j].u] != INF && dist[edges[j].u] + edges[j].weight < dist[edges[j].v]) {
                dist[edges[j].v] = dist[edges[j].u] + edges[j].weight;
            }
        }
    }

    // Check for negative weight cycle
    for (int j = 0; j < E; j++) {
        if (dist[edges[j].u] != INF && dist[edges[j].u] + edges[j].weight < dist[edges[j].v]) {
            printf("Graph contains negative weight cycle\n");
            return;
        }
    }

    // Print the distances
    printf("Vertex\tDistance from Source\n");
    for (int i = 0; i < V; i++) {
        printf("%d\t%d\n", i, dist[i]);
    }
}

int main() {
    int V, E, u, v, w;
    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    for (int i = 0; i < E; i++) {
        printf("Enter edge (u v w): ");
        scanf("%d %d %d", &u, &v, &w);
        edges[i].u = u;
        edges[i].v = v;
        edges[i].weight = w;
    }

    bellmanFord(V, E, 0);  // Find shortest paths from node 0
    return 0;
}
*/

// 23.Hashing
/*
Hashing in C
Hashing is a technique used to map data of arbitrary size (such as a string or a number) to a fixed size (usually an integer) using a function called a hash function. This technique is widely used in data structures like hash tables, where it allows for efficient data retrieval.

Why Hashing?
Efficient Searching: Hashing allows for efficient searching, insertion, and deletion operations in data structures, typically in O(1) time complexity.
Handling Large Data: Hashing helps handle large datasets by mapping data to a more manageable size (the hash value).
Collisions: A common problem in hashing is when two distinct inputs produce the same hash value. This is called a collision.
Hash Function
A hash function takes an input (like a string or number) and returns a fixed-size integer, which serves as the "address" or "index" where the value is stored in a hash table.

Common Hash Functions
Division Method:

c
Copy code
hash(key) = key % table_size;
Multiplication Method:

c
Copy code
hash(key) = floor(table_size * (key * A % 1))
Where A is a constant (like the golden ratio), and % 1 gives the fractional part.

Polynomial Rolling Hash (used for strings):

c
Copy code
hash(s) = (s[0] * p^0 + s[1] * p^1 + ... + s[n-1] * p^(n-1)) % m
Where p is a constant base (often a small prime number), and m is a modulus.

Hash Table
A hash table is a data structure that uses hashing to store key-value pairs. The idea is to compute the hash value of a key and then store the corresponding value at that index.

Components of a Hash Table:
Buckets or Slots: The hash table is an array of size m, where m is the number of slots (or buckets) in the table. Each slot contains a list or chain of elements.
Collision Resolution: When two keys hash to the same index (collision), we need to handle it using one of the collision resolution methods like chaining or open addressing.
Collision Resolution Techniques
Chaining: Each slot in the hash table contains a linked list (or a dynamic array) of elements. When a collision occurs, the new element is added to the list at that index.
Open Addressing: When a collision occurs, the algorithm searches for the next available slot using a probing sequence (like linear probing or quadratic probing).
Basic Operations in Hash Table
Insertion: Insert a key-value pair into the hash table by computing the hash of the key and storing it in the appropriate bucket or slot.
Searching: To search for a value, compute the hash of the key and check the corresponding slot.
Deletion: To delete a key-value pair, compute the hash of the key and remove it from the corresponding bucket or slot.
Hash Table Implementation in C
Here’s a basic implementation of a hash table using chaining for collision resolution:

c
Copy code
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 10

// Structure to represent a node in the linked list (for chaining)
struct Node {
    int key;
    int value;
    struct Node* next;
};

// Hash table with an array of linked lists (buckets)
struct HashTable {
    struct Node* table[TABLE_SIZE];
};

// Hash function (division method)
int hash(int key) {
    return key % TABLE_SIZE;
}

// Function to create a new node
struct Node* createNode(int key, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

// Initialize the hash table
void initHashTable(struct HashTable* ht) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i] = NULL; // Initialize all slots to NULL
    }
}

// Insert a key-value pair into the hash table
void insert(struct HashTable* ht, int key, int value) {
    int index = hash(key);
    struct Node* newNode = createNode(key, value);
    
    // Insert at the beginning of the linked list (chaining)
    newNode->next = ht->table[index];
    ht->table[index] = newNode;
}

// Search for a value by key in the hash table
int search(struct HashTable* ht, int key) {
    int index = hash(key);
    struct Node* current = ht->table[index];
    
    while (current != NULL) {
        if (current->key == key) {
            return current->value; // Key found
        }
        current = current->next; // Traverse the linked list
    }
    
    return -1; // Key not found
}

// Delete a key-value pair from the hash table
void delete(struct HashTable* ht, int key) {
    int index = hash(key);
    struct Node* current = ht->table[index];
    struct Node* prev = NULL;
    
    // Traverse the linked list
    while (current != NULL) {
        if (current->key == key) {
            if (prev == NULL) {
                ht->table[index] = current->next; // Remove from the front
            } else {
                prev->next = current->next; // Remove from the middle or end
            }
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
    
    printf("Key not found\n");
}

// Display the hash table
void display(struct HashTable* ht) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        struct Node* current = ht->table[i];
        if (current != NULL) {
            printf("Bucket %d: ", i);
            while (current != NULL) {
                printf("(%d, %d) -> ", current->key, current->value);
                current = current->next;
            }
            printf("NULL\n");
        }
    }
}

int main() {
    struct HashTable ht;
    initHashTable(&ht); // Initialize the hash table
    
    // Insert key-value pairs
    insert(&ht, 10, 100);
    insert(&ht, 20, 200);
    insert(&ht, 30, 300);
    insert(&ht, 25, 250);
    
    // Display the hash table
    printf("Hash Table after insertions:\n");
    display(&ht);
    
    // Search for a key
    int key = 20;
    int value = search(&ht, key);
    if (value != -1) {
        printf("Found key %d with value %d\n", key, value);
    } else {
        printf("Key %d not found\n", key);
    }
    
    // Delete a key
    delete(&ht, 25);
    printf("Hash Table after deletion of key 25:\n");
    display(&ht);
    
    return 0;
}
Explanation of the Code:
Hash Function:

The hash() function uses the division method (key % TABLE_SIZE) to compute the index for a given key.
Node Structure:

Each node in the hash table contains a key, a value, and a pointer to the next node (for handling collisions using chaining).
Hash Table Structure:

The hash table is an array of linked lists, where each linked list stores key-value pairs that have the same hash value (i.e., they hash to the same index).
Insert Operation:

The insert() function computes the hash index and inserts the key-value pair at the beginning of the linked list for that index.
Search Operation:

The search() function computes the hash index and searches through the linked list at that index to find the value associated with the key.
Delete Operation:

The delete() function computes the hash index and removes the key-value pair from the linked list at that index.
Display Function:

The display() function prints the contents of the hash table, showing the keys and values at each index.
Sample Output:
yaml
Copy code
Hash Table after insertions:
Bucket 0: (20, 200) -> NULL
Bucket 1: NULL
Bucket 2: NULL
Bucket 3: (30, 300) -> NULL
Bucket 4: NULL
Bucket 5: (25, 250) -> NULL
Bucket 6: NULL
Bucket 7: NULL
Bucket 8: NULL
Bucket 9: (10, 100) -> NULL

Found key 20 with value 200
Hash Table after deletion of key 25:
Bucket 0: (20, 200) -> NULL
Bucket 1: NULL
Bucket 2: NULL
Bucket 3: (30, 300) -> NULL
Bucket 4: NULL
Bucket 5: NULL
Bucket 6: NULL
Bucket 7: NULL
Bucket 8: NULL
Bucket 9: (10, 100) -> NULL
Time Complexity of Hash Table Operations:
Insert: O(1) on average, but can be O(n) in the worst case due to collisions.
Search: O(1) on average, but can be O(n) in the worst case due to collisions.
Delete: O(1) on average, but can be O(n) in the worst case due to collisions.
Advantages of Hashing:
Fast Lookups: Hashing provides constant-time average complexity for search, insert, and delete operations.
Efficient Memory Usage: By hashing, we can map large data to a fixed-size array, optimizing space.
Flexibility: Hash tables are used in many applications like caches, databases, and unique data storage.
Disadvantages:
Collisions: Collisions can degrade performance, especially with poor hash functions or too many elements.
Memory Overhead: Hash tables require additional memory to handle collisions, especially when using chaining or open addressing.
Complexity: Implementing efficient hash functions and collision resolution techniques can be complex.
*/

// Sets
/*
Sets in C (STL Set)
A set is a data structure that is used to store unique elements. The most commonly used set in C++ is the std::set from the Standard Template Library (STL). However, C doesn't provide a built-in set data structure like C++ does. In C, you would typically implement a set using other data structures such as arrays, hash tables, or binary search trees.

Key Characteristics of a Set:
Unique Elements: A set can only contain unique elements, meaning no duplicates are allowed.
Order: By default, elements in a set are stored in sorted order. For unordered sets, you would use an unordered_set, which stores elements in no particular order.
Efficient Operations: Common operations on sets such as insertion, deletion, and searching are optimized.
Insert: Adds an element to the set.
Erase: Removes an element from the set.
Search: Checks whether an element is in the set.
Set Operations in C++ (STL)
In C++, the std::set is an ordered collection of unique elements, typically implemented as a self-balancing binary search tree (BST), like a Red-Black Tree.

Basic Operations:
Insert: Add an element to the set.
Erase: Remove an element from the set.
Find: Search for an element in the set.
Size: Get the number of elements in the set.
Clear: Remove all elements from the set.
Begin and End: Access the first and last elements in the set.
Upper Bound and Lower Bound: Get the next and previous elements (depending on the element's value).
Set in C++ Example:
cpp
Copy code
#include <iostream>
#include <set>

int main() {
    std::set<int> mySet;

    // Inserting elements into the set
    mySet.insert(10);
    mySet.insert(20);
    mySet.insert(5);
    mySet.insert(20);  // Duplicate element (will not be inserted)
    
    // Displaying the set
    std::cout << "Elements of set: ";
    for (int element : mySet) {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    // Searching for an element
    if (mySet.find(10) != mySet.end()) {
        std::cout << "10 is present in the set." << std::endl;
    } else {
        std::cout << "10 is not found in the set." << std::endl;
    }

    // Erasing an element
    mySet.erase(5);
    std::cout << "Set after erasing 5: ";
    for (int element : mySet) {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    // Getting the size of the set
    std::cout << "Size of set: " << mySet.size() << std::endl;

    return 0;
}
Output:
python
Copy code
Elements of set: 5 10 20 
10 is present in the set.
Set after erasing 5: 10 20 
Size of set: 2
Explanation:
We first insert some elements into the set using the insert() function.
Then we use a loop to print all elements of the set. The set automatically sorts elements, so they are printed in ascending order.
Next, we use find() to check if an element exists in the set.
We remove the element 5 using erase(), which automatically handles whether the element exists or not.
Finally, we print the size of the set using size().
Set in C (Manual Implementation Using Hash Table or Array):
In C, you do not have direct access to a set data structure like in C++. To implement a set, you can either use an array with manual checking for duplicates, or more efficiently, a hash table (using arrays or linked lists for collisions).

Simple Implementation Using an Array:
This implementation checks for duplicates manually and ensures that only unique elements are inserted.

c
Copy code
#include <stdio.h>

#define MAX 100

// Function to check if an element exists in the set
int contains(int set[], int size, int element) {
    for (int i = 0; i < size; i++) {
        if (set[i] == element) {
            return 1;  // Element found
        }
    }
    return 0;  // Element not found
}

// Function to insert an element into the set
void insert(int set[], int *size, int element) {
    if (!contains(set, *size, element)) {
        set[*size] = element;
        (*size)++;
    }
}

// Function to display the set
void display(int set[], int size) {
    printf("Set: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", set[i]);
    }
    printf("\n");
}

int main() {
    int set[MAX];
    int size = 0;  // Size of the set

    // Inserting elements into the set
    insert(set, &size, 10);
    insert(set, &size, 20);
    insert(set, &size, 5);
    insert(set, &size, 20);  // Duplicate element (will not be inserted)
    
    // Display the set
    display(set, size);
    
    return 0;
}
Output:
javascript
Copy code
Set: 10 20 5 
Explanation:
We define a set[] array to store elements.
The contains() function checks if an element already exists in the set.
The insert() function adds a new element only if it’s not already in the set.
The display() function prints the elements of the set.
Set Operations in C using Hash Tables:
To implement a hash set in C, you would typically use a hash table to store elements, with collision resolution techniques such as chaining or open addressing.

Insert: Compute the hash of the element and insert it at the appropriate index in the hash table.
Search: Compute the hash and check if the element exists at that index.
Delete: Remove an element using its hash and handle any collisions.
Here is a simple illustration using a hash table:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

// Hash table node structure
struct Node {
    int data;
    struct Node* next;
};

// Hash function
int hash(int key) {
    return key % TABLE_SIZE;
}

// Function to insert a value into the hash table
void insert(struct Node* hashTable[], int key) {
    int index = hash(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = key;
    newNode->next = hashTable[index];
    hashTable[index] = newNode;
}

// Function to search for a value in the hash table
int search(struct Node* hashTable[], int key) {
    int index = hash(key);
    struct Node* current = hashTable[index];
    
    while (current != NULL) {
        if (current->data == key) {
            return 1;  // Found
        }
        current = current->next;
    }
    return 0;  // Not found
}

// Function to display the hash table
void display(struct Node* hashTable[]) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        struct Node* current = hashTable[i];
        if (current != NULL) {
            printf("Index %d: ", i);
            while (current != NULL) {
                printf("%d -> ", current->data);
                current = current->next;
            }
            printf("NULL\n");
        }
    }
}

int main() {
    struct Node* hashTable[TABLE_SIZE] = { NULL };

    // Insert values into the hash table
    insert(hashTable, 10);
    insert(hashTable, 20);
    insert(hashTable, 15);
    insert(hashTable, 25);

    // Display the hash table
    display(hashTable);

    // Search for a value
    printf("Search for 20: %s\n", search(hashTable, 20) ? "Found" : "Not Found");

    return 0;
}
Explanation of Hash Table:
The hash table uses an array of linked lists (for collision resolution).
The hash function maps a value to an index in the table.
Insert adds a node at the start of the linked list at the computed index.
Search looks for the element by traversing the linked list at the given index.
*/

// Disjoint Set Union
/*
Disjoint Set Union (DSU) / Union-Find
The Disjoint Set Union (DSU), also known as Union-Find, is a data structure that is used to manage a collection of disjoint sets. It supports two primary operations efficiently:

Union: Merges two sets into one.
Find: Finds the representative or leader of the set containing a particular element.
The primary use case for DSU is to manage and perform operations on sets that are divided into groups, typically used in algorithms for:

Connected components (e.g., finding connected components in a graph).
Kruskal's algorithm for finding the Minimum Spanning Tree (MST) in a graph.
Checking if elements belong to the same group/set in dynamic connectivity problems.
Basic Operations in DSU
Find:

The find operation determines which set a particular element is a part of. It returns the representative or "root" of the set that contains the element.
If two elements belong to the same set, the find() operation will return the same root.
Union:

The union operation merges two sets into one. It takes two elements, finds the roots of the sets they belong to, and connects the smaller set to the larger one.
Optimization Techniques
To improve the efficiency of the find and union operations, two techniques are commonly used:

Path Compression (for the find operation):
Path compression helps in flattening the structure of the tree whenever find is called. This makes future operations faster as it ensures that all nodes directly point to the root.
Union by Rank / Size (for the union operation):
Union by rank ensures that when two trees are merged, the smaller tree is always attached under the root of the larger tree, keeping the tree as flat as possible.
Time Complexity
Without optimizations: Both find and union operations would take O(n) time in the worst case.
With optimizations (path compression and union by rank/size): Both operations take amortized O(α(n)) time, where α(n) is the inverse Ackermann function, which grows very slowly. For all practical purposes, α(n) is a constant, making these operations nearly constant time.
Union-Find Data Structure Implementation
Here's an implementation of the Union-Find data structure with path compression and union by rank/size in C:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

#define MAX 1000  // Maximum number of elements

// DSU Structure
struct DisjointSet {
    int parent[MAX];
    int rank[MAX];
};

// Initialize the Disjoint Set
void init(struct DisjointSet *ds, int n) {
    for (int i = 0; i < n; i++) {
        ds->parent[i] = i;  // Each element is its own parent initially
        ds->rank[i] = 0;     // Initially, the rank is 0
    }
}

// Find the representative (root) of the set containing 'x'
int find(struct DisjointSet *ds, int x) {
    if (ds->parent[x] != x) {
        // Path compression: make the parent of x point to the root directly
        ds->parent[x] = find(ds, ds->parent[x]);
    }
    return ds->parent[x];
}

// Union of two sets containing 'x' and 'y'
void union_sets(struct DisjointSet *ds, int x, int y) {
    int rootX = find(ds, x);
    int rootY = find(ds, y);

    if (rootX != rootY) {
        // Union by rank: attach the smaller tree under the larger tree
        if (ds->rank[rootX] < ds->rank[rootY]) {
            ds->parent[rootX] = rootY;
        } else if (ds->rank[rootX] > ds->rank[rootY]) {
            ds->parent[rootY] = rootX;
        } else {
            // If the ranks are equal, make one root and increase the rank
            ds->parent[rootY] = rootX;
            ds->rank[rootX]++;
        }
    }
}

// Check if two elements are in the same set
int are_connected(struct DisjointSet *ds, int x, int y) {
    return find(ds, x) == find(ds, y);
}

// Main driver to test the Union-Find
int main() {
    int n = 10;  // Number of elements in the set
    struct DisjointSet ds;

    init(&ds, n);

    union_sets(&ds, 1, 2);
    union_sets(&ds, 2, 3);
    union_sets(&ds, 4, 5);

    printf("Are 1 and 3 connected? %s\n", are_connected(&ds, 1, 3) ? "Yes" : "No");
    printf("Are 1 and 4 connected? %s\n", are_connected(&ds, 1, 4) ? "Yes" : "No");

    union_sets(&ds, 3, 4);
    
    printf("Are 1 and 4 connected now? %s\n", are_connected(&ds, 1, 4) ? "Yes" : "No");

    return 0;
}
Explanation of the Code:
Structure Definition:

parent[MAX]: An array to store the parent of each element. Initially, each element is its own parent (i.e., a leader of its set).
rank[MAX]: An array to store the rank (or depth) of the tree for each set, which helps in union by rank.
Initialization (init):

Each element is initially its own leader (parent) and has rank 0.
Find with Path Compression:

The find() function checks the root (leader) of the set that contains element x. If x is not its own parent, the function recursively calls find() to find the root and performs path compression by making the parent of x point directly to the root.
Union by Rank:

The union_sets() function first finds the roots of x and y using find(). If they belong to different sets, it attaches the smaller tree under the larger tree. If the trees have the same rank, one tree becomes the new root, and the rank of that root is incremented.
Checking Connectivity:

The are_connected() function checks if two elements belong to the same set by comparing their roots. If they have the same root, they are in the same set.
Sample Output:
arduino
Copy code
Are 1 and 3 connected? Yes
Are 1 and 4 connected? No
Are 1 and 4 connected now? Yes
Use Cases of Union-Find:
Kruskal's Algorithm (MST):

Union-Find is crucial for Kruskal's algorithm to efficiently find the Minimum Spanning Tree (MST) in a graph. It helps to check whether adding an edge would create a cycle by checking if the two vertices of the edge belong to the same set.
Dynamic Connectivity:

In problems where you need to dynamically add edges between vertices and check if they are in the same connected component, Union-Find helps in efficiently solving these queries.
Network Connectivity:

DSU can be used to manage network components and check if two devices are connected, and to dynamically merge components when new connections are made.
Image Processing:

It is used in image processing for tasks like finding connected regions or clustering similar pixels.
*/

// Greedy Algorithm
/*
Greedy Algorithms
A Greedy Algorithm is a simple and intuitive approach to solving optimization problems. It builds a solution piece by piece, always choosing the next piece that offers the most immediate benefit (or seems to be the best option at that step) without considering the global problem. In other words, it makes a series of decisions by selecting the locally optimal choice at each step, with the hope that these local choices lead to a globally optimal solution.

Key Characteristics of Greedy Algorithms:
Greedy Choice Property:

A global optimum can be arrived at by selecting the local optimum at each step. It means that a locally optimal solution will lead to a globally optimal solution.
Optimal Substructure:

The problem can be broken down into smaller subproblems that are solved independently. If the solution to a problem can be constructed efficiently from the solutions to its subproblems, then it exhibits optimal substructure.
Irrevocability:

Once a decision is made, it is final. The algorithm does not backtrack or undo decisions once they have been made.
Steps in a Greedy Algorithm:
Initialization: Start with an empty solution set.
Selection: Select the best candidate that looks the most promising at the current step.
Feasibility Check: Ensure that the selection is valid and does not violate any constraints.
Solution Update: Update the current solution by including the selected candidate.
Repeat: Repeat the process until all subproblems have been solved, or the solution is finalized.
Advantages of Greedy Algorithms:
Simple and Efficient: They are typically simpler and faster than other algorithms like dynamic programming or backtracking.
Low Overhead: Greedy algorithms often require fewer resources as they don't need to store intermediate results or recompute them.
Optimal for Some Problems: In certain problems, a greedy approach always leads to the optimal solution.
Disadvantages of Greedy Algorithms:
May Not Always Lead to Optimal Solution: A greedy algorithm doesn't always guarantee the optimal solution, especially if the problem doesn't exhibit both greedy choice and optimal substructure properties.
Problem Specific: It is difficult to generalize greedy approaches; they work well for some problems but not for others.
Greedy Algorithms Examples
Fractional Knapsack Problem:

Given a set of items, each with a weight and a value, and a knapsack with a fixed capacity, the goal is to maximize the total value in the knapsack. In the fractional knapsack problem, we can take fractions of an item.
Greedy Approach: At each step, take the item with the highest value-to-weight ratio until the knapsack is full.

Code Example:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int weight;
    int value;
} Item;

int compare(const void *a, const void *b) {
    double r1 = ((Item*)a)->value / (double)((Item*)a)->weight;
    double r2 = ((Item*)b)->value / (double)((Item*)b)->weight;
    if (r1 < r2) return 1;
    else return -1;
}

double knapsack(Item items[], int n, int W) {
    qsort(items, n, sizeof(Item), compare);
    double totalValue = 0;
    for (int i = 0; i < n; i++) {
        if (W == 0) break;
        if (items[i].weight <= W) {
            totalValue += items[i].value;
            W -= items[i].weight;
        } else {
            totalValue += items[i].value * ((double)W / items[i].weight);
            break;
        }
    }
    return totalValue;
}

int main() {
    Item items[] = {{10, 60}, {20, 100}, {30, 120}};
    int W = 50;  // Knapsack capacity
    int n = sizeof(items) / sizeof(items[0]);
    printf("Maximum value in Knapsack = %.2f\n", knapsack(items, n, W));
    return 0;
}
Output:

java
Copy code
Maximum value in Knapsack = 240.00
Activity Selection Problem:

The problem involves selecting the maximum number of activities that can be performed by a single person, given their start and finish times.
Greedy Approach: Always choose the activity that finishes first and does not overlap with the previously selected activity.

Code Example:

c
Copy code
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int start;
    int finish;
} Activity;

int compare(const void *a, const void *b) {
    return ((Activity*)a)->finish - ((Activity*)b)->finish;
}

void activitySelection(Activity arr[], int n) {
    qsort(arr, n, sizeof(Activity), compare);
    int lastSelected = 0;  // First activity is always selected
    printf("Activity %d: (%d, %d)\n", 1, arr[lastSelected].start, arr[lastSelected].finish);
    for (int i = 1; i < n; i++) {
        if (arr[i].start >= arr[lastSelected].finish) {
            printf("Activity %d: (%d, %d)\n", i + 1, arr[i].start, arr[i].finish);
            lastSelected = i;
        }
    }
}

int main() {
    Activity arr[] = {{1, 3}, {2, 5}, {4, 6}, {7, 8}, {5, 7}};
    int n = sizeof(arr) / sizeof(arr[0]);
    activitySelection(arr, n);
    return 0;
}
Output:

yaml
Copy code
Activity 1: (1, 3)
Activity 2: (4, 6)
Activity 3: (7, 8)
Huffman Coding (for Data Compression):

This algorithm is used for lossless data compression. It assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.
Greedy Approach: Build the Huffman tree by always combining the two nodes with the lowest frequencies.

Dijkstra’s Algorithm (Shortest Path):

Given a graph with weighted edges, Dijkstra’s algorithm finds the shortest path from a source node to all other nodes in the graph.
Greedy Approach: At each step, pick the node with the smallest tentative distance and update the distances of its neighbors.
Coin Change Problem (Greedy for Certain Denominations):

Given a set of coin denominations and an amount, the goal is to find the minimum number of coins needed to make the amount. The greedy algorithm works if the coin denominations are such that the greedy choice leads to the optimal solution.
Greedy Approach: Always choose the largest coin denomination first, then subtract it from the total amount, and repeat.

Code Example:

c
Copy code
#include <stdio.h>

int coinChange(int coins[], int m, int V) {
    int count = 0;
    for (int i = m - 1; i >= 0; i--) {
        while (V >= coins[i]) {
            V -= coins[i];
            count++;
        }
    }
    return count;
}

int main() {
    int coins[] = {1, 5, 10, 25};
    int m = sizeof(coins) / sizeof(coins[0]);
    int V = 63;  // Amount to make change for
    printf("Minimum coins required: %d\n", coinChange(coins, m, V));
    return 0;
}
Output:

swift
Copy code
Minimum coins required: 6
When to Use Greedy Algorithms:
When the problem has the greedy choice property: If you can always make the best local decision that leads to the global optimum, greedy algorithms are a good fit.
When the problem exhibits optimal substructure: If the problem can be broken down into smaller subproblems where solving each subproblem optimally leads to the optimal solution for the entire problem.
When you need a quick, simple solution: Greedy algorithms are often easier to implement and faster than more complex algorithms like dynamic programming or backtracking, but they may not always give the best solution.
*/

// Dynamic Programming
/*
Dynamic Programming (DP)
Dynamic Programming (DP) is a technique used in algorithm design to solve optimization problems by breaking them down into simpler subproblems and solving each subproblem just once, storing the results to avoid redundant work. This method is particularly effective for problems involving overlapping subproblems and optimal substructure.

Key Concepts in Dynamic Programming
Optimal Substructure: A problem exhibits optimal substructure if the optimal solution to the problem can be constructed efficiently from the optimal solutions to its subproblems.

Overlapping Subproblems: In contrast to divide and conquer algorithms (like quicksort), which solve independent subproblems, DP solves subproblems that are re-used multiple times.

Memoization (Top-Down Approach): Memoization involves writing recursive algorithms and storing the results of expensive function calls to avoid redundant calculations. It is often implemented using a cache or a hash map.

Tabulation (Bottom-Up Approach): In this approach, you solve the problem iteratively and store intermediate results in a table. This eliminates recursion overhead and avoids the stack overflow problem.

Steps for Solving Problems with DP
Define the State: Decide what constitutes a subproblem, which is usually expressed in terms of one or more parameters (e.g., dp[i][j]).

Recurrence Relation: Find the relation between the solution of the current problem and the solutions of the subproblems. This helps to compute the solution of a larger problem based on smaller subproblems.

Base Case: Define the base case(s), which are the simplest subproblems that do not require further decomposition.

Compute and Store Results: Solve the problem bottom-up or top-down, and store the results of subproblems to avoid redundant calculations.

Example Problems in Dynamic Programming
1. Fibonacci Series
The Fibonacci sequence is a classic problem that can be solved efficiently using dynamic programming.

Recursive Formula:

𝐹
(
𝑛
)
=
𝐹
(
𝑛
−
1
)
+
𝐹
(
𝑛
−
2
)
F(n)=F(n−1)+F(n−2)
Base Case:

𝐹
(
0
)
=
0
,
𝐹
(
1
)
=
1
F(0)=0,F(1)=1
Solution Using Memoization (Top-Down):
c
Copy code
#include <stdio.h>

int memo[100]; // Array to store results of subproblems

int fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n]; // If already computed, return the value
    memo[n] = fib(n-1) + fib(n-2); // Store the result in memo array
    return memo[n];
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    // Initialize memo array with -1 (indicating uncomputed results)
    for (int i = 0; i <= n; i++) {
        memo[i] = -1;
    }
    
    printf("Fibonacci of %d is %d\n", n, fib(n));
    return 0;
}
Solution Using Tabulation (Bottom-Up):
c
Copy code
#include <stdio.h>

int fib(int n) {
    int dp[n+1];
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2]; // Fill the dp table
    }
    
    return dp[n];
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    printf("Fibonacci of %d is %d\n", n, fib(n));
    return 0;
}
Time Complexity: 
𝑂
(
𝑛
)
O(n)
Space Complexity: 
𝑂
(
𝑛
)
O(n)

2. Knapsack Problem
The Knapsack problem is a classic optimization problem where you are given a set of items, each with a weight and a value, and a knapsack with a fixed capacity. The goal is to determine the maximum value that can be carried without exceeding the knapsack's capacity.

Recursive Formula:

𝑑
𝑝
[
𝑖
]
[
𝑤
]
=
max
⁡
(
𝑑
𝑝
[
𝑖
−
1
]
[
𝑤
]
,
𝑑
𝑝
[
𝑖
−
1
]
[
𝑤
−
𝑤
𝑒
𝑖
𝑔
ℎ
𝑡
[
𝑖
]
]
+
𝑣
𝑎
𝑙
𝑢
𝑒
[
𝑖
]
)
dp[i][w]=max(dp[i−1][w],dp[i−1][w−weight[i]]+value[i])
Here, i represents the item index, and w represents the current weight capacity.

Base Case:

𝑑
𝑝
[
0
]
[
𝑤
]
=
0
for all
 
𝑤
dp[0][w]=0for allw
Solution Using Tabulation (Bottom-Up):
c
Copy code
#include <stdio.h>

int knapsack(int weights[], int values[], int n, int W) {
    int dp[n+1][W+1];
    
    // Initialize the base cases (when i=0 or w=0)
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0; // No items or zero capacity
            else if (weights[i-1] <= w)
                dp[i][w] = (dp[i-1][w] > dp[i-1][w-weights[i-1]] + values[i-1]) ?
                            dp[i-1][w] : dp[i-1][w-weights[i-1]] + values[i-1];
            else
                dp[i][w] = dp[i-1][w]; // Exclude the current item
        }
    }
    
    return dp[n][W]; // Return the maximum value
}

int main() {
    int n, W;
    printf("Enter number of items and knapsack capacity: ");
    scanf("%d %d", &n, &W);
    
    int weights[n], values[n];
    
    printf("Enter weights and values of items:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &weights[i], &values[i]);
    }
    
    printf("Maximum value that can be carried: %d\n", knapsack(weights, values, n, W));
    return 0;
}
Time Complexity: 
𝑂
(
𝑛
×
𝑊
)
O(n×W), where 
𝑛
n is the number of items and 
𝑊
W is the knapsack's capacity.
Space Complexity: 
𝑂
(
𝑛
×
𝑊
)
O(n×W)

3. Longest Common Subsequence (LCS)
The LCS problem involves finding the longest subsequence common to two sequences. It is a classic DP problem used in string matching, bioinformatics, and text comparison.

Recursive Formula:
𝑑
𝑝
[
𝑖
]
[
𝑗
]
=
{
0
if 
𝑖
=
=
0
 or 
𝑗
=
=
0
𝑑
𝑝
[
𝑖
−
1
]
[
𝑗
−
1
]
+
1
if 
𝑠
𝑡
𝑟
1
[
𝑖
−
1
]
=
=
𝑠
𝑡
𝑟
2
[
𝑗
−
1
]
max
⁡
(
𝑑
𝑝
[
𝑖
−
1
]
[
𝑗
]
,
𝑑
𝑝
[
𝑖
]
[
𝑗
−
1
]
)
otherwise
dp[i][j]= 
⎩
⎨
⎧
​
  
0
dp[i−1][j−1]+1
max(dp[i−1][j],dp[i][j−1])
​
  
if i==0 or j==0
if str1[i−1]==str2[j−1]
otherwise
​
 
Solution Using Tabulation (Bottom-Up):
c
Copy code
#include <stdio.h>
#include <string.h>

int lcs(char* str1, char* str2, int m, int n) {
    int dp[m+1][n+1];
    
    // Fill the dp table
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = (dp[i-1][j] > dp[i][j-1]) ? dp[i-1][j] : dp[i][j-1];
        }
    }
    
    return dp[m][n]; // Return the length of the longest common subsequence
}

int main() {
    char str1[] = "AGGTAB";
    char str2[] = "GXTXAYB";
    
    int m = strlen(str1);
    int n = strlen(str2);
    
    printf("Length of Longest Common Subsequence: %d\n", lcs(str1, str2, m, n));
    return 0;
}
Time Complexity: 
𝑂
(
𝑚
×
𝑛
)
O(m×n), where 
𝑚
m and 
𝑛
n are the lengths of the two strings.
Space Complexity: 
𝑂
(
𝑚
×
𝑛
)
O(m×n)

General Approach to Dynamic Programming
Identify subproblems: Break the problem into smaller subproblems.
Define the state: Represent the subproblem using an array or table.
Find a recurrence relation: Derive how to solve the problem in terms of smaller subproblems.
Fill the table (or memoize): Solve the subproblems iteratively or recursively.
Retrieve the answer: The solution to the original problem will be in the last cell of the DP table (or memoization structure).
*/

// Number Theory
/*
Number Theory
Number Theory is a branch of pure mathematics devoted to the study of integers and more specifically to the properties and relationships between numbers, especially prime numbers. It deals with topics like divisibility, prime factorization, greatest common divisors (GCD), least common multiples (LCM), and various number-theoretic functions. Number theory is one of the oldest branches of mathematics and has applications in cryptography, computer science, and other fields.

Key Concepts in Number Theory
1. Divisibility and Divisibility Rules
A number 
𝑎
a is divisible by 
𝑏
b if there is no remainder when 
𝑎
a is divided by 
𝑏
b, i.e., 
𝑎
m
o
d
 
 
𝑏
=
0
amodb=0.
Example: 18 is divisible by 3, because 
18
m
o
d
 
 
3
=
0
18mod3=0.
Common divisibility rules:

Divisibility by 2: A number is divisible by 2 if its last digit is even.
Divisibility by 3: A number is divisible by 3 if the sum of its digits is divisible by 3.
Divisibility by 5: A number is divisible by 5 if its last digit is 0 or 5.
2. Prime Numbers
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Examples: 2, 3, 5, 7, 11.
Sieve of Eratosthenes: An efficient algorithm to find all primes up to a given limit 
𝑛
n.
3. Greatest Common Divisor (GCD)
The greatest common divisor (GCD) of two integers 
𝑎
a and 
𝑏
b is the largest integer that divides both 
𝑎
a and 
𝑏
b.
The Euclidean Algorithm is used to compute the GCD of two numbers efficiently:
GCD
(
𝑎
,
𝑏
)
=
GCD
(
𝑏
,
𝑎
m
o
d
 
 
𝑏
)
GCD(a,b)=GCD(b,amodb)
This process repeats until 
𝑏
=
0
b=0, at which point 
𝑎
a is the GCD.
Code Example (Euclidean Algorithm):

c
Copy code
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
4. Least Common Multiple (LCM)
The least common multiple (LCM) of two integers 
𝑎
a and 
𝑏
b is the smallest integer that is divisible by both 
𝑎
a and 
𝑏
b.
The relationship between GCD and LCM is:
LCM
(
𝑎
,
𝑏
)
=
∣
𝑎
×
𝑏
∣
GCD
(
𝑎
,
𝑏
)
LCM(a,b)= 
GCD(a,b)
∣a×b∣
​
 
Code Example (LCM using GCD):

c
Copy code
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}
5. Modular Arithmetic
Modular arithmetic involves performing arithmetic operations on numbers with respect to a modulus.
For two integers 
𝑎
a and 
𝑏
b, we say 
𝑎
≡
𝑏
(
m
o
d
𝑚
)
a≡b(modm) if 
𝑎
a and 
𝑏
b leave the same remainder when divided by 
𝑚
m.
Properties of Modular Arithmetic:

(
𝑎
+
𝑏
)
m
o
d
 
 
𝑚
=
[
(
𝑎
m
o
d
 
 
𝑚
)
+
(
𝑏
m
o
d
 
 
𝑚
)
]
m
o
d
 
 
𝑚
(a+b)modm=[(amodm)+(bmodm)]modm
(
𝑎
×
𝑏
)
m
o
d
 
 
𝑚
=
[
(
𝑎
m
o
d
 
 
𝑚
)
×
(
𝑏
m
o
d
 
 
𝑚
)
]
m
o
d
 
 
𝑚
(a×b)modm=[(amodm)×(bmodm)]modm
Modular Exponentiation:

Given 
𝑎
a, 
𝑏
b, and 
𝑚
m, calculate 
𝑎
𝑏
m
o
d
 
 
𝑚
a 
b
 modm. This is an efficient way of calculating large powers under modulo.
Exponentiation by Squaring: A technique to compute 
𝑎
𝑏
m
o
d
 
 
𝑚
a 
b
 modm in 
𝑂
(
log
⁡
𝑏
)
O(logb) time.
Code Example (Modular Exponentiation):

c
Copy code
int mod_exp(int a, int b, int m) {
    int result = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            result = (result * a) % m;
        }
        a = (a * a) % m;
        b /= 2;
    }
    return result;
}
6. Prime Factorization
The prime factorization of a number is expressing it as the product of prime numbers. For example:
36
=
2
2
×
3
2
36=2 
2
 ×3 
2
 
Code Example (Prime Factorization):

c
Copy code
void prime_factors(int n) {
    while (n % 2 == 0) {
        printf("%d ", 2);
        n = n / 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            printf("%d ", i);
            n = n / i;
        }
    }
    if (n > 2) {
        printf("%d ", n);
    }
}
7. Fermat's Little Theorem
This theorem is a fundamental result in number theory used in cryptography and primality testing.
Statement: If 
𝑝
p is a prime number and 
𝑎
a is an integer not divisible by 
𝑝
p, then:
𝑎
𝑝
−
1
≡
1
(
m
o
d
𝑝
)
a 
p−1
 ≡1(modp)
Application: Fermat's Little Theorem is used in primality tests like the Miller-Rabin primality test.

8. Chinese Remainder Theorem
The Chinese Remainder Theorem (CRT) allows solving systems of simultaneous modular equations.
The theorem provides a way to find an integer 
𝑥
x that satisfies:
𝑥
≡
𝑎
1
(
m
o
d
𝑚
1
)
,
𝑥
≡
𝑎
2
(
m
o
d
𝑚
2
)
,
…
,
𝑥
≡
𝑎
𝑘
(
m
o
d
𝑚
𝑘
)
x≡a 
1
​
 (modm 
1
​
 ),x≡a 
2
​
 (modm 
2
​
 ),…,x≡a 
k
​
 (modm 
k
​
 )
where the moduli 
𝑚
1
,
𝑚
2
,
…
,
𝑚
𝑘
m 
1
​
 ,m 
2
​
 ,…,m 
k
​
  are pairwise coprime.
9. Euler’s Totient Function (
𝜙
(
𝑛
)
ϕ(n))
The Euler's totient function 
𝜙
(
𝑛
)
ϕ(n) counts the number of integers from 1 to 
𝑛
n that are coprime with 
𝑛
n.
For a prime number 
𝑝
p, 
𝜙
(
𝑝
)
=
𝑝
−
1
ϕ(p)=p−1.
For a number 
𝑛
n with prime factorization 
𝑛
=
𝑝
1
𝑒
1
×
𝑝
2
𝑒
2
×
…
n=p 
1
e 
1
​
 
​
 ×p 
2
e 
2
​
 
​
 ×…, the totient function is calculated as:
𝜙
(
𝑛
)
=
𝑛
×
(
1
−
1
𝑝
1
)
×
(
1
−
1
𝑝
2
)
×
…
ϕ(n)=n×(1− 
p 
1
​
 
1
​
 )×(1− 
p 
2
​
 
1
​
 )×…
Code Example (Euler’s Totient Function):

c
Copy code
int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            result -= result / i;
        }
    }
    if (n > 1) {
        result -= result / n;
    }
    return result;
}
Applications of Number Theory
Cryptography:

Number theory is the backbone of modern cryptography. Algorithms like RSA, Diffie-Hellman, and Elliptic Curve Cryptography (ECC) are based on number-theoretic concepts such as modular exponentiation, prime factorization, and Euler's totient function.
Hashing:

Prime numbers are used in hashing algorithms to minimize collisions in hash tables. The choice of a prime number for the size of a hash table can make hashing more efficient.
Computer Science:

Many algorithms in computer science (e.g., fast exponentiation, sieve algorithms, primality testing, modular arithmetic) rely on number theory concepts.
Error Detection and Correction:

Techniques in error detection, such as CRC (Cyclic Redundancy Check) and Hamming codes, use number-theoretic concepts to detect and correct errors in data transmission.
Algorithm Optimization:

Many advanced algorithms in areas like searching, sorting, and dynamic programming use number-theoretic techniques to improve efficiency.
*/

// Convex Hull
/*
Convex Hull
In computational geometry, the Convex Hull of a set of points is the smallest convex polygon that contains all the points in the set. Think of it as the shape formed by stretching a rubber band around the outermost points, then releasing it. The rubber band will form the convex hull. The convex hull is a fundamental concept in computational geometry and is widely used in fields like computer graphics, pattern recognition, and geographic information systems (GIS).

Properties of Convex Hull
The convex hull is always a convex polygon.
The convex hull contains all the input points on its boundary or inside it.
The convex hull can have fewer points than the original set of points if some points lie inside the convex hull.
Applications of Convex Hull
Collision detection in computer graphics and gaming (simplifies the objects involved in collision checks).
Pattern recognition and cluster analysis in machine learning.
Geographical information systems (GIS) for finding boundaries of a region.
Pathfinding algorithms in robotics or games.
Computational geometry for solving problems like finding the closest pair of points, convexity testing, and more.
Convex Hull Algorithms
There are several algorithms for finding the convex hull of a set of points. The most common algorithms include:

1. Graham's Scan Algorithm
Time Complexity: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)
Space Complexity: 
𝑂
(
𝑛
)
O(n)
Steps:

Sort the points: First, find the point with the lowest y-coordinate (and leftmost if there are ties), which will serve as the "pivot" or "anchor" point. Then, sort the remaining points based on the polar angle with respect to the anchor point.
Create the Hull: Starting from the sorted points, iterate through the points and add them to the convex hull. For each new point, check if adding it causes a left turn or right turn. If it forms a right turn, pop the previous point from the hull. This ensures that the hull remains convex.
Code Example (Graham's Scan):

c
Copy code
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

// A utility function to find orientation of ordered triplet (p, q, r).
// The function returns following values:
// 0 -> p, q and r are collinear
// 1 -> Clockwise
// 2 -> Counterclockwise
int orientation(struct Point p, struct Point q, struct Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;  // collinear
    return (val > 0) ? 1 : 2; // 1 -> clockwise, 2 -> counterclockwise
}

// A function to return the convex hull of a set of n points.
// The function uses the Graham's scan algorithm.
void convexHull(struct Point points[], int n) {
    // Sort points lexicographically by x, then by y coordinate.
    std::sort(points, points + n, [](Point a, Point b) {
        return (a.x == b.x) ? a.y < b.y : a.x < b.x;
    });

    // Create an empty stack and push the first three points to it
    std::vector<Point> hull;
    hull.push_back(points[0]);
    hull.push_back(points[1]);
    hull.push_back(points[2]);

    // Process remaining points
    for (int i = 3; i < n; i++) {
        // Keep popping from the stack while the angle formed by
        // points next-to-top, top, and points[i] is not a counterclockwise turn
        while (hull.size() >= 2 && orientation(hull[hull.size()-2], hull[hull.size()-1], points[i]) != 2)
            hull.pop_back();
        hull.push_back(points[i]);
    }

    // Print the points in the convex hull
    for (auto& p : hull)
        printf("(%d, %d)\n", p.x, p.y);
}
2. Jarvis March (Gift Wrapping Algorithm)
Time Complexity: 
𝑂
(
𝑛
ℎ
)
O(nh) where 
ℎ
h is the number of points on the convex hull.
Space Complexity: 
𝑂
(
𝑛
)
O(n)
Steps:

Find the leftmost point (the point with the smallest x-coordinate).
Iterate through the points: Starting from the leftmost point, choose the point that makes the smallest counterclockwise angle with the current point.
Repeat: Add the selected point to the convex hull, and repeat the process until you return to the starting point.
Code Example (Jarvis March):

c
Copy code
#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x, y;
};

// A utility function to find orientation of ordered triplet (p, q, r).
int orientation(struct Point p, struct Point q, struct Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;  // collinear
    return (val > 0) ? 1 : 2; // 1 -> clockwise, 2 -> counterclockwise
}

void convexHull(struct Point points[], int n) {
    // Find the leftmost point
    int leftmost = 0;
    for (int i = 1; i < n; i++) {
        if (points[i].x < points[leftmost].x) {
            leftmost = i;
        }
    }

    int p = leftmost;
    do {
        // Add current point to result
        int q = (p + 1) % n;
        
        // Find the point q such that orientation(p, q, x) is counterclockwise
        // for all points x. The idea is to keep track of the point
        // that is farthest from the line segment from p to q.
        for (int i = 0; i < n; i++) {
            if (orientation(points[p], points[i], points[q]) == 2)
                q = i;
        }

        // Now q is the most counterclockwise point in relation to p
        p = q;
    } while (p != leftmost);  // While we do not come back to the starting point
}
3. QuickHull Algorithm
Time Complexity: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) on average.
Space Complexity: 
𝑂
(
𝑛
)
O(n)
QuickHull works similarly to QuickSort and is based on divide and conquer. The algorithm works by recursively dividing the point set into two subsets: points on the left and right side of the line formed by the farthest points.

Convex Hull Algorithm Comparison
Algorithm	Time Complexity	Space Complexity	Best Use Case
Graham's Scan	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
)
O(n)	Sorted input, general cases
Jarvis March	
𝑂
(
𝑛
ℎ
)
O(nh)	
𝑂
(
𝑛
)
O(n)	Small convex hull, fewer points
QuickHull	
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn)	
𝑂
(
𝑛
)
O(n)	Randomly distributed points
Practical Example
Let’s consider a set of points like this:

scss
Copy code
(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 3)
The convex hull of these points would include the points forming the outer boundary of the set. For example, using the Graham's scan or Jarvis march, the convex hull might contain the points:

scss
Copy code
(0, 0), (1, 1), (4, 4), (3, 3)
These form the polygon that encloses all other points, which is the convex hull.
*/