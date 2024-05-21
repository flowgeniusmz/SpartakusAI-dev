# Form 137 - Commercial Auto Coverages/Limits Section

## Overview
ACORD Form 137 is typically used for commercial auto insurance. This form collects information about the vehicles, drivers, and business operations to assess the risk associated with insuring the company's vehicles.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Vehicle Information (e.g., type, age, value)
Driver Information (e.g., age, driving experience, driving record)
Business Type (NAICS code)
Annual Revenue
Claims History
Requested Coverage Limits

### Explanation
Class Initialization:

The CommercialAutoUnderwriter class is initialized with business information, vehicles (a list of vehicle details), drivers (a list of driver details), NAICS code, annual revenue, claims history, and requested coverage limits.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
Vehicle information: Different types, ages, and values of vehicles impact risk.
Driver information: The ages, driving experience, and driving records of drivers impact risk.
NAICS code: Different industries have different inherent risks.
Annual revenue: Higher revenue increases risk.
Claims history: The severity of prior claims impacts the risk score.
Requested coverage: Higher requested coverage limits increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the CommercialAutoUnderwriter class is created with sample data, and the underwriting decision is printed out.
This code provides a basic framework for an underwriting algorithm for commercial auto insurance and can be expanded with more sophisticated rules and additional data points as needed.

## Form Information Captured

```python
acord_form_137_data = {
  "applicantInformation": {
    "name": "string",
    "mailingAddress": {
      "address": "string",
      "city": "string",
      "state": "string",
      "zipCode": "string"
    },
    "contact": {
      "phoneNumber": "string",
      "emailAddress": "string"
    },
    "FEIN": "string"
  },
  "generalInformation": {
    "effectiveDate": "string",
    "expirationDate": "string",
    "policyNumber": "string"
  },
  "coverageInformation": {
    "liabilityCoverage": {
      "limit": "number",
      "deductible": "number"
    },
    "personalInjuryProtection": {
      "limit": "number",
      "deductible": "number"
    },
    "uninsuredMotoristCoverage": {
      "limit": "number"
    },
    "underinsuredMotoristCoverage": {
      "limit": "number"
    },
    "medicalPaymentsCoverage": {
      "limit": "number"
    },
    "physicalDamageCoverage": {
      "comprehensive": {
        "deductible": "number",
        "limit": "number"
      },
      "collision": {
        "deductible": "number",
        "limit": "number"
      },
      "specifiedPerils": {
        "deductible": "number",
        "limit": "number"
      }
    },
    "hiredAutoCoverage": {
      "liabilityLimit": "number",
      "physicalDamageLimit": "number"
    },
    "nonOwnedAutoCoverage": {
      "liabilityLimit": "number",
      "physicalDamageLimit": "number"
    }
  },
  "remarks": {
    "additionalInformation": "string"
  },
  "signature": {
    "applicantSignature": "string",
    "date": "string",
    "agentBrokerInformation": {
      "name": "string",
      "contactDetails": "string",
      "signature": "string"
    }
  }
}



```

## Underwriter Function

```python
class CommercialAutoUnderwriter:
    def __init__(self, business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage):
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

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Transport",
        "address": "789 Industrial Ave, Transport City, USA"
    }
    vehicles = [
        {"type": "Truck", "age": 8, "value": 60000},
        {"type": "Van", "age": 3, "value": 30000}
    ]
    drivers = [
        {"age": 45, "experience": 20, "record": "Clean"},
        {"age": 30, "experience": 7, "record": "Fair"}
    ]
    naics_code = "484"  # Transportation
    annual_revenue = 15000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    requested_coverage = 2000000

    underwriter = CommercialAutoUnderwriter(business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_commercial_auto_insurance",
  "description": "Underwrite commercial auto insurance based on ACORD Form 137.",
  "parameters": {
    "type": "object",
    "properties": {
      "business_info": {
        "type": "object",
        "description": "Information about the business.",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the business."
          },
          "address": {
            "type": "string",
            "description": "Address of the business."
          }
        },
        "required": ["name", "address"]
      },
      "vehicles": {
        "type": "array",
        "description": "List of vehicles with details.",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "description": "Type of vehicle (e.g., Truck, Car)."
            },
            "age": {
              "type": "integer",
              "description": "Age of the vehicle in years."
            },
            "value": {
              "type": "number",
              "description": "Value of the vehicle."
            }
          },
          "required": ["type", "age", "value"]
        }
      },
      "drivers": {
        "type": "array",
        "description": "List of drivers with details.",
        "items": {
          "type": "object",
          "properties": {
            "age": {
              "type": "integer",
              "description": "Age of the driver."
            },
            "experience": {
              "type": "integer",
              "description": "Years of driving experience."
            },
            "record": {
              "type": "string",
              "description": "Driving record (e.g., Clean, Fair, Poor)."
            }
          },
          "required": ["age", "experience", "record"]
        }
      },
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "claims_history": {
        "type": "array",
        "description": "List of prior claims with details.",
        "items": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "Year of the claim."
            },
            "severity": {
              "type": "string",
              "description": "Severity of the claim (e.g., High, Medium, Low)."
            }
          },
          "required": ["year", "severity"]
        }
      },
      "requested_coverage": {
        "type": "number",
        "description": "Requested auto coverage limit."
      }
    },
    "required": ["business_info", "vehicles", "drivers", "naics_code", "annual_revenue", "claims_history", "requested_coverage"]
  }
}


```