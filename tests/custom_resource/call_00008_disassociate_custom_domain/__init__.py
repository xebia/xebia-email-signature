import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "signature.mark.binx.dev",
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
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
        "Status": "deleting",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "82187e8d-aee2-4541-9c79-85bc96b1f178",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:44:06 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "741",
            "connection": "keep-alive",
            "x-amzn-requestid": "82187e8d-aee2-4541-9c79-85bc96b1f178",
        },
        "RetryAttempts": 0,
    },
}
