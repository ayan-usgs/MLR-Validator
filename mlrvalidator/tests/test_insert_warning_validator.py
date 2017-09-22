
from unittest import TestCase
from mlrvalidator.site_file_validator_warnings import SitefileWarningValidator
from mlrvalidator.schema import schema_registry

schema = schema_registry.get('insert_warning_schema')
site_validator = SitefileWarningValidator()
site_validator.allow_unknown = True


class ValidateWarningsCase(TestCase):
    def setUp(self):
        self.good_data = {
            'stationName': '12345'
        }
        self.bad_data = {
            'stationName': "12345'"
        }

    def test_validate_ok(self):
        self.assertTrue(site_validator.validate(self.good_data, schema))

    def test_with_validate_not_ok(self):
        self.assertFalse(site_validator.validate(self.bad_data, schema))