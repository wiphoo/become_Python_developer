## Date
ref: https://docs.python.org/3/library/datetime.html#datetime.date

#### Convert date from string to date object. What is date object?

##### ISO format YYYY-MM-DD i.e. 2022-01-04

    from datetime import date
    date.fromisoformat('2021-01-01')

##### Today

    date.today()
    date(2022, 1, 4)    

#### Calculate how old are you (in days, seconds).

    my_birthday = date.fromisoformat('1999-01-01')

#### Counting days to my birthday.

    this_year_birthday = date(date.today().year, 11, 11)

#### Determine weekday or weekend

    date.today().weekday()
    date(2022, 1, 2).weekday()
