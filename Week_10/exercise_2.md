## Date/Time
ref: https://docs.python.org/3/library/datetime.html#datetime-objects


#### Convert to datetime object.

    import datetime
    datetime.datetime(year=2021, month=1, day=4, hour=19, minute=0 )

###### today

    datetime.today()


###### convert any date/time format

    datetime.datetime.strptime('3 Jan 2022 10:00AM', 
    '%w %b %Y %I:%M%p')

    datetime.datetime.strptime('3 Jan 2022 10:00PM', '%w %b %Y %I:%M%p')

    datetime.datetime.strptime('2022-01-01 22:00:01', '%Y-%m-%d %H:%M:%S')

    
