#!/usr/bin/python3
"""Task 0: Start a script"""
import sys
import os
# import markdown


def markdownhtml():
    """Takes 2 arguments and print in stderr"""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    else:
        filename = sys.argv[1]
        output = sys.argv[2]
        if os.path.isfile(filename):
            # markdown.markdownFromFile(
            #     input=filename,
            #     output=output,
            #     encoding='utf-8',)
            # with open(output, 'a') as file_output:
            #     file_output.write("\n")
            sys.exit(0)
        else:
            print("Missing {}".format(filename), file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    markdownhtml()
