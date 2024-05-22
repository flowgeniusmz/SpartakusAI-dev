import streamlit as st
from streamlit_extras import stylable_container as sc


class Style():
    def __init__(self):
        self.initialize_styles()
        self.initialize_elements()
        
    def display_styled_homepage(self):
        self.container_style1 = self.create_styled_element(element_type="container", style_type=1)
        self.expander_style_1 = self.create_styled_element(element_type="expander", style_type=1)
    
    def initialize_styles(self):
        self.style1 = """
            {
                border: 1px solid rgba(34, 163, 97);
                background-color: rgba(40, 94, 159, 0.5);
                border-radius: 0.5rem;
                padding: calc(1em - 1px);
                overflow: hidden; /* Prevents the content from overflowing */
                box-sizing: border-box; 
            }
            """
        
        self.style2 = """
        {
            border: 2px solid rgba(0, 0, 0, 0.2); /* Changed border color to a subtle grey */
            background-color: rgba(40, 94, 159, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """

        self.style3 = """
        {
            border: 2px solid rgba(40, 94, 159, 0.75); /* Changed border color to a subtle grey */
            background-color: rgba(255, 255, 255, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """


    def create_stylable_container(self, style_type):
        if style_type == 1:
            css_styles = self.style1
        elif style_type == 2:
            css_styles = self.style2
        elif style_type == 3:
            css_styles = self.style3

        styled_container = sc.stylable_container(key="adfadf", css_styles=css_styles)
        return styled_container
    
    def create_styled_element(self, element_type, style_type):
        style = self.create_stylable_container(style_type=style_type)
        with style:
            if element_type == "container": 
                styled_element = st.container(height=200, border=False).markdown("yo")
            elif element_type == "expander":
                styled_element = st.expander(label="test").markdown("hey")
            elif element_type == "popover":
                styled_element == st.popover()
            return styled_element


