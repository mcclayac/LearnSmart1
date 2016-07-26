__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/24/16'
__revision__ = '$'
__revision_date__ = '$'


def dateTime1():
    from datetime import date

    now = date.today()
    print("now: ", now)

    print("' strfttime forat:", now.strftime(('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')))

    birthday = date(1969, 3, 29)
    age = now - birthday
    print("age is days: ", age.days)
    print("age is years: ", age)

