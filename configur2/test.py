import pytest

def test_file():
    f = open("temp.mmd", 'r')
    data = f.read()
    f.close()
    assert data == '''flowchart TB
	6e35356 --> 1cea44f
	1cea44f --> 3ba8224
	3ba8224 --> af7553b
	af7553b --> bee9086
	bee9086 --> 14c581e
	14c581e --> 7fafe92
	7fafe92 --> 01f2e60
	f1acb47 --> b4bb1a8
	01f2e60 --> f1acb47
	7fafe92 --> f1acb47
	6e35356(.gitattributes
.gitignore
)
	1cea44f(.gitattributes
.gitignore
configur1.sln
configur1/configur1.py
configur1/configur1.pyproj
)
	3ba8224(.gitattributes
.gitignore
configur1.sln
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
)
	af7553b(.gitattributes
.gitignore
configur1.sln
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
)
	bee9086(.gitattributes
.gitignore
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
)
	14c581e(.gitattributes
.gitignore
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
configur1/test.py
pytest.exe
)
	7fafe92(.gitattributes
.gitignore
README.md
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
configur1/test.py
pytest.exe
)
	01f2e60(.gitattributes
.gitignore
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
configur1/test.py
pytest.exe
)
	f1acb47(.gitattributes
.gitignore
README.md
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
configur1/test.py
pytest.exe
)
	b4bb1a8(.gitattributes
.gitignore
README.md
configur1.sln
configur1/conf.toml
configur1/configur1.py
configur1/configur1.pyproj
configur1/files.tar
configur1/test.py
pytest.exe
)\n'''