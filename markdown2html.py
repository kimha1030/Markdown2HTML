#!/usr/bin/python3
"""Task 0: Start a script"""
import sys
import os
import markdown


def markdownhtml():
    """Takes 2 arguments and print in stderr"""
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    else:
        filename = sys.argv[1]
        output = sys.argv[2]
        if os.path.isfile(filename):
            with open(filename, 'a') as writer:
                writer.write("&nbsp;")
            markdown.markdownFromFile(
                input=filename,
                output=output,
                encoding='utf8',)
            sys.exit(0)
        else:
            print("Missing {}".format(filename), file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    markdownhtml()
