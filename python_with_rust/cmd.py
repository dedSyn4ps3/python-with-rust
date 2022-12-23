#!/usr/bin/env python

import argparse
from rich_argparse import RichHelpFormatter

from python_with_rust.api import update
import rusty_python as rp

d1 = """
API test application using a combination
of pure Python functions and additional 
helper modules written in Rust
"""
d2 = """
This application uses several Python libraries to 
create a colorful commandline app with example 
functionality implemented in Rust
"""

d = f"{d1}\n{d2}"

def cli():
    parser = argparse.ArgumentParser(
        description=d,
        formatter_class=RichHelpFormatter
    )

    parser.add_argument(
        "-n", "--app-name",
        action="store",
        required=False,
        help="App name to use for update download simulation")

    parser.add_argument(
        "-l", "--loop",
        action="store_true",
        required=False,
        help="Run some test loops!. Uses `run_loops` functionality implemented in Rust")

    parser.add_argument(
        "-r", "--rust-arg",
        action="store",
        required=False,
        help="""
        Tell us your name! This `string` value gets passed 
        to the `say_hello` function implemented in Rust. The function also runs 
        multiple `async` requests
        """
        )

    args = parser.parse_args()

    if args:
        if args.app_name:
            update.checkVersion(args.app_name)
        if args.loop:
            rp.run_loops()
        if args.rust_arg:
            rp.say_hello(args.rust_arg)
            rp.begin_request_test()
        
    else:
        #print("No arguments provided, bye bye :)")
        parser.print_usage()
