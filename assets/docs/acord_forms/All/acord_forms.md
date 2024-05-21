# Form 36 - Business Auto Section

## Overview
ACORD Form 127 is typically used for Business Auto Insurance, which includes coverage for commercial vehicles used in business operations. For this underwriting algorithm, we'll consider factors such as:

- Business Information
    - Vehicle Information (e.g., type, age, value)
    - Driver Information (e.g., age, driving experience, driving record)
    - Business Type (NAICS code)
    - Annual Revenue
    - Claims History
    - Requested Coverage Limits

- Algorithm
    - The underwriting algorithm will assess the risk based on the following rules:
        - Higher risk for trucks and heavy equipment compared to cars and vans.
        - Higher risk for older and higher-value vehicles.
        - Higher risk for younger or senior drivers and those with poor driving records.
        - Higher risk for certain high-risk industries.
        - Higher risk for higher annual revenue.
        - Higher risk for frequent and severe prior claims.
        - Higher requested coverage limits increase risk.

## Form Information Captured

```python

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
```
## Underwriter Function
Here's the Python code for the underwriting algorithm for ACORD Form 127:

```python

class BusinessAutoUnderwriter:
    def __init__(self, business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage):
        self.business_info = business_info
        self.vehicles = vehicles  # List of vehicle details
        self.drivers = drivers  # List of driver details
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Vehicle information
        for vehicle in self.vehicles:
            vehicle_type = vehicle.get("type", "")
            vehicle_age = vehicle.get("age", 0)
            vehicle_value = vehicle.get("value", 0)

            if vehicle_type in ["Truck", "Heavy Equipment"]:
                risk_score += 30  # Higher risk for trucks and heavy equipment
            elif vehicle_type in ["Car", "Van"]:
                risk_score += 10  # Lower risk for cars and vans

            if vehicle_age > 10:
                risk_score += 20  # Higher risk for older vehicles
            elif vehicle_age > 5:
                risk_score += 10

            if vehicle_value > 50000:
                risk_score += 20  # Higher risk for high-value vehicles
            elif vehicle_value > 20000:
                risk_score += 10

        # Driver information
        for driver in self.drivers:
            driver_age = driver.get("age", 0)
            driving_experience = driver.get("experience", 0)
            driving_record = driver.get("record", "Clean")

            if driver_age < 25 or driver_age > 65:
                risk_score += 20  # Higher risk for young or senior drivers
            elif driver_age < 30 or driver_age > 55:
                risk_score += 10

            if driving_experience < 5:
                risk_score += 20  # Higher risk for less experienced drivers
            elif driving_experience < 10:
                risk_score += 10

            if driving_record == "Poor":
                risk_score += 30  # Higher risk for poor driving records
            elif driving_record == "Fair":
                risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "484"]  # Construction, Manufacturing, Transportation
        low_risk_industries = ["541", "611", "722"]  # Professional Services, Education, Food Services

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 1000000:
            risk_score += 20
        elif self.requested_coverage > 500000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Transport",
        "address": "789 Industrial Ave, Transport City, USA"
    }
    vehicles = [
        {"type": "Truck", "age": 8, "value": 60000},
        {"type": "Van", "age": 3, "value": 30000}
    ]
    drivers = [
        {"age": 45, "experience": 20, "record": "Clean"},
        {"age": 30, "experience": 7, "record": "Fair"}
    ]
    naics_code = "484"  # Transportation
    annual_revenue = 15000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    requested_coverage = 2000000

    underwriter = BusinessAutoUnderwriter(business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")

```

## OpenAI Function / Tool Schema
Here's the OpenAI function / tool JSON schema for ACORD Form 127:

```json

{
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
```

# Form 125 - Commercial Insurance Application"

## Overview
Sure, I'll provide a simplified underwriting algorithm for commercial insurance using ACORD Form 125, along with the complete Python code and explanations. ACORD Form 125 is a standard form used to collect basic information about the insured and their operations. This example will cover some basic underwriting checks.

