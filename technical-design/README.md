# Technical Design
This document outlines the technical architecture and implementation strategy for Big Bang Brokers, a full-stack web application designed for selling planets to clients. It details the technologies, frameworks, and data storage solutions that will be used to support a strong and maintainable system.


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
  Official SQLite documentation: [https://www.sqlite.org/docs.html]
    
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
  - Official SQLite documentation: [https://www.sqlite.org/docs.html] <br> <br>
**sqlite3** <br>
  - Python’s sqlite3 module will allow our Flask application to read and write to the database.
  - We will use SQL queries to insert users, store products, update carts, and process orders.
  - Official sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html
    
  ## Entity Relationship Diagram

  ## Entity/Field Descriptions
  #### 1. User
  | Property     | Type | Default       | Nullable | Relationship | Notes                                      |
  |:-------------| :--- |:--------------| :--- | :--- |:-------------------------------------------|
  | **UserID**   | INT | AUTOINCREMENT | No | PK | Unique identification number for the user. |
  | **Username** | VARCHAR(50) |               | No | | Unique username used to login.             |
  | **Email**    | VARCHAR(100) |               | No | | User's email.                              |
  | **Password** | VARCHAR(255) |               | No | | Unique password used to login.             |
  | **IsAdmin**  | BOOLEAN | False         | No | | `True` if the user is an admin.            |

  <br>

  #### 2. Planet
  | Property | Type | Default | Nullable | Relationship | Notes                                              |
  | :--- | :--- | :--- | :--- | :--- |:---------------------------------------------------|
  | **PlanetID** | INT | AUTOINCREMENT | No | PK | Unique identification number for the planet.       |
  | **Name** | VARCHAR(50) | | No | | Name of the planet.                                |
  | **Description** | TEXT | | Yes | | Short description of the planet.                   |
  | **Price** | DECIMAL(10, 2) | | No | | Price of the planet. (e.g. 250 = 250B)             |
  | **ImageURL** | VARCHAR(255) | | Yes | | THe file name used to display the planet's picture |
  | **IsSold** | BOOLEAN | False | No | | `True` if the planet has been purchased.           |

  <br>

  #### 3. Cart
  | Property | Type | Default | Nullable | Relationship | Notes                                               |
  | :--- | :--- | :--- | :--- | :--- |:----------------------------------------------------|
  | **CartID** | INT | AUTOINCREMENT | No | PK | Unique identification number for the shopping cart. |
  | **UserID** | INT | | No | FK (User.UserID) | Links the cart to a specific user.                  |
  
  <br>
  
  #### 4. CartItem
  | Property | Type | Default | Nullable | Relationship | Notes                                                 |
  | :--- | :--- | :--- | :--- | :--- |:------------------------------------------------------|
  | **CartItemID** | INT | AUTOINCREMENT | No | PK | Unique identification number for items inside a cart. |
  | **CartID** | INT | | No | FK (Cart.CartID) | The cart this item belongs to.                        |
  | **PlanetID** | INT | | No | FK (Planet.PlanetID) | The planet being added to the cart.                   |
  
  <br>

  #### 5. OrderAddress
  | Property | Type | Default | Nullable | Relationship | Notes                                  |
  | :--- | :--- | :--- | :--- | :--- |:---------------------------------------|
  | **AddressID** | INT | AUTOINCREMENT | No | PK | Unique identifier for a saved address. |
  | **FullName** | VARCHAR(100) | | No | | Name of the recipient/biller.          |
  | **PhoneNumber** | VARCHAR(20) | | Yes | | Contact number.                        |
  | **Email** | VARCHAR(100) | | No | | Email for order updates.               |
  | **AddressLine1** | VARCHAR(255) | | No | | Street Address.                        |
  | **AddressLine2** | VARCHAR(255) | | Yes | | Street Address (optional).             |
  | **ZipCode** | VARCHAR(20) | | No | | Zip Code.                              |
  
  <br>
  
  #### 6. Order
  | Property | Type | Default       | Nullable | Relationship | Notes                                                 |
  | :--- | :--- |:--------------| :--- | :--- |:------------------------------------------------------|
  | **OrderID** | INT | AUTOINCREMENT | No | PK | Unique identification number for the completed order. |
  | **UserID** | INT |               | No | FK (User.UserID) | The user who placed the order.                        |
  | **BillingAddressID** | INT |               | No | FK (OrderAddress.AddressID) | Link to billing details.                              |
  | **ShippingAddressID** | INT |               | No | FK (OrderAddress.AddressID) | Link to shipping details.                             |
  | **OrderDate** | DATETIME | REAL          | No | | Timestamp when the order was placed.                  |
  | **ShippingCost** | DECIMAL(10, 2) |               | No | | Cost based on shipping type selected.                 |
  | **Tax** | DECIMAL(10, 2) |               | No | | Calculated tax amount (6%).                           |
  | **TotalAmount** | DECIMAL(10, 2) |               | No | | Final amount due (Subtotal + Tax + Shipping).         |
  | **OrderStatus** | VARCHAR(50) | "Processing"  | No | | E.g., Processing, Shipped, Delivered.                 |
  
  <br>

  #### 7. OrderItem
  | Property | Type | Default       | Nullable | Relationship | Notes                                                                      |
  | :--- | :--- |:--------------| :--- | :--- |:---------------------------------------------------------------------------|
  | **OrderItemID** | INT | AUTOINCREMENT | No | PK | Unique identification number for a line item in an order.                  |
  | **OrderID** | INT |               | No | FK (Order.OrderID) | The order this item belongs to.                                            |
  | **PlanetID** | INT |               | No | FK (Planet.PlanetID) | The planet purchased.                                                      |
  | **PriceAtPurchase** | DECIMAL(10, 2) |               | No | | Copy of price at time of sale (in Billions) (For use in the sales report). |
  ## Data Examples

  ## Authentication and Authorization Plan

  ## Coding Style Guide

  ## Technical Design Presentation
  
  

