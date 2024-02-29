import azure.functions as func
import json
import logging

def main(req: func.HttpRequest, readItem: func.SqlRowList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    rows = list(map(lambda r: json.loads(r.to_json()), readItem))

    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )