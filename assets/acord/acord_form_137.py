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
