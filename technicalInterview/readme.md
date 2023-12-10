# JSON: JavaScript Object Notation
 - text format with JavaScript Object Notation, for storing and exchanging and transforming data (object with keys and values)


## manipulate JSON with python: Using Python JSON Package
 - JSON Module helps with JSON serialization and deserialization
 (https://stackoverflow.com/questions/3316762/what-is-deserialize-and-serialize-in-json)
 - parse JSON string by using json.loads() method
 - JSONDecodeError is an exception class that is raised when there's an issue decoding a JSON-formatted string. This exception is part of the json module and is specifically raised by the json.loads() function and related functions when they encounter problems during the decoding process.
 - The f"" is a string literal that stands for an "f-string" or "formatted string literal." F-strings were introduced in Python 3.6 and provide a concise and convenient way to embed expressions inside string literals.

# Request HTTP LIbrary:
 - Requests is an elegant and simple HTTP library for Python, built for human beings.

 - retrieving JSON Response Content(response.json())


# Bash Script:

 - Important Note: 
 * IFS => Internal Field Separator, by default it's set to whitespace
 * Expanding of $* vs $@: 
    - $* Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the IFS special variable.
    - $@ Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, each parameter expands to a separate word.

 - From there we pipe the resulting string using echo to the READ-END of awk:
    - awk will change every line with the tolower() function


