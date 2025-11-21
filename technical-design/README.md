# Technical Design
This document outlines the technical architecture and implementation strategy for Big Bang Brokers, a full-stack web application designed for selling planets online. It details the technologies, frameworks, and data storage solutions that will be used to support a strong and maintainable system.


## Table of Contents

- [Implementation Languages]()
- [Implementation Framework]()
- [Data Storage Plan]()
- [Entity Relationship Diagram]()
- [Entity/Field Descriptions]()
- [Data Examples]()
- [Database Seed Data]()
- [Authentication and Authorization Plan]()
- [Coding Style Guide]()
- [Technical Design Presentation]()

  ## Implementation Languages
**Backend:** Python <br>
- Python was chosen because our team is familiar with it and it works smoothly with the Flask framework for web development.
- Python’s syntax is beginner-friendly and allows for fast development.
- Official Python documentation can be found here: [https://docs.python.org/] <br>
  
**Frontend:** HTML & CSS <br>
- HTML and CSS will be used to build the structure and visual design of our web pages. Flask also supports HTML templates.
- Official HTML documentation: [https://developer.mozilla.org/en-US/docs/Web/HTML]
- Official CSS documentation: [https://developer.mozilla.org/en-US/docs/Web/CSS] 

**Data:** 
- **SQLite:**  
  We chose SQLite because:  
  - It is lightweight and requires no database server.  
  - All data is stored in a single file, making it easy to maintain and share.  
  - It is persistent—data remains even after the application is closed.  
  **Official SQLite documentation:** https://www.sqlite.org/docs.html
    
  ## Implementation Framework
  Our team selected Flask as our main framework. <br>
  **Flask** <br>
  - Flask is a lightweight Python web framework that requires very little configuration.
  - It allows us to easily create routes, handle forms, manage sessions, and connect to our SQL database.
  - Official Flask documentation can be found here: [https://flask.palletsprojects.com/]
  ## Data Storage Plan
  Our project will use SQLite as the database and sqlite3 library to communicate with it.
  <br>
**SQLite** <br>
  - It is lightweight and requires no database server.
  - All data is stored in a single file, making it easy to maintain and share.
  - It is persistent, data remains even after the application is closed.
  - Official SQLite documentation: [https://www.sqlite.org/docs.html] <br>
  <br>
  **sqlite3**
  - Python’s sqlite3 module will allow our Flask application to read and write to the database.
  - We will use SQL queries to insert users, store products, update carts, and process orders.
  - Official sqlite3 documentation: [https://docs.python.org/3/library/sqlite3.html]  
    
  ## Entity Relationship Diagram

  ## Entity/Field Descriptions

  ## Data Examples

  ## Authentication and Authorization Plan

  ## Coding Style Guide

  ## Technical Design Presentation
  
  

