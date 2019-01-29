def pytest_addoption(parser):
    parser.addoption('--apk',
                     action='store',
                     default=None,
                     help='Url or local path to apk')
