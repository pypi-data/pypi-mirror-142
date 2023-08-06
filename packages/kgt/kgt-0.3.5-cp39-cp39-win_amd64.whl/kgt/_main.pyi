from ._cached import validate_license_key_cached as validate_license_key_cached
from ._exceptions import LicenseError as LicenseError, ValidationError as ValidationError
from ._offline_keys import validate_offline_key as validate_offline_key
from datetime import timedelta

def validate_all_with_user_prompt(product_name: str, account_id: str, keygen_verify_key: Union[str, None] = ..., product_id: Union[str, None] = ..., fallback_key: Union[str, None] = ..., refresh_cache_period: timedelta = ..., cache_age_warning: timedelta = ..., cache_age_error: timedelta = ..., expiry_warning: timedelta = ...) -> None: ...
