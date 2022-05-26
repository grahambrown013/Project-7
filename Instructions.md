# Project-7

Goal:
This project is designed to reinforce the techniques around Python lists, dictionaries, and files.

Description:
The program will consist of many functions related to “comma-separated values”.

Extra-Credit Opportunities
Check Gradescope for opportunities to earn extra credit for getting things working early.

Forbidden:
Your program may not use any techniques or Python features forbidden below. Do not use the following list-related functionality:

Do not use any string methods other than lower.

Do not “import” any functionality into your code.

Do not use list slicing.

Do not use any techniques not covered in class.

You may use list’s append method

Violating these rules will sacrifice correctness credit.

Functional Requirements:
This program requires implementation of all of the user-defined functions outlined below.

Each function description is followed by assertions that should hold true for your implmentation.

def separate_by_commas(string):
This function separates a string into a list of strings based on commas. It returns that list.

The only complication is that the initial string may quote things by putting them inside a pair of double-quotation marks. Commas inside such double-quotes are ignored and do not separate the initial string.

Quoted portions of the string cannot contain a quotation mark. All quotation marks either begin or end a quoted portion.

assert separate_by_commas("a,b,c") == ["a", "b", "c"]
assert separate_by_commas('"a,b",c') == ["a,b", "c"]
assert separate_by_commas(',"b,c"') == ["", "b,c"]
assert separate_by_commas('a,"b,c",d') == ["a", "b,c", "d"]
def create_comma_separated_string(list_of_strings):
This function is the inverse of the previous function. It takes a list of strings and creates a comma-separated string as its return value.

The function will add quotation marks to any string that contains a comma.

Your code may assume that none of the initial strings contains quotation marks.

assert create_comma_separated_string(["a", "b", "c"]) == "a,b,c"
assert create_comma_separated_string(["a", "b,c", ""]) == 'a,"b,c",'
def csv_file_to_list_of_lists(filename):
This function reads in a file based on its filename. Each comma-separated line of the file will become a list of strings. And, therefore, the whole file will become a list of those lists.

It should do the following:

Open and read the file into one giant string. Close the file its done reading.
Separate that string into a list of lines using .split("\n")
Use separate_by_commas to turn each of those lines into a list of strings.
If there are any problems opening or reading the file, it should return None. Otherwise, it should return a list of those lists of strings.
This file:

a,b
x
would become [ ["a", "b"], ["x"] ].

def list_of_lists_to_csv_file(filename, list_of_lists):
This function is basically the inverse of the preceding function. It takes a list of lists of strings and writes it to the named file as comma-separated values.

The code should do the following:

Open the named file for writing. Your code may assume that this will succeed if done properly.
Encode each list using create_comma_separated_string
Write each line to the opened file, using a newline (\n) between lines. (Note that this is between lines, not after them.)
Close the file after it’s done accepting writes.
It should return the number of lines of output it generated.
def csv_file_to_list_of_dictionaries(filename):
This function reads a comma-separated file that is encoded to represent dictionaries. It returns a list of those dictionaries.

The file is formatted/encoded just like the files for the list-of-lists functions above. (That is a hint on how to save yourself some work.)

What makes these files more interesting is that the first row of the file is the list of keys that are are associated with the values in the same column below it in the file.

So, this file:

name,number
Alice,555-1234
Bob,555-9999
would represent this list of dictionaries:

[ { "name": "Alice", "number": "555-1234"}, { "name": "Bob", "number": "555-9999" } ]
Note that the list of dictionaries is one shorter than the list of lines in the CSV file because the first row is special.

def list_of_dictionaries_to_csv_file(filename, list_of_dictionaries):
This function is essentially the inverse of the previous function. Given a list of dictionaries, it creates a file that encodes those dictionaries in the format described above.

A few things to note:

Your code may assume that all of the dictionaries have exactly the same keys.
Your code must output the fields in the same order as the keys of the first dictionary in the list. I.e., your code needs to use the ordering given by for key in dictionaries[0]:.
This function will return the number of lines of output that it generates. If there are no dictionaries, it should return None.
Testing file-based programs
Developing and testing file-based programs is more complicated than simple assert-based development we’ve done previously.

I will provide some sample input files. I suggest doing the following:

Write the code to read in a CSV file and simply print the results to see if they look right.
Once convinced the output looks right, use the corresponding function to write that same data to a different file. Check if the results are what you expect. If not, then something is probably wrong.
Advice:
Start early.
Do the first two non-file functions first. They are needed for all subsequent functions.
Do the functions in pairs: the list-of-lists first, and then the list-of-dictionaries.
Read the requirements carefully, including the forbidden/required elements. Note that there are per-function requirements and some program-wide requirements.
Do one function at a time, get it working, and then move on the the next function.
Start early.
Code Style Requirements:
Please see the Style Guide posted to D2L for docstring formatting requirements. It is located under Content > Table of Contents > Project Information > Project Style Guide

This link may work: Project Style Guide

Grading:
The project will be graded on passing all the test cases (70%) and adherence to expectations (30%) (e.g., docstring format, avoiding forbidden things).

NOTE: There are 6 problems worth 14 points each in the autograder, so solving all of them is 84 points. It’s an opportunity to get extra credit for doing all of them.

Turn-In Process:
What to turn in: A single file called, “separated.py”, that includes the functions described above. (The grading system is case-sensitive, so make sure your filename is in all lower-case letters.)

Where to turn it in: https://gradescope.com/

Note that the test cases are automatically run when you submit your program. If you wish to resubmit your program (prior to the deadline), you may do so as many times as you like. I.e., you can fix bugs and resubmit.

NOTE: This assignment is NOT turned in via D2L. It must be turned in via Gradescope.
Late Policy
Projects are not accepted late.

Due Date
Apr 21, 2022 8:00 PM
Attachments
files.zip (844 Bytes)			
Completion Date: Apr 21, 2022 8:00 PM
