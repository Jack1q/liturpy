# Definitely not finished yet

import datetime

# Day Enums
class DayOfWeek:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class Month:
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class LiturgicalCalendar:

    def __init__(self, year:int):
        self.year = year

        # Calculated dates
        self.epiphany_date = self.calculate_epiphany_date()
        self.date_of_easter = self.calculate_date_of_easter()
        self.start_of_advent = self.calculate_start_of_advent()
        

        # Ordinary Time
        self.first_sunday_OT = self.baptism_of_the_lord_date = self.calculate_baptism_of_the_lord()
        self.second_sunday_OT = self.first_sunday_OT + datetime.timedelta(weeks=1)


        # Lent + Easter related calculations
        self.ash_wednesday = self.date_of_easter - datetime.timedelta(days=46)
        self.first_sunday_lent = self.ash_wednesday + datetime.timedelta(days=4)

        self.palm_sunday = self.date_of_easter - datetime.timedelta(days=7)
        self.holy_thursday = self.date_of_easter - datetime.timedelta(days=3)
        self.good_friday = self.holy_thursday + datetime.timedelta(days=1)
        self.easter_vigil = self.good_friday + datetime.timedelta(days=1)
        self.divine_mercy_sunday = self.date_of_easter + datetime.timedelta(weeks=1) 
        
        self.ascension_thursday = self.date_of_easter + datetime.timedelta(days=39)
        self.pentecost_sunday = self.ascension_thursday + datetime.timedelta(days=10)
        self.trinity_sunday = self.pentecost_sunday + datetime.timedelta(weeks=1)




        # Hard-coded dates
        # January
        self.solemnity_of_mary = datetime.date(year=self.year, month=Month.JANUARY, day=1)
        self.conversion_of_st_paul = datetime.date(year=self.year, month=Month.JANUARY, day=25)
        # February
        self.presentation_of_the_lord = datetime.date(year=self.year, month=Month.FEBRUARY, day=2)
        self.chair_of_st_peter_feast = datetime.date(self.year, Month.FEBRUARY, 22)
        # March
        self.joseph_feast = datetime.date(self.year, Month.MARCH, 19)
        self.annunciation = datetime.date(self.year, Month.MARCH, 25)
        # May
        self.philip_and_james_feast = datetime.date(self.year, Month.MAY, 3)
        self.matthias_feast = datetime.date(self.year, Month.MAY, 14)
        self.visitation = datetime.date(self.year, Month.MAY, 31)
        # June
        self.justin_martyr_feast = datetime.date(self.year, Month.JUNE, 1)
        
















    
    def get_date_of_easter(self):
        return self.date_of_easter

    def calculate_date_of_easter(self):
        a = self.year % 19
        b = self.year // 100
        c = self.year % 100
        h = (19 * a + b - b // 4 - (b - (b + 8) // 25 + 1) // 3 + 15) % 30
        l = (32 + 2 * b % 4 + 2 * c // 4 - h - c % 4) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return datetime.date(year=self.year, month=month, day=day)
    
    def calculate_start_of_advent(self):
        nov_30 = datetime.date(self.year, 11, 30)
        week_day_value = nov_30.weekday()
        if week_day_value >= DayOfWeek.THURSDAY:
            while nov_30.weekday() != DayOfWeek.SUNDAY:
                nov_30 += datetime.timedelta(days=1)
        else:
            while nov_30.weekday() != DayOfWeek.SUNDAY:
                nov_30 -= datetime.timedelta(days=1)
        return nov_30
    
    # Epiphany sunday 
    def calculate_epiphany_date(self):
        d = datetime.date(self.year - 1, 12, 25) + datetime.timedelta(weeks=1)
        while d.weekday() != DayOfWeek.SUNDAY:
            d += datetime.timedelta(days=1)
        return d
    
    # First sunday in ordinary time = Baptism sunday
    def calculate_baptism_of_the_lord(self):
        return self.epiphany_date + datetime.timedelta(weeks=1)
    
    
# print(LiturgicalCalendar(2020).calculate_epiphany_date())
        