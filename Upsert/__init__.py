import logging
import azure.functions as func

def main(req: func.HttpRequest, upsertItem:func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
        row = func.SqlRow.from_dict(req_body)
        upsertItem.set(row)
    except ValueError:
        pass

    if req_body:
        return func.HttpResponse(f"Success, {req_body}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "Failed to upsert item. Please pass a valid item in the request body.",
             status_code=200
        )
