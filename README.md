- create virtual environment
  ```bash
  py -m venv .venv
  ```
- to activate virtual environment
  ```bash
  .venv\scripts\activate
  ```
- to install new package
  ```bash
  py -m pip install <package_name>
  ```
- to create requirements.txt file
  ```bash
  py -m pip freeze > requirements.txt
  ```  
- to install all packages from requirments.txt file
  ```bash
  py -m pip install -r requirements.txt
  ```
- to run streamlit app => streamlit run <file_name>
 ```bash
 streamlit run coder_chat.py
 ```
