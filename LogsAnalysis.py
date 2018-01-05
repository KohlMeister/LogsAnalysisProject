#!/usr/bin/env python

import psycopg2


# Funciton to connect to database and run query
def dbquery(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Queries and prints results 1
def answer_one():
    query1 = "SELECT title, popular FROM popular_articles LIMIT 3;"
    results1 = dbquery(query1)
    print '\nTop Three Articles: \n'
    for r in results1:
        print '"' + str(r[0]) + '" --- ' + str(r[1]) + ' views.'


# Queries and prints results 2
def answer_two():
    query2 = "SELECT name, pop_auth FROM popular_authors;"
    results2 = dbquery(query2)
    print '\nMost Popular Authors of all Time: \n'
    for r in results2:
        print str(r[0]) + ' --- ' + str(r[1]) + ' views.'


# Queries and prints results 3
def answer_three():
    query3 = "SELECT day, percent FROM v_errors_answer"
    results3 = dbquery(query3)
    print '\nDays with Errors Greater than One Percent: \n'
    for r in results3:
        print str(r[0].strftime('%B %d, %Y')) + ' --- ' + \
            str(round(r[1]*100, 2)) + '% errors'


# Writes queries into txt file
def write_to_file():
    # Create a txt file
    f = open("Answers.txt", "w+")
    # Answers to question 1
    f.write("Top Three Arcticles:\n")
    query1 = "SELECT title, popular FROM popular_articles LIMIT 3;"
    results1 = dbquery(query1)
    for r in results1:
        f.write('\n"' + str(r[0]) + '" --- ' + str(r[1]) + ' views.')
    # Answers to question 2
    f.write("\n\nMost Popular Authors of all Time:\n")
    query2 = "SELECT name, pop_auth FROM popular_authors;"
    results2 = dbquery(query2)
    for r in results2:
        f.write('\n' + str(r[0]) + ' --- ' + str(r[1]) + ' views.')
    # Answers to question 3
    f.write("\n\nDays with Errors Greater than One Percent:\n")
    query3 = "SELECT day, percent FROM v_errors_answer"
    results3 = dbquery(query3)
    for r in results3:
        f.write('\n' + str(r[0].strftime('%B %d, %Y')) + ' --- ' +
                str(round(r[1]*100, 2)) + '% errors')

if __name__ == "__main__":
    answer_one()
    answer_two()
    answer_three()
    write_to_file()
