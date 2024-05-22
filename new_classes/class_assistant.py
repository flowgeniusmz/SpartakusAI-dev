import streamlit as st
from openai import OpenAI
from datetime import datetime
from new_classes import class_chathistory, class_messages



class Assistant:
    def __init__(self):
        self.initialize_openai()
        self.create_message = class_messages.CreateMessage()
        self.retrieve_message = class_messages.RetrieveMessage()
        self.initialize_chathistory()

    def initialize_openai(self):
        self.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        self.assistant_id = st.secrets.openai.assistant_id
        self.thread_id = st.session_state.thread_id

    def add_thread_message(self, role, content, image_urls: list = None, image_paths: list = None, file_paths: list = None):
        self.create_message.add_thread_message(role, content, image_urls, image_paths, file_paths)

    def display_thread_message(self):
        self.create_message.display_thread_message()

    def retrieve_latest_message(self):
        self.retrieve_message.get_thread_message_latest()
        self.retrieve_message.display_message()

