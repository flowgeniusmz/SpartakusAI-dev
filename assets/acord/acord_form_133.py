import streamlit as st

acord_form_133_name = "Contractors Supplement"

acord_form_133_data = {
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
    "yearsInBusiness": "number",
    "yearsWithCurrentManagement": "number",
    "contractorLicenseNumber": "string",
    "licenseExpirationDate": "string"
  },
  "operations": {
    "descriptionOfOperations": "string",
    "percentageOfWorkSubcontracted": "number",
    "annualGrossReceipts": "number",
    "annualPayroll": "number",
    "numberOfEmployees": "number"
  },
  "jobInformation": [
    {
      "jobDescription": "string",
      "jobLocation": {
        "address": "string",
        "city": "string",
        "state": "string",
        "zipCode": "string"
      },
      "projectedStartDate": "string",
      "projectedEndDate": "string",
      "totalJobCost": "number"
    }
  ],
  "equipmentInformation": {
    "ownedEquipmentValue": "number",
    "leasedEquipmentValue": "number"
  },
  "claimsHistory": [
    {
      "dateOfLoss": "string",
      "description": "string",
      "amountPaid": "number",
      "amountReserved": "number"
    }
  ],
  "safetyInformation": {
    "safetyProgramInPlace": "boolean",
    "oshaViolations": "boolean",
    "oshaViolationDetails": "string"
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
