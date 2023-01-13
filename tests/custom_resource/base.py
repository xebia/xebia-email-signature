"""
Generated base class for the custom_resource unit test. The setup will provide stubbed
responses for all recorded requests.

** generated code - do not edit **
"""
import unittest
import botocore.session
from botocore.stub import Stubber

from custom_resource import call_00001_associate_custom_domain

from custom_resource import call_00002_describe_custom_domains

from custom_resource import call_00003_describe_custom_domains

from custom_resource import call_00004_describe_custom_domains

from custom_resource import call_00005_associate_custom_domain

from custom_resource import call_00006_describe_custom_domains

from custom_resource import call_00007_describe_custom_domains

from custom_resource import call_00008_disassociate_custom_domain

from custom_resource import call_00009_disassociate_custom_domain


class CustomResourceUnitTestBase(unittest.TestCase):
    def setUp(self) -> None:
        """
        add stubs for all AWS API calls
        """
        self.session = botocore.session.get_session()
        self.clients = {
            service: self.session.create_client(service) for service in ["apprunner"]
        }
        self.stubs = {
            service: Stubber(client) for service, client in self.clients.items()
        }

        self.stubs["apprunner"].add_response(
            "associate_custom_domain",
            call_00001_associate_custom_domain.response,
            call_00001_associate_custom_domain.request,
        )

        self.stubs["apprunner"].add_response(
            "describe_custom_domains",
            call_00002_describe_custom_domains.response,
            call_00002_describe_custom_domains.request,
        )

        self.stubs["apprunner"].add_response(
            "describe_custom_domains",
            call_00003_describe_custom_domains.response,
            call_00003_describe_custom_domains.request,
        )

        self.stubs["apprunner"].add_response(
            "describe_custom_domains",
            call_00004_describe_custom_domains.response,
            call_00004_describe_custom_domains.request,
        )

        self.stubs["apprunner"].add_response(
            "associate_custom_domain",
            call_00005_associate_custom_domain.response,
            call_00005_associate_custom_domain.request,
        )

        self.stubs["apprunner"].add_response(
            "describe_custom_domains",
            call_00006_describe_custom_domains.response,
            call_00006_describe_custom_domains.request,
        )

        self.stubs["apprunner"].add_response(
            "describe_custom_domains",
            call_00007_describe_custom_domains.response,
            call_00007_describe_custom_domains.request,
        )

        self.stubs["apprunner"].add_response(
            "disassociate_custom_domain",
            call_00008_disassociate_custom_domain.response,
            call_00008_disassociate_custom_domain.request,
        )

        self.stubs["apprunner"].add_response(
            "disassociate_custom_domain",
            call_00009_disassociate_custom_domain.response,
            call_00009_disassociate_custom_domain.request,
        )

        for _, stub in self.stubs.items():
            stub.activate()
        self.session.client = lambda x: self.clients[x]

    def tearDown(self) -> None:
        """
        check all api calls were executed
        """
        for service, stub in self.stubs.items():
            stub.assert_no_pending_responses()
            stub.deactivate()
