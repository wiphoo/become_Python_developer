## Timezone
ref: https://docs.python.org/3.7/library/datetime.html?highlight=timezone#timezone-objects

#### Create Bangkok and Greenwich timezones

    import datetime
    
    bkk_timezone = datetime.timezone(datetime.timedelta(hours=7),name='Asia/Bangkok')
    greenwich_timezone = datetime.timezone(datetime.timedelta(hours=0),name='Europe/Greenwich')

    bkk_thailand = datetime.datetime.now(tz=bkk_timezone)
    greenwich_uk = datetime.datetime.now(tz=greenwich_timezone)


#### Create Tokyo timezone.

    ...
