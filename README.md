1327108

## Python Course exercise 1

This is the repository for the first exercise of **120.050 Introduction to Python
programming for geoscience**. This exercise will be handed in via Github. The
process of doing this can be daunting for a first time user so we will try to
provide detailed instructions below and we will also show it during the exercise
handout.

### Instructions

All of the functions you will write during this exercise have a test associated
with it which can be found in the `tests` folder. If an explanation of what a
function should do is not completely clear then look at the test function for an
example of the expected output.

#### Git Background

You can find numerous tutorials about the Git basics on the web. A first start
can be
- [Github tutorial](https://try.github.io/levels/1/challenges/1)
- [Slides of this course](https://github.com/TUW-GEO-python-intro/slide-deck/blob/master/03.1-Intro%20to%20Git/slides.org)
- [Official Git Book](https://git-scm.com/book/en/v2)

#### Step by step instructions

To complete the exercise follow these steps:

1. Create an account on [github](https://github.com/)
2. Login
3. [Setup Git](https://help.github.com/articles/set-up-git/)
4. Fork this repository to your account.
   [What does this mean?](https://help.github.com/articles/fork-a-repo/)
5. Clone this repository to your development machine. This is also step 2 in the
   [forking tutorial](https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork)
6. You should now have folder on your Computer that contains the files listed above.
7. Try switching to the directory where you have the code in the console and
   run `python setup.py test`. This should run all the tests in the `tests`
   folder. One test will pass while all the others will fail.
8. Look into the `.py` files in the `ex1` folder. In there you will find
   instructions about the things you have to program to make all the tests pass.
9. Write code and commit your changes to git.
10. Push your commits to Github
11. Repeat 8. to 10. as often as necessary.

#### Hand in

When you want to hand in the exercise
[create a Pull Request (PR)](https://help.github.com/articles/using-pull-requests/)
against the `TUW-GEO-python-intro/ex1` repository. You should not have to change
any settings in the Pull Request dialog to do that.

Opening a PR will automatically run the test scripts so that we can both see if
the tests pass, or why they fail. The PR also allows us to review your code and
give comments on the implementation.

#### Hand in date

Please open a Pull Request by the 30th of November.

#### Grading

The grade for this exercise will be 80 % based on the percentage of passed tests
and 20 % on the implementation style/documentation of your code.

##### Requirements for the implementation style and documentation

- Comment your code to explain **why** it works. How it works should be obvious
  from the source code. We do not need line by line *subtitles* for the code.
- Document the functions you write.
- Good commit messages [see this article](http://chris.beams.io/posts/git-commit/)

The recieved percentage score translates to grades in the following way:

1. 91-100
2. 81-90
3. 66-80
4. 51-65
5. < 51
