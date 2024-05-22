import streamlit as st
from openai import OpenAI
from supabase import create_client


class UserFlow:
    def __init__(self):
        self.authenticated = st.session_state.authenticated

    def initial_render(self):
        if not self.authenticated:

    @st.experimental_dialog("User Login", width="large")
    def display_authentication_form(self):
        self.username = st.text_input("Username", key="username")
        self.password = st.text_input("Password", key="password", type="password")
        self.attempted_auth = st.button(label="Submit", key="attempted_auth", type="primary", on_click=self.authenticate_user, args=[st.session_state.username, st.session_state.password])

    def authenticate_user(self, username, password):
        self.supabase_client = create_client(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)
        self.select_string = st.session_state.authentication_select_string
        self.username_column = st.secrets.supabase.username_column
        self.password_column = st.secrets.supabase.password_column
        self.auth_response = self.supabase_client.table(st.secrets.supabase.users_table).select(self.select_string).eq(self.username_column, username).eq(self.password_column, password)

