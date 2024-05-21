import streamlit as st

acord_form_137_name = "Commercial Auto Coverages/Limits Section"

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

acord_form_137_tool = {
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
