# Code Reviews
## Benefits
* Catch errors
* Ensure readabilty
* Check if standards are met for production level code.
* Share knowledge among teams.

## Tip: Use a code linter
This isn't really a tip for code review, but it can save you lots of time in a code review. Using a Python code linter like **pylint** can automatically check for coding standards and PEP 8 guidelines for you. It's also a good idea to agree on a style guide as a team to handle disagreements on code style, whether that's an existing style guide or one you create together incrementally as a team.

```
pip install pylint
```

## Questions to ask yourself when conducting a code review
* First, let's look over some of the questions we might ask ourselves while reviewing code.

### Is the code clean and modular?
* Can I understand the code easily?
* Does it use meaningful names and whitespace?
* Is there duplicated code?
* Can I provide another layer of abstraction?
* Is each function and module necessary?
* Is each function or module too long?

### Is the code efficient?
* Are there loops or other steps I can vectorize?
* Can I use better data structures to optimize any steps?
* Can I shorten the number of calculations needed for any steps?
* Can I use generators or multiprocessing to optimize any steps?

### Is the documentation effective?
* Are inline comments concise and meaningful?
* Is there complex code that's missing documentation?
* Do functions use effective docstrings?
* Is the necessary project documentation provided?

### Is the code well tested?
* Does the code high test coverage?
* Do tests check for interesting cases?
* Are the tests readable?
* Can the tests be made more efficient?

### Is the logging effective?
* Are log messages clear, concise, and professional?
* Do they include all relevant and useful information?
* Do they use the appropriate logging level?