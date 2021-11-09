from app import index


# import sys
#
# sys.path.append('/Volumes/Seagate_Haykay/python-github-actions-CI-CD/src/app')
#
# import app


def test_index():
    assert index() == "Hello World"
