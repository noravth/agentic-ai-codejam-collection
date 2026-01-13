from dotenv import load_dotenv
from rpt1.call_rpt1 import RPT1Client

def main():
    # Load env vars if needed
    load_dotenv()
    rpt1_client = RPT1Client()

    # Define the JSON payload for prediction
    json_payload = {
        "prediction_config": {
            "target_columns": [
                {
                    "name": "COSTCENTER",
                    "prediction_placeholder": "[PREDICT]",
                    "task_type": "classification",
                },
                {
                    "name": "PRICE",
                    "prediction_placeholder": "[PREDICT]",
                    "task_type": "regression",
                }
            ]
        },
        "index_column": "ID",
        "rows": [
            {
                "PRODUCT": "Couch",
                "PRICE": "[PREDICT]",
                "ORDERDATE": "28-11-2025",
                "ID": "35",
                "COSTCENTER": "[PREDICT]",
            },
            {
                "PRODUCT": "Office Chair",
                "PRICE": 150.8,
                "ORDERDATE": "02-11-2025",
                "ID": "44",
                "COSTCENTER": "Office Furniture",
            },
            {
                "PRODUCT": "Server Rack",
                "PRICE": 210.0,
                "ORDERDATE": "01-11-2025",
                "ID": "108",
                "COSTCENTER": "Data Infrastructure",
            },
            {
                "PRODUCT": "Server Rack",
                "PRICE": "[PREDICT]",
                "ORDERDATE": "01-11-2025",
                "ID": "104",
                "COSTCENTER": "[PREDICT]",
            }
        ],
        "data_schema": {
            "PRODUCT": {"dtype": "string"},
            "PRICE": {"dtype": "numeric"},
            "ORDERDATE": {"dtype": "date"},
            "ID": {"dtype": "string"},
            "COSTCENTER": {"dtype": "string"},
        }
    }
    
    response = rpt1_client.post_request(json_payload=json_payload)
    print("Prediction response status code:", response.status_code)
    print("Prediction response JSON:", response.json())


if __name__ == "__main__":
    main()