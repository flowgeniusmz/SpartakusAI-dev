import streamlit as st

acord_form_130_name = "Workers Compensation Application"

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

acord_form_130_tool = {
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
