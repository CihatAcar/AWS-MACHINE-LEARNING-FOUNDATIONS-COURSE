# Logging
* Logging is valuable for understanding the events that occur while running your program. 
    * For example, if you run your model overnight and the results the following morning are not what you expect, log messages can help you understand more about the context in those results occurred.

# Log Messages
* Logging is the process of recording messages to describe events that have occurred while running your software. 
## Examples
### Tip: Be Professional and Clear
```
Bad: Hmmm... this isn't working???
Bad: idk.... :(
Good: Couldn't parse file.
```
### Tip: Be concise and use normal capitalization
```
Bad: Start Product Recommendation Process
Bad: We have completed the steps necessary and will now proceed with the recommendation process for the records in our product database.
Good: Generating product recommendations.
```
### Tip: Choose the appropriate level for logging
```
Debug: Use this level for anything that happens in the program. 
Error: Use this level to record any error that occurs. 
Info: Use this level to record all actions that are user driven or system specific, such as regularly scheduled operations.
```
### Tip: Provide any useful information
```
Bad: Failed to read location data
Good: Failed to read location data: store_id 8324971
```