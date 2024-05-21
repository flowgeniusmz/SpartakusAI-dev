# Form 126 - Commercial General Liability Section

## Overview
Sure, let's create an underwriting algorithm for ACORD Form 126, which is typically used for general liability insurance. The information required for this form usually includes:

Business Information
Description of Operations
Hazard Information
Additional Coverages and Limits
Prior Loss Information
For simplicity, we will focus on a few key factors that affect underwriting decisions:

Business Type: Certain business types have higher inherent risks.
Location: Different locations might have different risk levels.
Annual Revenue: Higher revenue could indicate higher risk.
Number of Employees: More employees might mean more exposure.
Years in Business: More years in business might indicate stability.
Prior Claims: More claims in the past indicate higher risk.


### Explanation
Class Initialization:

The GeneralLiabilityUnderwriter class is initialized with business information, business type, location, annual revenue, number of employees, years in business, and prior claims.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
Business type: Different business types have different inherent risks.
Location: Some locations are riskier than others.
Annual revenue: Higher revenue increases risk.
Number of employees: More employees increase risk.
Years in business: More years reduce risk.
Prior claims: More claims increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the GeneralLiabilityUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured

```python
acord_form_126_data = {
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
  "businessDescription": {
    "typeOfBusiness": "string",
    "detailedDescription": "string"
  },
  "limitsOfInsurance": {
    "eachOccurrence": "number",
    "generalAggregate": "number",
    "productsCompletedOpsAggregate": "number",
    "personalAndAdvertisingInjury": "number",
    "fireDamage": "number",
    "medicalExpense": "number"
  },
  "classification": [
    {
      "classCode": "string",
      "classification": "string",
      "premiumBasis": "string",
      "rate": "number",
      "exposure": "number"
    }
  ],
  "additionalCoverage": {
    "hiredAndNonOwnedAuto": "boolean",
    "employeeBenefitsLiability": "boolean",
    "stopGapCoverage": "boolean"
  },
  "additionalInsureds": [
    {
      "name": "string",
      "relationship": "string",
      "address": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      }
    }
  ],
  "claimsInformation": {
    "anyClaims": "boolean",
    "claimsDetails": [
      {
        "dateOfClaim": "string",
        "description": "string",
        "amountPaid": "number",
        "amountReserved": "number"
      }
    ]
  },
  "premisesInformation": [
    {
      "location": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "occupancy": "string",
      "constructionType": "string",
      "yearBuilt": "number",
      "squareFootage": "number"
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

```python
class GeneralLiabilityUnderwriter:
    def __init__(self, business_info, business_type, location, annual_revenue, number_of_employees, years_in_business, prior_claims):
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

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Corp",
        "address": "456 Market St, Metropolis, USA"
    }
    business_type = "Manufacturing"
    location = "Urban"
    annual_revenue = 6000000
    number_of_employees = 120
    years_in_business = 5
    prior_claims = 3

    underwriter = GeneralLiabilityUnderwriter(business_info, business_type, location, annual_revenue, number_of_employees, years_in_business, prior_claims)
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
  "name": "underwrite_general_liability_insurance",
  "description": "Underwrite general liability insurance based on ACORD Form 126.",
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
      "location": {
        "type": "string",
        "description": "Location of the business (e.g., Urban, Suburban)."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
      },
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      }
    },
    "required": ["business_info", "business_type", "location", "annual_revenue", "number_of_employees", "years_in_business", "prior_claims"]
  }
}






```
