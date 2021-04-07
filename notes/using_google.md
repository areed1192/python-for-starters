# Googling Errors

## Introduction

One thing is guaranteed, your code, at some point, will not work the way you expected it to.
The reasons why it does not work can range from a bug existing in your code, calling the wrong
variable at the wrong time, or not updating values correctly.

Some of these errors are easier to diagnose than others. For example, some will give you an error
warning and stop your code during execution, telling you that an error has been encountered. Others won't
display anything and will run correctly, but the output you get is not what you wanted.

Regardless of the type of error or the cause of the error, you'll want to fix it. Fixing the error is where
Google can come in to save the day.

Now that we know Google can be our best friend, how do we use it? Well, to use it correctly, it's essential
to know a few things.

• Is the error even worth Googling?
• How to phrase the question.
• What sources do you start with first?

## Is it Even Worth Googling?

In some cases, the program will tell you explicitly what the error is; for example, in Python, you could encounter
some of the following errors:

• TypeError: Cannot property `Name` of undefined.
• SyntaxError: `myFunction` is not defined.

In the case of this type of error would represent the structure of your code. These types of errors can wield
inconsistent Google results, and it's best to approach these types of errors differently. Identify where the problem
is in the code.

Read over the problem, keeping tabs of what you're telling the computer to do at each step. Are you multiplying the
answer by the total when you should just be adding it to the total?

## Parsing the Error

Before you begin to search Google, you must know what to Google! Parsing the error before Googling it can help you quickly
identify easy fixes before investing too much time or help isolate the type of error you received.

Does the error return a specific line number? Awesome, look at the line the error is happening and see what's going on.
Additionally, you'll want to read the stack trace and try to diagnose the error that way. At this point, I don't expect you
to know how to read a stack trace or even what a stack trace is. However, I will be releasing a document that will explain how
to read them. All you need to know at this point is a traceback is a report containing the function calls made in your code at
a specific position.

## Issues with No Errors

These tend to be the tricky ones, you have something that isn't working as you expected, but the script is saying there is nothing
wrong. While these may difficult to diagnose, you still have some tools are your disposal. Using print functions or the debugger.

Sometimes, a simple solution is to carefully add print statements to different parts of your code so that way, you can test it. They
can help us see what the data looks like at different parts of the code, whether a specific section of the code is even running or
whether the data being returned is the correct type.

If you want, you can also use the debugger tool found on your IDE. The debugger allows you to watch each step of your code during
execution. With this, you can see where the code is breaking and what the program is receiving for each variable.

## Building Our Question

Keep it focused, how can you describe your problem in the most concise manner, the most generic way, and using the appropriate terms.

For example:
• How to add an element in a list?
• How to delete a value from a dictionary?

Make sure to add the appropriate language/tech to your question.

For example:
• How to add an element in a list in Python?
• How to write a for loop in JavaScript?

In some cases, you’ll want more recent results. In this case, append “YEAR” to your result.

For example:
• How to create a dropdown in JavaScript 2019?

Before searching your error message, delete the file and variable names. Alternatively, you can replace them with `_` to serve as
placeholders. The `_` is crucial for queries that are either partially or entirely enclosed in quotation marks.

For Example:
• BAD: C:\User\Alex\MyPersonalFile.xlsx file cannot be found in VBA?
• GOOD: `_ file cannot be found error VBA?`
• GOOD: `_ “file cannot be found” error in VBA?`

## Prioritizing Results

Typically, you should go in the following order when reading results.

1. The Official Documentation.
2. Stack Overflow
3. GitHub
4. Reddit
5. Quora
6. Other Blogs

The hierarchy can change depending on the language you're using; for example, most languages developed by Microsoft can have dedicated
forums you can search.

**Official Documentation:**

The official documentation can vary in quality, sometimes the examples they provide are so simple that they don't represent a real-life
use, or it can be so out of date that it's worthless. However, major companies usually do an excellent job of keeping the official
documentation up to date.

**Stack Overflow:**

Go right to the comments with this one, very rarely is the person who is asking the question setting up the problem exactly as you did.

**GitHub:**

GitHub is usually where the source code for a library can be stored, some of the repositories can contain known issues that'll help you
determine if there is just something wrong with the library you're using. Additionally, they usually, if they can, give you workarounds.

**Reddit:**

Surprisingly, these forums can provide useful information more so for simple answers.

**Quora:**

A bunch of nerdy people who ask questions for fun, surprisingly, I've learned a lot from Quora in the name of coding.
