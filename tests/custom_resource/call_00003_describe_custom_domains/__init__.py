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
            "Status": "pending_certificate_dns_validation",
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
        "RequestId": "f937e395-6542-4440-b6a2-ed0b7c96080f",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:24:41 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "1263",
            "connection": "keep-alive",
            "x-amzn-requestid": "f937e395-6542-4440-b6a2-ed0b7c96080f",
        },
        "RetryAttempts": 0,
    },
}
