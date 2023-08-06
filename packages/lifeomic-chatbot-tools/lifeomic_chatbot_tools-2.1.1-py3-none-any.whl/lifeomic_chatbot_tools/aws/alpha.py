import json
import typing as t

import requests
from pydantic import BaseModel

from lifeomic_chatbot_tools._utils import ImportExtraError


try:
    import boto3
except ImportError:
    raise ImportExtraError("aws", __name__)


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
        """
        If ``target`` begins with ``lambda://`` e.g. ``lambda://function-name``, then ``boto3`` will attempt to use the
        environment credentials and call an actual Lambda function named ``function-name``. Alternatively, an actual URL
        can be passed in as the ``target`` to support calling e.g. a locally running Lambda function.
        """
        self._target = target
        self._client = None
        if target.startswith("lambda://"):
            self._target = target.lstrip("lambda://")
            self._client = boto3.client("lambda")

    def get(self, path: str, params: t.Optional[t.Dict[str, t.Any]] = None):
        params = params if params else {}
        payload = {"path": path, "httpMethod": "GET", "queryStringParameters": params}
        return self._invoke_lambda(payload)

    def post(self, path: str, body: dict):
        payload = {"path": path, "httpMethod": "POST", "body": json.dumps(body)}
        return self._invoke_lambda(payload)

    def put(self, path: str, body: dict):
        payload = {"path": path, "httpMethod": "PUT", "body": json.dumps(body)}
        return self._invoke_lambda(payload)

    def delete(self, path: str):
        payload = {"path": path, "httpMethod": "DELETE"}
        return self._invoke_lambda(payload)

    def _invoke_lambda(self, payload: dict):
        if self._client:
            res = self._client.invoke(FunctionName=self._target, Payload=json.dumps(payload))
            return self._parse_response(res["Payload"].read())
        else:
            res = requests.post(self._target, json=payload)
            return self._parse_response(res.content)

    @staticmethod
    def _parse_response(payload: bytes):
        """Creates an `AlphaResponse` object from a raw Lambda response payload."""
        parsed = json.loads(payload.decode("utf-8"))
        return AlphaResponse(status_code=parsed["statusCode"], body=json.loads(parsed["body"]))
