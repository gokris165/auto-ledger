# Feature List
...work in progress...<br>

# Installation Guide

You'll need to have Python installed for this project. This project has been
tested on **Windows 10** and **Python version 3.12.1**, it may or may not work on older versions of python.

Run "setup.sh" from the command line with the following command(on Windows with Git Bash): `source setup.sh <path-to-your-python.exe>`. <br>
For example: `source setup.sh C:/dev/Python/python.exe`. <br>
The script will automatically create and start a virtual envinroment, and download the necessary dependencies. 
We just need to start the server after the setup script finishes with: `uvicorn main:app` inside the src directory.

If the setup script doesn't work then go through the following steps for a manual setup:

1. Create a virtual environment (venv)
   - Create a venv with `<path-to-python.exe> -m venv <name-of-venv>`
   - For example: `C:/Python/python.exe -m venv .venv`
   - You can exit the virtual environment later by typing `deactivate` in the terminal
2. Activate virtual environment
   - Linux: `source <name-of-venv>/bin/activate`
   - Windows: `source <name-of-venv>/Scripts/activate`
      - There's different scripts depending on whether you're running bash or powershell
      - For example, there's `activate.bat` for cmd and `activate.ps1` for powershell
3. Install necessary dependencies with  `pip install -r requirements.txt`
4. Run the app from the terminal with `uvicorn main:app`

Once the app is running, you can run the test script with: `sh test.sh` inside the tests directory.

<!--
# Solution Context and Assumptions

Context: Given a .csv file with valid data, generate expense/income report. Use curl to access endpoints 
or use browser HTML UI for file upload.
- Assumed that persistance is not necessary (from hint)
- .csv delimiter is always comma
- If there are 4 values, the input is valid and in the right order
- Only .csv files will be sent to the server
- There are no typos in data entry
- Only 1 client will be using this at a time


# Shortcomings

- Non-csv files can be sent to the server via command line. For example
the following results in a success:
   ```
   curl -X POST 'http://127.0.0.1:8000/transactions' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@index.html;type=text/csv'
   ```
   The last line `file=@index.html;type=text/csv` bypasses the server's .csv file
check and outputs "File Upload Successful!!!"
- Curl request now requires 2 -H parameters, "accept" and "Content-Type", which were
originally not part of the given test script. Maybe a different framework or 
logic would have resulted in a simpler Curl script. 
- Frontend UI is very minimal and doesn't show generated report
- No persistence, reports and data are not saved between server restarts
- No multi-user support


# Potential Features 

If there was more time available then the following features/bug fixes would've been 
implemented:

- Robust file checking, only allow .csv files to be submitted even if the command line 
exploit from before was run
- Frontend UI improvements
   - Make it look modern and stylish with CSS libraries and JavaScript
   - Display report on same webpage UI instead of only the file selector and switching to the `/transactions` path
- Robust data verification, check if inputs are valid and follow the data entry specification
- Add persistence to the server
- Make use of Date and Memo in some ways:
   - Support storing multiple reports and viewing them via the browser HTML page
   - Support some sort of search ability to filter expenses via Memo input
   - Add a map with income locations from Memo highlighted for some visual output
- Add multi-user support, support multiple users uploading their .csv files 
and getting their corresponding report instead of the latest report based on the latest transaction.csv file
- Think/implement more test cases to make sure everything works as intended

-->