import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "zig.mark.binx.dev",
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "zig.mark.binx.dev",
        "EnableWWWSubdomain": False,
        "CertificateValidationRecords": [
            {
                "Name": "_3bf446e046b43e0a75dc8868d5758126.zig.mark.binx.dev.",
                "Type": "CNAME",
                "Value": "_27584e9cdfeb027ec1fd9b5548294386.kqlycvwlbp.acm-validations.aws.",
                "Status": "PENDING_VALIDATION",
            },
            {
                "Name": "_6dacd428861fbaa903735bde8f19bc5b.2a57j77sf95ir4fj35gouo102bbx0e2.zig.mark.binx.dev.",
                "Type": "CNAME",
                "Value": "_c77dbe0a4501325b6b858a95e97c0764.kqlycvwlbp.acm-validations.aws.",
                "Status": "PENDING_VALIDATION",
            },
        ],
        "Status": "deleting",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "3051483f-b2c9-4406-81b7-495668c3fae4",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:25:01 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "723",
            "connection": "keep-alive",
            "x-amzn-requestid": "3051483f-b2c9-4406-81b7-495668c3fae4",
        },
        "RetryAttempts": 0,
    },
}
