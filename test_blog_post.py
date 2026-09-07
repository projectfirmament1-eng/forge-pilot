import subprocess


def test_python_version():
    result = subprocess.run(['python', '--version'], capture_output=True, text=True)
    assert 'Python 3.8' in result.stdout or 'Python 3.9' in result.stdout \
        or 'Python 3.10' in result.stdout or 'Python 3.11' in result.stdout


def test_dependencies():
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    assert 'requests' in result.stdout
