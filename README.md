# Repository for Markdown to HTML

## Description

Markdown is awesome! All your README.md are made in Markdown, but do you know how Github are rendering them? It’s time to code a Markdown to HTML!

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7 or higher)
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.\*)
- All your files must be executable
- All your modules should be documented: python3 -c 'print(**import**("my_module").**doc**)'
- Your code should not be executed when imported (by using if **name** == "**main**":)

## Tasks

0. Start a script:
   Write a script markdown2html.py that takes an argument 2 strings:

- First argument is the name of the Markdown file
- Second argument is the output file name

1. Headings:
   Improve markdown2html.py by parsing Headings Markdown syntax for generating HTML.

2. Unordered listing:
   Improve markdown2html.py by parsing Unordered listing syntax for generating HTML.

3. Ordered listing:
   Improve markdown2html.py by parsing Ordered listing syntax for generating HTML.

4. Simple text:
   Improve markdown2html.py by parsing paragraph syntax for generating HTML.

5. Bold and emphasis text:
   Improve markdown2html.py by parsing bold syntax for generating HTML

6. ... but why??
   Improve markdown2html.py by parsing bold syntax for generating HTML
