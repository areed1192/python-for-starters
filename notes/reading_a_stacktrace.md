# Reading a StackTrace in Python

Congratulations you wrote your first program and no less than 3 seconds after finishing it
you run it only to see that it failed you get a bunch of text in your terminal. Take for example
our simple python script below:

```python
def split_full_name(string: str) -> list:
    """Takes a full name and splits it into first and last.

    Parameters
    ----------
    string : str
        The full name to be parsed.

    Returns
    -------
    list
        The first and the last name.
    """

    return string.split(" ")

# Test it out.
print(split_full_name(string=100000000))
```

Hopefully, it's pretty self explanatory what this function does. It will take a full name like
`Alex Reed` and split it on the `" "` space to return a list of both the first and last name:
`['Alex', 'Reed']`.

However, we have an issue! We aren't passing through a string we are passing through a number!
That means our function will break. If we try to run it, we get this mess of text:

```terminal
Traceback (most recent call last):
  File "c:\Users\Alex\OneDrive\Desktop\Sigma\Repo - Simple Project\python-for-starters\my_bad_script.py", line 19, in <module>
    print(split_full_name(string=100000000))
  File "c:\Users\Alex\OneDrive\Desktop\Sigma\Repo - Simple Project\python-for-starters\my_bad_script.py", line 16, in split_full_name
    return string.split(" ")
AttributeError: 'int' object has no attribute 'split'
```

What the heck is this? Well this is what we call Traceback. In Python, A traceback is a report containing
the function calls made in your code at a specific point i.e when you get an error. It is recommended that
you should trace it backward(traceback). Whenever the code gets an exception, the traceback will give the
information about what went wrong in the code.

So if you want to read the Traceback correctly, you would start with this line:

```terminal
AttributeError: 'int' object has no attribute 'split'
```

This line tells us the error that we encountered. In this case it was an `AttributeError` which means you
are calling an attribute that a particular object type doesn’t possess. In this case `int` doesn't have an
attribute called `split`.

Okay now that we know the error we would read up the TraceBack. The next section we would look at is:

```terminal
File ["c:\Users\Alex\OneDrive\Desktop\Sigma\Repo - Simple Project\python-for-starters\my_bad_script.py"] [line 16], [in split_full_name]
    return string.split(" ")
```

This is where we encountered the `AttributeError`. In fact if you look at it the top line you can see the file
that we encountered the error, the line on which it occured and the function it occured. I've put `[]` around them
so you can more easily see them. THIS IS SUPER HELPFUL!!!!!

It's really hard to diagnose an issue if you don't even know where the issue is being caused!!! In some cases we don't
get a traceback and those moments suck because you have nothing to point you in the right direction.

If we continue up, we finally see the last line. This is where we call the function that raised the error. It tells us it
happened on line 19 and we can see the function with the argument passed through.

```terminal
File ["c:\Users\Alex\OneDrive\Desktop\Sigma\Repo - Simple Project\python-for-starters\my_bad_script.py"], [line 19], in [<module>]
    print(split_full_name(string=100000000))
```

Now, for me it's easy to see the issue. We passed through a number instead of a string. That is what caused our issue and the easy
fix is to paass through a string. Here's the issue though it's easy for me to say that because I've read 1000s and 1000s of Tracebacks.
However, when I first started coding I would've had to look this error up because I wouldn't know what was going on.

However, as time went on I found these tracebacks extremely valuable even when getting help. Knowning how to read them can save you
so much time when it comes to debugging, so even though you might not get your answer from it you'd be surprised how it can help you
when it comes to getting help.
