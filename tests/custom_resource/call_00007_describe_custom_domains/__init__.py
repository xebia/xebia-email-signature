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
            "DomainName": "mark.binx.dev",
            "EnableWWWSubdomain": False,
            "CertificateValidationRecords": [
                {
                    "Name": "_dbedba91818b09beb96e6613a42d2cfa.mark.binx.dev.",
                    "Type": "CNAME",
                    "Value": "_29f21d1110d5ad8d730125c0c75ccae6.xmkpffzlvd.acm-validations.aws.",
                    "Status": "PENDING_VALIDATION",
                },
                {
                    "Name": "_0082e842699ae3463618b55ed0f4bbed.2a57j77sf95ir4fj35gouo102bbx0e2.mark.binx.dev.",
                    "Type": "CNAME",
                    "Value": "_5fbf853e842b6f8fa09ea328ae7b8114.xmkpffzlvd.acm-validations.aws.",
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
                    "Status": "PENDING_VALIDATION",
                },
                {
                    "Name": "_fb6cc74845afd3867cb3a14df06d2331.2a57j7852qs07smr4qj2ilatq79cyvg.signature.mark.binx.dev.",
                    "Type": "CNAME",
                    "Value": "_925514878b731170e6a1068441eca949.xmkpffzlvd.acm-validations.aws.",
                    "Status": "PENDING_VALIDATION",
                },
            ],
            "Status": "pending_certificate_dns_validation",
        },
    ],
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "5cc54690-e297-4188-90e9-6f0b7cee255f",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:44:06 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "1301",
            "connection": "keep-alive",
            "x-amzn-requestid": "5cc54690-e297-4188-90e9-6f0b7cee255f",
        },
        "RetryAttempts": 0,
    },
}
