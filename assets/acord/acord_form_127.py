import streamlit as st

acord_form_127_name = "Business Auto Section"

acord_form_127_data = {
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
  "vehicleInformation": [
    {
      "vehicleNumber": "string",
      "year": "number",
      "make": "string",
      "model": "string",
      "VIN": "string",
      "costNew": "number",
      "vehicleType": "string",
      "garageLocation": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "radiusOfOperations": "number",
      "usage": "string"
    }
  ],
  "coverageInformation": {
    "liabilityCoverage": {
      "limit": "number"
    },
    "physicalDamageCoverage": {
      "comprehensiveDeductible": "number",
      "collisionDeductible": "number"
    },
    "uninsuredMotoristCoverage": "boolean",
    "underinsuredMotoristCoverage": "boolean",
    "medicalPaymentsCoverage": "number",
    "hiredAutoCoverage": "boolean",
    "nonOwnedAutoCoverage": "boolean"
  },
  "driverInformation": [
    {
      "name": "string",
      "dateOfBirth": "string",
      "licenseNumber": "string",
      "licenseState": "string",
      "yearsLicensed": "number",
      "accidentsViolations": [
        {
          "date": "string",
          "description": "string",
          "amountPaid": "number"
        }
      ]
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

acord_form_127_tool = {
  "name": "underwrite_business_auto_insurance",
  "description": "Underwrite business auto insurance based on ACORD Form 127.",
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
