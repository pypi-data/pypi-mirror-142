# Copyright 2021 Red Hat.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from oslo_log import log as logging
from designate_tempest_plugin.common import constants as const
from tempest import config
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc


from designate_tempest_plugin.tests import base

CONF = config.CONF
LOG = logging.getLogger(__name__)


class ServiceStatus(base.BaseDnsV2Test):

    credentials = ["primary", "admin", "system_admin", "alt"]

    @classmethod
    def setup_credentials(cls):
        # Do not create network resources for these test.
        cls.set_network_resources()
        super(ServiceStatus, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(ServiceStatus, cls).setup_clients()
        if CONF.enforce_scope.designate:
            cls.admin_client = cls.os_system_admin.dns_v2.ServiceClient()
        else:
            cls.admin_client = cls.os_admin.dns_v2.ServiceClient()
        cls.client = cls.os_primary.dns_v2.ServiceClient()

        cls.primary_client = cls.os_primary.dns_v2.ServiceClient()
        cls.alt_client = cls.os_alt.dns_v2.ServiceClient()

    @decorators.idempotent_id('bf277a76-8583-11eb-a557-74e5f9e2a801')
    def test_admin_list_service_statuses(self):

        services_statuses_tup = [
            (item['service_name'],
             item['status']) for item in self.admin_client.list_statuses()]
        LOG.info("Listed service tuples: (name,status)' are:{} ".format(
            services_statuses_tup))

        LOG.info('Make sure that all expected/mandatory services are '
                 'listed in API response.')
        expected_services = ['central', 'mdns', 'worker', 'producer']
        for service in expected_services:
            self.assertIn(
                service, [item[0] for item in services_statuses_tup],
                "Failed, expected service: {} wasn't detected in API "
                "response".format(service))

        LOG.info('Make sure that all listed services are in UP status.')
        self.assertEqual(
            {const.UP}, set([item[1] for item in services_statuses_tup]),
            "Failed, not all listed services are in UP status, "
            "services: {}".format(services_statuses_tup))

    @decorators.idempotent_id('d4753f76-de43-11eb-91d1-74e5f9e2a801')
    def test_primary_is_forbidden_to_list_service_statuses(self):

        LOG.info('Try to "list service statuses" as Primary user')
        self.assertRaises(
            lib_exc.Forbidden, self.primary_client.list_statuses)

        headers = [{'x-auth-all-projects': True},
                   {'x-auth-sudo-project-id': self.alt_client.project_id}]
        for header in headers:
            LOG.info('Try to "list service statuses" using {} '
                     'HTTP header'.format(header))
            self.assertRaises(
                lib_exc.Forbidden, self.primary_client.list_statuses,
                headers=header)
