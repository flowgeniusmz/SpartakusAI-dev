import streamlit as st
from openai import OpenAI
from datetime import datetime

class ChatHistory:
    def __init__(self):
        self.initialize_openai()
        self.initialize_message_template()
        self.initialize_chathistory_messages()

    def initialize_openai(self):
        self.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        self.assistant_id = st.secrets.openai.assistant_id
        self.thread_id = st.session_state.thread_id
        self.thread_messages = self.openai_client.beta.threads.messages.list(thread_id=self.thread_id)

    def initialize_message_template(self):
        self.message_template = st.session_state.message_template

    def initialize_chathistory_messages(self):
        self.chathistory_messages = []
        for thread_message in self.thread_messages:
            new_message = self.message_template
            new_message.update({"username": st.session_state.username, "businessid": st.session_state.businses_id, "assistantid": st.secrets.openai.assistant_id, "threadid": self.thread_id, "runid": thread_message.run_id, "messageid": thread_message.id, "messagerole": thread_message.role, "messagecontent": thread_message.content[0].text.value, "createdatunix": thread_message.created_at, "createdatdatetime": datetime.fromtimestamp(thread_message.created_at).strftime('%Y-%m-%d %H:%M:%S') })
            self.chathistory_messages.append(new_message)
            self.update_sessionstate()

    def add_chathistory_message(self, messageid):
        thread_message = self.openai_client.beta.threads.messages.retrieve(message_id=messageid, thread_id=self.thread_id)
        new_message = self.message_template
        new_message.update({"username": st.session_state.username, "businessid": st.session_state.businses_id, "assistantid": st.secrets.openai.assistant_id, "threadid": self.thread_id, "runid": thread_message.run_id, "messageid": thread_message.id, "messagerole": thread_message.role, "messagecontent": thread_message.content[0].text.value, "createdatunix": thread_message.created_at, "createdatdatetime": datetime.fromtimestamp(thread_message.created_at).strftime('%Y-%m-%d %H:%M:%S') })
        self.chathistory_messages.append(new_message)
        self.update_sessionstate()

    def update_sessionstate(self):
        st.session_state.messages = self.chathistory_messages
