For this project, I used the pandas library, the numpy library, and the sklearn library for this project. 

For the majority of my project, I followed the steps listed on the website https://www.learndatasci.com/glossary/binary-classification/ but gained a more in depth understanding of what exactly I was doing by looking at https://medium.com/maheshkkumar/implementing-a-binary-classifier-in-python-b69d08d8da21.
I heavily relied on pandas and gaining a deeper understanding of it so I referred a lot to the w3schools pandas guide(https://www.w3schools.com/python/pandas/default.asp) and the pandas API reference (https://pandas.pydata.org/docs/reference/index.html)
Furthermore, since the data given wasn't in int values, I got help from a stackoverflow post (https://stackoverflow.com/questions/34007308/linear-regression-analysis-with-string-categorical-features-variables) that detailed how to convert strings/characters to int variables using the pandas .getdummies() function.

The only issue I found when testing the code was that in order to have a test case, the test Dataframe needed to have every value for each attribute, something that is kind of unreasonable if you only want to test for a few specific mushroom attributes.

On a side note, I completed and ran my code on the virtual environment on the website repl.it because I was unable to import packages for Python on my computer.