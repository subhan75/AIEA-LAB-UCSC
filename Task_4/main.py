'''Flow of the code
1. Load the knowledge base
2. Translate the question to a Prolog query
3. Execute the query
4. Generate a natural language response
'''
from pyswip import Prolog
from openai import OpenAI
import os

# Initialize OpenAI and Prolog
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prolog = Prolog()

# Conversation history for OpenAI
conversation_history = [
    {"role": "system", "content": "You are a Prolog expert that translates natural language questions into correct Prolog queries, ensuring they match the given Prolog knowledge base precisely."}
]

def chat_with_openai(user_input):
    """Interacts with OpenAI API to generate responses."""
    conversation_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=0
    )
    model_response = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": model_response})
    return model_response

def load_knowledge_base(file_path="kb.pl"):
    """Loads the Prolog knowledge base into pyswip."""
    try:
        prolog.consult(file_path)
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return None

def translate_to_prolog_query(question, knowledge_base):
    """Translates a natural language question into a valid Prolog query."""
    prompt = (
        f"Here is a Prolog knowledge base:\n{knowledge_base}\n\n"
        f"Convert the following natural language question into a valid Prolog query.\n"
        f"- Use only predicates and facts that exist in the knowledge base.\n"
        f"- Do not include explanations, comments, or '?-'.\n"
        f"- Ensure Prolog variables start with uppercase letters.\n\n"
        f"Question: {question}\n"
    )
    prolog_query = chat_with_openai(prompt)
    return prolog_query.strip()

def execute_prolog_query(query):
    """Executes a Prolog query and returns results."""
    try:
        results = [res for res in prolog.query(query)]
        return results
    except Exception as e:
        print(f"Error executing Prolog query: {e}")
        return None

def generate_natural_language_response(question, results):
    """Generates a natural language explanation of the query results."""
    if not results:
        return "No results found for your query."
    
    prompt = (
        f"Here are the results of a Prolog query:\n{results}\n\n"
        f"Explain these results in natural language in response to the original question:\n"
        f"Question: {question}\n\n"
        f"Provide a clear and concise explanation, using the same terminology as the question."
    )
    return chat_with_openai(prompt)

# Example usage
if __name__ == "__main__":
    # Load knowledge base
    kb = load_knowledge_base()
    if kb:
        # Get user question
        question = input("Enter your question: ")
        # Translate to Prolog query
        prolog_query = translate_to_prolog_query(question, kb)
        print(f"\nGenerated Prolog Query: {prolog_query}")
        # Execute query
        results = execute_prolog_query(prolog_query)
        print(f"\nQuery Results: {results}")
        # Generate natural language response
        natural_response = generate_natural_language_response(question, results)
        print(f"\nResponse: {natural_response}")