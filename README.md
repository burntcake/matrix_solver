# matrix_solver
Given a n * m matrix, matrix.py will read the matrix into a string, reading from top to bottom and left to right.
All contiguous groups of non-alpha numeric characters between two alphanumeric characters will be replaced with a space.
No if conditions are allowed.

## Algorithm Design
The first part of the problem is simple the matrix is read into a string by iterating through the columns and rows(columns in the outer for loop).
Then the solution can be generated using regular experessions, in particular using re.sub() to match and then replace the correct characters.
The expression is given below:
re.sub(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])',' ', string)
The first argument is the regular expression used to match the group of characters to be replaced, the second argument the string that they will be replaced with(space)
and third the string to be decoded.

### The regular expression
Our main capturing group is ([^a-zA-Z0-9]+). This will greedily match 1 or more non-alphanumeric characters.
In order to ensure that only non-alpha numeric characters between two alphanumeric characters will be matched, a positive lookbehind assertion and a lookahead assertion are used.

(?<=[a-zA-Z0-9]) 
This is the positive lookbehind assertion, the main capturing group is not matched unless it is preceeded by an alphanumeric character.

(?=[a-zA-Z0-9])
This is a lookahead assertion, it requires that the main caturing group is followed by an alphanumric character in order to be matched.

### Performance
Python uses a recursive backtracking algorithm for regular expressions, see https://swtch.com/~rsc/regexp/regexp1.html and https://github.com/python/cpython/blob/master/Lib/re.py 
in order to support features like lookbehind. 
This algorithm can potentially have an exponential running time (allowing denial of service attacks with very inefficient regex), however this particular regex expression 
will not cause an exponential running time since there is only one look behind and one lookahead. 

An alternative to lookbehind and lookahead would be to have three seperate regular expressions.
^([^a-zA-Z0-9]+)[a-zA-Z0-9] : To match and cut non-alphanumric characters from the front of the string

[a-zA-Z0-9]/([^a-zA-Z0-9]+)$ : To match and cut non-alphanumeric characters from the end of the string

([^a-zA-Z0-9]+): To match non alpha numeric characters left and replace with a space
And then splice them back togethor. However this method would require some if conditions.
