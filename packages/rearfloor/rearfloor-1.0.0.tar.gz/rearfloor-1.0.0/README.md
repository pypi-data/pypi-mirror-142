# RearFloor (Background)

![Useless badge](https://img.shields.io/badge/USELESS-but%20it%20saves%20you%20a%20Google-%23333333?style=for-the-badge)

![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-%23informational?style=for-the-badge)

RearFloor is a library to make your functions and class methods run in the background asynchronously with just 10 characters.

This is a lightweight library that takes <5 minutes to audit. Whether you're a small developer looking for a solution, or a large and soulless corporation, this library will save you ***seconds*** in both server response time and finding an answer on StackOverflow that does the same thing.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install RearFloor.

```bash
pip install rearfloor
```

## Usage

```python
from rearfloor import rearfloor


# Here's a boring, synchronous function
def synchronousFunction(text_to_print: str):
    print("Synchronous:", text_to_print)


# Now use that function.
# The rest of the program waits for it to stop before moving on.
synchronousFunction("Lame")


# Here's a rad, asynchronous function
@rearfloor
def asynchronousFunction(text_to_print: str):
    print("Asynchronous:", text_to_print)

# Now use *that* function.
# The rest of the program moves on, reducing your wait time on tasks
# that aren't going to return or modify a value.
asynchronousFunction("Sick")
```

I use this to asynchronously write to the database in a high traffic, low response time Flask application. Now my customers can get a response in <90ms instead of 400-1500ms and the data is still recorded!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)