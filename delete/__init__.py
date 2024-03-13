import azure.functions as func
import json
import logging

def main(req: func.HttpRequest, deleteItem: func.SqlRowList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    rows = list(map(lambda r: json.loads(r.to_json()), deleteItem))
    if not rows or rows[0]['rowsAffected'] == 0:
        return func.HttpResponse(
            f"No data found for id = {req.params['id']}",
            status_code=404
        )
    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )