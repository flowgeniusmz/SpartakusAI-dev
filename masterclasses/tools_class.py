import streamlit as st
from masterclasses import client_class, utils_class

class Tools:
    def __init__(self):

    def initialize_tool_types(self):
        self.tool_code_interpreter = {"type": "code_interpreter"}
        self.tool_file_search = {"type": "file_search"}