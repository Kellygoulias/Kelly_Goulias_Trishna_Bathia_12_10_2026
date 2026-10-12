# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._







------------------------------------------


# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
