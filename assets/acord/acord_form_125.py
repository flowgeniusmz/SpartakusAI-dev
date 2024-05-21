import streamlit as st

acord_form_125_name = "Commercial Insurance Application"
acord_form_125_data = {
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
      "emailAddress": "string",
      "websiteAddress": "string"
    },
    "identification": {
      "FEIN": "string",
      "SSN": "string",
      "DUNSNumber": "string"
    }
  },
  "businessInformation": {
    "typeOfBusiness": "string",
    "descriptionOfOperations": "string",
    "yearsInBusiness": "number",
    "yearsWithCurrentManagement": "number"
  },
  "insuranceHistory": {
    "currentInsurance": {
      "carrier": "string",
      "policyNumber": "string",
      "expirationDate": "string"
    },
    "lossHistory": [
      {
        "dateOfLoss": "string",
        "typeOfLoss": "string",
        "amountPaid": "number",
        "description": "string"
      }
    ]
  },
  "coverageRequested": {
    "effectiveDate": "string",
    "expirationDate": "string",
    "coverages": [
      "General Liability",
      "Property",
      "Auto"
    ]
  },
  "propertyInformation": [
    {
      "locationAddress": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "occupancy": "string",
      "constructionType": "string",
      "yearBuilt": "number",
      "squareFootage": "number",
      "protectionClass": "string"
    }
  ],
  "generalLiabilityInformation": {
    "limitsOfLiability": "number",
    "medicalPayments": "number",
    "personalAndAdvertisingInjury": "number",
    "productsAndCompletedOperations": "number"
  },
  "automobileInformation": {
    "vehicleSchedule": [
      {
        "make": "string",
        "model": "string",
        "year": "number",
        "VIN": "string",
        "use": "string"
      }
    ],
    "driverInformation": [
      {
        "name": "string",
        "dateOfBirth": "string",
        "licenseNumber": "string",
        "yearsOfDrivingExperience": "number"
      }
    ]
  },
  "additionalInterests": {
    "certificateHolders": [
      {
        "name": "string",
        "address": "string"
      }
    ],
    "additionalInsureds": [
      {
        "name": "string",
        "address": "string"
      }
    ]
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

acord_form_125_tool = {
  "name": "underwrite_commercial_insurance",
  "description": "Underwrite commercial insurance based on ACORD Form 125.",
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
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      }
    },
    "required": ["business_info", "business_type", "years_in_business", "number_of_employees", "annual_revenue", "prior_claims"]
  }
}

