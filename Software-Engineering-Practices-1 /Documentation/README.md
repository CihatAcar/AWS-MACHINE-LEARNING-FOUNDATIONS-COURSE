# Why Documentation is important?
* Clarify complex parts of code
* Navigate code easily
* Describe use and purpose of components.

# Types of documentation
* Line level
	* Inline comments are text following hash symbols throughout your code. They are used to explain parts of your code, and really help future contributors understand your work.
	* Comments often document the major steps of complex code. Readers may not have to understand the code to follow what it does if the comments explain it. However, others would argue that this is using comments to justify 		bad code, and that if code requires comments to follow, it is a sign refactoring is needed.
	* Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was implemented a specific way. Sometimes an unconventional or seemingly arbitrary approach may be applied 	because of some obscure external variable causing side effects. These things are difficult to explain with code.
* Function or module level
	* Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code. Ideally, each of your functions should always have a docstring.
	* Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.
	* If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one-line summary.
	* The next element of a docstring is an explanation of the function's arguments. Here, you list the arguments, state their purpose, and state what types the arguments should be. 
	* Finally, it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice.
* Project level
	*Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or developers who may contribute to your code. 
	* A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.
	* Whether it's an application or a package, your project should absolutely come with a README file. 
	* At a minimum, this should explain what it does, list its dependencies, and provide sufficiently detailed instructions on how to use it. 
	* Make it as simple as possible for others to understand the purpose of your project and quickly get something working.
	* Translating all your ideas and thoughts formally on paper can be a little difficult, but you'll get better over time, and doing so makes a significant difference in helping others realize the value of your project. 
	* Writing this documentation can also help you improve the design of your code, as you're forced to think through your design decisions more thoroughly. It also helps future contributors to follow your original intentions.