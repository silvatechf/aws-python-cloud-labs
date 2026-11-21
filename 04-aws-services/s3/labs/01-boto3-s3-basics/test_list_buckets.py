from unittest.mock import Mock

from list_buckets import list_bucket_names


def test_list_bucket_names_returns_names_from_one_page() -> None:
    s3 = Mock()
    s3.list_buckets.return_value = {
        "Buckets": [{"Name": "alpha"}, {"Name": "beta"}]
    }

    assert list_bucket_names(s3) == ["alpha", "beta"]
    s3.list_buckets.assert_called_once_with(MaxBuckets=1000)


def test_list_bucket_names_follows_continuation_token() -> None:
    s3 = Mock()
    s3.list_buckets.side_effect = [
        {
            "Buckets": [{"Name": "alpha"}],
            "ContinuationToken": "next-page-token",
        },
        {"Buckets": [{"Name": "beta"}]},
    ]

    assert list_bucket_names(s3) == ["alpha", "beta"]
    assert s3.list_buckets.call_count == 2
    s3.list_buckets.assert_any_call(
        MaxBuckets=1000,
        ContinuationToken="next-page-token",
    )


def test_list_bucket_names_handles_empty_result() -> None:
    s3 = Mock()
    s3.list_buckets.return_value = {"Buckets": []}

    assert list_bucket_names(s3) == []
