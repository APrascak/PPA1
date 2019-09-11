# PPA1 - CIS4930 SW Testing for Continuous Development
***
Name: Alexander Prascak  
UFID: 2299-5066

### Naming and organizational conventions
Language: Python 3  
Framework: unittest  
  
All of the functions are defined in ppa1.py.  
The command line interface also runs through the ppa1.py file.  
  
Each of the functions have their own respective files for their unit tests. The naming convention for these files is test_*function_name*.py.  
Within each file is the class for the unit tests and then the assertions for each test. The tests are named test_condition. Where the condition is the specific case of the function that is being tested.

### Setup and execution instructions
Language: Python 3.7.4 [Download Here](https://www.python.org/downloads/)  
OS: macOS Mojave 10.14.6  
The built in *unittest* framework is used. It is imported within each testing file. No other installations required.
  
To ensure that you have the proper Python version installed run: `python3 --version`
You should see `Python 3.7.4` as the output.

To run each the unit tests for each function, simply run: `python3 -m unittest -v test_function_name.py`
`-v` can be removed for a less detailed test summary.
  
To run the command line application: `python3 ppa1.py`
Here is the UI:
```
PRASCAK PPA1 PROGRAM MENU
Enter # for function selection.
0. Exit Program
1. Calculate BMI
2. Calculate Retirement Age
3. Calculate Shortest Distance
4. Email Verifier
5. Split the Tip
Function #: 
```

### Screenshots of tests passing
![BMI Testing](https://github.com/APrascak/PPA1/blob/master/screenshots/test_bmi_ss.png?raw=true)
  
![Retirement Testing](https://github.com/APrascak/PPA1/blob/master/screenshots/test_retirement_ss.png?raw=true)
  
![Shortest Distance Testing](https://github.com/APrascak/PPA1/blob/master/screenshots/test_shortest_distance_ss.png?raw=true)
  
![Email Verifier Testing](https://github.com/APrascak/PPA1/blob/master/screenshots/test_email_verifier_ss.png?raw=true)
  
![Split Testing](https://github.com/APrascak/PPA1/blob/master/screenshots/test_calculator_tip_ss.png?raw=true)

### Test coverage report
I utilized the "coverage.py" coverage report tool.
  
![Coverage report](https://github.com/APrascak/PPA1/blob/master/screenshots/Screen%20Shot%202019-09-10%20at%2010.24.06%20PM.png?raw=true)
  
The coverage report would not test lines that were inside of functions or based on inputs form the command line, so the coverage report would not go higher than 28% regardless of how I adjusted the testing files or function definitions. I need to find a more accurate way of determining test coverage.


### Conclusion
Having never worked with TDD before, I was really happy with how it worked out. I feel like it definitely made the development process a lot smoother and easier to think through. I wasn't worried about testing my code after finalizing an algorithm, I could test my code along the path of developing my code. This made a less stressful environment where I could focus more on actual development.  
  
Unit testing & TDD are definitely very useful to practical software development. Having already defined what my code would need to do beforehand was very useful in figuring out exactly what I needed my code to accomplish. Although Unit Testing in itself consumes time that could be spent on development, it made the development time significantly shorter.  
  
TDD is very beneficial for development in my experience. It makes the overall development process much more organized, while still maintaining a lot of flexibility. One of the strongest benefits of it in my opinion is that it prevents testing bias. I couldn't write unit tests to fit my code, as they were already written before I even started development. One of the downfalls is that with much more loosely defined requirements, it can become very difficult to figure out how to make unit tests for your code. Without a solid understanding of your system requirements, TDD seems to fall apart.
  
The video for functionality is `ppa1_functions_prascak.mov`  
The video for TDD evidence is `ppa1_rgr_evidence.mov`