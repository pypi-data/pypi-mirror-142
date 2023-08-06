from okera.tests import pycerebro_test_common as common

class MiscTest(common.TestBase):
    def test_parse_commit_message(self):
        msg = 'W3Rlc3RzXVtyZXdyaXRlXSBBZGQgc29tZSBDVEUgdGVzdHMgYW5kIHNvbWUgdGVzdCByZWZhY3RvcmluZwoKKldoYXQgdGhpcyBQUiBkb2VzIC8gd2h5IHdlIG5lZWQgaXQ6KgpGaXhlcyBvbmUgZXhwZWN0ZWQgdGVzdCBjaGFuZ2UgZnJvbToKCmh0dHBzOi8vZ2Vycml0Lm9rZXJhLmRldi9jL2NlcmVicm8vKy8xNzMwMwoKKlNwZWNpYWwgbm90ZXMgZm9yIHlvdXIgcmV2aWV3ZXI6KgoKKkFkZGl0aW9uYWwgdGVzdGluZyB0aGF0IHdhcyBkb25lOioKCkFERElUSU9OQUxfQ0lfVEVTVFM6IHNub3dmbGFrZS1jdGUKYGBgClJlbGVhc2Ugbm90ZToKYGBgCgpDaGFuZ2UtSWQ6IEk1YzBlMDRhMGM5MDUzMmNmY2RhOWMwMzQwYTQ5ZDc0ODMzOTUxMjMxCg=='
        result = common.get_ci_test_cases(msg)
        self.assertEqual(['snowflake-cte'], result)


