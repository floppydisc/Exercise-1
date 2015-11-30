# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
Exercises for using the datetime and the calendar module
'''

# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.
import calendar as cal

import datetime as date
def last_of_month(dt):
    return date.date(dt.year, dt.month, cal.monthrange(dt.year, dt.month)[1])
    # -> as calender.monthrange(datetime) would return a list
    # of the first weekday and the number of days of the submitted month,
    # we just need the the second element of (0,31) ect.
#print last_of_month(date.date.today())
print last_of_month(date.date(2007, 5, 31))
print last_of_month(date.date(2007, 5, 23))

# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.
def feed_the_gremlin(time):
    return not(date.time(0,0) <= time < date.time(6,30))
    #python will check if the submitted time (not) is in the range
    # where the first datetime is start and the third datetime is end.
    #a little bit more complicated would be if start > end - eg 23.00 - 06.00
    # then we'd have to return (start <= time or time <= end)
#print feed_the_gremlin(date.datetime.now().time())
print feed_the_gremlin(date.time(6, 30))

# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'
def how_long(dt, ref):
    future = (ref>dt)
    if not(future): #switch dates to get positive difference
        tmp = ref
        ref = dt
        dt = tmp
    d = divmod((ref-dt).total_seconds(),86400)  # days
    h = divmod(d[1],3600)  # hours
    m = divmod(h[1],60)  # minutes
    s = m[1]  # seconds

    diff = "{0:02d} days, {1:02d} minutes, {2:02d} seconds".format(int(d[0]),int(m[0]),int(s))
    
    return diff+" "+("until "+str(ref) if future else "since "+str(dt))
print how_long(date.datetime.now(), date.datetime.now())

d1 = date.datetime(2000, 1, 1, 12, 34, 56)
d2 = date.datetime(1985, 4, 23, 12, 0, 0)

print "5366 days, 34 minutes, 56 seconds since 1985-04-23 12:00:00"
print how_long(d1, d2) 

print "5366 days, 34 minutes, 56 seconds until 2000-01-01 12:34:56"
print how_long(d2, d1)
