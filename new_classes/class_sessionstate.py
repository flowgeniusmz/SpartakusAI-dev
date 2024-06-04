import streamlit as st
from new_classes import class_chathistory
from simple_salesforce import Salesforce as sfdcClient
from supabase import create_client as supaClient
from openai import OpenAI as oaiClient
from googlemaps import Client as gClient
from tavily import TavilyClient as tavClient

class SessionState:
    def __init__(self):
        if "initialized" not in st.session_state:
            self.initialize_sessionstate_openai()
            self.initialize_sessionstate_user()
            self.initialize_sessionstate_other()

    def initialize_sessionstate_openai(self):
        st.session_state.assistant_id = st.secrets.openai.assistant_id

    def initialize_sessionstate_user(self):
        st.session_state.username = None
        st.session_state.password = None
        st.session_state.firstname = None
        st.session_state.lastname = None
        st.session_state.fullname = None
        st.session_state.email = None
        st.session_state.thread_id = None
        st.session_state.vectorstore_id = None
        st.session_state.createddate = None
        st.session_state.userrole = None
        st.session_state.business_id = None
        st.session_state.authenticated = False
        st.session_state.authentication_select_string = f"{st.secrets.supabase.username_column}, {st.secrets.supabase.password_column}, {st.secrets.supabase.firstname_column}, {st.secrets.supabase.lastname_column}, {st.secrets.supabase.fullname_column}, {st.secrets.supabase.email_column}, {st.secrets.supabase.createddate_column}, {st.secrets.supabase.userrole_columns}, {st.secrets.supabase.vstoreid_column}, {st.secrets.supabase.threadid_column}, {st.secrets.supabase.businessid_column}"

    def initalize_sessionstate_chathistory(self):
        st.session_state.message_template = {"username": None, "businessid": None, "assistantid": st.secrets.openai.assistant_id, "threadid": None, "runid": None, "messageid": None, "messagerole": None, "messagecontent": None, "createdatunix": None, "createdatdatetime": None }
        st.session_state.messages = []
        st.session_state.chat_history = class_chathistory.ChatHistory()

    def initialize_sessionstate_other(self):
        st.session_state.request_headers = {'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate, br'}

    def initialize_clients(self):
        st.session_state.google_client = gClient(key=st.secrets.google.api_key)
        st.session_state.salesforce_client = sfdcClient(username=st.secrets.salesforce.username, password=st.secrets.salesforce.password, security_token=st.secrets.salesforce.security_token)
        st.session_state.tavily_client = tavClient(api_key=st.secrets.tavily.api_key)
        st.session_state.openai_client = oaiClient(api_key=st.secrets.openai.api_key)
        st.session_state.supabase_client = supaClient(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
