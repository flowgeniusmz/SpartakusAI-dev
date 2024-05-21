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