Let's assume we're focusing on basic details like:

Business Information (e.g., name, address)
Business Type
Years in Business
Number of Employees
Annual Revenue
Prior Claims
The underwriting algorithm will assess the risk based on the following rules:

Businesses with more than 10 years in operation are considered lower risk.
Businesses with more than 50 employees are considered higher risk.
Annual revenue impacts the risk rating, with higher revenue potentially indicating higher risk.
Prior claims in the last 5 years increase the risk score.


### Explanation
Class Initialization:

The CommercialInsuranceUnderwriter class is initialized with business information such as business type, years in business, number of employees, annual revenue, and prior claims.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria.
More years in business reduce risk.
More employees increase risk.
Higher annual revenue increases risk.
Prior claims increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 20 results in acceptance with a premium discount.
A risk score between 20 and 40 results in acceptance with standard conditions.
A risk score above 40 results in decline.
Example Usage:

An example instance of the CommercialInsuranceUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured
```python
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



```

## Underwriter Function
Here's the Python code for the underwriting algorithm for ACORD Form 125:

```python
class CommercialInsuranceUnderwriter:
    def __init__(self, business_info, business_type, years_in_business, number_of_employees, annual_revenue, prior_claims):
        self.business_info = business_info
        self.business_type = business_type
        self.years_in_business = years_in_business
        self.number_of_employees = number_of_employees
        self.annual_revenue = annual_revenue
        self.prior_claims = prior_claims

    def calculate_risk_score(self):
        risk_score = 0

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10  # Lower risk for established businesses
        else:
            risk_score += 20  # Higher risk for newer businesses

        # Number of employees
        if self.number_of_employees > 50:
            risk_score += 15  # Higher risk for larger businesses
        else:
            risk_score -= 5  # Lower risk for smaller businesses

        # Annual revenue
        if self.annual_revenue > 1000000:
            risk_score += 10  # Higher risk for high-revenue businesses
        else:
            risk_score -= 5  # Lower risk for lower-revenue businesses

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 5  # Add 5 points for each prior claim

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 20:
            decision = "Accept"
            premium_modifier = 0.9  # 10% discount
        elif 20 <= risk_score < 40:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "ABC Corp",
        "address": "123 Main St, Anytown, USA"
    }
    business_type = "Manufacturing"
    years_in_business = 15
    number_of_employees = 60
    annual_revenue = 2000000
    prior_claims = 2

    underwriter = CommercialInsuranceUnderwriter(business_info, business_type, years_in_business, number_of_employees, annual_revenue, prior_claims)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema
Here's the OpenAI function / tool JSON schema for ACORD Form 125:

```json
{
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

```


# Form 126 - Commercial General Liability Section

## Overview
Sure, let's create an underwriting algorithm for ACORD Form 126, which is typically used for general liability insurance. The information required for this form usually includes:

Business Information
Description of Operations
Hazard Information
Additional Coverages and Limits
Prior Loss Information
For simplicity, we will focus on a few key factors that affect underwriting decisions:

Business Type: Certain business types have higher inherent risks.
Location: Different locations might have different risk levels.
Annual Revenue: Higher revenue could indicate higher risk.
Number of Employees: More employees might mean more exposure.
Years in Business: More years in business might indicate stability.
Prior Claims: More claims in the past indicate higher risk.


### Explanation
Class Initialization:

The GeneralLiabilityUnderwriter class is initialized with business information, business type, location, annual revenue, number of employees, years in business, and prior claims.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
Business type: Different business types have different inherent risks.
Location: Some locations are riskier than others.
Annual revenue: Higher revenue increases risk.
Number of employees: More employees increase risk.
Years in business: More years reduce risk.
Prior claims: More claims increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the GeneralLiabilityUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured

```python
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



```

## Underwriter Function

```python
class GeneralLiabilityUnderwriter:
    def __init__(self, business_info, business_type, location, annual_revenue, number_of_employees, years_in_business, prior_claims):
        self.business_info = business_info
        self.business_type = business_type
        self.location = location
        self.annual_revenue = annual_revenue
        self.number_of_employees = number_of_employees
        self.years_in_business = years_in_business
        self.prior_claims = prior_claims

    def calculate_risk_score(self):
        risk_score = 0

        # Business type risk factor
        high_risk_businesses = ["Construction", "Manufacturing", "Nightclub"]
        low_risk_businesses = ["Office", "Retail", "Restaurant"]
        
        if self.business_type in high_risk_businesses:
            risk_score += 30
        elif self.business_type in low_risk_businesses:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other business types

        # Location risk factor
        high_risk_locations = ["Urban", "Coastal"]
        low_risk_locations = ["Suburban", "Rural"]
        
        if self.location in high_risk_locations:
            risk_score += 20
        elif self.location in low_risk_locations:
            risk_score += 10
        else:
            risk_score += 15  # Default risk score for other locations

        # Annual revenue
        if self.annual_revenue > 5000000:
            risk_score += 20
        elif self.annual_revenue > 1000000:
            risk_score += 10
        else:
            risk_score += 5

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 10

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Corp",
        "address": "456 Market St, Metropolis, USA"
    }
    business_type = "Manufacturing"
    location = "Urban"
    annual_revenue = 6000000
    number_of_employees = 120
    years_in_business = 5
    prior_claims = 3

    underwriter = GeneralLiabilityUnderwriter(business_info, business_type, location, annual_revenue, number_of_employees, years_in_business, prior_claims)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_general_liability_insurance",
  "description": "Underwrite general liability insurance based on ACORD Form 126.",
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
      "location": {
        "type": "string",
        "description": "Location of the business (e.g., Urban, Suburban)."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
      },
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      }
    },
    "required": ["business_info", "business_type", "location", "annual_revenue", "number_of_employees", "years_in_business", "prior_claims"]
  }
}






