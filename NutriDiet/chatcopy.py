import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory
load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
def get_response(query,user:str):
    UPSTASH_URL = "https://smooth-pika-45632.upstash.io"
    UPSTASH_TOKEN = "AbJAAAIncDFhMWY1NDBlYWI2ZmI0NzY3OWZkNDRhNTJlYjM4YjQxZnAxNDU2MzI"


    history = UpstashRedisChatMessageHistory(
        url=UPSTASH_URL,
        token=UPSTASH_TOKEN,
        session_id=user,
    )
    # history.add_user_message(f"my name is {user}")
    # stored_history = history.messages  
    # for message in stored_history:
    #     st.session_state.chat_history.append(message)
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=key,
        temperature=0.5,
    )

    prompt = ChatPromptTemplate.from_messages([

        ('system', '{user_name}  is the username. Address the user with their name.You are a diet planner.Ask the user necessary questions  like weight, height, ask about their activity,veg or non veg ,what purpose like gain weight or lose etc , any allergy, preferred cuisine in a intractive format and consider the chat history .just give breakfast,lunch ,snacks,dinner along with their approx macronutrients.'),
        MessagesPlaceholder("chat_history"),
        ('human', '{input}')
    ])
    print(user)
    prompt=prompt.partial(user_name=user)
    print(prompt)
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        chat_memory=history,
    )

    chain = LLMChain(
        llm=model,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
    response = chain.invoke({
        "input": query,
                             })
    return response['text']
def show_chat(user):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.title("Dietrix")

    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message("human"):
                st.markdown(message.content)
        else:
            with st.chat_message("Dietrix"):
                st.markdown(message.content)

    user_query = st.chat_input("Your Message")
    if user_query:
        st.session_state.chat_history.append(HumanMessage(user_query))
        with st.chat_message("human"):
            st.markdown(user_query)
        with st.chat_message("Dietrix"):
            msg = get_response(user_query,user)
            st.markdown(msg)
        st.session_state.chat_history.append(AIMessage(msg))
if __name__ == "__main__":
    user="abhi"
    show_chat(user)
