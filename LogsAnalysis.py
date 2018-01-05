import psycopg2


def dbquery(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_to_screen(title, results, string):
    print title
    for i in results:
        print string


def answer_one():
    query1 = "select title, popular from popular_articles limit 3;"
    results1 = dbquery(query1)
    print '\nTop Three Articles: \n'
    for r in results1:
        print '"' + str(r[0]) + '" --- ' + str(r[1]) + ' views.'


def answer_two():
    query2 = "select name, pop_auth from popular_authors;"
    results2 = dbquery(query2)
    print '\nMost Popular Authors of all Time: \n'
    for r in results2:
        print str(r[0]) + ' --- ' + str(r[1]) + ' views.'


def answer_three():
    query3 = "select day, percent from v_errors_answer"
    results3 = dbquery(query3)
    print '\nDays with Errors Greater than One Percent: \n'
    for r in results3:
        print str(r[0].strftime('%B %d, %Y')) + ' --- ' + \
            str(round(r[1]*100, 2)) + '% errors'


def write_to_file():
    f = open("Answers.txt", "w+")
    f.write("Top Three Arcticles:\n")
    query1 = "select title, popular from popular_articles limit 3;"
    results1 = dbquery(query1)
    for r in results1:
        f.write('\n"' + str(r[0]) + '" --- ' + str(r[1]) + ' views.')
    f.write("\n\nMost Popular Authors of all Time:\n")
    query2 = "select name, pop_auth from popular_authors;"
    results2 = dbquery(query2)
    for r in results2:
        f.write('\n' + str(r[0]) + ' --- ' + str(r[1]) + ' views.')
    f.write("\n\nDays with Errors Greater than One Percent:\n")
    query3 = "select day, percent from v_errors_answer"
    results3 = dbquery(query3)
    for r in results3:
        f.write('\n' + str(r[0].strftime('%B %d, %Y')) + ' --- ' +
                str(round(r[1]*100, 2)) + '% errors')

if __name__ == "__main__":
    answer_one()
    answer_two()
    answer_three()
    write_to_file()
