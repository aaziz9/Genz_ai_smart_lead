from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GenZ Co-Pilot Plugin API",
    description="Allows co-pilot to fetch ",
    version="1.0.0",
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "GenZ Co-pilot Plugin API that can response with lead account information"
        },
    ]
)

# Add the CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


v1_router = APIRouter()


@v1_router.get(path="/accounts",
               summary="Get all lead accounts information.",
               description="Get information of all lead accounts. This includes information such as expected revenue, "
                           "owner info and score")
def get_lead_account_info():
    return [
        {
            "Opportunity Name": "wonder_1",
            "Expected Revenue": "OMR 20000",
            "Opportunity Owner": {
                "Name": "Mr.A",
                "ID": "abcdef"
            },
            "Opportunity Type": "New Business",
            "Account": {
                "Number": "12345",
                "Name": "Omantel"
            },
            "Sector": "Financial",
            "Status": "Qualification",
            "Probability": 0,
            "Score": 50,
            "Created By": {
                "UserID": "l8520020",
                "Date": "24 Jul 2023"
            }
        },
        {
            "Opportunity Name": "wonder_2",
            "Expected Revenue": "OMR 10000",
            "Opportunity Owner": {
                "Name": "Mr.B",
                "ID": "ghijkl"
            },
            "Opportunity Type": "New Business",
            "Account": {
                "Number": "67890",
                "Name": "Omantel"
            },
            "Sector": "Financial",
            "Status": "Qualification",
            "Probability": 0,
            "Score": 80,
            "Created By": {
                "UserID": "l8520020",
                "Date": "24 Jul 2023"
            }
        }
    ]


@v1_router.get(path="/accounts/{account_no}",
               summary="Get a specific lead account information",
               description="Based on an account number, fetch the information such as expected revenue, "
                           "owner info and score")
def get_lead_account_info(account_no: int):
    """
    Get specific account details.
    :param account_no: The unique identifier for the account
    :return:
    """
    return {
      "Opportunity Name": "test",
      "Expected Revenue": "OMR 10000",
      "Opportunity Owner": {
        "Name": "Mr.A",
        "ID": "abcdef"
      },
      "Opportunity Type": "New Business",
      "Account": {
        "Number": f"{account_no}",
        "Name": "Omantel"
      },
      "Sector": "Financial",
      "Status": "Qualification",
      "Probability": 0,
      "Score": 50,
      "Created By": {
        "UserID": "l8520020",
        "Date": "24 Jul 2023"
      }
    }


# Routers
app.include_router(v1_router, prefix="/api/v1")
