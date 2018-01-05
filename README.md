# UdacityL Logs Analysis Project

Project 3 - Full Stack Web Developer

## Getting Starting

The files within this repo will query a database and return the prescribed results to the screen.
To get started, download the provided files within the reop.

### Files

* *Answers.txt*
* *LogsAnalysis.py*

## Running the Program

Prerequisits:
* Install Virtual Machine as provided by Udacity
* Download News SQL Dump to populate database

The Program:
* 6 views must be created in the database to generate the correct results. They are as follows:
```sql
  create view V_errors as
  select time::date as day, count(*) as errors 
  from log where status = '404 NOT FOUND' 
  group by day;
  ```
  ```sql 
  create view v_total as
  select time::date as day, count(*) as total 
  from log where status = '200 OK' 
  group by day;
  ```
  ```sql 
  create view v_percentages as
  select e.day, errors, total, cast(errors as decimal)/cast(total as decimal) as percent 
  from v_errors e, v_total t 
  where e.day = t.day 
  order by errors desc;
  ```
  ```sql 
  create view popular_articles as
  select a.title, count(l.path) as popular 
  from articles a, log l 
  where concat('/arcitle/', a.slug) = l.path 
  group by a.title 
  order by popular desc;
  ```
  ```sql 
  create view popular_authors as 
  select au.name, count(l.path) as pop_auth 
  from authors au, articles a, log l 
  where au.id = a.author 
  and concat('/article/', a.slug) = l.path 
  group by au.name 
  order by pop_auth desc;
  ```
  ```sql 
  create view v_errors_answer as
  select day, percent 
  from v_percentages 
  where percent > 0.01;
  ```
  
* Once the views are created, the program can be run with:
  ```python
  python LogsAnalysis.py
  ```

* Running the python file will print the results to the terminal, as well as create a text document, Answers.txt, with the results.

## Built with

* [Python 2.7](https://www.python.org) - Used for creation of .py files
* Atom 1.21.2 (https://atom.io/)

## Authors

* **Kohl Meister** - Wrote the .py file.
