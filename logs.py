#!/usr/bin/env python2

import datetime
import psycopg2
print '\n\n'
print '##################################'
print '##################################'
print '##                              ##'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print '## Welcome to log analysis tool ##'
print '##                              ##'
print '##################################'
print '##################################'
print '\n\n'


# Function to option database connection and display status of connection.
def db_connect():
<<<<<<< HEAD
  try:
      print ("[-] Connecting to database...")
      db = psycopg2.connect(database = "news")
      c = db.cursor()
      print ("[x] Connected.")
      return db, c
  except:
      print ("[x] Connection to database failed. Exiting...")
        
=======
    try:
        print ("[-] Connecting to database...")
        db = psycopg2.connect(database="news")
        c = db.cursor()
        print ("[x] Connected.")
        return db, c
    except (Exception, psycopg2.DatabaseError) as error:
        print ("[x] Connection to database failed. Exiting...")


# Function to send database query to database and close database connection.
# Note: db.close() must take place before the return statement or function
# will exit before connection has been closed.
>>>>>>> 599abc654c20eb9d25d1213edbcd5eaa76758102
def db_query(query):
    db, c = db_connect()
    print ("[-] Sending query...")
    c.execute(query)
    print ("[x] Query complete.")
    qresults = c.fetchall()
    db.close()
    print ("[x] Databse connection closed.")
    return qresults


# Function to loop through results of db query and display in a list
# This function also passes the query to the db_query function for execution
def display_results(query, selection):
    query_results = db_query(query)
    print "[-] Displaying results..."
    if (selection == '1') or (selection == '2'):
        for c, results in enumerate(query_results):
            views = (str(results[1]))
            views = views[:-1] + " views"
            c = str(c+1) + ". "
            print (c + results[0] + " - " + views)
    if selection == '3':
        for c, results in enumerate(query_results):
            errors = (str(results[1]))
            errors = errors[:-1] + "% error rate."
            c = str(c+1) + ". "
            print (c + "On " + results[0] + " there was " + errors)


# Create menu and wait for user input
menu = {}
menu['1'] = "Display top 3 most popular articles."
menu['2'] = "Display most popular authors."
menu['3'] = "Display days with a high number of errors."
menu['4'] = "Exit"
while True:
    options = menu.keys()
    options.sort()
    print "\nMenu:"
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("\nPlease Select: ")
# If user selects first option then prepare DB query to retrieve
# top 3 most popular articles and pass to display_results
    if selection == '1':
        print "\n[-] 1. Retrieving top 3 most popular articles..."
        q = ("SELECT articles.title, COUNT(*) as hits "
             "FROM articles INNER JOIN log ON log.path "
             "LIKE CONCAT('%', articles.slug, '%') "
             "WHERE log.status = '200 OK' GROUP BY "
             "articles.title, log.path ORDER BY hits DESC LIMIT 3")
        display_results(q, selection)
# If user selects second option then prepare DB query to retrieve
# most popular authors and pass to display_results
    elif selection == '2':
        print "\n[-] 2. Retrieving most popular authors..."
        q = ("SELECT authors.name, COUNT(*) AS hits from ARTICLES INNER "
             "JOIN authors ON articles.author = authors.id "
             "INNER JOIN log ON log.path "
             "LIKE CONCAT('%', articles.slug, '%') "
             "WHERE log.status = '200 OK' "
             "GROUP BY authors.name ORDER BY hits DESC")
        display_results(q, selection)
# If user selects third option then prepare DB query to retrieve
# days with high errors and pass to display_results
    elif selection == '3':
        print "\n[-] 3. listing bad error days..."
        q = ("SELECT day, perc FROM ("
             "SELECT day, ROUND((SUM(requests)/(SELECT COUNT(*) "
             "FROM log WHERE "
             "SUBSTRING(cast(log.time as text), 0, 11) = day) * 100), 2) AS "
             "perc FROM (select substring(cast(log.time as text), 0, 11) "
             "AS day, COUNT(*) AS requests FROM log WHERE status LIKE '%404%' "
             "GROUP BY day) AS log_percentage GROUP BY day  "
             "ORDER BY perc DESC) as final_query WHERE perc >= 1")
        display_results(q, selection)
# If user selects fourth option then exit
    elif selection == '4':
        print "\n[-] Closing.... \n\n"
        break
# Display error if user does not enter 1, 2, 3 or 4
    else:
        print "Invalid selection."
