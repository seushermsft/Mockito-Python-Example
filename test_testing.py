import unittest
from mockito import when, mock, unstub

import main

# To run this, run 'pytest'
# Pytest searches for files beginning with 'test_' and calls their main function.
# unittest.main() finds classes that inherit from 'unittest.TestCase', and run all functions whose names starts with 'test_'
class Test(unittest.TestCase):

    def test_one(self):

        # Expected return value for stubbed method
        expectedOne = "thisIsOne"
        expectedTwo = "thisIsTwo"

        when(main.Testing).doSomething("one").thenReturn(expectedOne)
        when(main.Testing).doSomething("two").thenReturn(expectedTwo)

        # Simulate an error for this specific input - This might trigger function error-handling logic
        when(main.Testing).doSomething("three").thenRaise(ValueError)
        
        # Create an instance of the Testing class - we could fully mock this instead of using Testing, but this is nicer
        test = main.Testing()

        # Call doSomething and verify that we got the expected output
        resultOne = test.doSomething("one")
        self.assertEqual(expectedOne, resultOne)

        # Call doSomething and verify that we got the expected output
        resultTwo = test.doSomething("two")
        self.assertEqual(expectedTwo, resultTwo)
        
        # Since we're learning, let's see how to verify a function raises an exception we expect it to
        with self.assertRaises(ValueError):
            print(test.doSomething("three"))
        
        # Uncomment to cause a test failure due to calling with an unstubbed parameter
        #test.doSomething("four")

        # remove all stubs - This may not be needed since we stub within a single function, but I haven't tested
        unstub()

if __name__ == '__main__':
    unittest.main()