```





# Form 127 - Business Auto Section

## Overview
ACORD Form 127 is typically used for Business Auto Insurance, which includes coverage for commercial vehicles used in business operations. For this underwriting algorithm, we'll consider factors such as:

- Business Information
    - Vehicle Information (e.g., type, age, value)
    - Driver Information (e.g., age, driving experience, driving record)
    - Business Type (NAICS code)
    - Annual Revenue
    - Claims History
    - Requested Coverage Limits

- Algorithm
    - The underwriting algorithm will assess the risk based on the following rules:
        - Higher risk for trucks and heavy equipment compared to cars and vans.
        - Higher risk for older and higher-value vehicles.
        - Higher risk for younger or senior drivers and those with poor driving records.
        - Higher risk for certain high-risk industries.
        - Higher risk for higher annual revenue.
        - Higher risk for frequent and severe prior claims.
        - Higher requested coverage limits increase risk.

## Form Information Captured

```python

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
```
## Underwriter Function
Here's the Python code for the underwriting algorithm for ACORD Form 127:

```python

class BusinessAutoUnderwriter:
    def __init__(self, business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage):
        self.business_info = business_info
        self.vehicles = vehicles  # List of vehicle details
        self.drivers = drivers  # List of driver details
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Vehicle information
        for vehicle in self.vehicles:
            vehicle_type = vehicle.get("type", "")
            vehicle_age = vehicle.get("age", 0)
            vehicle_value = vehicle.get("value", 0)

            if vehicle_type in ["Truck", "Heavy Equipment"]:
                risk_score += 30  # Higher risk for trucks and heavy equipment
            elif vehicle_type in ["Car", "Van"]:
                risk_score += 10  # Lower risk for cars and vans

            if vehicle_age > 10:
                risk_score += 20  # Higher risk for older vehicles
            elif vehicle_age > 5:
                risk_score += 10

            if vehicle_value > 50000:
                risk_score += 20  # Higher risk for high-value vehicles
            elif vehicle_value > 20000:
                risk_score += 10

        # Driver information
        for driver in self.drivers:
            driver_age = driver.get("age", 0)
            driving_experience = driver.get("experience", 0)
            driving_record = driver.get("record", "Clean")

            if driver_age < 25 or driver_age > 65:
                risk_score += 20  # Higher risk for young or senior drivers
            elif driver_age < 30 or driver_age > 55:
                risk_score += 10

            if driving_experience < 5:
                risk_score += 20  # Higher risk for less experienced drivers
            elif driving_experience < 10:
                risk_score += 10

            if driving_record == "Poor":
                risk_score += 30  # Higher risk for poor driving records
            elif driving_record == "Fair":
                risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "484"]  # Construction, Manufacturing, Transportation
        low_risk_industries = ["541", "611", "722"]  # Professional Services, Education, Food Services

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 1000000:
            risk_score += 20
        elif self.requested_coverage > 500000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Transport",
        "address": "789 Industrial Ave, Transport City, USA"
    }
    vehicles = [
        {"type": "Truck", "age": 8, "value": 60000},
        {"type": "Van", "age": 3, "value": 30000}
    ]
    drivers = [
        {"age": 45, "experience": 20, "record": "Clean"},
        {"age": 30, "experience": 7, "record": "Fair"}
    ]
    naics_code = "484"  # Transportation
    annual_revenue = 15000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    requested_coverage = 2000000

    underwriter = BusinessAutoUnderwriter(business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")

```

## OpenAI Function / Tool Schema
Here's the OpenAI function / tool JSON schema for ACORD Form 127:

```json

{
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
```

# Form 130 - Workers Compensation Application

## Overview
ACORD Form 130 is typically used for workers' compensation insurance. This form collects detailed information about the business and its operations to assess the risk associated with insuring the company's employees.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Industry Classification (NAICS code)
Number of Employees
Total Payroll
Years in Business
Prior Claims (frequency and severity)

### Explanation
Class Initialization:

The WorkersCompensationUnderwriter class is initialized with business information, NAICS code, number of employees, total payroll, years in business, prior claims, and claim severity.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
NAICS code: Different industries have different inherent risks. Here, we use the first three digits of the NAICS code to categorize industries.
Number of employees: More employees increase risk.
Total payroll: Higher payroll increases risk.
Years in business: More years reduce risk.
Prior claims: More claims increase risk, with additional weight based on the severity of the claims.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the WorkersCompensationUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured

```python
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



```

## Underwriter Function

```python
class WorkersCompensationUnderwriter:
    def __init__(self, business_info, naics_code, number_of_employees, total_payroll, years_in_business, prior_claims, claim_severity):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.total_payroll = total_payroll
        self.years_in_business = years_in_business
        self.prior_claims = prior_claims
        self.claim_severity = claim_severity

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Total payroll
        if self.total_payroll > 10000000:
            risk_score += 20
        elif self.total_payroll > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Years in business
        if self.years_in_business > 10:
            risk_score -= 10
        else:
            risk_score += 10

        # Prior claims
        if self.prior_claims > 0:
            risk_score += self.prior_claims * 10
            # Severity of claims
            if self.claim_severity == "High":
                risk_score += 20
            elif self.claim_severity == "Medium":
                risk_score += 10
            else:
                risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Construction",
        "address": "789 Industrial Ave, Construction City, USA"
    }
    naics_code = "238"  # Construction
    number_of_employees = 150
    total_payroll = 12000000
    years_in_business = 12
    prior_claims = 5
    claim_severity = "High"

    underwriter = WorkersCompensationUnderwriter(business_info, naics_code, number_of_employees, total_payroll, years_in_business, prior_claims, claim_severity)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_workers_compensation_insurance",
  "description": "Underwrite workers' compensation insurance based on ACORD Form 130.",
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
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
      },
      "total_payroll": {
        "type": "number",
        "description": "Total payroll of the business."
      },
      "years_in_business": {
        "type": "integer",
        "description": "Number of years the business has been in operation."
      },
      "prior_claims": {
        "type": "integer",
        "description": "Number of prior claims in the last 5 years."
      },
      "claim_severity": {
        "type": "string",
        "description": "Severity of prior claims (e.g., High, Medium, Low)."
      }
    },
    "required": ["business_info", "naics_code", "number_of_employees", "total_payroll", "years_in_business", "prior_claims", "claim_severity"]
  }
}


