We covered this material that remained from Wednesday's lecture in Recitation on 2024-02-11. It took about 40 minutes to get through the material.

## Initial steps
1.	Navigate to: https://github.com/cmu-crafting-software/in-class-2024/
2.	Code-->Codespaces-->(+)
3.	If prompted, install the Python tools and ignore the linter warning
4.	In terminal:
    * `git status` --> to see that you are on the main branch
    * `cd feb-7-testing`
    * `pytest` --> to see that all tests pass

## Using the code to help us think of tests
1.	We saw last time that we could write code while writing tests. Why did we do that? (Because writing tests helps us think through what our code should be doing)
2.	Look in `wordle_parts_test.py`
3.	I added two new tests at the bottom today. What are they checking for?
4.	Now look in `wordle_parts.py`
5.	I’ve replaced Wednesday’s implementation of `is_yellow` with one that is more complete.
6.	Let’s read through it (go top to bottom)

7.	Ok, so we can use tests to help us write the program. We saw that last week.
8.	But did you know that we can also use the program to help us write tests? 
9.  Let’s see that in action.

9.	In `wordle_parts_test.py`, comment out the last two tests.
10.	In `wordle_partys.py`, commend out lines 29 and 34 to create a bug in our program.
11.	Run `pytest`
12.	What happened? Why?

13.	Now uncomment the two tests. 
14.	Run `pytest`
15.	Do our tests detect the bug?
16.	In `wordle_partys.py`, uncommend out lines 29 and 34 to “fix” the bug.

## Implementing is_green
1.	What should `is_green` do?
2.	Write out some test cases on the whiteboard.
3.	Implement the unit tests
4.	Run `pytest`
5.	What happened?
6.	Now implement the function
7.	Run `pytest`
8.	What happened?
