import streamlit as st
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory
def share_story():
    st.title("Share Your Story")

    
    with st.form(key='story_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        story = st.text_area("Your Story")
        
        submit_button = st.form_submit_button(label='Submit')
    UPSTASH_URL = "https://smooth-pika-45632.upstash.io"
    UPSTASH_TOKEN = "AbJAAAIncDFhMWY1NDBlYWI2ZmI0NzY3OWZkNDRhNTJlYjM4YjQxZnAxNDU2MzI"


    history = UpstashRedisChatMessageHistory(
        url=UPSTASH_URL,
        token=UPSTASH_TOKEN,
        session_id="story",
    )
 
    if submit_button:
        if name and email and story:
            if 'stories' not in st.session_state:
                st.session_state.stories = []
            
            st.session_state.stories.append({'name': name, 'email': email, 'story': story})
        
            history.add_user_message(st.session_state.stories)
            st.success("Thank you for sharing your story!")
        else:
            st.error("Please fill out all fields.")
    for i in range(len(history.messages)):
        a = history.messages[i].content
        txt = ''
        name = str(a[0]['name'])
        story = str(a[0]['story'])
        # txt.join(name + '\n' + story)
        st.markdown("Name:"+name)  
        st.markdown(story)
        st.markdown("-"*50)
    # st.subheader("Stories Shared by Our Community")

   

share_story()

