import streamlit as st
from enum import Enum
#from classes.acord_form_class_ind import AccordForm36, AccordForm125, AccordForm126, AccordForm127, AccordForm130, AccordForm133, AccordForm137, AccordForm140
from classes import acord_form_class_ind


class AcordForms:
    def __init__(self):
        self.Form_36 = acord_form_class_ind.AccordForm36()
        self.Form_125 = acord_form_class_ind.AccordForm125()
        self.Form_126 = acord_form_class_ind.AccordForm126()
        self.Form_127= acord_form_class_ind.AccordForm127()
        self.Form_130 = acord_form_class_ind.AccordForm130()
        self.Form_133 = acord_form_class_ind.AccordForm133()
        self.Form_137 = acord_form_class_ind.AccordForm137()
        self.Form_140 = acord_form_class_ind.AccordForm140()


a = AcordForms()
b = a.Form_125.form_data
print(b)

