# Graduate Assignment

tree sitter identifier detection and filter

## Instructions to run

To use the package enchant for dictionaries, execute the command

pip install pyenchant==2.0.0


- code.py contains the main code
- inbuilt_list.py contains the lists of inbuilt functions for each language

Executions Steps:

- python3 code.py https://github.com/hgupta/magic-squares-ruby .rb ruby /Users/sneha/ /Users/sneha/
- python3 code.py https://github.com/holidayextras/example-js-project .js javascript /Users/sneha/ /Users/sneha/
- python3 code.py https://github.com/go-training/helloworld .go go /Users/sneha/ /Users/sneha/
- python3 code.py https://github.com/hcvazquez/python-string-manipulation .py python /Users/sneha/ /Users/sneha/

template : python3 code.py <github-link> <extension> <language> <path1> <path2>

- code gets cloned to the folder gitRepo
- output files will be stored in the current directory if invalid directory is provided
