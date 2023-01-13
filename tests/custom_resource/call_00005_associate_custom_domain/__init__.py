import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "zag.mark.binx.dev",
    "EnableWWWSubdomain": False,
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "zag.mark.binx.dev",
        "EnableWWWSubdomain": False,
        "Status": "creating",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "0a44acdc-c067-4c1c-8834-4887ccc9471d",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:24:41 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "288",
            "connection": "keep-alive",
            "x-amzn-requestid": "0a44acdc-c067-4c1c-8834-4887ccc9471d",
        },
        "RetryAttempts": 0,
    },
}
