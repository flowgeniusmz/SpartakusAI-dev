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