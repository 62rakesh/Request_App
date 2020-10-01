REM pytest -v -s --html=./Reports/TC01_login.html Testcases\login_test.py
pytest -v -s -m "regression" --html=./Reports/TC01_regression.html Testcases\ --browser=chrome