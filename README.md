
# The Phone Bill Calculator!

This is my solution for the proposed challenge:
Implement an application that receives call detail records
and calculates monthly bills for a given telephone number.

# How to run and test this project:
1. Create a **python 3** virtualenv envoirement.
2. Create a **MySQL** database.
3. Rename **settings.sample.ini** to **settings.ini** and configure it as you need (set your database credentials and parameters, debug status,secret key and allowed hosts).
4. Install the project requirements using this command: **pip install -r requirements**.
5. Apply the migrations to the database: **python manage.py migrate**
6. Run the server: **python manage.py runserver**
7.To test this project run the following command: **python manage.py test**
  
# This project was created and tested using the following softwares:
* **OS:** Ubuntu 16.04
* **IDE:** Pycharm 2018 Professional Edition

# Technologies used to build this project:
* **Python 3.6 -** Project Language.
* **Django -** Python Web framework.
* **Django Rest -** Rest Full Framework for Django.
* **Coverage -** Code coverage testing for Python.
* **Core API -** Format-independent Document Object Model for representing Web APIs.
* **Model Mommy -** Smart way to create fixtures for testing in Django.
* **MySQL -** Relational database.
* **Protobuf -** Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.
* **Decouple -** Helps you to organize your settings so that you can change parameters without having to redeploy your app.
* **Pytz -** This library allows accurate and cross platform timezone calculations using Python.

# APIs routes available in this project:
1. **/bills/api/v1/bill/{source_number} (Get):**
   * Returns a telephone bill of a given number at a give reference period.
     * To pass a reference month and a reference year, user this pattern: month={month}&year={year}

Examples:
    
    /bills/api/v1/bill/99988526423?month=9?year=2018
    /bills/api/v1/bill/99988526423

2. /calls/api/v1/callrecord/ (Post):
   * Creates a new Call record.
   * Parameters
     * timestamp -> string in formats YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].
     * call_type -> integer (Use 1 for 'start' calls records and 2 for 'end' calls records).
     * call_id   -> integer (Unique ID for each call record pair)
     * source    -> string in format AAXXXXXXXXX, where AA is the area code and XXXXXXXXX is the phone number. The phone number is composed of 8 or 9 digits.
     * destination -> string inf format AAXXXXXXXXX, where AA is the area code and XXXXXXXXX is the phone number. The phone number is composed of 8 or 9 digits.

Examples:

1. Call Start Record

```
{
    "id": 36,
    "timestamp": "2017-12-12T12:00:00",
    "call_type": 1,
    "call_id": 12,
    "source": "99988526423",
    "destination": "9993468278"
}
```

2. Call End Record

```
{
    "id": 37,
    "timestamp": "2017-12-12T00:01:00",
    "call_type": 2,
    "call_id": 12,
    "source": "",
    "destination": ""
}
```

* You can also find the API documentation by accessing the application's landing page!

