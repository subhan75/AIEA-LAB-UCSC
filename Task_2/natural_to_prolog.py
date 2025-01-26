from openai import OpenAI

client = OpenAI()

# Function to convert natural language to Prolog
def natural_language_to_prolog_via_client(natural_language_query):
    """
    Converts a natural language query to a Prolog statement using OpenAI's Chat Completions API.
    """
    # Define the conversation
    messages = [
        {"role": "developer", "content": "You are a Prolog expert. Convert natural language queries into valid Prolog statements."},
        {"role": "user", "content": f"Convert this query to Prolog: {natural_language_query}"}
    ]
    
    
        # Call the chat completions endpoint
    completion = client.chat.completions.create(
            model="gpt-4",  # Use the GPT-4 model
            messages=messages,
            temperature=0.2,  # Low temperature for deterministic responses
            max_tokens=100  # Limit tokens for concise output
        )
        
        # Extract and return the Prolog statement
    prolog_statement = completion.choices[0].message.content.strip()
    return prolog_statement

    
    return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example queries to test
    queries = [
        "Find all the parents of John.",
        "Does Sarah have a sibling named Jack?",
        "List all employees in the IT department.",
        "Who are the children of Alice?"
    ]
    
    for query in queries:
        print(f"Natural Language Query: {query}")
        prolog_statement = natural_language_to_prolog_via_client(query)
        print(f"Prolog Statement: {prolog_statement}\n")