```


# Form 133 - Contractors Supplement

## Overview
ACORD Form 133 is typically used for umbrella or excess liability insurance. This type of insurance provides additional liability coverage above the limits of the insured's underlying policies, such as general liability, auto liability, and employer's liability.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Industry Classification (NAICS code)
Number of Employees
Annual Revenue
Claims History
Limits of Underlying Policies
Requested Umbrella Coverage Limit

### Explanation
Class Initialization:

The UmbrellaLiabilityUnderwriter class is initialized with business information, NAICS code, number of employees, annual revenue, claims history, underlying policy limits, and the requested umbrella coverage limit.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
NAICS code: Different industries have different inherent risks. Here, we use the first three digits of the NAICS code to categorize industries.
Number of employees: More employees increase risk.
Annual revenue: Higher revenue increases risk.
Claims history: The severity of prior claims impacts the risk score.
Underlying policy limits: If the limits of underlying policies are below the minimum required limits, the risk score increases.
Requested umbrella coverage limit: Higher requested limits increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the UmbrellaLiabilityUnderwriter class is created with sample data, and the underwriting decision is printed out.
This code provides a basic framework for an underwriting algorithm for umbrella or excess liability insurance and can be expanded with more sophisticated rules and additional data points as needed.

## Form Information Captured

```python
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



