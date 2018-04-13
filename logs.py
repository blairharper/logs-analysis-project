# 1. What are the most popular three articles of all time? Which articles have been accessed the most? 
# Present this information as a sorted list with the most popular article at the top.

import datetime
import psycopg2
print '\n\n'
print '##################################'
print '##################################'
print '##                              ##'
print '## Welcome to log analysis tool ##'
print '##                              ##'
print '##################################'
print '##################################'
print '\n\n'

def db_connect():
    try:
        print ("[-] Connecting to database...")
        db = psycopg2.connect(database = "news")
        c = db.cursor()
        print ("[x] Connected.")
        return db, c
    except:
        print ("[x] Connection to database failed. Exiting...")
        
def db_query(query):
    db, c = db_connect()
    print ("[-] Sending query...")
    c.execute(query)
    print ("[x] Query complete.")
    qresults = c.fetchall()
    db.close()
    print ("[x] Databse connection closed.")
    return qresults


# def :
#     qresults = db_query(query)
#     print ("[x] Displaying results...\n")
#     print (qresults[1])
#     for index, results in enumerate(qresults[0]):
#         print ( "\t", index+1, "-", results[0],
#                 "\t - ", str(results[1]), "views")

def display_results(query):
    query_results = db_query(query)
    print "[-] Displaying results..."
    print query_results
 

menu = {}
menu['1']="Display top 3 most popular articles." 
menu['2']="..."
menu['3']="...."
menu['4']="Exit"
while True: 
    options=menu.keys()
    options.sort()
    print "\nMenu:"
    for entry in options: 
        print entry, menu[entry]
        
    selection=raw_input("\nPlease Select: ") 
    if selection =='1': 
      print "\n[-] Option 1 selected, preparing query to retrieve top 3 most popular articles..."
      q = ("SELECT articles.title, COUNT(*) as hits "
           "FROM articles INNER JOIN log ON log.path "
           "LIKE CONCAT('%', articles.slug, '%') "
           "WHERE log.status = '200 OK' GROUP BY "
           "articles.title, log.path ORDER BY hits DESC LIMIT 3")
      display_results(q)
    elif selection == '2': 
      print "\n[x] Function not yet written \n\n"
    elif selection == '3':
      print "\n[x] Function not yet written \n\n" 
    elif selection == '4': 
      print "\n[-] Closing.... \n\n"   
      break
    else: 
      print "Invalid selection." 