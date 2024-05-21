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
