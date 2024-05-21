# Form 125 - Commercial Insurance Application"

## Overview
Sure, I'll provide a simplified underwriting algorithm for commercial insurance using ACORD Form 125, along with the complete Python code and explanations. ACORD Form 125 is a standard form used to collect basic information about the insured and their operations. This example will cover some basic underwriting checks.

Let's assume we're focusing on basic details like:

Business Information (e.g., name, address)
Business Type
Years in Business
Number of Employees
Annual Revenue
Prior Claims
The underwriting algorithm will assess the risk based on the following rules:

Businesses with more than 10 years in operation are considered lower risk.
Businesses with more than 50 employees are considered higher risk.
Annual revenue impacts the risk rating, with higher revenue potentially indicating higher risk.
Prior claims in the last 5 years increase the risk score.


### Explanation
Class Initialization:

The CommercialInsuranceUnderwriter class is initialized with business information such as business type, years in business, number of employees, annual revenue, and prior claims.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria.
More years in business reduce risk.
More employees increase risk.
Higher annual revenue increases risk.
Prior claims increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 20 results in acceptance with a premium discount.
A risk score between 20 and 40 results in acceptance with standard conditions.
A risk score above 40 results in decline.
Example Usage:

An example instance of the CommercialInsuranceUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured
```python
acord_form_125_data = {
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
      "emailAddress": "string",
      "websiteAddress": "string"
    },
    "identification": {
      "FEIN": "string",
      "SSN": "string",
      "DUNSNumber": "string"
    }
  },
  "businessInformation": {
    "typeOfBusiness": "string",
    "descriptionOfOperations": "string",
    "yearsInBusiness": "number",
    "yearsWithCurrentManagement": "number"
  },
  "insuranceHistory": {
    "currentInsurance": {
      "carrier": "string",
      "policyNumber": "string",
      "expirationDate": "string"
    },
    "lossHistory": [
      {
        "dateOfLoss": "string",
        "typeOfLoss": "string",
        "amountPaid": "number",
        "description": "string"
      }
    ]
  },
  "coverageRequested": {
    "effectiveDate": "string",
    "expirationDate": "string",
    "coverages": [
      "General Liability",
      "Property",
      "Auto"
    ]
  },
  "propertyInformation": [
    {
      "locationAddress": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "occupancy": "string",
      "constructionType": "string",
      "yearBuilt": "number",
      "squareFootage": "number",
      "protectionClass": "string"
    }
  ],
  "generalLiabilityInformation": {
    "limitsOfLiability": "number",
    "medicalPayments": "number",
    "personalAndAdvertisingInjury": "number",
    "productsAndCompletedOperations": "number"
  },
  "automobileInformation": {
    "vehicleSchedule": [
      {
        "make": "string",
        "model": "string",
        "year": "number",
        "VIN": "string",
        "use": "string"
      }
    ],
    "driverInformation": [
      {
        "name": "string",
        "dateOfBirth": "string",
        "licenseNumber": "string",
        "yearsOfDrivingExperience": "number"
      }
    ]
  },
  "additionalInterests": {
    "certificateHolders": [
      {
        "name": "string",
        "address": "string"
      }
    ],
    "additionalInsureds": [
      {
        "name": "string",
        "address": "string"
      }
    ]
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
Here's the Python code for the underwriting algorithm for ACORD Form 125:

```python
class CommercialInsuranceUnderwriter:
    def __init__(self, business_info, business_type, years_in_business, number_of_employees, annual_revenue, prior_claims):
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

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "ABC Corp",
        "address": "123 Main St, Anytown, USA"
    }
    business_type = "Manufacturing"
    years_in_business = 15
    number_of_employees = 60
    annual_revenue = 2000000
    prior_claims = 2

    underwriter = CommercialInsuranceUnderwriter(business_info, business_type, years_in_business, number_of_employees, annual_revenue, prior_claims)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema
Here's the OpenAI function / tool JSON schema for ACORD Form 125:

```json
{
  "name": "underwrite_commercial_insurance",
  "description": "Underwrite commercial insurance based on ACORD Form 125.",
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
      "business_type": {
        "type": "string",
        "description": "Type of the business (e.g., Manufacturing, Retail)."
      },
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      }
    },
    "required": ["business_info", "business_type", "years_in_business", "number_of_employees", "annual_revenue", "prior_claims"]
  }
}

```

