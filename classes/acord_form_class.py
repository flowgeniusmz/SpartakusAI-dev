import streamlit as st
from assets.acord import acord_form_125, acord_form_126, acord_form_127, acord_form_130, acord_form_133, acord_form_137, acord_form_140, acord_form_36



class AcordForm():
    def __init__(self):
        self.initialize_form_name
        self.initialize_form_data

    def initialize_form_data(self):
        self.form_125_data = acord_form_125.acord_form_125_data
        self.form_126_data = acord_form_126.acord_form_126_data
        self.form_127_data = acord_form_127.acord_form_127_data
        self.form_130_data = acord_form_130.acord_form_130_data
        self.form_133_data = acord_form_133.acord_form_133_data
        self.form_137_data = acord_form_137.acord_form_137_data
        self.form_140_data = acord_form_140.acord_form_140_data
        self.form_36_data = acord_form_36.acord_form_36_data

    def initialize_form_name(self):
        self.form_125_name = acord_form_125.acord_form_125_name
        self.form_126_name = acord_form_126.acord_form_126_name
        self.form_127_name = acord_form_127.acord_form_127_name
        self.form_130_name = acord_form_130.acord_form_130_name
        self.form_133_name = acord_form_133.acord_form_133_name
        self.form_137_name = acord_form_137.acord_form_137_name
        self.form_140_name = acord_form_140.acord_form_140_name
        self.form_36_name = acord_form_36.acord_form_36_name