import streamlit as st
from openai import OpenAI as oaiClient
from tavily import TavilyClient as tavClient
from simple_salesforce import Salesforce as sfdcClient
from googlemaps import Client as gClient
from supabase import create_client as supaClient


class Clients:
    def __init__(self):
        self.openai_client = oaiClient(api_key=st.secrets.openai.api_key)
        self.salesforce_client  = sfdcClient(username=st.secrets.salesforce.username, password=st.secrets.salesforce.password, security_token=st.secrets.salesforce.security_token)
        self.supabase_client = supaClient(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
        self.tavily_client = tavClient(api_key=st.secrets.tavily.api_key)
        self.google_client = gClient(key=st.secrets.google.api_key)

    def get_openai_client(self):
        return self.openai_client
    
    def get_salesforce_client(self):
        return self.salesforce_client
    
    def get_supabase_client(self):
        return self.supabase_client
    
    def get_tavily_client(self):
        return self.tavily_client
    
    def get_google_client(self):
        return self.google_client
