from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import csv

app = FastAPI(title="Canonical coding assessment")
report_list = []


@app.get("/")
def index():
    return FileResponse("./index.html")


@app.post("/transactions")
def upload(file: UploadFile):
    if file.content_type != "text/csv":
        raise HTTPException(
            status_code=400, detail="Media type error, only .csv files accepted."
        )

    result = parse_transaction_csv(file)
    return result


def parse_transaction_csv(csv_file: UploadFile):
    TYPE = 1
    AMOUNT = 2

    expense = 0
    revenue = 0

    try:
        transaction_data = csv_file.file.read()
        transaction_data = transaction_data.decode("utf-8")
        transaction_data = transaction_data.splitlines()

        transaction_reader = csv.reader(transaction_data, delimiter=",")
        for row in transaction_reader:
            if len(row) != 4:
                continue
            if row[TYPE].strip() == "Expense":
                expense += float(row[AMOUNT].strip())
            elif row[TYPE].strip() == "Income":
                revenue += float(row[AMOUNT].strip())
    except Exception as e:
        print(e)
        return {"Status": "File Upload FAILED"}

    summary = {
        "gross-revenue": revenue,
        "expenses": expense,
        "net-revenue": revenue - expense,
    }
    report_list.append(summary)

    return {"Status": "File Upload Successful!!!"}


@app.get("/report")
def report():
    if len(report_list) < 1:
        return {"Status:": "No reports generated"}
    return report_list[-1]
