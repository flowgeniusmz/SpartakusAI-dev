import streamlit as st
from openai import OpenAI
from datetime import datetime
from new_classes import class_chathistory



class CreateMessage:
    def __init__(self):
        self.initialize_openai()

    def initialize_openai(self):
        self.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        self.assistant_id = st.secrets.openai.assistant_id
        self.thread_id = st.session_state.thread_id

    def add_thread_message(self, role, content, image_urls: list = None, image_paths: list = None, file_paths: list = None):
        self.format_thread_message_content(content=content, image_paths=image_paths, image_urls=image_urls)
        self.format_thread_message_attachments(file_paths=file_paths)
        self.thread_message = self.openai_client.beta.threads.messages.create(thread_id=self.thread_id, role=role, content=self.thread_message_content, attachments=self.thread_message_attachments)
        self.thread_message_id = self.thread_message.id
        st.session_state.chat_history.add_chathistory_message(messageid=self.thread_message_id)

    def format_thread_message_content(self, content, image_urls: list = None, image_paths: list = None):
        self.thread_message_content = None
        if image_urls is None and image_paths is None:
            self.thread_message_content = content
        else:
            self.thread_message_content = [{"type": "text", "text": content}]
            if image_urls is not None:
                for image_url in image_urls:
                    self.thread_message_content.append({"type": "image_url", "image_url": {"url": image_url, "detail": "auto"}})
            if image_paths is not None:
                for image_path in image_paths:
                    self.create_openai_file(file_path=image_path, purpose="vision")
                    self.thread_message_content.append({"type": "image_file", "image_file": {"file_id": self.file_id, "detail": "auto"}})

    def format_thread_message_attachments(self, file_paths: list = None):
        self.thread_message_attachments = None
        if file_paths is not None:
            self.thread_message_attachments = []
            for file_path in file_paths:
                self.create_openai_file(file_path=file_path, purpose="assistants")
                self.thread_message_attachments.append({"file_id": self.file_id, "tools": [{"type": "code_interpreter"}]})

    def create_openai_file(self, file_path, purpose):
        file = self.openai_client.files.create(file=open(file=file_path, mode="rb"), purpose=purpose)
        self.file_id = file.id

    def display_thread_message(self):
        with st.chat_message(name=self.thread_message.role):
            st.markdown(body=self.thread_message.content[0].text.value)

class RetrieveMessage:
    def __init__(self):
        self.initialize_openai()
        self.get_thread_messages()
        self.get_thread_message_latest()
        self.get_thread_message_content(include_annotations=True)

    def initialize_openai(self):
        self.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        self.assistant_id = st.secrets.openai.assistant_id
        self.thread_id = st.session_state.thread_id

    def get_thread_messages(self, runid: str = None):
        if runid is None:
            self.thread_messages = self.openai_client.beta.threads.messages.list(thread_id=self.thread_id)
        else:
            self.thread_messages = self.openai_client.beta.threads.messages.list(thread_id=self.thread_id, run_id=runid)

    def get_thread_message_by_id(self, messageid):
        self.thread_message = self.openai_client.beta.threads.messages.retrieve(message_id=messageid, thread_id=self.thread_id)
        self.add_message_to_chathistory()

    def get_thread_message_by_runid(self, runid):
        for thread_message in self.thread_messages:
            if thread_message.role == "assistant" and thread_message.run_id == runid:
                self.thread_message = thread_message
                self.add_message_to_chathistory()

    def get_thread_message_latest(self):
        self.thread_message = self.thread_messages.data[0]
        self.add_message_to_chathistory()

    def add_message_to_chathistory(self):
        self.thread_message_id = self.thread_message.id
        st.session_state.chat_history.add_chathistory_message(messageid=self.thread_message_id)

    def get_thread_message_content(self, include_annotations: bool = False):
        if not include_annotations:
            self.thread_message_content = self.thread_message.content[0].text.value
        else:
            self.thread_message_text = self.thread_message.content[0].text
            self.thread_message_annotations = self.thread_message_text.annotations
            self.thread_message_citations = []
            for index, annotation in enumerate(self.thread_message_annotations):
                self.thread_message_text = self.thread_message_text.value.replace(annotation.text, f' [{index}]')
                if (file_citation := getattr(annotation, 'file_citation', None)):
                    cited_file = self.openai_client.files.retrieve(file_id=file_citation.file_id)
                    self.thread_message_citations.append(f"[{index}] {file_citation.quote} from {cited_file.filename}")
                elif (file_path := getattr(annotation, 'file_path', None)):
                    cited_file = self.openai_client.files.retrieve(file_id=file_path.file_id)
                    self.thread_message_citations.append(f"[{index}] Click {file_path} to download {cited_file.filename} ({file_path.file_id})")
            self.thread_message_content = self.thread_message_text.value + '\n' + '\n'.join(self.thread_message_citations)

    def display_message(self):
        with st.chat_message(name=self.thread_message.role):
            st.markdown(self.thread_message_content)