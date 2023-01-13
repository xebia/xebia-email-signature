import logging
from urllib.request import urlopen, Request
from time import sleep
import boto3
import json
from botocore.exceptions import ClientError


class AppRunnerCustomDomainProvider:
    """
    temporary implementation of AWS::AppRunner::CustomDomain
    """

    def __init__(self, apprunner, sleep_time: float = 10.0):
        self.apprunner = apprunner
        self.sleep_time = sleep_time
        if not self.apprunner:
            self.apprunner = boto3.client("apprunner")

    @staticmethod
    def extract_attributes(response: dict) -> dict:
        set_identifier = response["ServiceArn"].split("/")[-1]
        return {
            "DNSTarget": response["DNSTarget"],
            "ValidationResourceRecords": [
                {
                    "Name": r["Name"],
                    "Type": r["Type"],
                    "ResourceRecords": [r["Value"]],
                    "SetIdentifier": set_identifier,
                    "Weight": "100",
                    "TTL": "60",
                }
                for r in response["CustomDomain"]["CertificateValidationRecords"]
            ],
        }

    def create(self, request, response):
        """
        associates a Custom Domain with an AppRunner service
        """
        kwargs = {
            "ServiceArn": request.get("ResourceProperties", {}).get("ServiceArn"),
            "DomainName": request.get("ResourceProperties", {}).get("DomainName"),
            "EnableWWWSubdomain": False,
        }

        _ = self.apprunner.associate_custom_domain(**kwargs)

        response["PhysicalResourceId"] = "{ServiceArn},{DomainName}".format(**kwargs)
        self.read(request, response)

    def update(self, request, response):
        """
        updates an association of a Custom Domain with an AppRunner service
        """
        kwargs = {
            "ServiceArn": request.get("ResourceProperties", {}).get("ServiceArn"),
            "DomainName": request.get("ResourceProperties", {}).get("DomainName"),
        }

        old_kwargs = {
            "ServiceArn": request.get("OldResourceProperties", {}).get("ServiceArn"),
            "DomainName": request.get("OldResourceProperties", {}).get("DomainName"),
        }

        if old_kwargs == kwargs:
            response["Reason"] = "Nothing has changed"
            response["PhysicalResourceId"] = request["PhysicalResourceId"]
            self.read(request, response)
            return

        self.create(request, response)

    def read(self, request, response):
        """
        reads the current custom domain and sets the resource attributes.
        """
        service_arn = request.get("ResourceProperties", {}).get("ServiceArn")
        domain_name = request.get("ResourceProperties", {}).get("DomainName")

        attempt = 0
        custom_domain = {}
        while custom_domain.get("Status", "creating") == "creating" and attempt < 6:
            custom_domains = self.apprunner.describe_custom_domains(
                ServiceArn=service_arn
            )
            custom_domain = next(
                filter(
                    lambda r: r["DomainName"] == domain_name
                    and r["Status"] != "creating",
                    custom_domains["CustomDomains"],
                ),
                {},
            )
            if not custom_domain:
                attempt += 1
                logging.info(
                    f"sleeping {self.sleep_time}s to await the arrival of the validation records"
                )
                sleep(self.sleep_time)

        if not custom_domain:
            response["Status"] = "FAILED"
            response["Reason"] = f"No custom domain found for {domain_name}"
            return

        custom_domains["CustomDomain"] = custom_domain
        response["Data"] = self.extract_attributes(custom_domains)
        response["Status"] = "SUCCESS"

    def delete(self, request, response):
        """
        disassociate a Custom Domain from an AppRunner service
        """
        if not request["PhysicalResourceId"].startswith("arn:aws:apprunner"):
            response["Reason"] = "ignoring failed create"
            response["Status"] = "SUCCESS"
            return

        kwargs = {
            "ServiceArn": request.get("ResourceProperties", {}).get("ServiceArn"),
            "DomainName": request.get("ResourceProperties", {}).get("DomainName"),
        }
        try:
            _ = self.apprunner.disassociate_custom_domain(**kwargs)
        except ClientError as error:
            response["Reason"] = "ignoring error to disassociate custom domain"
            logging.error("%s, %s", response["Reason"], error)
        response["Status"] = "SUCCESS"

    def handle(self, request):
        """
        handles a cloudformation resource create, update or delete request
        """
        response = {
            "StackId": request["StackId"],
            "RequestId": request["RequestId"],
            "LogicalResourceId": request["LogicalResourceId"],
            "Status": "SUCCESS",
        }
        if request.get("PhysicalResourceId", None):
            response["PhysicalResourceId"] = request["PhysicalResourceId"]

        try:
            request_type = request.get("RequestType")
            if request_type == "Create":
                self.create(request, response)
            elif request_type == "Update":
                self.update(request, response)
            elif request_type == "Delete":
                self.delete(request, response)
            else:
                response["Status"] = "FAILED"
                response["Reason"] = f"unknown request type {request_type}"
        except Exception as error:
            response["Status"] = "FAILED"
            response["Reason"] = f"exception while processing {request_type}, {error}"
            logging.error("%s, %s", response["Reason"], error)

        return response


def post_response_to_cloudformation(url: str, response: dict):
    """ "
    posts the response message to CloudFormation
    """
    data = json.dumps(response).encode("utf-8")
    logging.error("%s", data)
    put_request = Request(
        url=url,
        data=data,
        headers={"Content-Length": len(data), "Content-Type": ""},
        method="PUT",
    )
    urlopen(put_request)


def handler(request, _):
    provider = AppRunnerCustomDomainProvider(boto3.client("apprunner"))
    post_response_to_cloudformation(request["ResponseURL"], provider.handle(request))
