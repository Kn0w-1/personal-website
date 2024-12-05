from helper_functions import get_llm_response

def create_llm_prompt(crypto_currency):
    prompt = f"I have a cryptocurrency called {crypto_currency}. Could you please summarize the top three key attributes of this currency and list them as bullet points?"
    return prompt

def get_crypto_summaries(crypto_list):
    # Open file to write summaries
    with open('crypto_summaries.txt', 'w') as f:
        for crypto in crypto_list:
            prompt = create_llm_prompt(crypto)
            response = get_llm_response(prompt)
            summary = f"Summary for {crypto}:\n{response}\n\n"
            print(summary)  # Still print to console
            f.write(summary)  # Also write to file

def load_crypto_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Specify the full path to the text file
file_path = '/Users/hal1/Desktop/       CascadeProjects/personal-website/crypto_list.txt'

# Load the cryptocurrency list from the text file
crypto_list = load_crypto_list(file_path)
get_crypto_summaries(crypto_list)