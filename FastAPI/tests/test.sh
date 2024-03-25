# simple curl test of 2 endpoints assuming default port for Flask, adjust as needed
# adjusted for FastAPI, default port 8000

echo "TEST 1"
curl -X POST 'http://127.0.0.1:8000/transactions' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@data.csv;type=text/csv'

echo
curl http://127.0.0.1:8000/report
echo "Expected: gross-revenue = 225.0, expenses = 72.93, net-revenue = 152.07"
echo

echo "TEST 2"
curl -X POST 'http://127.0.0.1:8000/transactions' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@data2.csv;type=text/csv'

echo
curl http://127.0.0.1:8000/report
echo "Expected: gross-revenue = 0, expenses = 0, net-revenue = 0"
