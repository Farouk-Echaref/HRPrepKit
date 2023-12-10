#!/usr/bin/python3

#Use type hints for type safety
# using the JSON library for decoding the json string 
import json

# function to check validity of a JSON string:
#  takes a JSON String and returns message (Message whether the json is valid or not)
def checkJSON(jsonString: str) -> str:
    # we will use Try/Except testing block for errors because the library can throw error:

    try:
        # decoding json
        json.loads(jsonString)
        return ("Valid Json")
    except json.JSONDecodeError as e:
        # catching the error and making a format errorMsg
        errorMsg = f"message:the line {e.lineno} contains wrong char {jsonString[e.pos]}"
        return (errorMsg)

# main function
if __name__  == "__main__":
    json1 = '{"prenom":"rafael", "adresse":"casablanca maarif", "age":"29"}'
    json2 = '{"ville":{"tanger": 44, "kenitra": 94}}'

    checkJSON(json1)
    checkJSON(json2)
