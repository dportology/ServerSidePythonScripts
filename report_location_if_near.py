__author__ = 'dportology'
import MySQLdb
from gcm import *


db = MySQLdb.connect(host="localhost", user="root", passwd="9872598725", db="testDB")
print 'MySQL Connection Sucessful!'

cur = db.cursor()

#need to add relevant teams as well
sqlstmt = "SELECT player_ID, longitude, latitude FROM player;"

cur.execute(sqlstmt)

numrows = int(cur.rowcount)

# will hold all latitude and longitudes as well as player ID
my_list = []

# loop to populate my_list
for x in range(0,numrows):
    row = cur.fetchone()
    my_list.append([row[0],row[1], row[2]])

for x in my_list:
    print x

# for every coordinate set in my_list, compare with every other, and if there are two that are close by,
# send the appropriate user a notification

for x in my_list:
    if x[1] != None:
        for y in my_list:
            if y[1] != None and x[0] != y[0]:
                if (abs((float(x[1]) - float(y[1]))) < 0.0004) and (abs((float(x[2]) - float(y[2]))) < 0.0004):
                    # if this is the case, need to send a notification to this player
                    print 'we have a match'
                    print float(x[1])
                    print float(y[1])
		    gcm = GCM("AIzaSyB3i92OH_E1BkLP2u0Rt92HV4Q40RM3m2U")
                    data = {'the_message': 'You are a total loser!', 'param2': 'value2'}
                    reg_id = 'phone reg-id - very long'
                    #gcm.plaintext_request(registration_id=reg_id, data=data)






