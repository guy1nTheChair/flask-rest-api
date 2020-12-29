##Flask REST API
1. Clone the repo 

2. Install virtualenv
   ```
   python/python3 -m pip install virtualenv
   ```
2. Run depending python variable
   ```
   python/python3 -m virtualenv env
   ```
3. Activate Virtualenv: 
   ```
   .\env\Scripts\activate (Windows Command Promt)
   source ./env/bin/activate (Linux)
   ```
4. Run 
   ```
   pip install -r requirements.txt
   ```
5. Use 'set' for Windows and 'export' for Linux
   ```
   set/export FLASK_APP=main.py
   set/export FLASK_ENV=development
   ```
7. Run 
   ```
   flask run --reload --host 0.0.0.0 --port 8080
   ```
8. Do 
   ```
   curl http://localhost:8080/
   ```
9. Run tests
    ```
   pytest tests.py
    ```
10. To deactivate virtualenv: 
   ```deactivate
   ```