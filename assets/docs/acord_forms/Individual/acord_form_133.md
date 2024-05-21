# Form 133 - Contractors Supplement

## Overview
ACORD Form 133 is typically used for umbrella or excess liability insurance. This type of insurance provides additional liability coverage above the limits of the insured's underlying policies, such as general liability, auto liability, and employer's liability.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Industry Classification (NAICS code)
Number of Employees
Annual Revenue
Claims History
Limits of Underlying Policies
Requested Umbrella Coverage Limit

### Explanation
Class Initialization:

The UmbrellaLiabilityUnderwriter class is initialized with business information, NAICS code, number of employees, annual revenue, claims history, underlying policy limits, and the requested umbrella coverage limit.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
NAICS code: Different industries have different inherent risks. Here, we use the first three digits of the NAICS code to categorize industries.
Number of employees: More employees increase risk.
Annual revenue: Higher revenue increases risk.
Claims history: The severity of prior claims impacts the risk score.
Underlying policy limits: If the limits of underlying policies are below the minimum required limits, the risk score increases.
Requested umbrella coverage limit: Higher requested limits increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the UmbrellaLiabilityUnderwriter class is created with sample data, and the underwriting decision is printed out.
This code provides a basic framework for an underwriting algorithm for umbrella or excess liability insurance and can be expanded with more sophisticated rules and additional data points as needed.

## Form Information Captured

```python
acord_form_133_data = {
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
  "businessInformation": {
    "typeOfBusiness": "string",
    "yearsInBusiness": "number",
    "yearsWithCurrentManagement": "number",
    "contractorLicenseNumber": "string",
    "licenseExpirationDate": "string"
  },
  "operations": {
    "descriptionOfOperations": "string",
    "percentageOfWorkSubcontracted": "number",
    "annualGrossReceipts": "number",
    "annualPayroll": "number",
    "numberOfEmployees": "number"
  },
  "jobInformation": [
    {
      "jobDescription": "string",
      "jobLocation": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "projectedStartDate": "string",
      "projectedEndDate": "string",
      "totalJobCost": "number"
    }
  ],
  "equipmentInformation": {
    "ownedEquipmentValue": "number",
    "leasedEquipmentValue": "number"
  },
  "claimsHistory": [
    {
      "dateOfLoss": "string",
      "description": "string",
      "amountPaid": "number",
      "amountReserved": "number"
    }
  ],
  "safetyInformation": {
    "safetyProgramInPlace": "boolean",
    "oshaViolations": "boolean",
    "oshaViolationDetails": "string"
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
class UmbrellaLiabilityUnderwriter:
    def __init__(self, business_info, naics_code, number_of_employees, annual_revenue, claims_history, underlying_limits, requested_umbrella_limit):
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

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Corp",
        "address": "456 Market St, Metropolis, USA"
    }
    naics_code = "238"  # Construction
    number_of_employees = 150
    annual_revenue = 12000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    underlying_limits = {
        "general_liability": 1000000,
        "auto_liability": 1000000,
        "employers_liability": 500000
    }
    requested_umbrella_limit = 7000000

    underwriter = UmbrellaLiabilityUnderwriter(business_info, naics_code, number_of_employees, annual_revenue, claims_history, underlying_limits, requested_umbrella_limit)
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
  "name": "underwrite_umbrella_liability_insurance",
  "description": "Underwrite umbrella/excess liability insurance based on ACORD Form 133.",
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
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
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
      "underlying_limits": {
        "type": "object",
        "description": "Limits of underlying policies.",
        "properties": {
          "general_liability": {
            "type": "number",
            "description": "Limit for general liability."
          },
          "auto_liability": {
            "type": "number",
            "description": "Limit for auto liability."
          },
          "employers_liability": {
            "type": "number",
            "description": "Limit for employers liability."
          }
        },
        "required": ["general_liability", "auto_liability", "employers_liability"]
      },
      "requested_umbrella_limit": {
        "type": "number",
        "description": "Requested umbrella coverage limit."
      }
    },
    "required": ["business_info", "naics_code", "number_of_employees", "annual_revenue", "claims_history", "underlying_limits", "requested_umbrella_limit"]
  }
}


```