# 🐍 python-with-rust 🦀

## A project meant to demonstrate how to use modules implemented in Rust from within a Python application

<br>

> This application was written to test with the [rusty-python]("https://github.com/dedsyn4ps3/python-with-rust") test crate 

<br>

<br>

## Overview 🔍
Even though this is an extremely simple example of a Python command line application, it's meant to serve as a starting point for implementing custom modules written in Rust, with the goal of providing additional speed and native IO performance that a pure Python app may not always be able to achieve by itself.

<br>

## Building Blocks 🧱
This module utilizes the packaging and dependency management tool `poetry` to create a minimal command line application to demonstrate using Python packages implemented in Rust.

The steps for creating the application are pretty straightforward:

 - Use `poetry add` to add any needed dependencies to our project's `pyproject.toml` file
 - Create a new `api` directory to simulate an internal module for our app to import
 - Add an `import` statement and function calls for our custom Rust crate just like we do for any other function

<br>

## Next Steps 🗺
After getting your code all put together, it's time to test everything out! Technically, there's no requirement of building a small CLI to just run code implemented in Rust.

That being said, the whole purpose of creating a hybrid crate such as `rusty-python` is to add modularity to Python applications looking to incorporate slightly more efficient code. The best way to do that, of course, is to slap together a small app like this to do just that!

To keep things neat and tidy, along with providing some separation between your system's installed packages, go ahead and create a virtual environment to run the application in and install the external crate:

<br>

```
$ python3 -m venv .test-env
$ source .test-env/bin/activate
```
<br>

Once inside the virtual environment, we can go ahead and install the external package implemented in Rust so that our program will run without any kind of errors. The URL passed to the install command may be different depending on whether you've created your own Rust package or are using the example put together for this project.

<br>

If using the `rusty-python` package, go ahead and run the following to retrieve and install it from it's Github repo:

<br>

```
$ pip install git+https://github.com/dedsyn4ps3/rust-python@main
```

<br>

> **NOTE:** The `@main` at the end of the command ensures you're installing the most current version of the package.

> **PS:** It's also possible to install the Rust package from other sources as well ( such as PyPi ) just like you do for any other regular `pip install` command. The `rusty-python` package used in this project, for example, was made available on [test.pypi.org]("https://test.pypi.org") and could've also been installed using `pip install -i https://test.pypi.org/simple/ rusty-python`

<br>

<br>

## Wrapping Up 🏁
For more detailed information on how to develop a Rust-Python project from start to be, be sure to check out Parts 1 & 2 of `Make your Python Faster with Rust` on [**Medium**](https://www.medium.com/@erutherford_nullreturn)