```

## Underwriter Function

```python
class UmbrellaLiabilityUnderwriter:
    def __init__(self, business_info, naics_code, number_of_employees, annual_revenue, claims_history, underlying_limits, requested_umbrella_limit):
        self.business_info = business_info
        self.naics_code = naics_code
        self.number_of_employees = number_of_employees
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.underlying_limits = underlying_limits  # Dictionary of underlying policy limits
        self.requested_umbrella_limit = requested_umbrella_limit

    def calculate_risk_score(self):
        risk_score = 0

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Number of employees
        if self.number_of_employees > 100:
            risk_score += 20
        elif self.number_of_employees > 50:
            risk_score += 10
        else:
            risk_score += 5

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Underlying policy limits
        minimum_required_limits = {
            "general_liability": 1000000,
            "auto_liability": 1000000,
            "employers_liability": 500000
        }
        
        for policy, limit in self.underlying_limits.items():
            required_limit = minimum_required_limits.get(policy, 0)
            if limit < required_limit:
                risk_score += 20

        # Requested umbrella coverage limit
        if self.requested_umbrella_limit > 5000000:
            risk_score += 20
        elif self.requested_umbrella_limit > 1000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Corp",
        "address": "456 Market St, Metropolis, USA"
    }
    naics_code = "238"  # Construction
    number_of_employees = 150
    annual_revenue = 12000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    underlying_limits = {
        "general_liability": 1000000,
        "auto_liability": 1000000,
        "employers_liability": 500000
    }
    requested_umbrella_limit = 7000000

    underwriter = UmbrellaLiabilityUnderwriter(business_info, naics_code, number_of_employees, annual_revenue, claims_history, underlying_limits, requested_umbrella_limit)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_umbrella_liability_insurance",
  "description": "Underwrite umbrella/excess liability insurance based on ACORD Form 133.",
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
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "number_of_employees": {
        "type": "integer",
        "description": "Number of employees in the business."
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
      "underlying_limits": {
        "type": "object",
        "description": "Limits of underlying policies.",
        "properties": {
          "general_liability": {
            "type": "number",
            "description": "Limit for general liability."
          },
          "auto_liability": {
            "type": "number",
            "description": "Limit for auto liability."
          },
          "employers_liability": {
            "type": "number",
            "description": "Limit for employers liability."
          }
        },
        "required": ["general_liability", "auto_liability", "employers_liability"]
      },
      "requested_umbrella_limit": {
        "type": "number",
        "description": "Requested umbrella coverage limit."
      }
    },
    "required": ["business_info", "naics_code", "number_of_employees", "annual_revenue", "claims_history", "underlying_limits", "requested_umbrella_limit"]
  }
}


```


# Form 137 - Commercial Auto Coverages/Limits Section

## Overview
ACORD Form 137 is typically used for commercial auto insurance. This form collects information about the vehicles, drivers, and business operations to assess the risk associated with insuring the company's vehicles.

For the underwriting algorithm, we'll consider factors such as:

Business Information
Vehicle Information (e.g., type, age, value)
Driver Information (e.g., age, driving experience, driving record)
Business Type (NAICS code)
Annual Revenue
Claims History
Requested Coverage Limits

### Explanation
Class Initialization:

The CommercialAutoUnderwriter class is initialized with business information, vehicles (a list of vehicle details), drivers (a list of driver details), NAICS code, annual revenue, claims history, and requested coverage limits.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
Vehicle information: Different types, ages, and values of vehicles impact risk.
Driver information: The ages, driving experience, and driving records of drivers impact risk.
NAICS code: Different industries have different inherent risks.
Annual revenue: Higher revenue increases risk.
Claims history: The severity of prior claims impacts the risk score.
Requested coverage: Higher requested coverage limits increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the CommercialAutoUnderwriter class is created with sample data, and the underwriting decision is printed out.
This code provides a basic framework for an underwriting algorithm for commercial auto insurance and can be expanded with more sophisticated rules and additional data points as needed.

## Form Information Captured

```python
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



