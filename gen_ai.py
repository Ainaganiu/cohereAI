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


write_topic('animal')

st.title("🚀 Startup Idea Generator")

form = st.form(key="user_settings")
with form:
    industry_input = st.text_input("Topic", key = "topic_input")
    generate_button = form.form_submit_button("Generate Idea")
    if generate_button:
        startup_idea = generate_idea(industry_input)
        st.markdown("##### " + startup_name)
        st.write(startup_idea)