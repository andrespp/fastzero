def test_settings(settings):
    assert isinstance(settings.DATABASE_URL, str)
