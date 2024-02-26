import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, readItem: func.SqlRowList) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    rows = list(map(lambda r: json.loads(r.to_json()), readItem))
    if not rows:
        return func.HttpResponse(
            "No items found",
            status_code=404
        )
    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )