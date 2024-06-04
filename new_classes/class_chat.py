import streamlit as st
from openai import OpenAI as oaiClient
import time
import json
from tavily import TavilyClient as tavClient
from datetime import datetime
from simple_salesforce import Salesforce as sfdcClient
from enum import Enum
from typing import List, Dict, Union, Any, Optional
from pydantic import BaseModel, Field
import googlemaps.addressvalidation
import googlemaps.geocoding
import pandas as pd
import requests
from googlemaps import Client as gClient, addressvalidation, places, geocoding, geolocation
from supabase import create_client as supaClient


class Clients:
    def __init__(self):
        self.openai_client = oaiClient(api_key=st.secrets.openai.api_key)
        self.salesforce_client  = sfdcClient(username=st.secrets.salesforce.username, password=st.secrets.salesforce.password, security_token=st.secrets.salesforce.security_token)
        self.supabase_client = supaClient(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
        self.tavily_client = tavClient(api_key=st.secrets.tavily.api_key)
        self.google_client = gClient(key=st.secrets.google.api_key)

class Utils:
    def __init__(self):
        self.clients = Clients()

    def get_request_headers(self):
        request_headers = {'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate, br'}
        return request_headers

    def create_openai_file(self, file_path, purpose):
        openai_file = self.clients.openai_client.files.create(file=open(file=file_path, mode="rb"), purpose=purpose)
        openai_file_id = openai_file.id
        return openai_file_id



class Assistant:
    def __init__(self):
        self.clients = Clients()
        self.assistant_id = st.secrets.openai.assistant_id
        
    
    def initialize_clients(self):
        self.openai_client = st.session_state.openai_clients


class Thread:
    def __init__(self):
        self.clients = Clients()
        self.thread_id = st.session_state.thread_id


class Tools:
    def __init__(self):
        self.clients = Clients()
        self.utils = Utils()
        self.request_headers = self.utils.get_request_headers()

    def yelp_business_search(self, query, postalcode, start_page, num_pages):
        results_df = pd.DataFrame(columns=['URL', 'Response Status', 'Response Text', 'Response JSON'])
        for i in range(start_page, start_page + num_pages * 20, 20):
            url = self.yelp_base_url.format(query=query, postalcode=postalcode, i=i)
            response = requests.get(url, headers=self.headers)
            response_status = response.status_code
            response_text = response.text
            try:
                response_json = response.json()
            except ValueError:
                response_json = None
            new_row = pd.DataFrame([{
                'URL': url,
                'Response Status': response_status,
                'Response Text': response_text,
                'Response JSON': response_json
            }])
            results_df = pd.concat([results_df, new_row], ignore_index=True)
        return results_df

