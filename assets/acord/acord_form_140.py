import streamlit as st

acord_form_140_name = "Property Section"

acord_form_140_data = {
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
  "propertyInformation": [
    {
      "locationAddress": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "constructionType": "string",
      "occupancy": "string",
      "yearBuilt": "number",
      "squareFootage": "number",
      "protectionClass": "string"
    }
  ],
  "coverageRequested": {
    "buildingCoverage": "number",
    "contentsCoverage": "number",
    "businessIncomeCoverage": "number",
    "extraExpenseCoverage": "number",
    "equipmentBreakdownCoverage": "boolean"
  },
  "additionalCoverage": {
    "earthquakeCoverage": "boolean",
    "floodCoverage": "boolean",
    "ordinanceOrLawCoverage": "boolean",
    "signCoverage": "boolean",
    "crimeCoverage": "boolean"
  },
  "claimsHistory": [
    {
      "dateOfLoss": "string",
      "description": "string",
      "amountPaid": "number",
      "amountReserved": "number"
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


acord_form_140_tool = {
  "name": "underwrite_property_insurance",
  "description": "Underwrite property insurance based on ACORD Form 140.",
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
      "location": {
        "type": "string",
        "description": "Location of the property (e.g., Urban, Suburban)."
      },
      "building_info": {
        "type": "object",
        "description": "Information about the building.",
        "properties": {
          "construction_type": {
            "type": "string",
            "description": "Type of construction (e.g., Masonry, Frame)."
          },
          "age": {
            "type": "integer",
            "description": "Age of the building in years."
          },
          "square_footage": {
            "type": "integer",
            "description": "Total square footage of the building."
          }
        },
        "required": ["construction_type", "age", "square_footage"]
      },
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "loss_history": {
        "type": "array",
        "description": "List of prior losses with details.",
        "items": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "Year of the loss."
            },
            "severity": {
              "type": "string",
              "description": "Severity of the loss (e.g., High, Medium, Low)."
            }
          },
          "required": ["year", "severity"]
        }
      },
      "requested_coverage": {
        "type": "number",
        "description": "Requested property coverage limit."
      }
    },
    "required": ["business_info", "location", "building_info", "naics_code", "annual_revenue", "loss_history", "requested_coverage"]
  }
}
