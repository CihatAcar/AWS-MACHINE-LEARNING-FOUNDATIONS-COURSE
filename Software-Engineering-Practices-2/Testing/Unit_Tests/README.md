# Unit Tests
* We want to test our functions in a way that is repeatable and automated. 
* Ideally, we'd run a test program that runs all our unit tests and cleanly lets us know which ones failed and which ones succeeded. 
* Fortunately, there are great tools available in Python that we can use to create effective unit tests!


# Unit test advantages and disadvantages
* The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved. 
* They don't require access to databases, APIs, or other external sources of information. 
* However, passing unit tests isn’t always enough to prove that our program is working successfully. 
* To show that all the parts of our program work with each other properly, communicating and transferring data between them correctly, we use integration tests. 
* When you start building larger programs, you will want to use integration tests as well.

# Unit Testing Tools
* To install pytest, run pip install -U pytest in your terminal.

* Create a test file starting with test_.
* Define unit test functions that start with test_ inside the test file.
* Enter pytest into your terminal in the directory of your test file and it detects these tests for you.
* test_ is the default; if you wish to change this, you can learn how in this pytest configuration.

* In the test output, periods represent successful unit tests and Fs represent failed unit tests. 
* Since all you see is which test functions failed, it's wise to have only one assert statement per test. Otherwise, you won't know exactly how many tests failed or which tests failed.

* Your test won't be stopped by failed assert statements, but it will stop if you have syntax errors.