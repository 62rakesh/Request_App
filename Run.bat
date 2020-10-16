REM pytest -v -s --html=./Reports/TC01_login.html Testcases\login_test.py
REM pytest -v -s --html=./Reports/TC02_workflow.html Testcases\create_workflow_test.py
REM pytest -v -s -m "regression" --html=./Reports/TC02_regression.html Testcases\ --browser=chrome
REM behave features\FirstFeature.feature
pytest -v -s -m "regression" --html=./Reports/TC03_assignstatus.html Testcases\ --browser=chrome
pytest -v -s --html=./Reports/TC03_assignstatus.html Testcases\assignStatus_test.py --browser=chrome