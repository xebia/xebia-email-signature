import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18"
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomains": [
        {
            "DomainName": "signature.mark.binx.dev",
            "EnableWWWSubdomain": False,
            "Status": "creating",
        }
    ],
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "6eb171a2-333f-47d5-98f9-a9690911f8b3",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:43:46 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "297",
            "connection": "keep-alive",
            "x-amzn-requestid": "6eb171a2-333f-47d5-98f9-a9690911f8b3",
        },
        "RetryAttempts": 0,
    },
}
