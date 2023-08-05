import json
import typing as t

import requests
from pydantic import BaseModel


class AlphaResponse(BaseModel):
    status_code: int  # the http response status code
    body: t.Union[str, dict, list, bool, float, int]  # the http response body


class Alpha:
    """
    A minimal Python port of LifeOmic's `alpha` utility for calling Lambda functions that operate
    as web services using the [AWS API Gateway event format](https://docs.aws.amazon.com/lambda/latest/dg/services-apiga
    teway.html#apigateway-example-event).
    """

    def __init__(self, target: str):
        self._target = target

    def get(self, path: str, params: t.Optional[t.Dict] = None):
        params = params if params else {}
        res = requests.post(self._target, json={"path": path, "httpMethod": "GET", "queryStringParameters": params})
        return self._transform_lambda_response(res)

    def post(self, path: str, body: dict):
        res = requests.post(self._target, json={"path": path, "httpMethod": "POST", "body": json.dumps(body)})
        return self._transform_lambda_response(res)

    def put(self, path: str, body: dict):
        res = requests.post(self._target, json={"path": path, "httpMethod": "PUT", "body": json.dumps(body)})
        return self._transform_lambda_response(res)

    def delete(self, path: str):
        res = requests.post(self._target, json={"path": path, "httpMethod": "DELETE"})
        return self._transform_lambda_response(res)

    @staticmethod
    def _transform_lambda_response(res: requests.Response) -> AlphaResponse:
        data = res.json()
        return AlphaResponse(status_code=data["statusCode"], body=json.loads(data["body"]))