```

## Underwriter Function

```python
class CommercialAutoUnderwriter:
    def __init__(self, business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage):
        self.business_info = business_info
        self.vehicles = vehicles  # List of vehicle details
        self.drivers = drivers  # List of driver details
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.claims_history = claims_history  # List of claims with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Vehicle information
        for vehicle in self.vehicles:
            vehicle_type = vehicle.get("type", "")
            vehicle_age = vehicle.get("age", 0)
            vehicle_value = vehicle.get("value", 0)

            if vehicle_type in ["Truck", "Heavy Equipment"]:
                risk_score += 30  # Higher risk for trucks and heavy equipment
            elif vehicle_type in ["Car", "Van"]:
                risk_score += 10  # Lower risk for cars and vans

            if vehicle_age > 10:
                risk_score += 20  # Higher risk for older vehicles
            elif vehicle_age > 5:
                risk_score += 10

            if vehicle_value > 50000:
                risk_score += 20  # Higher risk for high-value vehicles
            elif vehicle_value > 20000:
                risk_score += 10

        # Driver information
        for driver in self.drivers:
            driver_age = driver.get("age", 0)
            driving_experience = driver.get("experience", 0)
            driving_record = driver.get("record", "Clean")

            if driver_age < 25 or driver_age > 65:
                risk_score += 20  # Higher risk for young or senior drivers
            elif driver_age < 30 or driver_age > 55:
                risk_score += 10

            if driving_experience < 5:
                risk_score += 20  # Higher risk for less experienced drivers
            elif driving_experience < 10:
                risk_score += 10

            if driving_record == "Poor":
                risk_score += 30  # Higher risk for poor driving records
            elif driving_record == "Fair":
                risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "484"]  # Construction, Manufacturing, Transportation
        low_risk_industries = ["541", "611", "722"]  # Professional Services, Education, Food Services

        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Claims history
        for claim in self.claims_history:
            if claim['severity'] == "High":
                risk_score += 30
            elif claim['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 1000000:
            risk_score += 20
        elif self.requested_coverage > 500000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Transport",
        "address": "789 Industrial Ave, Transport City, USA"
    }
    vehicles = [
        {"type": "Truck", "age": 8, "value": 60000},
        {"type": "Van", "age": 3, "value": 30000}
    ]
    drivers = [
        {"age": 45, "experience": 20, "record": "Clean"},
        {"age": 30, "experience": 7, "record": "Fair"}
    ]
    naics_code = "484"  # Transportation
    annual_revenue = 15000000
    claims_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    requested_coverage = 2000000

    underwriter = CommercialAutoUnderwriter(business_info, vehicles, drivers, naics_code, annual_revenue, claims_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_commercial_auto_insurance",
  "description": "Underwrite commercial auto insurance based on ACORD Form 137.",
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


```


# Form 140 - Property Section

## Overview
ACORD Form 140 is typically used for property insurance, which includes coverage for buildings, personal property, and loss of business income. For this underwriting algorithm, we'll consider factors such as:

Business Information
Property Location
Building Information (e.g., construction type, age, square footage)
Business Type (NAICS code)
Annual Revenue
Loss History
Requested Coverage Limits

### Explanation
Class Initialization:

The PropertyInsuranceUnderwriter class is initialized with business information, location, building information (construction type, age, square footage), NAICS code, annual revenue, loss history, and requested coverage limits.
Risk Score Calculation:

The calculate_risk_score method calculates the risk score based on predefined criteria:
Location: Different locations have different inherent risks.
Building information: Different construction types, building ages, and square footage impact risk.
NAICS code: Different industries have different inherent risks.
Annual revenue: Higher revenue increases risk.
Loss history: The severity of prior losses impacts the risk score.
Requested coverage: Higher requested coverage limits increase risk.
Underwriting Decision:

The underwrite method uses the risk score to make a decision:
A risk score below 50 results in acceptance with a premium discount.
A risk score between 50 and 80 results in acceptance with standard conditions.
A risk score above 80 results in decline.
Example Usage:

An example instance of the PropertyInsuranceUnderwriter class is created with sample data, and the underwriting decision is printed out.

## Form Information Captured

```python
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




```

## Underwriter Function

```python
class PropertyInsuranceUnderwriter:
    def __init__(self, business_info, location, building_info, naics_code, annual_revenue, loss_history, requested_coverage):
        self.business_info = business_info
        self.location = location
        self.building_info = building_info
        self.naics_code = naics_code
        self.annual_revenue = annual_revenue
        self.loss_history = loss_history  # List of losses with details
        self.requested_coverage = requested_coverage

    def calculate_risk_score(self):
        risk_score = 0

        # Location risk factor
        high_risk_locations = ["Coastal", "Urban"]
        low_risk_locations = ["Suburban", "Rural"]
        
        if self.location in high_risk_locations:
            risk_score += 30
        elif self.location in low_risk_locations:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other locations

        # Building information
        construction_type = self.building_info.get("construction_type", "")
        building_age = self.building_info.get("age", 0)
        square_footage = self.building_info.get("square_footage", 0)
        
        if construction_type in ["Frame", "Wood"]:
            risk_score += 30  # Higher risk for wood/frame construction
        elif construction_type in ["Masonry", "Steel"]:
            risk_score += 10  # Lower risk for masonry/steel construction

        if building_age > 50:
            risk_score += 20  # Higher risk for older buildings
        elif building_age > 20:
            risk_score += 10

        if square_footage > 50000:
            risk_score += 20  # Higher risk for larger buildings
        elif square_footage > 20000:
            risk_score += 10

        # NAICS code risk factor (simplified)
        high_risk_industries = ["238", "336", "622"]  # Construction, Manufacturing, Healthcare
        low_risk_industries = ["541", "611", "721"]  # Professional Services, Education, Accommodation
        
        if self.naics_code[:3] in high_risk_industries:
            risk_score += 40
        elif self.naics_code[:3] in low_risk_industries:
            risk_score += 10
        else:
            risk_score += 20  # Default risk score for other industries

        # Annual revenue
        if self.annual_revenue > 10000000:
            risk_score += 20
        elif self.annual_revenue > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        # Loss history
        for loss in self.loss_history:
            if loss['severity'] == "High":
                risk_score += 30
            elif loss['severity'] == "Medium":
                risk_score += 20
            else:
                risk_score += 10

        # Requested coverage
        if self.requested_coverage > 10000000:
            risk_score += 20
        elif self.requested_coverage > 5000000:
            risk_score += 10
        else:
            risk_score += 5

        return risk_score

    def underwrite(self):
        risk_score = self.calculate_risk_score()
        if risk_score < 0:
            risk_score = 0  # Minimum risk score is 0

        # Simple underwriting decision based on risk score
        if risk_score < 50:
            decision = "Accept"
            premium_modifier = 0.8  # 20% discount
        elif 50 <= risk_score < 80:
            decision = "Accept with conditions"
            premium_modifier = 1.0  # No discount
        else:
            decision = "Decline"
            premium_modifier = None  # Not applicable

        return {
            "decision": decision,
            "risk_score": risk_score,
            "premium_modifier": premium_modifier
        }

# Example usage
if __name__ == "__main__":
    business_info = {
        "name": "XYZ Corp",
        "address": "789 Industrial Ave, Metropolis, USA"
    }
    location = "Urban"
    building_info = {
        "construction_type": "Masonry",
        "age": 30,
        "square_footage": 25000
    }
    naics_code = "238"  # Construction
    annual_revenue = 12000000
    loss_history = [
        {"year": 2021, "severity": "High"},
        {"year": 2020, "severity": "Medium"},
        {"year": 2019, "severity": "Low"}
    ]
    requested_coverage = 8000000

    underwriter = PropertyInsuranceUnderwriter(business_info, location, building_info, naics_code, annual_revenue, loss_history, requested_coverage)
    result = underwriter.underwrite()

    print(f"Underwriting Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    if result['premium_modifier'] is not None:
        print(f"Premium Modifier: {result['premium_modifier']:.2f}")
    else:
        print("Premium Modifier: Not Applicable")



```

## OpenAI Function / Tool Schema

```json
{
  "name": "underwrite_property_insurance",
  "description": "Underwrite property insurance based on ACORD Form 140.",
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
      "location": {
        "type": "string",
        "description": "Location of the property (e.g., Urban, Suburban)."
      },
      "building_info": {
        "type": "object",
        "description": "Information about the building.",
        "properties": {
          "construction_type": {
            "type": "string",
            "description": "Type of construction (e.g., Masonry, Frame)."
          },
          "age": {
            "type": "integer",
            "description": "Age of the building in years."
          },
          "square_footage": {
            "type": "integer",
            "description": "Total square footage of the building."
          }
        },
        "required": ["construction_type", "age", "square_footage"]
      },
      "naics_code": {
        "type": "string",
        "description": "NAICS code for the industry."
      },
      "annual_revenue": {
        "type": "number",
        "description": "Annual revenue of the business."
      },
      "loss_history": {
        "type": "array",
        "description": "List of prior losses with details.",
        "items": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "Year of the loss."
            },
            "severity": {
              "type": "string",
              "description": "Severity of the loss (e.g., High, Medium, Low)."
            }
          },
          "required": ["year", "severity"]
        }
      },
      "requested_coverage": {
        "type": "number",
        "description": "Requested property coverage limit."
      }
    },
    "required": ["business_info", "location", "building_info", "naics_code", "annual_revenue", "loss_history", "requested_coverage"]
  }
}

```
