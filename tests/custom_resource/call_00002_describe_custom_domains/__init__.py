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
            "DomainName": "zig.mark.binx.dev",
            "EnableWWWSubdomain": False,
            "Status": "creating",
        },
        {
            "DomainName": "signature.mark.binx.dev",
            "EnableWWWSubdomain": False,
            "CertificateValidationRecords": [
                {
                    "Name": "_6a48a026f1c7647adb4fefcd983abe27.signature.mark.binx.dev.",
                    "Type": "CNAME",
                    "Value": "_e77977a32cca64e784b82e72932f644d.xmkpffzlvd.acm-validations.aws.",
                    "Status": "SUCCESS",
                },
                {
                    "Name": "_fb6cc74845afd3867cb3a14df06d2331.2a57j7852qs07smr4qj2ilatq79cyvg.signature.mark.binx.dev.",
                    "Type": "CNAME",
                    "Value": "_925514878b731170e6a1068441eca949.xmkpffzlvd.acm-validations.aws.",
                    "Status": "SUCCESS",
                },
            ],
            "Status": "active",
        },
    ],
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "c33363cb-1ea1-437b-95ed-a58c11454dd8",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:24:30 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "802",
            "connection": "keep-alive",
            "x-amzn-requestid": "c33363cb-1ea1-437b-95ed-a58c11454dd8",
        },
        "RetryAttempts": 0,
    },
}
