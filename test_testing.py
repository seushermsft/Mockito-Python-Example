import unittest
from mockito import when, mock, unstub, verify, ANY

import main

# To run this, run 'pytest'
# Pytest searches for files beginning with 'test_' and calls their main function.
# unittest.main() finds classes that inherit from 'unittest.TestCase', and run all functions whose names starts with 'test_'
class Test(unittest.TestCase):

    def test_one(self):

        # Create an instance of the Testing class - we could fully mock this instead of creating an instance of Testing, but this is nicer
        test = main.Testing()

        # Expected return value for stubbed method
        expectedOne = "thisIsOne"
        expectedTwo = "thisIsTwo"
        expectedThree = "thisIsThree"

        when(main.Testing).doSomething("one").thenReturn(expectedOne)
        when(main.Testing).doSomething("two").thenReturn(expectedTwo)
        when(main.Testing).doSomething("three").thenReturn(expectedThree)

        # Simulate an error for this specific input - This might trigger function error-handling logic
        when(main.Testing).doSomething("four").thenRaise(ValueError)

        # Call doSomething and verify that we got the expected output
        resultOne = test.doSomething("one")
        self.assertEqual(expectedOne, resultOne)

        # Call doSomething and verify that we got the expected output
        resultTwo = test.doSomething("two")
        self.assertEqual(expectedTwo, resultTwo)
        
        # call Tester.run() and verify that we got the expected output
        resultThree = main.Tester().run(test, "three")
        self.assertEqual(expectedThree, resultThree)

        # Since we're learning, let's see how to verify a function raises an exception we expect it to
        with self.assertRaises(ValueError):
            print(test.doSomething("four"))

        # Verify that we only called doSomething 4 times (once from Tester().run()). 
        # Generally, you would use this to ensure the function you passed your mock into called the mocked
        # function the correct number of times 
        # (ex: perhaps the function is called once for each object in a list)
        # You can change the value passed to 'times' to see a failure
        # We pass 'ANY' to doSomething to verify that, overall, the function was called 4 times.
        # We could pass in a specific value for the parameter and verify how many times it was called with a give parameter value
        verify(main.Testing, times=4).doSomething(ANY)

        # Uncomment to cause a test failure due to calling with an unstubbed parameter
        #test.doSomething("five")

        # remove all stubs - This may not be needed since we stub within a single function, but I haven't tested
        unstub()

if __name__ == '__main__':
    unittest.main()