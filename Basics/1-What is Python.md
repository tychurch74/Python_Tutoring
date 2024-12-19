# What is Python and What's the Point?
Python is a computer programming language; one of many different languages (C, Java, R, etc).

A programming language is how you communicate directly with a computer; how you can write instructions for a computer to do whatever you want.

Different programming languages tend to be suited or designed with certain tasks in mind. For example Javascript is usually used for webpages and web development, C++ for software development.

*note that SQL is technically not a programming language as it only deals with databases and doesn't let you legitmately control a computer itself.

Python stands out among languages due to it being largely a general purpose language. Want to build a website? You can do it in Python. Want to analyze spreadsheets, databases and other data storage? You can use python. Want to develop complex AI algorithms? Look at GPT, it was developed in python. Want to scrub baseball stats from the internet and feed it into an algorithm that deduces top player trade picks for a given season? Yup, you can do it in Python.

## Programming is 5% knowing the language itself and 95% abstract reasoning
There's really only a few basic rules and formatting standards you need to know in order to write really powerfull code with python. 

The thing about programming you need to understand is that computers are dumb. A computer can't read your code and guess what you're trying to actually do. Every single step needs to be spelled out clearly, every intention is an specific instruction.

Think of spreadsheets in Excel or Google Sheets. The concepts of computer programming are actually very similar to creating spreadsheets. If you want to add two numbers in excel you need to write an instruction that basically states "this cell is equal to the sum of the numbers in these cells". A specific instruction, in a specific format, for a specific result.

## The python community
Far and away python has the largest collection of publicly created "libraries" that anyone and everyone can use.

"Libraries" are collections of code user's have created and encapsulated into easy to use "functions" that you can then download yourself and use.

For example the "pybaseball" library I showed you. The code that retrieved data from the web about current and historic MLB team standings was only a few lines with the bulk of the actual task encapsulated to the "standings" function. Without that function the "pybaseball" team created the code to do the same from scratch would have been enourmous. Think about it, that function has to tell the computer to:

1. Pull data from a specific location on the web 
2. Find the standings data from that location according to the specified season
3. Re-format that data in a way that is easily accesible via python