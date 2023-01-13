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
            "Status": "pending_certificate_dns_validation",
        },
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
        "RequestId": "3d9f45b8-94ae-427c-93ee-a26dd37b3384",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Fri, 13 Jan 2023 12:25:01 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "1806",
            "connection": "keep-alive",
            "x-amzn-requestid": "3d9f45b8-94ae-427c-93ee-a26dd37b3384",
        },
        "RetryAttempts": 0,
    },
}
