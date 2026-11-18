from pathlib import Path
from unittest.mock import Mock, patch

from jmail import JmailClient


def test_download_creates_cache_directory_when_cache_disabled(tmp_path: Path) -> None:
    cache_dir = tmp_path / "nested" / "cache"
    response = Mock()
    response.status_code = 200
    response.headers = {}
    response.iter_content.return_value = [b"parquet data"]

    client = JmailClient(cache=False, cache_dir=cache_dir)
    with patch("jmail.requests.get", return_value=response):
        downloaded = client._download("emails")

    assert downloaded == cache_dir / "emails.parquet"
    assert downloaded.read_bytes() == b"parquet data"
