from ._helpers import safeget as safeget, string_to_dict as string_to_dict, to_datetime as to_datetime
from datetime import timedelta
from pathlib import Path

def validate_license_key_cached(account_id: str, key: str, keygen_verify_key: Union[str, None], cache_path: Union[Path, str], refresh_cache_period: Union[timedelta, int]): ...
