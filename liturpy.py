# Inspired by Romcal - I wanted to create my own that would let people easily generate any year's calendar
# Dates from https://www.usccb.org/resources/2020cal.pdf and https://www.usccb.org/resources/2021cal.pdf
# Definitely not finished yet
# Tasks:
# - Complete adding date configurations 
# - implement into a Flask web-app that gives the calendar for any month of any year


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

    JANUARY_LENGTH = 31
    FEBRUARY_LENGTH = 28
    FEBRUARY_LEAP_LENGTH = 29
    MARCH_LENGTH = 31
    APRIL_LENGTH = 30
    MAY_LENGTH = 31
    JUNE_LENGTH = 30
    JULY_LENGTH = 31
    AUGUST_LENGTH = 31
    SEPTEMBER_LENGTH = 30
    OCTOBER_LENGTH = 31
    NOVEMBER_LENGTH = 30
    DECEMBER_LENGTH = 31

class LiturgicalCalendar:

    def __init__(self, year=None):
        if year is None:
            self.year = datetime.datetime.now().year
        else: 
            self.year = year
        self.main_calendar = self.__create_calendar()
        self.__fill_calendar()
    
    def get_main_calendar(self):
        return self.main_calendar

    def __is_leap_year(self):
        return self.year % 4 == 0 if self.year % 100 != 0 else self.year % 400 == 0

    def __create_month_dict(self, month_length):
        return {str(day + 1) : [] for day in range(month_length)}

    def __create_calendar(self):
        main_calendar = { # i should definitely shorten this code lol
            '1'  : self.__create_month_dict(Month.JANUARY_LENGTH),
            '2'  : self.__create_month_dict(Month.FEBRUARY_LEAP_LENGTH if self.__is_leap_year() else Month.FEBRUARY_LENGTH),
            '3'  : self.__create_month_dict(Month.MARCH_LENGTH),
            '4'  : self.__create_month_dict(Month.APRIL_LENGTH),
            '5'  : self.__create_month_dict(Month.MAY_LENGTH),
            '6'  : self.__create_month_dict(Month.JUNE_LENGTH),
            '7'  : self.__create_month_dict(Month.JULY_LENGTH),
            '8'  : self.__create_month_dict(Month.AUGUST_LENGTH),
            '9'  : self.__create_month_dict(Month.SEPTEMBER_LENGTH),
            '10' : self.__create_month_dict(Month.OCTOBER_LENGTH),
            '11' : self.__create_month_dict(Month.NOVEMBER_LENGTH),
            '12' : self.__create_month_dict(Month.DECEMBER_LENGTH)
        }
        return main_calendar

    def __add_datetime_to_cal(self,date, description):
        self.main_calendar[str(date.month)][str(date.day)].append(description)

    # just to make hard-coding dates easier
    def __add_month_day_to_cal(self,month,day,description):
        self.main_calendar[str(month)][str(day)].append(description)

    def __fill_calendar(self):
        # Calculated dates
        #################################################################################
        self.epiphany_date = self.__calculate_epiphany_date()
        self.__add_datetime_to_cal(self.epiphany_date, ('Epiphany of Our Lord','Solemnity'))

        self.date_of_easter = self.__calculate_date_of_easter()
        self.__add_datetime_to_cal(self.date_of_easter, ('Easter Sunday', 'Solemnity'))

        self.start_of_advent = self.__calculate_start_of_advent()
        self.__add_datetime_to_cal(self.start_of_advent, ('First Sunday of Advent', 'Sunday'))
        #################################################################################

        # Ordinary Time
        #################################################################################
        self.first_sunday_OT = self.baptism_of_the_lord_date = self.__calculate_baptism_of_the_lord()
        self.__add_datetime_to_cal(self.first_sunday_OT, ('First Sunday of Ordinary Time', 'Sunday'))

        self.second_sunday_OT = self.first_sunday_OT + datetime.timedelta(weeks=1)
        self.__add_datetime_to_cal(self.second_sunday_OT, ('Second Sunday of Ordinary Time', 'Sunday'))
        #################################################################################

        # Lent + Easter related calculations
        #################################################################################
        self.ash_wednesday = self.date_of_easter - datetime.timedelta(days=46)
        self.__add_datetime_to_cal(self.ash_wednesday, ('Ash Wednesday', 'Weekday'))

        self.first_sunday_lent = self.ash_wednesday + datetime.timedelta(days=4)
        self.__add_datetime_to_cal(self.first_sunday_lent, ('First Sunday of Lent', 'Sunday'))

        self.palm_sunday = self.date_of_easter - datetime.timedelta(days=7)
        self.__add_datetime_to_cal(self.palm_sunday, ('Palm Sunday', 'Sunday'))

        self.holy_thursday = self.date_of_easter - datetime.timedelta(days=3)
        self.__add_datetime_to_cal(self.holy_thursday, ('Holy Thursday', 'Triduum'))

        self.good_friday = self.holy_thursday + datetime.timedelta(days=1)
        self.__add_datetime_to_cal(self.good_friday, ('Good Friday', 'Triduum'))

        self.easter_vigil = self.good_friday + datetime.timedelta(days=1)
        self.__add_datetime_to_cal(self.easter_vigil, ('Easter Vigil', 'Triduum'))

        self.divine_mercy_sunday = self.date_of_easter + datetime.timedelta(weeks=1) 
        self.__add_datetime_to_cal(self.divine_mercy_sunday, ('Sunday of Divine Mercy', 'Solemnity'))

        self.ascension_thursday = self.date_of_easter + datetime.timedelta(days=39)
        self.__add_datetime_to_cal(self.ascension_thursday, ('Ascension of the Lord', 'Solemnity'))

        self.pentecost_sunday = self.ascension_thursday + datetime.timedelta(days=10)
        self.__add_datetime_to_cal(self.pentecost_sunday, ('Pentecoste Sunday', 'Solemnity'))

        self.trinity_sunday = self.pentecost_sunday + datetime.timedelta(weeks=1)
        self.__add_datetime_to_cal(self.trinity_sunday, ('Trinity Sunday', 'Solemnity'))
        #################################################################################   


        # Hard-coded dates - later, place in json and load it from there
        # STILL VERY INCOMPLETE
        # January
        self.__add_month_day_to_cal('1','1',('Solemnity of Mary, Mother of God', 'Solemnity'))
        self.__add_month_day_to_cal('1','2',('Saints Basil the Great and Gregory Nazianzen, Bishops and Doctors of the Church', 'Memorial'))
        self.__add_month_day_to_cal('1','4',('Saint Elizabeth Ann Seton','Memorial'))
        self.__add_month_day_to_cal('1','5',('Saint John Neumann, Bishop','Memorial'))
        self.__add_month_day_to_cal('1','6',('Saint Andre Bessette, Religious'))
        self.__add_month_day_to_cal('1','22',('Day of Prayer for the Legal Protection of Unborn Children'))
        self.__add_month_day_to_cal('1','23',('Saint Vincent, Deacon and Martyr'))
        self.__add_month_day_to_cal('1','23',('Saint Marianne Cope'))
        self.__add_month_day_to_cal('1','25',('Conversion of Saint Paul the Apostle','Feast Day'))
        # February
        self.__add_month_day_to_cal('2','2',('Presentation of the Lord', 'Feast Day'))
        self.__add_month_day_to_cal('2','22',('Chair of Peter, the Apostle'))
        # March
        self.__add_month_day_to_cal('3','3',('Saint Katharine Drexel, Virgin'))
        self.__add_month_day_to_cal('3','19',('Joseph, Husband of Mary','Solemnity'))
        self.__add_month_day_to_cal('3','25',('Annunciation','Solemnity'))
        # May
        self.philip_and_james_feast = datetime.date(self.year, Month.MAY, 3)
        self.__add_month_day_to_cal('5','10',('Saint Damien de Veuster, Priest'))
        self.matthias_feast = datetime.date(self.year, Month.MAY, 14)
        self.__add_month_day_to_cal('5','15',('Saint Isidore'))
        self.visitation = datetime.date(self.year, Month.MAY, 31)
        # June
        self.justin_martyr_feast = datetime.date(self.year, Month.JUNE, 1)
        # July
        self.__add_month_day_to_cal('7','1',('Saint Junipero Serra, Priest'))
        self.__add_month_day_to_cal('7','5',('Saint Elizabeth of Portugal'))
        self.__add_month_day_to_cal('7','14',('Saint Kateri Tekakwitha','Memorial'))
        self.__add_month_day_to_cal('7','18',('Saint Camillus de Lellis, Priest'))
        # September
        self.__add_month_day_to_cal('9','9',('Saint Peter Claver, Priest','Memorial'))
        # October
        self.__add_month_day_to_cal('10','5',('Blessed Francis Xavier Seelos, Priest'))
        self.__add_month_day_to_cal('10','6',('Blessed Marie Rose Durocher'))
        self.__add_month_day_to_cal('10','19',('Saints John de Brebeuf and Isaac Jogues, Priests, and Companions, Martyrs','Memorial'))
        self.__add_month_day_to_cal('10','20',('Saint Paul of the Cross, Priest'))
        # November
        self.__add_month_day_to_cal('11','13',('Saint Frances Xavier Cabrini','Memorial'))
        self.__add_month_day_to_cal('11','18',('Saint Rose Philippine Duchesne'))
        self.__add_month_day_to_cal('11','23',('Blessed Miguel Agustin Pro, Priest and Martyr'))
        # December
        self.__add_month_day_to_cal('12','8',('The Immaculate Conception of the Blessed Virgin Mary','Solemnity'))
        self.__add_month_day_to_cal('12','12',('Our Lady of Guadalupe','Feast'))
        self.__add_month_day_to_cal('12','25',('Christmas','Solemnity'))
        
    
    def __get_date_of_easter(self):
        return self.date_of_easter

    def __calculate_date_of_easter(self):
        a = self.year % 19
        b = self.year // 100
        c = self.year % 100
        h = (19 * a + b - b // 4 - (b - (b + 8) // 25 + 1) // 3 + 15) % 30
        l = (32 + 2 * b % 4 + 2 * c // 4 - h - c % 4) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return datetime.date(year=self.year, month=month, day=day)
    
    def __calculate_start_of_advent(self):
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
    def __calculate_epiphany_date(self):
        d = datetime.date(self.year - 1, 12, 25) + datetime.timedelta(weeks=1)
        while d.weekday() != DayOfWeek.SUNDAY:
            d += datetime.timedelta(days=1)
        return d
    
    # First sunday in ordinary time = Baptism sunday
    def __calculate_baptism_of_the_lord(self):
        return self.epiphany_date + datetime.timedelta(weeks=1)
    
if __name__ == '__main__':
    print(LiturgicalCalendar(int(input('Enter year > '))).get_main_calendar())