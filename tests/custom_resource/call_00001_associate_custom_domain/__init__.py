import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "zig.mark.binx.dev",
    "EnableWWWSubdomain": False,
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "zig.mark.binx.dev",
        "EnableWWWSubdomain": False,
        "Status": "creating",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "f46741cc-5d9d-4dd0-88ec-1311439aaa3d",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:24:30 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "288",
            "connection": "keep-alive",
            "x-amzn-requestid": "f46741cc-5d9d-4dd0-88ec-1311439aaa3d",
        },
        "RetryAttempts": 0,
    },
}
