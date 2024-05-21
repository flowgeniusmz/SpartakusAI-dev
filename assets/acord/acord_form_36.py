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
