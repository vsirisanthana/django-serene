SET PROJECT_PATH=test_projects/env_packages/
echo %PYTHONPATH%
SET PYTHONPATH=%PYTHONPATH%;%PROJECT_PATH%;.
echo %PYTHONPATH%
python %PROJECT_PATH%manage.py test serene --with-coverage --cover-package=serene
