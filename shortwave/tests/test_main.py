import subprocess


def test_version():
    """Test for version output."""
    output = subprocess.run(['shortwave-searcher', '--version'], stdout=subprocess.PIPE)
    assert output == "0.0.1"
