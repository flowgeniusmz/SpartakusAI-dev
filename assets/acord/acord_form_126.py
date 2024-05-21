import streamlit as st

acord_form_126_name = "Commercial General Liability Section"
acord_form_126_data = {
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
  "businessDescription": {
    "typeOfBusiness": "string",
    "detailedDescription": "string"
  },
  "limitsOfInsurance": {
    "eachOccurrence": "number",
    "generalAggregate": "number",
    "productsCompletedOpsAggregate": "number",
    "personalAndAdvertisingInjury": "number",
    "fireDamage": "number",
    "medicalExpense": "number"
  },
  "classification": [
    {
      "classCode": "string",
      "classification": "string",
      "premiumBasis": "string",
      "rate": "number",
      "exposure": "number"
    }
  ],
  "additionalCoverage": {
    "hiredAndNonOwnedAuto": "boolean",
    "employeeBenefitsLiability": "boolean",
    "stopGapCoverage": "boolean"
  },
  "additionalInsureds": [
    {
      "name": "string",
      "relationship": "string",
      "address": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      }
    }
  ],
  "claimsInformation": {
    "anyClaims": "boolean",
    "claimsDetails": [
      {
        "dateOfClaim": "string",
        "description": "string",
        "amountPaid": "number",
        "amountReserved": "number"
      }
    ]
  },
  "premisesInformation": [
    {
      "location": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "occupancy": "string",
      "constructionType": "string",
      "yearBuilt": "number",
      "squareFootage": "number"
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
