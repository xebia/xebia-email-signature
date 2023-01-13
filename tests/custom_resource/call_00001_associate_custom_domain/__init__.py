import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "signature.mark.binx.dev",
    "EnableWWWSubdomain": False,
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "signature.mark.binx.dev",
        "EnableWWWSubdomain": False,
        "Status": "creating",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "b4175563-8948-4480-8dca-9d98a328e2e5",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:43:45 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "294",
            "connection": "keep-alive",
            "x-amzn-requestid": "b4175563-8948-4480-8dca-9d98a328e2e5",
        },
        "RetryAttempts": 0,
    },
}
