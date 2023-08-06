from ._exceptions import LicenseError as LicenseError, ValidationError as ValidationError
from ._helpers import safeget as safeget, string_to_dict as string_to_dict, to_datetime as to_datetime
from ._offline_keys import validate_offline_key as validate_offline_key
from datetime import timedelta

def check_key(software_name: str, account_id: str, keygen_verify_key: Union[str, None] = ..., product_id: Union[str, None] = ..., refresh_cache_period: timedelta = ..., cache_age_warning: timedelta = ..., cache_age_error: timedelta = ..., expiry_warning: timedelta = ...) -> None: ...
def validate_license_key_online(account_id: str, key: str): ...
