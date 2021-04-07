# Git Vs. GitBash Vs. GitHub

## Introduction

You probably heard multiple times the terms GitHub, Git Bash, and Git. What is the difference between
all these different tools? Well, in this tutorial, we will lay out some of those differences. Before
we jump into it, it's essential to think about a couple of things as they'll help give some context
as to why these tools work the way they do. These tools try to solve a problem by developing a solution
that tackles the issue. When thinking about these tools, ask yourself what is the problem they are trying
to solve and how are they trying to solve it?

Here are some problems to think about:

1. How do I keep track of changes to my code?
2. How can I go back to previous versions of my code?
3. How do you make working with a tool easier?
4. How can I share my code?
5. How can I make the process of developing an application more accessible and more consistent for companies?

## What is Git?

Let’s start at the core and move outwards. Git is the most widely used version control system in the World.
Developed in 2005 by Linus Torvalds, Git has morphed into a popular and mature open source project that companies
across the World have to come to rely on. Git has developed a strong following for many reasons, but some of them
include performance, security, and flexibility.

### Performance

Git is fast; its algorithms have been optimized for performance. It can handle file content confidently and has created
a distributed framework that makes development easier.

### Security

All the objects inside of Git are secured with the SHA1 secure hashing algorithm. With security top of mind, this makes
maintaining the integrity of the source code clear.

### Flexibility

Git can be used on small and large projects, is compatible with many different systems and protocols, and allows for non-linear
development using branching.

While Git is a powerful tool at your disposal, it also has criticism. One of the biggest criticisms is that it's hard to learn
for newcomers because of unique terminology.

**Problem:**

How do I keep track of changes in my code, go back to previous versions, and keep it secure?

**Git Solution:**

Create places called repositories to store and track changes of your code and encrypt them for security.

## What is GitBash?

At its core, Git is a set of command-line utility programs that are designed to execute on a Unix style command-line environment.
Operating systems like Linux and macOS include a built-in Unix command line terminal that makes working with Git complementary.
Windows, on the other hand, uses the Windows Command Prompt, which is a non-Unix terminal.

In Windows, Git is often packaged in a GUI (Graphical User Interface) that abstracts and hides underlying components of Git, making
working with Git easier. One of those GUIs is called Git Bash. Git Bash is a Windows application that allows you to work with Git
using a command-line experience.

Bash is an acronym for Bourne Again Shell, and a shell is just a terminal application. You can use a terminal form to interface with
the operating system using written commands. On Linux and macOS, the default application is Bash. On Windows, you have Git Bash,
which will install Bash, Git, and some common bash utilities on the Windows operating system.

I want to be precise. Nothing is stopping you from installing Git Bash on Linux or macOS. It’s just in the case of these operating
systems that they already come with Bash.

**Problem:**

Using Git is hard to use and has a steep learning curve.

**Git Bash Solution:**

Let’s create a terminal application that abstracts away a lot of the nuances of Git.

## What is GitHub?

We’ve established that Git is a version control system. Version control systems keep revisions to code straight and store modifications
to code in a central repository. Allowing developers to collaborate easily, make changes, and upload the newest revision. It also gives
access for every developer to see these new changes, download them, and contribute.

GitHub is where developers can store and share their repositories with likeminded developers. You can think of GitHub like OneDrive or
iCloud, all it does is act as an online hosting service where you can store your code. However, GitHub also adds new functionality
that makes sharing and copying your repository easier.

Along with providing a graphical user interface, GitHub offers a functionality called "forking." The idea behind forking is to allow for
users who don't have write access to the project to copy the repository under their account and make modifications there. If you make
some changes that you think the owner will like, you can submit a "pull request." If the owner decides they want your changes, then they
can "merge" your changes.

I always like to think of GitHub as the social media component of coding. You use Instagram to share photos, and you use GitHub to share
code.

**Problem:**

I have all this code and no way to easily share it.

**GitHub Solution:**

Have an online hosting service to store your code, and use forking to make it easy to share code.
