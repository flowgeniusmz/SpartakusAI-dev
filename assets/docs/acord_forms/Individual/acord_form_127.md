# Form 127 - Business Auto Section

## Overview
ACORD Form 127 is typically used for Business Auto Insurance, which includes coverage for commercial vehicles used in business operations. For this underwriting algorithm, we'll consider factors such as:

- Business Information
    - Vehicle Information (e.g., type, age, value)
    - Driver Information (e.g., age, driving experience, driving record)
    - Business Type (NAICS code)
    - Annual Revenue
    - Claims History
    - Requested Coverage Limits

- Algorithm
    - The underwriting algorithm will assess the risk based on the following rules:
        - Higher risk for trucks and heavy equipment compared to cars and vans.
        - Higher risk for older and higher-value vehicles.
        - Higher risk for younger or senior drivers and those with poor driving records.
        - Higher risk for certain high-risk industries.
        - Higher risk for higher annual revenue.
        - Higher risk for frequent and severe prior claims.
        - Higher requested coverage limits increase risk.

## Form Information Captured

```python

acord_form_127_data = {
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
  "vehicleInformation": [
    {
      "vehicleNumber": "string",
      "year": "number",
      "make": "string",
      "model": "string",
      "VIN": "string",
      "costNew": "number",
      "vehicleType": "string",
      "garageLocation": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "radiusOfOperations": "number",
      "usage": "string"
    }
  ],
  "coverageInformation": {
    "liabilityCoverage": {
      "limit": "number"
    },
    "physicalDamageCoverage": {
      "comprehensiveDeductible": "number",
      "collisionDeductible": "number"
    },
    "uninsuredMotoristCoverage": "boolean",
    "underinsuredMotoristCoverage": "boolean",
    "medicalPaymentsCoverage": "number",
    "hiredAutoCoverage": "boolean",
    "nonOwnedAutoCoverage": "boolean"
  },
  "driverInformation": [
    {
      "name": "string",
      "dateOfBirth": "string",
      "licenseNumber": "string",
      "licenseState": "string",
      "yearsLicensed": "number",
      "accidentsViolations": [
        {
          "date": "string",
          "description": "string",
          "amountPaid": "number"
        }
      ]
    }
  ],
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
Here's the Python code for the underwriting algorithm for ACORD Form 127:

```python

class BusinessAutoUnderwriter:
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

    underwriter = BusinessAutoUnderwriter(business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")

```

## OpenAI Function / Tool Schema
Here's the OpenAI function / tool JSON schema for ACORD Form 127:

```json

{
  "name": "underwrite_business_auto_insurance",
  "description": "Underwrite business auto insurance based on ACORD Form 127.",
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