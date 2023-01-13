import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "zag.mark.binx.dev",
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
        "DomainName": "zag.mark.binx.dev",
        "EnableWWWSubdomain": False,
        "CertificateValidationRecords": [
            {
                "Name": "_9550c1211003dccc65b4e9ef49598351.zag.mark.binx.dev.",
                "Type": "CNAME",
                "Value": "_80aa93a556ac3f5a8d7d86eec550bc5a.kqlycvwlbp.acm-validations.aws.",
                "Status": "PENDING_VALIDATION",
            },
            {
                "Name": "_66b259c95e2931cf6593b54eed7939d0.2a57j7852qs07smr4qj2ilatq79cyvg.zag.mark.binx.dev.",
                "Type": "CNAME",
                "Value": "_b98f33848e57124ab8d7b74b90cc976c.kqlycvwlbp.acm-validations.aws.",
                "Status": "PENDING_VALIDATION",
            },
        ],
        "Status": "deleting",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "34f8f826-a5d4-4766-9f63-338e7ed0bf94",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:25:01 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "723",
            "connection": "keep-alive",
            "x-amzn-requestid": "34f8f826-a5d4-4766-9f63-338e7ed0bf94",
        },
        "RetryAttempts": 0,
    },
}
