from ._exceptions import ValidationError as ValidationError
from ._helpers import safeget as safeget, to_datetime as to_datetime

def validate_license_key_online(account_id: str, key: str): ...
