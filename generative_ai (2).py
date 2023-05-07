# -*- coding: utf-8 -*-
"""generative_ai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZulfvdJuqp90rloC5RSGdDoudIIA2YdU
"""

!pip install requests gradio -q

!pip install cohere -q

import cohere
co = cohere.Client('gh7zeWIg1ZDBOGjYP09jnBDpUoHpo7Q4GEZwQ2zq')
def write_topic(topic):
  topic = str(topic)
  response = co.generate(
    model='command-xlarge-nightly',
    prompt= f'Create a SEO blogpost with Table of Contents for the \"{topic}"\:',
    max_tokens=2130,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return print('Prediction: {}'.format(response.generations[0].text))

# Define the Streamlit app
def app():
    st.title('SEO Blogpost Generator with Table of Contents')

    # Add a text input for the topic
    topic = st.text_input('Enter the topic for the blog post:', value='')

    # Add a button to generate the blog post
    if st.button('Generate Blog Post'):
        # Call the generate_blogpost function and display the result
        blogpost = write_topic(topic)
        st.text_area('Generated Blog Post:', value=blogpost, height=400)

# Launch the app in a Jupyter Notebook
if __name__ == '__main__':
    app()

# Define the Streamlit app
st.title('SEO Blogpost Generator with Table of Contents')

# Add a text input for the topic
topic = st.text_input('Enter the topic for the blog post:', value='')

# Add a button to generate the blog post
if st.button('Generate Blog Post'):
    # Call the generate_blogpost function and display the result
    blogpost = write_topic(topic)
    st.text_area('Generated Blog Post:', value=blogpost, height=400)

import gradio as gr

with gr.Blocks() as demo:
  gr.Markdown("# AI generated Blogpost with Cohere API")
  #with gr.Row():
  inp = gr.Textbox(placeholder="Enter your Topic for Blog post Generation", label = "Topic")
  btn = gr.Button("Generate ")
  out = gr.Textbox()
  btn.click(fn=write_topic, inputs=inp, outputs=out)

demo.launch(debug=False)
