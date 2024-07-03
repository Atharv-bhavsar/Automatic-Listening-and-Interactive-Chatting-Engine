# File to perform basic arithmetic operations using ALICE

# Import necessary modules
import ai_speak
import wolframalpha


# Function to query WolframAlpha API for arithmetic operations
def wolf_ram_alpha(query):
    # WolframAlpha API key
    apikey = "V8RY44-UU5T8A624H"
    # Create a client for querying WolframAlpha
    requester = wolframalpha.Client(apikey)
    # Query the WolframAlpha API with the given query
    requested = requester.query(query)

    try:
        # Extract and return the answer from the API response
        answer = next(requested.results).text
        return answer
    except Exception as e:
        # Handle exceptions and inform the user if the value is not answerable
        print(e)
        ai_speak.speak("The value is not answerable")


# Function to perform arithmetic calculations
def calc(query):
    # Convert the query to string
    term = str(query)
    # Replace words with symbols for arithmetic operations
    term = term.replace("calculate", "")
    term = term.replace("multiply", "*")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("divide", "/")

    # Convert the final term to string
    final = str(term)
    try:
        # Query WolframAlpha API with the final term and get the result
        result = wolf_ram_alpha(final)
        return result

    except Exception as e:
        # Handle exceptions and inform the user if the value is not answerable
        print(e)
        return "The value is not answerable"
