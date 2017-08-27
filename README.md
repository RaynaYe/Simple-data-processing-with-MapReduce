# mapreduce

Task1: Take file webLarge.txt, and produce a version which is all upper-case. For example, the sentence John
loves Mary. would become JOHN LOVES MARY. Call this the upper-case version. For purposes of correctness
marks, changing the order of the lines is permissible.

Task2: Using MAPREDUCE write a program that will filter the upper-case version (from task 1) such that only lines
that appear exactly once will be in the output. Call this the unique-only version. Your approach should be
exact (do not use approximate techniques). The output will be used for some of the following tasks. For
example, for the file:  
bob had a little lamb and a small cat   
alice had one tiger
bob had a little lamb and a small cat
mary had some small dogs and a rabbit
mary had some small dogs and a rabbit
bob had a little lamb and a small cat
the output should be:
alice had one tiger
because alice had one tiger is the only line that appeared exactly once in the input.

Task3: Compute the length of the longest token and the length of the longest line in the unique-only version. We
define a token the same way Python’s split() function does: anything separated by runs of whitespace
(space ’ ’, tab ’\t’, carriage return ’\r’, new line ’\n’, or form feed ’\f’). The length of a line does not
include the newline character; see the example.
Your output should be a single file on HDFS. For example, the following file example.txt:
bob had a little lamb and a small cat and a tiny fish
alice had one kangaroo
mary had some small dogs and a rabbit
should have the following result (8 is the length of the longest token and 53 is the length of the longest line):
8 53 

Task4: On the unique-only version, find all three-word sequences and their counts. For example, the two sentences:
2
mary had a little lamb
mary had a little tiger
have the following three-word sequences and counts:
Sequence Count
mary had a 2
had a little 2
a little lamb 1
a little tiger 1

Task 5:
What are the top twenty most frequent three-word sequences? Produce a single output file. Each line in
the output should contain a count of a three-word sequence followed by a space followed by the actual
three-word sequence. The output should be sorted in decreasing frequency order (i.e. the most frequent
three-word sequence should be first)

Task 6:
Using the three-word sequence counts you found in task 4, find the entropy of words for each two-word
context.
 Relational Join using MAPREDUCE
In this task you will perform a join operation in Hadoop. Let us assume that we have the relations student(studentId,
name) and marks(studentId, courseId, mark). and need to join them on the studentId field. Traditionally, this is an easy task when we deal with relational
databases and can be performed by using the relational join operator. However, the way this join operation
is performed drastically changes, when we assume our input is into a single file that stores information
from both relations.
Assume the format of such a single input file storing data from two relations is as follows:
student 1 George
mark 1 EXC 70
student 2 Anna
mark 1 ADBS 80
mark 2 EXC 65
mark 1 TTS 80

Task 7: Use the uniLarge.txt file perform a join operation on the studentId key and produce an output that will
have the grades of each student as follows:
name --> (course1, mark1) (course2, mark2) (course3, mark3) . . .

Task 8:
What is the fictional name of the student (or students in case of equality) with the highest average when
the number of lessons examined is greater than three? 
