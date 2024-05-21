import streamlit as st

acord_form_126_name = "Commercial General Liability Section"
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

acord_form_126_tool = {
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




