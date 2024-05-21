# Form 130 - Workers Compensation Application

## Overview
ACORD Form 130 is typically used for workers' compensation insurance. This form collects detailed information about the business and its operations to assess the risk associated with insuring the company's employees.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Industry Classification (NAICS code)
Number of Employees
Total Payroll
Years in Business
Prior Claims (frequency and severity)

### Explanation
Class Initialization:

The WorkersCompensationUnderwriter class is initialized with business information, NAICS code, number of employees, total payroll, years in business, prior claims, and claim severity.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
NAICS code: Different industries have different inherent risks. Here, we use the first three digits of the NAICS code to categorize industries.
Number of employees: More employees increase risk.
Total payroll: Higher payroll increases risk.
Years in business: More years reduce risk.
Prior claims: More claims increase risk, with additional weight based on the severity of the claims.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the WorkersCompensationUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured

```python
acord_form_130_data = {
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
    "detailedDescription": "string",
    "yearsInBusiness": "number",
    "yearsWithCurrentManagement": "number"
  },
  "coverageRequested": {
    "partOneWorkersCompensation": "number",
    "partTwoEmployersLiability": {
      "eachAccident": "number",
      "diseasePolicyLimit": "number",
      "diseaseEachEmployee": "number"
    },
    "otherStatesInsurance": "string",
    "deductibles": {
      "amount": "number",
      "type": "string"
    }
  },
  "ratingInformation": [
    {
      "classCode": "string",
      "description": "string",
      "annualRemuneration": "number",
      "rate": "number",
      "estimatedAnnualPremium": "number"
    }
  ],
  "experienceModification": {
    "modificationRate": "number",
    "effectiveDate": "string"
  },
  "claimsHistory": [
    {
      "dateOfLoss": "string",
      "description": "string",
      "amountPaid": "number",
      "amountReserved": "number"
    }
  ],
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
class WorkersCompensationUnderwriter:
    def __init__(self, business_info, naics_code, number_of_employees, total_payroll, years_in_business, prior_claims, claim_severity):
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

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Construction",
        "address": "789 Industrial Ave, Construction City, USA"
    }
    naics_code = "238"  # Construction
    number_of_employees = 150
    total_payroll = 12000000
    years_in_business = 12
    prior_claims = 5
    claim_severity = "High"

    underwriter = WorkersCompensationUnderwriter(business_info, naics_code, number_of_employees, total_payroll, years_in_business, prior_claims, claim_severity)
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
  "name": "underwrite_workers_compensation_insurance",
  "description": "Underwrite workers' compensation insurance based on ACORD Form 130.",
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
      "total_payroll": {
        "type": "number",
        "description": "Total payroll of the business."
      },
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      },
      "claim_severity": {
        "type": "string",
        "description": "Severity of prior claims (e.g., High, Medium, Low)."
      }
    },
    "required": ["business_info", "naics_code", "number_of_employees", "total_payroll", "years_in_business", "prior_claims", "claim_severity"]
  }
}


```