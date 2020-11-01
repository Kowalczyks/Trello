Automation tests

The main configuration file is local.ini and there you can change your login credentials and other arguments. 
At the moment it is set as it was in the requirements. I encourage you to watch the log msg's while the test is running
there is a lot of helpful information there specially on backend tests.

There are separate test for backend and frontend layers. I used Pycharm as a IDE.

### Install packages
```
pip install -r requirements.txt

and

setup.py install

```

### Install Chrome
```
86.0.4240.111 siutable for chromedriver 

```



### PLEASE RUN BACKEND TEST FIRST!
**Backend**

To run backend tests from Pycharm, add pyest configuration.
Mark Script Path and browse to backend/tests/tests.py. Check attached ConfigurationBackend.png
To run backend test from Cmdl go to backend/tests pytest tests.py

**Fronted**

To run frontend tests prom Pycharm, create configuration pointed to ../Trello/frontend/testCases/test_login.py as Script.py
To run frontend tests from Cmdl from main folder Trello run 
python -m pytest
or
python -m pytest --html=name_of_report.html it will generate report




