import botocore
import datetime
from dateutil.tz import tzutc, tzlocal


request = {
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "DomainName": "mark.binx.dev",
}
response = {
    "DNSTarget": "42rip6hbxu.eu-west-1.awsapprunner.com",
    "ServiceArn": "arn:aws:apprunner:eu-west-1:444093529715:service/xebia-email-signature/b108f9000e04480e88d3997868fb8e18",
    "CustomDomain": {
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
        "Status": "deleting",
    },
    "VpcDNSTargets": [],
    "ResponseMetadata": {
        "RequestId": "8bb8aa63-8baa-4169-828a-3fd6adda8912",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 12 Jan 2023 20:44:07 GMT",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "711",
            "connection": "keep-alive",
            "x-amzn-requestid": "8bb8aa63-8baa-4169-828a-3fd6adda8912",
        },
        "RetryAttempts": 0,
    },
}
