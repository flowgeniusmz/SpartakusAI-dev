import streamlit as st
import test1

class AcordForms:
    def __init__(self):
        self.Form_36 = test1.AccordForm36()
        self.Form_125 = test1.AccordForm125()
        self.Form_126 = test1.AccordForm126()
        self.Form_127= test1.AccordForm127()
        self.Form_130 = test1.AccordForm130()
        self.Form_133 = test1.AccordForm133()
        self.Form_137 = test1.AccordForm137()
        self.Form_140 = test1.AccordForm140()


a = AcordForms()
b = a.Form_125.form_name
print(b)