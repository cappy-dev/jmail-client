from pathlib import Path
from unittest.mock import Mock, patch

from jmail import JmailClient


def test_download_304_with_missing_cache(tmp_path: Path) -> None:
    """Test that 304 without existing cache file triggers fresh download."""
    cache_dir = tmp_path / "nested" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # First call returns 304, second call returns 200 with content
    mock_304 = Mock()
    mock_304.status_code = 304
    mock_304.headers = {}
    mock_304.iter_content.return_value = []
    mock_304.close = Mock()
    
    mock_200 = Mock()
    mock_200.status_code = 200
    mock_200.headers = {}
    mock_200.iter_content.return_value = [b"parquet data"]
    
    with patch("jmail.requests.get", side_effect=[mock_304, mock_200]):
        client = JmailClient(cache=True, cache_dir=cache_dir)
        downloaded = client._download("emails")
    
    assert downloaded == cache_dir / "emails.parquet"
    assert downloaded.read_bytes() == b"parquet data"
