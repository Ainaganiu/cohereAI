import streamlit as st
import cohere

# Create a Cohere client with your API key
co = cohere.Client('gh7zeWIg1ZDBOGjYP09jnBDpUoHpo7Q4GEZwQ2zq')

# Define a Streamlit app
def app():
    # Set the app title
    st.title("AI Generated Blog Post")

    # Create a text input for the user to enter their topic
    topic = st.text_input("Enter topic for blog post")

    # Create a button that the user can click to generate the blog post
    if st.button("Generate Blog Post"):
        # Call the Cohere API to generate the blog post
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=f'Create a SEO blogpost with Table of Contents for the \"{topic}"\:',
            max_tokens=2130,
            temperature=0.9,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        
        # Get the generated text from the API response and display it to the user
        generated_text = response.generations[0].text
        st.write(generated_text)

# Run the app
if __name__ == "__main__":
    app()
