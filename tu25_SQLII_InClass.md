## Further SQL Queries

### 1. Introduction

Blah

We’ll be using 2 databases today, `rexon_metals.db` and a new database, `weather_stations.db`

-  `rexon_metals.db` - 3 tables: CUSTOMER. CUSTOMER_ORDER, PRODUCT
- weather_stations.db - A single table: STATION_DATA

### 2. More WHERE Clause Use

#### WHERE on text  data

The following should make sense to you (run it anyway, just to confirm).

```sqlite
SELECT *  
FROM customer
WHERE state == "TX" ;
```

No surprise there. But what if we wanted all the rows in which part of a string variable matched a pattern? To do this, we can use the `LIKE` keyword with a text string containing one or both of the wildcards “%” or “_”. The percent sign is a wildcard that matches any number of characters, and the underscore matches any single character. So

* “”%“” - matches, for example, “hello”, “h”, “World”, or “yada123blah456yada”
* “_” - matches, for example, “a”, “K”, “1” but **not** “apple”, “King”, or “11”

Perhaps the name of the company we want to look at is on the tip of our tongue, but we’re pretty sure it starts with “R”. Select records where the customer name starts with “R”. We could make a query like this

```sqlite
SELECT * 
FROM customer
WHERE name LIKE "R%";
```

Or perhaps we want to search in a fairly tight geographical region. You could filter on the first three digits of the ZIP code.

```sqlite
SELECT * 
FROM customer
WHERE CAST(zip AS TEXT) LIKE '750%';
```

Finally, if we wanted all the weather records in which the 2^nd^ letter of the `report_code` was “F”, we could do this.

```sqlite
SELECT * 
FROM STATION_DATA
WHERE report_code LIKE '_F%';
```

#### WHERE Clauses with Booleans

- Introduction to filtering with boolean data regarding weather conditions.
- **Example Query**: Select weather data where it was foggy but not raining.

```sqlite
SELECT * FROM station_data WHERE fog = 1 AND rain = 0;
```

####  Using BETWEEN, AND, OR, and IN with WHERE

- Discuss the use of these operators to refine query results in both databases.
- **Example Query for Products**: Select products within a certain price range.

```sqlite
SELECT * FROM product
WHERE price BETWEEN 100 AND 200;
```

- **Example Query for Weather**: Select station data from specific months when either rain or hail was reported.

```sqlite
SELECT * FROM station_data
WHERE month IN (4, 5) AND (rain = 1 OR hail = 1);
```

#### The BYs for WHERE

#####  GROUP BY

- Explain grouping results by one or more columns.
- **Example Query for STATION_DATA**: Group by year and calculate average temperature.

```sqlite
SELECT year, AVG(temperature) AS ave_temp
FROM station_data
GROUP BY year;
```

##### ORDER BY

- How to sort query results.
- **Example Query for Weather**: Order station data by temperature in descending order.

```sqlite
SELECT * FROM station_data
ORDER BY temperature DESC;
```

### 3. CASE

- Use of `CASE` for conditional expressions in SQL queries.
- **Example Query for Weather**: Categorize days based on temperature.

```sqlite
SELECT station_number, temperature,
CASE 
    WHEN temperature > 80 THEN 'Hot'
    WHEN temperature BETWEEN 50 AND 80 THEN 'Mild'
    ELSE 'Cold'
END AS weather_condition
FROM station_data;
```

### 4. ALIASES

#### Table Aliases

A table alias is a temporary name assigned to a table in a SQL query. The alias is used for the duration of the query and does not affect the table's name outside of that query.

#### Why Use Table Aliases?

1. **Simplification**: When table names are long or complex, aliases can simplify their references in the query.
2. **Clarification**: In queries involving multiple tables, aliases help clarify which columns are coming from which tables.
3. **Necessity**: In self-joins, where a table joins to itself, aliases are necessary to distinguish the different instances of the table.

#### Syntax

The syntax to define a table alias is straightforward. After stating the table name, you place the keyword `AS` followed by the alias name. The `AS` keyword is optional but can make the query clearer. Here’s the general syntax:

```sqlite
SELECT column1, column2
FROM table_name AS alias_name
WHERE alias_name.column1 = condition;
```



### Using Column Aliases

You can also create aliases for columns to either shorten their names or to give more descriptive names to columns in the result set.

#### Syntax

The syntax for column aliases follows a similar pattern. After the column name, you place the `AS` keyword followed by the alias name for the column. Here’s how you might do it:

```sqlite
SELECT column_name AS alias_name FROM table_name;
```

#### Example

```sqlite
SELECT description AS product_description, price AS product_price
FROM product;
```

In this example, `product_description` and `product_price` are aliases for the `description` and `price` columns from the `product` table, making the output more understandable.

### 5. JOINs

#### Explanation of JOIN Types

- **INNER JOIN**: Returns rows when there is a match in both tables.
- **LEFT JOIN**: Returns all rows from the left table, and the matched rows from the right table.
- **RIGHT JOIN** and **FULL JOIN**: These types of joins are not supported directly by SQLite but can be emulated using specific queries.

#### Example Queries

##### INNER JOIN

- **Purpose**: To find all orders along with their corresponding product descriptions and customer information.
- **Example Query**:

```sqlite
SELECT c.customer_name, p.description, p.price
FROM customer_order co
INNER JOIN customer c ON co.customer_id = c.customer_id
INNER JOIN product p ON co.product_id = p.product_id;
```

##### LEFT JOIN

- **Purpose**: List all customers and their orders, including those who have not placed any orders.
- **Example Query**:

```sqlite
SELECT c.customer_name, p.description, p.price
FROM customer c
LEFT JOIN customer_order co ON c.customer_id = co.customer_id
LEFT JOIN product p ON co.product_id = p.product_id;
```

#### Aggregating Data with JOINs

- **Purpose**: Calculate the total amount spent by each customer.
- **Example Query**:

```sqlite
SELECT c.customer_name, SUM(p.price) AS total_spent
FROM customer c
JOIN customer_order co ON c.customer_id = co.customer_id
JOIN product p ON co.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
```

#### Using Aliases with JOIN

##### Example Without Aliases

Consider a query on the `rexon_metals.db` database where we need to join the `customer`, `product`, and `customer_order` tables:

```sqlite
SELECT customer.customer_name, product.description, product.price
FROM customer_order
JOIN customer ON customer_order.customer_id = customer.customer_id
JOIN product ON customer_order.product_id = product.product_id;
```

##### Example With Aliases

Here’s the same query using aliases to make it more concise:

```sqlite
SELECT c.customer_name, p.description, p.price
FROM customer_order co
JOIN customer c ON co.customer_id = c.customer_id
JOIN product p ON co.product_id = p.product_id;
```

In this example, `co` is an alias for `customer_order`, `c` for `customer`, and `p` for `product`. These aliases are used to reference the respective tables in the `JOIN` conditions and when selecting columns.

### 6. Putting It All Together

- Since the databases cannot be joined, this section will focus on more complex queries within each database independently.
- **Example Query for Weather**:

```sqlite
SELECT station_number, COUNT(*) AS days_with_precipitation,
CASE
    WHEN SUM(rain) > 10 THEN 'Wet Station'
    ELSE 'Dry Station'
END AS station_type
FROM station_data
WHERE rain = 1 OR hail = 1
GROUP BY station_number
ORDER BY days_with_precipitation DESC;
```

### 7. Summary

- Recap of the topics covered.
- Tips for further learning and troubleshooting common issues.