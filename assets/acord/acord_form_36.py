import streamlit as st

acord_form_36_name = "Statement of No Loss"

acord_form_36_data = {
  "applicantInformation": {
    "name": "string",
    "policyNumber": "string",
    "effectiveDate": "string",
    "expirationDate": "string",
    "address": {
      "address": "string",
      "city": "string",
      "state": "string",
      "zipCode": "string"
    },
    "contact": {
      "phoneNumber": "string",
      "emailAddress": "string"
    }
  },
  "statementOfNoLoss": {
    "coverageType": "string",
    "statementPeriod": {
      "startDate": "string",
      "endDate": "string"
    },
    "noLossStatement": "string"
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

acord_form_36_tool = {
  "name": "underwrite_complex_workers_comp_insurance",
  "description": "Underwrite workers' compensation insurance for complex risks based on ACORD Form 36.",
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
      "safety_programs": {
        "type": "object",
        "description": "Information about safety programs and their effectiveness.",
        "properties": {
          "program_name": {
            "type": "string",
            "description": "Name of the safety program."
          },
          "effectiveness": {
            "type": "string",
            "description": "Effectiveness of the safety program (e.g., Excellent, Good, Average)."
          }
        },
        "required": ["program_name", "effectiveness"]
      },
      "requested_coverage": {
        "type": "number",
        "description": "Requested workers' compensation coverage limit."
      }
    },
    "required": ["business_info", "naics_code", "number_of_employees", "total_payroll", "years_in_business", "claims_history", "safety_programs", "requested_coverage"]
  }
}
