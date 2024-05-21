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
