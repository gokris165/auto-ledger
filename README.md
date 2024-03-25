# Auto Ledger

An experimental project to parse CSV files of the format `YYYY-MM-DD, Type, Cost, Memo` 
and generate a summary for the user. The app will provide REST APIs for the 
user to upload their file and to view a generated summary of that file.

Here's what the example data looks like: 
```
2024-07-01, Expense, 18.77, Gas
2024-07-04, Income, 40.00, 347 Woodrow
2024-07-06, Income, 35.00, 219 Pleasant
2024-07-12, Expense, 49.50, Repairs
```

# Project Objectives

This is a mono repo with 3 different implementations of the same project. 
The inspiration for this project is to try out different **Python Web Frameworks** 
as well as different **Frontend Frameworks**, and see their differences. The app 
will be runnable through the terminal as well as have a frontend browser component. 

Here are the main objectives of this project ordered by priority:
1. Trying out **FastAPI, Django, and Flask** for developing REST APIs
2. Utilizing different Frontend Frameworks like **React, Angular, and Vue**
3. Getting experience with different **CSS libraries** 
4. Getting familiarity with **TypeScript** for frontend development
5. Eventually work on a **C, C++, and C#** implementation of the backend REST APIs

The goal of this project is to get hands on experience with all the different 
technologies specified. 

# Structure


<table>
    <tr>
        <th>Directory</th>
        <th>Web Framework</th>
        <th>Frontend Framework</th>
        <th>CSS Library</th>
    </tr>
    <tr>
        <th>./Django/</th>
        <th>Django</th>
        <th>Vue</th>
        <th>Material</th>
    </tr>
    <tr>
        <th>./FastAPI/</th>
        <th>FastAPI</th>
        <th>Angular</th>
        <th>Tailwind + DaisyUI</th>
    </tr>
    <tr>
        <th>./Flask/</th>
        <th>Flask</th>
        <th>React</th>
        <th>Bootstrap</th>
    </tr>
</table>
<br>

<table>
    <tr>
        <th>-</th>
        <th>Backend</th>
        <th>Frontend</th>
    </tr>
    <tr>
        <th>Language</th>
        <th>Python</th>
        <th>TypeScript</th>
    </tr>
    <tr>
        <th>Formatter</th>
        <th>Ruff</th>
        <th>Prettier</th>
    </tr>
</table>
