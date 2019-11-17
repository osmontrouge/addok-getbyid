import json

from addok import core

class GetByIdView:

    def on_get(self, req, resp, doc_id):
        result = core.Result.from_id(doc_id)
        resp.body = json.dumps(result.format())
        resp.content_type = 'application/json; charset=utf-8'

def register_http_endpoint(api):
  api.add_route('/id/{doc_id}', GetByIdView())
