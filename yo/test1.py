import streamlit as st
from assets.acord import acord_form_125, acord_form_126, acord_form_127, acord_form_130, acord_form_133, acord_form_137, acord_form_140, acord_form_36
from enum import Enum





class AccordForm36:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_36.acord_form_36_name
        self.form_data = acord_form_36.acord_form_36_data
        self.form_tool = acord_form_36.acord_form_36_tool

    def submit_underwriter_data(self, business_info, naics_code, number_of_employees, total_payroll, years_in_business, claims_history, safety_programs, requested_coverage):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.total_payroll = total_payroll
        self.years_in_business = years_in_business
        self.claims_history = claims_history  # List of claims with details
        self.safety_programs = safety_programs  # Dictionary of safety programs and their effectiveness
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 1000:
            risk_score += 30
        elif self.number_of_employees > 500:
            risk_score += 20
        elif self.number_of_employees > 100:
            risk_score += 10
        else:
            risk_score += 5

        # Total payroll
        if self.total_payroll > 50000000:
            risk_score += 30
        elif self.total_payroll > 20000000:
            risk_score += 20
        elif self.total_payroll > 10000000:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Safety programs
        for program, effectiveness in self.safety_programs.items():
            if effectiveness == "Excellent":
                risk_score -= 10
            elif effectiveness == "Good":
                risk_score -= 5
            # No change for "Average" or below

        # Requested coverage
        if self.requested_coverage > 10000000:
            risk_score += 20
        elif self.requested_coverage > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm125:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_125.acord_form_125_name
        self.form_data = acord_form_125.acord_form_125_data
        self.form_tool = acord_form_125.acord_form_125_tool

    def submit_underwriter_data(self, business_info, business_type, years_in_business, number_of_employees, annual_revenue, prior_claims):
        self.business_info = business_info
        self.business_type = business_type
        self.years_in_business = years_in_business
        self.number_of_employees = number_of_employees
        self.annual_revenue = annual_revenue
        self.prior_claims = prior_claims

    def calculate_risk_score(self):
        risk_score = 0

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10  # Lower risk for established businesses
        else:
            risk_score += 20  # Higher risk for newer businesses

        # Number of employees
        if self.number_of_employees > 50:
            risk_score += 15  # Higher risk for larger businesses
        else:
            risk_score -= 5  # Lower risk for smaller businesses

        # Annual revenue
        if self.annual_revenue > 1000000:
            risk_score += 10  # Higher risk for high-revenue businesses
        else:
            risk_score -= 5  # Lower risk for lower-revenue businesses

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 5  # Add 5 points for each prior claim

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 20:
            decision = "Accept"
            premium_modifier = 0.9  # 10% discount
        elif 20 <= risk_score < 40:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm126:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_126.acord_form_126_name
        self.form_data = acord_form_126.acord_form_126_data
        self.form_tool = acord_form_126.acord_form_126_tool

    def submit_underwriter_data(self, business_info, business_type, location, annual_revenue, number_of_employees, years_in_business, prior_claims):
        self.business_info = business_info
        self.business_type = business_type
        self.location = location
        self.annual_revenue = annual_revenue
        self.number_of_employees = number_of_employees
        self.years_in_business = years_in_business
        self.prior_claims = prior_claims

    def calculate_risk_score(self):
        risk_score = 0

        # Business type risk factor
        high_risk_businesses = ["Construction", "Manufacturing", "Nightclub"]
        low_risk_businesses = ["Office", "Retail", "Restaurant"]
        
        if self.business_type in high_risk_businesses:
            risk_score += 30
        elif self.business_type in low_risk_businesses:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other business types

        # Location risk factor
        high_risk_locations = ["Urban", "Coastal"]
        low_risk_locations = ["Suburban", "Rural"]
        
        if self.location in high_risk_locations:
            risk_score += 20
        elif self.location in low_risk_locations:
            risk_score += 10
        else:
            risk_score += 15  # Default risk score for other locations

        # Annual revenue
        if self.annual_revenue > 5000000:
            risk_score += 20
        elif self.annual_revenue > 1000000:
            risk_score += 10
        else:
            risk_score += 5

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 10

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm127:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_127.acord_form_127_name
        self.form_data = acord_form_127.acord_form_127_data
        self.form_tool = acord_form_127.acord_form_127_tool

    def submit_underwriter_data(self, business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage):
        self.business_info = business_info
        self.vehicles = vehicles  # List of vehicle details
        self.drivers = drivers  # List of driver details
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Vehicle information
        for vehicle in self.vehicles:
            vehicle_type = vehicle.get("type", "")
            vehicle_age = vehicle.get("age", 0)
            vehicle_value = vehicle.get("value", 0)

            if vehicle_type in ["Truck", "Heavy Equipment"]:
                risk_score += 30  # Higher risk for trucks and heavy equipment
            elif vehicle_type in ["Car", "Van"]:
                risk_score += 10  # Lower risk for cars and vans

            if vehicle_age > 10:
                risk_score += 20  # Higher risk for older vehicles
            elif vehicle_age > 5:
                risk_score += 10

            if vehicle_value > 50000:
                risk_score += 20  # Higher risk for high-value vehicles
            elif vehicle_value > 20000:
                risk_score += 10

        # Driver information
        for driver in self.drivers:
            driver_age = driver.get("age", 0)
            driving_experience = driver.get("experience", 0)
            driving_record = driver.get("record", "Clean")

            if driver_age < 25 or driver_age > 65:
                risk_score += 20  # Higher risk for young or senior drivers
            elif driver_age < 30 or driver_age > 55:
                risk_score += 10

            if driving_experience < 5:
                risk_score += 20  # Higher risk for less experienced drivers
            elif driving_experience < 10:
                risk_score += 10

            if driving_record == "Poor":
                risk_score += 30  # Higher risk for poor driving records
            elif driving_record == "Fair":
                risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "484"]  # Construction, Manufacturing, Transportation
        low_risk_industries = ["541", "611", "722"]  # Professional Services, Education, Food Services

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 1000000:
            risk_score += 20
        elif self.requested_coverage > 500000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }
    
class AccordForm130:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_130.acord_form_130_name
        self.form_data = acord_form_130.acord_form_130_data
        self.form_tool = acord_form_130.acord_form_130_tool

    def submit_underwriter_data(self, business_info, naics_code, number_of_employees, total_payroll, years_in_business, prior_claims, claim_severity):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.total_payroll = total_payroll
        self.years_in_business = years_in_business
        self.prior_claims = prior_claims
        self.claim_severity = claim_severity

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Total payroll
        if self.total_payroll > 10000000:
            risk_score += 20
        elif self.total_payroll > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 10
            # Severity of claims
            if self.claim_severity == "High":
                risk_score += 20
            elif self.claim_severity == "Medium":
                risk_score += 10
            else:
                risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm133:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_133.acord_form_133_name
        self.form_data = acord_form_133.acord_form_133_data
        self.form_tool = acord_form_133.acord_form_133_tool

    def submit_underwriter_data(self, business_info, naics_code, number_of_employees, annual_revenue, claims_history, underlying_limits, requested_umbrella_limit):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.underlying_limits = underlying_limits  # Dictionary of underlying policy limits
        self.requested_umbrella_limit = requested_umbrella_limit

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Underlying policy limits
        minimum_required_limits = {
            "general_liability": 1000000,
            "auto_liability": 1000000,
            "employers_liability": 500000
        }
        
        for policy, limit in self.underlying_limits.items():
            required_limit = minimum_required_limits.get(policy, 0)
            if limit < required_limit:
                risk_score += 20

        # Requested umbrella coverage limit
        if self.requested_umbrella_limit > 5000000:
            risk_score += 20
        elif self.requested_umbrella_limit > 1000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm137:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_137.acord_form_137_name
        self.form_data = acord_form_137.acord_form_137_data
        self.form_tool = acord_form_137.acord_form_137_tool

    def submit_underwriter_data(self, business_info, naics_code, number_of_employees, total_payroll, years_in_business, claims_history, safety_programs, requested_coverage):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.total_payroll = total_payroll
        self.years_in_business = years_in_business
        self.claims_history = claims_history  # List of claims with details
        self.safety_programs = safety_programs  # Dictionary of safety programs and their effectiveness
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 1000:
            risk_score += 30
        elif self.number_of_employees > 500:
            risk_score += 20
        elif self.number_of_employees > 100:
            risk_score += 10
        else:
            risk_score += 5

        # Total payroll
        if self.total_payroll > 50000000:
            risk_score += 30
        elif self.total_payroll > 20000000:
            risk_score += 20
        elif self.total_payroll > 10000000:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Safety programs
        for program, effectiveness in self.safety_programs.items():
            if effectiveness == "Excellent":
                risk_score -= 10
            elif effectiveness == "Good":
                risk_score -= 5
            # No change for "Average" or below

        # Requested coverage
        if self.requested_coverage > 10000000:
            risk_score += 20
        elif self.requested_coverage > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

class AccordForm140:
    def __init__(self):
        self.initialize_form()

    def initialize_form(self):
        self.form_name = acord_form_140.acord_form_140_name
        self.form_data = acord_form_140.acord_form_140_data
        self.form_tool = acord_form_140.acord_form_140_tool

    def submit_underwriter_data(self, business_info, location, building_info, naics_code, annual_revenue, loss_history, requested_coverage):
        self.business_info = business_info
        self.location = location
        self.building_info = building_info
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.loss_history = loss_history  # List of losses with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Location risk factor
        high_risk_locations = ["Coastal", "Urban"]
        low_risk_locations = ["Suburban", "Rural"]
        
        if self.location in high_risk_locations:
            risk_score += 30
        elif self.location in low_risk_locations:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other locations

        # Building information
        construction_type = self.building_info.get("construction_type", "")
        building_age = self.building_info.get("age", 0)
        square_footage = self.building_info.get("square_footage", 0)
        
        if construction_type in ["Frame", "Wood"]:
            risk_score += 30  # Higher risk for wood/frame construction
        elif construction_type in ["Masonry", "Steel"]:
            risk_score += 10  # Lower risk for masonry/steel construction

        if building_age > 50:
            risk_score += 20  # Higher risk for older buildings
        elif building_age > 20:
            risk_score += 10

        if square_footage > 50000:
            risk_score += 20  # Higher risk for larger buildings
        elif square_footage > 20000:
            risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation
        
        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Loss history
        for loss in self.loss_history:
            if loss['severity'] == "High":
                risk_score += 30
            elif loss['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 10000000:
            risk_score += 20
        elif self.requested_coverage > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }
    

