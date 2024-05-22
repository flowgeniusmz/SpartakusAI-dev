import streamlit as st
from openai import OpenAI
import time
from new_classes import class_tools
import json

class Run:
    def __init__(self):
        self.initialize_openai()
        self.assistant_tools = class_tools.Tools()

    def initialize_openai(self):
        self.openai_client = OpenAI(api_key=st.secrets.openai.api_key)
        self.thread_id = st.session_state.thread_id
        self.assistant_id = st.secrets.openai.assistant_id
        self.run_id = None
        self.run_status = None
        self.tool_outputs = None

    def execute_run(self):
        self.run = self.openai_client.beta.threads.runs.create_and_poll(assistant_id=self.assistant_id, thread_id=self.thread)
        self.run_id = self.run.id
        self.run_status = self.run.status
        if self.run_status == "completed":
            print(self.run_status)
        elif self.run_status == "requires_action":
            self.tool_calls = self.run.required_action.submit_tool_outputs.tool_calls
            if self.tool_calls:
                self.handle_required_action()
            if self.tool_outputs:
                self.submit_tool_outputs()

    def handle_required_action(self):
        self.tool_outputs = []
        for tool_call in self.tool_calls:
            tool_id = tool_call.id
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            # Dynamically call the tool method if it exists in the Tools class
            if hasattr(self.assistant_tools, tool_name):
                tool_method = getattr(self.assistant_tools, tool_name)
                tool_output = tool_method(**tool_args)
                tool_call_output = {"tool_call_id": tool_id, "output": tool_output}
                self.tool_outputs.append(tool_call_output)

    def submit_tool_outputs(self):
        self.run = self.openai_client.beta.threads.runs.submit_tool_outputs_and_poll(tool_outputs=self.tool_outputs, run_id=self.run_id, thread_id=self.thread_id)

            