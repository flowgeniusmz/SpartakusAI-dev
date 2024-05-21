import streamlit as st

acord_form_133_name = "Contractors Supplement"

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

acord_form_133_tool = {
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
