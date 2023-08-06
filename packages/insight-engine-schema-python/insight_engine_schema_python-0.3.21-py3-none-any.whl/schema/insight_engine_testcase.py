import json
from typing import List
from pydantic import Field

from fhir.resources.claim import Claim
from fhir.resources import domainresource

from schema.insight_engine_request import InsightEngineRequest
from schema.insight_engine_response import InsightEngineResponse


class InsightEngineTestCase(domainresource.DomainResource):
    """ Insight Engine Test Case.

    This test case contains an InsightEngineRequest and the expected InsightEngineResponse
    (as well as a test case name).
    During policy test the engine will be invoked with this request and it's
    result will be compared with the expected response.
    """

    resource_type = "InsightEngineTestCase"

    name: str = Field("")
    insight_engine_request: InsightEngineRequest = Field(None)
    insight_engine_response: InsightEngineResponse = Field(None)

    @classmethod
    def elements_sequence(cls):
        return ["name", "insight_engine_request", "insight_engine_response"]

    def to_json(self) -> str:
        return self.json()

    def save(self, filename: str):
        jsplain = self.json()
        js = json.loads(jsplain)
        with open(filename, 'w') as file:
            json.dump(js, file, indent=2)
            # file.write(js)


def load_claim(filename: str) -> Claim:
    return Claim.parse_file(filename)


def load_test_case(filename: str) -> InsightEngineTestCase:
    return InsightEngineTestCase.parse_file(filename)


def save_history(history: List[Claim], filename: str):
    claims = []
    for claim in history:
        js = json.loads(claim.json())
        claims.append(js)
    with open(filename, 'w') as file:
        json.dump(claims, file, indent=2)