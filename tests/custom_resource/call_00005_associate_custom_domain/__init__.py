import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "mark.binx.dev",
    "EnableWWWSubdomain": False,
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "mark.binx.dev",
        "EnableWWWSubdomain": False,
        "Status": "creating",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "5f3a26bd-17f0-4071-a1f8-e43f7023b5ff",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:43:56 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "284",
            "connection": "keep-alive",
            "x-amzn-requestid": "5f3a26bd-17f0-4071-a1f8-e43f7023b5ff",
        },
        "RetryAttempts": 0,
    },
}
