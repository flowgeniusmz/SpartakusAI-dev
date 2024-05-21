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
