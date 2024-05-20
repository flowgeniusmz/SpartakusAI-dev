import streamlit as st
from openai import OpenAI
import time
import json
from tavily import TavilyClient
from classes.tools_class import Tools

class Assistant():
    def __init__(self):
        self.initialize_openai()
        self.initialize_tools()
        self.initialize_messages()
        self.assistant_tools = Tools()
        
    def initialize_openai(self):
        self.client = OpenAI(api_key=st.secrets.openai.api_key)
        self.thread_id = st.session_state.user_data.thread_id
        self.vector_store_id = st.session_state.user_data.vector_store_id
        self.assistant_id = st.secrets.openai.assistant_id
        self.file_ids = []
        
    def initialize_tools(self):
        self.tools_code_interpreter = {"type": "code_interpreter"}
        self.tools_file_search = {"type": "file_search"} 
        self.tools_functions = []
        
        
    def initialize_messages(self):
        self.existing_thread_messages = self.client.beta.threads.messages.list(thread_id=self.thread_id, order="desc")
        self.display_messages = [{"role": "assistant", "content": st.secrets.messageconfig.initial_assistant_message}]
        self.existing_messages = []
        for thread_message in self.existing_thread_messages:
            existing_message = {"role": thread_message.role, "content": thread_message.content[0].text.value}
            self.existing_messages.append(existing_message)
            
    def create_message(self, role, prompt):
        self.user_message = self.client.beta.threads.messages.create(thread_id=self.thread_id, role=role, content=prompt)
        self.user_message_id = self.user_message.id
        self.display_messages.append({"role": role, "content": prompt})
        self.existing_messages.append({"role": role, "content": prompt})
        
    def get_response(self, run_id):
        self.thread_message_list = self.client.beta.threads.messages.list(thread_id=self.thread_id, run_id=run_id)
        for response in self.thread_message_list:
            if response.role == "assistant":
                self.display_messages.append({"role": "assistant", "content": response.content[0].text.value})
                self.existing_messages.append({"role": "assistant", "content": response.content[0].text.value})
                
    def get_thread_messages(self):
        self.thread_messages = self.client.beta.threads.messages.list(thread_id=self.thread_id)
        
    def get_response_messages(self):
        for thread_message in self.thread_messages:
            if thread_message.role == "assistant" and thread_message.run_id == self.run_id:
                self.assistant_message_id = thread_message.id
                self.assistant_message_content = thread_message.content[0].text.value
                
    def create_run(self):
        self.run = self.client.beta.threads.runs.create(thread_id=self.thread_id, assistant_id=self.assistant_id)
        self.run_id = self.run.id
        self.run_status = self.run_status
        
    def retrieve_run(self):
        self.run = self.client.beta.threads.runs.retrieve(run_id=self.run_id, thread_id=self.thread_id)
        self.run_status = self.run.status
        
    def wait_on_run(self):
        while self.run_status != "completed":
            time.sleep(2)
            self.retrieve_run()
            if self.run_status == "completed": 
                self.get_thread_messages()
                self.get_response_messages()
                break
            elif self.run.status == "requires_action":
                self.tool_calls = self.run.required_action.submit_tool_outputs.tool_calls
                self.requires_action_type = self.run.required_action.type #should be submit tool outputs
                self.submit_tool_outputs()
                if self.tool_outputs:
                    self.retrieve_run()
                
    def submit_tool_outputs(self):
        self.tool_outputs = []
        for tool_call in self.tool_calls:
            toolname = tool_call.function.name
            toolargs = json.loads(tool_call.function.arguments)
            toolid = tool_call.id
            if toolname == "tavily_search":
                toolarg = toolargs['query']
                tooloutput = self.assistant_tools.tavily_search(query=toolarg)
                toolcalloutput = {"tool_call_id": toolid, "output": tooloutput}
                self.tool_outputs.append(toolcalloutput)