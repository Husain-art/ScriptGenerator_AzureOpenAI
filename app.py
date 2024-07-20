# from flask import Flask, request, jsonify
import streamlit as st
# from flask import Flask, request

# Initialize the Flask application
# app = Flask(__name__)

# Set up the OpenAI API key (replace 'your-api-key' with your actual API key)
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://gaming-azure-openai.openai.azure.com/",
    api_key="Give Your Id",
    api_version="2023-03-15-preview"
)


# Define a route for the API
# @app.route('/api', methods=['POST'])
def genrate_result(system_message,user_message):
    # Get the data from the request
    # data = request.json
    # prompt = data.get('prompt', '')

    message_text = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]

    # Call the OpenAI API with the prompt
    response = client.chat.completions.create(
        model="ModelName",  # model = "gpt-35-turbo-16k"
        messages=message_text,
        temperature=0,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return response.choices[0].message.content
    # # response = openai.Completion.create(
    # #     engine="davinci",
    # #     prompt=prompt,
    # #     max_tokens=150
    # # )

    # # Return the response from OpenAI API
    # return jsonify(response)

# Define a Streamlit interface
def streamlit_interface():
    st.title("scope Query Generator")
    st.write("Enter your criteria to generate Scope and view results.")
    
    # fileName = "C:\\Users\\v-hcyclewala\\PycharmProjects\\Azure-OpenAI-SQL-master\\Azure-OpenAI-SQL-master\\Prompts.txt"
    
    fileName = "Prompts.txt"
    infile = open(fileName, 'r')
    Context = infile.read()

    user_message = st.text_input("Enter your message:")
    # user_input = st.text_area("Enter your prompt:")
    # if st.button('Submit'):
    if user_message:
        formatted_system_message = Context
        # Call the Flask API with the user input
        # response = get_completion_from_messages(formatted_system_message, user_message)
        response = genrate_result(formatted_system_message, user_message)
        st.write(response)

# Run the Streamlit interface if the script is run directly
if __name__ == '__main__':
    streamlit_interface()



# Run the Flask application:
# python app.py

# Access the Streamlit interface:
# streamlit run app.py