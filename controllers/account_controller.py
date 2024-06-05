from __future__ import annotations

from fastapi import APIRouter

from models.account_model import Account


v1_account_router = APIRouter()


@v1_account_router.get(path="/",
                       summary="Get all lead accounts information.",
                       description="Get information of all lead accounts. This includes information such as "
                                   "expected revenue, owner info and score")
def get_lead_account_info() -> list[Account]:
    user_account_1: Account = Account(**{
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
    })

    user_account_2: Account = Account(**{
        "opportunity_name": "wonder_2",
        "expected_revenue": "OMR 1000",
        "opportunity_owner": {
            "name": "Mr.B",
            "id": "efghij"
        },
        "opportunity_type": "Old Business",
        "account": {
            "number": "67890",
            "name": "Omantel"
        },
        "sector": "Financial",
        "status": "Qualification",
        "probability": 0,
        "score": 80,
        "created_by": {
            "user_id": "l1120021",
            "date": "24 Mar 2023"
        }
    })

    return [user_account_1, user_account_2]


@v1_account_router.get(path="/{account_no}",
                       summary="Get a specific lead account information",
                       description="Based on an account number, fetch the information such as expected revenue, "
                                   "owner info and score")
def get_lead_account_info(account_no: int) -> Account:
    """
    Get specific account details.
    :param account_no: The unique identifier for the account
    :return:
    """
    return Account(**{
        "opportunity_name": "wonder_2",
        "expected_revenue": "OMR 1000",
        "opportunity_owner": {
            "name": "Mr.B",
            "id": "efghij"
        },
        "opportunity_type": "Old Business",
        "account": {
            "number": f"{account_no}",
            "name": "Omantel"
        },
        "sector": "Financial",
        "status": "Qualification",
        "probability": 0,
        "score": 80,
        "created_by": {
            "user_id": "l1120021",
            "date": "24 Mar 2023"
        }
    })
