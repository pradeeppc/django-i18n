from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

# from myapp.management.commands import wait_for_db


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """ Test waiting for db when db is available """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as getitem:
            getitem.return_value = True
            call_command('wait_for_db')
            self.assertEqual(getitem.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test waiting for db."""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as getitem:
            getitem.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(getitem.call_count, 6)
