from pydantic import BaseModel, Field


class OpportunityOwner(BaseModel):
    name: str
    id: str


class AccountDetails(BaseModel):
    number: str
    name: str


class CreatedBy(BaseModel):
    user_id: str
    date: str


class Account(BaseModel):
    opportunity_name: str = Field(..., alias="opportunity_name")
    expected_revenue: str = Field(..., alias="expected_revenue")
    opportunity_owner: OpportunityOwner = Field(..., alias="opportunity_owner")
    opportunity_type: str = Field(..., alias="opportunity_type")
    account: AccountDetails
    sector: str
    status: str
    probability: int
    score: int
    created_by: CreatedBy = Field(..., alias="created_by")


# Example usage:
example_json = {
    "opportunity_name": "wonder_1",
    "expected_revenue": "OMR 20000",
    "opportunity_owner": {
        "name": "Mr.A",
        "id": "abcdef"
    },
    "opportunity_type": "New Business",
    "account": {
        "number": "12345",
        "name": "Omantel"
    },
    "sector": "Financial",
    "status": "Qualification",
    "probability": 0,
    "score": 50,
    "created_by": {
        "user_id": "l8520020",
        "date": "24 Jul 2023"
    }
}

account = Account(**example_json)
print(account)
