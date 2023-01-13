import os
import boto3
from copy import deepcopy
from custom_resource.base import CustomResourceUnitTestBase
from app_runner_custom_domain_resource_provider import (
    AppRunnerCustomDomainProvider,
    post_response_to_cloudformation,
)
from jsonschema import validate, ValidationError, SchemaError

_attributes_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "required": ["DNSTarget", "ValidationResourceRecords"],
    "properties": {
        "DNSTarget": {"type": "string"},
        "ValidationResourceRecords": {
            "type": "array",
            "minsize": 1,
            "items": [
                {
                    "type": "object",
                    "required": [
                        "Name",
                        "Type",
                        "ResourceRecords",
                        "SetIdentifier",
                        "Weight",
                        "TTL",
                    ],
                    "properties": {
                        "Name": {"type": "string"},
                        "Type": {"type": "string"},
                        "ResourceRecords": {
                            "type": "array",
                            "minContains": 1,
                            "items": [{"type": "string"}],
                        },
                        "SetIdentifier": {"type": "string"},
                        "Weight": {"type": "string", "minimum": 1},
                        "TTL": {"type": "string", "minimum": 60},
                    },
                }
            ],
        },
    },
}


class TestCustomResource(CustomResourceUnitTestBase):
    def setUp(self) -> None:
        sleep_time = 10
        if os.getenv("BOTOCORE_STUBBER_RECORDER") == "on":
            self.start_recorder()
        else:
            sleep_time = 0.1
            super().setUp()
        self.provider = AppRunnerCustomDomainProvider(
            self.session.client("apprunner"), sleep_time=sleep_time
        )

    def tearDown(self) -> None:
        if os.getenv("BOTOCORE_STUBBER_RECORDER") == "on":
            self.write_stubs()
        else:
            super().tearDown()

    def start_recorder(self):
        from botocore_stubber_recorder import BotoRecorder

        boto3.setup_default_session()
        self.recorder = BotoRecorder(boto3.DEFAULT_SESSION)
        self.session = self.recorder.session

    def write_stubs(self):
        from botocore_stubber_recorder import UnitTestGenerator
        from pathlib import Path

        test_name = Path(__file__).parent.stem
        directory = Path(__file__).parent.parent
        generator = UnitTestGenerator(test_name, directory, "")
        generator.generate(self.recorder, False, True)

    def test_crud_cycle(self):
        self._test_extract_attributes()
        self._test_post_response_to_cloudformation()

        request = {
            "ResourceProperties": {
                "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
                "DomainName": "zig.mark.binx.dev",
            }
        }
        response = {}
        self.provider.create(request, response)
        self.assertEqual("SUCCESS", response["Status"], response.get("Reason"))

        self.assertEqual(
            "{ServiceArn},{DomainName}".format(**request["ResourceProperties"]),
            response.get("PhysicalResourceId"),
        )
        validate(response.get("Data", {}), _attributes_schema)

        ## noop update test
        request["PhysicalResourceId"] = response["PhysicalResourceId"]
        request["OldResourceProperties"] = deepcopy(request["ResourceProperties"])
        update_response = {}
        self.provider.update(request, update_response)
        self.assertEqual(
            "SUCCESS", update_response["Status"], update_response["Reason"]
        )

        self.assertEqual(
            "{ServiceArn},{DomainName}".format(**request["ResourceProperties"]),
            update_response.get("PhysicalResourceId"),
        )
        validate(update_response.get("Data", {}), _attributes_schema)

        ## replace update
        original_request = deepcopy(request)
        request["ResourceProperties"]["DomainName"] = "zag.mark.binx.dev"
        update_response = {}
        self.provider.update(request, update_response)
        self.assertEqual(
            "SUCCESS", update_response["Status"], update_response.get("Reason")
        )
        self.assertEqual(
            "{ServiceArn},{DomainName}".format(**request["ResourceProperties"]),
            update_response.get("PhysicalResourceId"),
        )
        validate(update_response.get("Data", {}), _attributes_schema)
        self.assertNotEqual(response.get("Data", {}), update_response.get("Data", {}))

        delete_response = {}
        self.provider.delete(original_request, delete_response)
        self.assertEqual(
            "SUCCESS", delete_response["Status"], delete_response.get("Reason")
        )
        self.assertFalse(delete_response.get("Reason"))

        delete_response = {}
        self.provider.delete(request, delete_response)
        self.assertEqual(
            "SUCCESS", delete_response["Status"], delete_response.get("Reason")
        )
        self.assertFalse(delete_response.get("Reason"))

    def _test_extract_attributes(self):
        create_service_response = {
            "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
            "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
            "CustomDomain": {
                "DomainName": "signature.mark.binx.dev",
                "EnableWWWSubdomain": False,
                "CertificateValidationRecords": [
                    {
                        "Name": "_6a48a026f1c7647adb4fefcd983abe27.signature.mark.binx.dev.",
                        "Type": "CNAME",
                        "Value": "_e77977a32cca64e784b82e72932f644d.xmkpffzlvd.acm-validations.aws.",
                        "Status": "PENDING_VALIDATION",
                    },
                    {
                        "Name": "_fb6cc74845afd3867cb3a14df06d2331.2a57j7852qs07smr4qj2ilatq79cyvg.signature.mark.binx.dev.",
                        "Type": "CNAME",
                        "Value": "_925514878b731170e6a1068441eca949.xmkpffzlvd.acm-validations.aws.",
                        "Status": "PENDING_VALIDATION",
                    },
                ],
                "Status": "deleting",
            },
            "VpcDNSTargets": [],
        }
        attributes = self.provider.extract_attributes(create_service_response)
        self.assertEqual(
            {
                "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
                "ValidationResourceRecords": [
                    {
                        "Name": "_6a48a026f1c7647adb4fefcd983abe27.signature.mark.binx.dev.",
                        "Type": "CNAME",
                        "ResourceRecords": [
                            "_e77977a32cca64e784b82e72932f644d.xmkpffzlvd.acm-validations.aws."
                        ],
                        "SetIdentifier": "b108f9000e04480e88d3997868fb8e18",
                        "Weight": "100",
                        "TTL": "60",
                    },
                    {
                        "Name": "_fb6cc74845afd3867cb3a14df06d2331.2a57j7852qs07smr4qj2ilatq79cyvg.signature.mark.binx.dev.",
                        "Type": "CNAME",
                        "ResourceRecords": [
                            "_925514878b731170e6a1068441eca949.xmkpffzlvd.acm-validations.aws."
                        ],
                        "SetIdentifier": "b108f9000e04480e88d3997868fb8e18",
                        "Weight": "100",
                        "TTL": "60",
                    },
                ],
            },
            attributes,
        )
        validate(attributes, _attributes_schema)

    def _test_post_response_to_cloudformation(self):
        post_response_to_cloudformation(
            "https://httpbin.org/anything", {"hello": "world"}
        )
