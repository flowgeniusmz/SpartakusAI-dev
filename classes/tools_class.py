import googlemaps.addressvalidation
import googlemaps.geocoding
import streamlit as st
from openai import OpenAI
from simple_salesforce import Salesforce
from tavily import TavilyClient
import pandas as pd
import json
import time
import requests
from googlemaps import Client as gClient, addressvalidation, places, geocoding, geolocation

class Tools:
    def __init__(self):
        self.salesforce_client = Salesforce(username=st.secrets.salesforce.username, password=st.secrets.salesforce.password, security_token=st.secrets.salesforce.security_token)
        self.tavily_client = TavilyClient(api_key=st.secrets.tavily.api_key)
        self.google_client = gClient(key=st.secrets.googleconfig.maps_api_key)
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        self.yelp_base_url = st.secrets.urlconfig.yelp_search_url
    
    def fetch_yelp_data(self, query, postalcode, start_page, num_pages):
        """
        Fetch data from Yelp search results.

        Parameters:
        - query (str): The search term for Yelp.
        - postalcode (str): The postal code for the search location.
        - start_page (int): The starting page number.
        - num_pages (int): The number of pages to fetch.

        Returns:
        - pd.DataFrame: A dataframe with columns URL, Response Status, Response Text, and Response JSON.
        """
        # Initialize an empty dataframe
        results_df = pd.DataFrame(columns=['URL', 'Response Status', 'Response Text', 'Response JSON'])
        
        # Loop through the specified number of pages
        for i in range(start_page, start_page + num_pages * 20, 20):
            # Construct the URL using the base URL from secrets
            url = self.yelp_base_url.format(query=query, postalcode=postalcode, i=i)
            
            # Make the request
            response = requests.get(url, headers=self.headers)
            
            # Collect the response details
            response_status = response.status_code
            response_text = response.text
            try:
                response_json = response.json()
            except ValueError:
                response_json = None
            
            # Append to the dataframe
            new_row = pd.DataFrame([{
                'URL': url,
                'Response Status': response_status,
                'Response Text': response_text,
                'Response JSON': response_json
            }])
            results_df = pd.concat([results_df, new_row], ignore_index=True)
        
        return results_df

    def search_tavily(self, query: str = None):
        """
        Searches for information using the TavilyClient.

        Parameters:
        - query (str): The search query string.

        Returns:
        - dict: The search response containing results, raw content, and answer if applicable.
        """
        include_raw_content = True
        max_results = 10
        include_answer = True
        search_depth = "advanced"
        
        # Perform the search with the given parameters
        search_response = self.tavily_client.search(
            query=query, 
            search_depth=search_depth, 
            include_raw_content=include_raw_content, 
            include_answer=include_answer
        )
        
        return search_response

    def validate_address(self, address_lines):
        self.address_validation_response = addressvalidation.addressvalidation(client=self.google_client, addressLines=address_lines, regionCode="US", enableUspsCass=True)
        # print(self.addvalidate)
        # ['1840 Coralito Ln', 'Elgin, IL 60124']
    
    def get_geocode(self, address_lines):
        self.address_geocode_response = geocoding.geocode(client=self.google_client, address=address_lines, region="US")

    def places_search(self, query):
        self.places_search_response = places.places(client=self.google_client, query=query, region="US")

    def execute_soql_query(self, query):
        """
        Execute a SOQL query and return the results.

        Parameters:
        - query (str): The SOQL query to be executed.

        Returns:
        - dict: The query results or an error message.
        """
        try:
            response = self.sf.query_all(query)
            return response['records']
        except Exception as e:
            return {"error": str(e)}

    def execute_python_code(self, code):
        """
        Execute the provided Python code.

        Parameters:
        - code (str): The Python code to be executed.

        Returns:
        - dict: The result of the code execution or an error message.
        """
        try:
            exec_globals = {}
            exec(code, exec_globals)
            return {"result": exec_globals}
        except Exception as e:
            return {"error": str(e)}

    def get_openai_json_schema(self):
        """
        Returns the OpenAI JSON schema list for each tool.

        Returns:
        - list: A list of schemas for each tool.
        """
        return [
            {
                "type": "function",
                "function": {
                    "name": "fetch_yelp_data",
                    "description": "Fetch data from Yelp search results",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search term for Yelp"
                            },
                            "postalcode": {
                                "type": "string",
                                "description": "The postal code for the search location"
                            },
                            "start_page": {
                                "type": "integer",
                                "description": "The starting page number"
                            },
                            "num_pages": {
                                "type": "integer",
                                "description": "The number of pages to fetch"
                            }
                        },
                        "required": ["query", "postalcode", "start_page", "num_pages"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "search_tavily",
                    "description": "Searches for information using the TavilyClient",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query string"
                            }
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "execute_soql_query",
                    "description": "Execute a SOQL query in Salesforce and return the results",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The SOQL query to be executed"
                            }
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "execute_python_code",
                    "description": "Use this function to execute the generated code which requires internet access or external API access",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "The python code generated by the code interpreter"
                            }
                        },
                        "required": ["code"]
                    }
                }
            }
        ]
    
a = Tools()
#b = a.validate_address()
#b = a.get_geocode(address_lines=['1840 Coralito Ln', 'Elgin, IL 60124'])
# b = a.places_search(query="Jewel Osco Elgin IL")
# print(a.places_search_response)

print(a.search_tavily(query="What year was the Jewel Osco in South Elgin built? How old is its roof?"))