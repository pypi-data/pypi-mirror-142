from ._exceptions import ValidationError as ValidationError
from ._helpers import to_datetime as to_datetime

def validate_offline_key(license_scheme: str, license_key: str, keygen_verify_key: str) -> dict: ...
