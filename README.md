# 2k Factorial Design of Experiments Code
This code will run the analysis for a 2k Factorial design of experiments test with 1 to 26 variable parameters of interest.

You can choose to run the analysis code with results put directly into the code in the variable "test" on line 73 or to read in a .txt file with saved values with the "filename" on line 77.

* It is important that your testing order match up with the order in the code. The pattern is described in the comments of the code, but in general starts at the all low (-) case and alternates sign based on the order of the column number (e.g. the 1st column switches low to high with every test, the 2nd column switches low to high with every two tests, etc.). The testing matrix can be seen by uncommenting out line 98 (# print(tm)).

I have run this code with the following versions of software/libraries:
  Python	  3.8.8
  pyDOE2    1.3.0
  spyder    5.3.3
