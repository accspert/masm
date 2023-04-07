from django.shortcuts import render
from django.utils.safestring import mark_safe
import calendar
from calendar import HTMLCalendar
from datetime import datetime, date


class CourseCalendar(HTMLCalendar):
    def __init__(self, courses):
        self.cssclass_month = "table table-responsive"
        super().__init__()
        self.courses = courses

    def formatday(self, day, weekday):
        try:

            if day != 0:
                cssclass = self.cssclasses[weekday]
                if date.today() == datetime.now().date().replace(day=day):
                    cssclass += ' today'
                body = []
                for course in self.courses:
                    if course.day_of_week == calendar.day_name[weekday]:
                        body.append(f'<li>{course.course_name} ({course.start_time.strftime("%H:%M")} - {course.end_time.strftime("%H:%M")})</li>')
                if day == datetime.now().day:
                    return f'<td class="{cssclass}"><span class="date today">{day}</span><ul class="events">{"".join(body)}</ul></td>'
                return f'<td class="{cssclass}"><span class="date">{day}</span><ul class="events">{"".join(body)}</ul></td>'

        except Exception as e:
            # day was not found f.ex. day 31 for month XY
            print(e)
            return ""

        return '<td class="noday">&nbsp;</td>'

    def formatweek(self, theweek):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday)
        return f'<tr>{week}</tr>'

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super().formatmonth(year, month)