## Mo’ sql





#### 1. Introduction

- Brief overview of the databases: `rexon_metals.db` for metal products and `weather_stations.db` for weather data.
- Setting up the SQLite environment.

#### 2. WHERE Clauses on Text Data

- Explain text-based filtering using `WHERE` in the context of product descriptions.
- **Example Query**: Select records where the product description includes "Steel".

```
sqlCopy code
SELECT * FROM product WHERE description LIKE '%Steel%';
```

#### 3. WHERE Clauses with Booleans

- Introduction to filtering with boolean data regarding weather conditions.
- **Example Query**: Select weather data where it was foggy but not raining.

```
sqlCopy code
SELECT * FROM station_data WHERE fog = 1 AND rain = 0;
```

#### 4. Using BETWEEN, AND, OR, and IN

- Discuss the use of these operators to refine query results in both databases.
- **Example Query for Products**: Select products within a certain price range.

```
sqlCopy code
SELECT * FROM product
WHERE price BETWEEN 100 AND 200;
```

- **Example Query for Weather**: Select station data from specific months when either rain or hail was reported.

```
sqlCopy code
SELECT * FROM station_data
WHERE month IN (4, 5) AND (rain = 1 OR hail = 1);
```

#### 5. GROUP BY

- Explain grouping results by one or more columns.
- **Example Query for Products**: Group products by description and calculate average price.

```
sqlCopy code
SELECT description, AVG(price) AS average_price
FROM product
GROUP BY description;
```

#### 6. ORDER BY

- How to sort query results.
- **Example Query for Weather**: Order station data by temperature in descending order.

```
sqlCopy code
SELECT * FROM station_data
ORDER BY temperature DESC;
```

#### 7. CASE

- Use of `CASE` for conditional expressions in SQL queries.
- **Example Query for Weather**: Categorize days based on temperature.

```
sqlCopy code
SELECT station_number, temperature,
CASE 
    WHEN temperature > 80 THEN 'Hot'
    WHEN temperature BETWEEN 50 AND 80 THEN 'Mild'
    ELSE 'Cold'
END AS weather_condition
FROM station_data;
```

### What is a Table Alias?

A table alias is a temporary name assigned to a table in a SQL query. The alias is used for the duration of the query and does not affect the table's name outside of that query.

### Why Use Table Aliases?

1. **Simplification**: When table names are long or complex, aliases can simplify their references in the query.
2. **Clarification**: In queries involving multiple tables, aliases help clarify which columns are coming from which tables.
3. **Necessity**: In self-joins, where a table joins to itself, aliases are necessary to distinguish the different instances of the table.

### How to Define and Use Table Aliases

#### Syntax

The syntax to define a table alias is straightforward. After stating the table name, you place the keyword `AS` followed by the alias name. The `AS` keyword is optional but can make the query clearer. Here’s the general syntax:

```
sqlCopy code
SELECT column1, column2
FROM table_name AS alias_name
WHERE alias_name.column1 = condition;
```



### Using Column Aliases

You can also create aliases for columns to either shorten their names or to give more descriptive names to columns in the result set.

#### Syntax for Column Aliases

The syntax for column aliases follows a similar pattern. After the column name, you place the `AS` keyword followed by the alias name for the column. Here’s how you might do it:

```
sqlCopy code
SELECT column_name AS alias_name FROM table_name;
```

#### Example

```
sqlCopy code
SELECT description AS product_description, price AS product_price
FROM product;
```

In this example, `product_description` and `product_price` are aliases for the `description` and `price` columns from the `product` table, making the output more understandable.

#### 8. JOINs

### JOINs within rexon_metals.db

#### Explanation of JOIN Types

- **INNER JOIN**: Returns rows when there is a match in both tables.
- **LEFT JOIN**: Returns all rows from the left table, and the matched rows from the right table.
- **RIGHT JOIN** and **FULL JOIN**: These types of joins are not supported directly by SQLite but can be emulated using specific queries.

#### Example Queries

#### Example Without Aliases

Consider a query on the `rexon_metals.db` database where we need to join the `customer`, `product`, and `customer_order` tables:

```
sqlCopy code
SELECT customer.customer_name, product.description, product.price
FROM customer_order
JOIN customer ON customer_order.customer_id = customer.customer_id
JOIN product ON customer_order.product_id = product.product_id;
```

#### Example With Aliases

Here’s the same query using aliases to make it more concise:

```
sqlCopy code
SELECT c.customer_name, p.description, p.price
FROM customer_order co
JOIN customer c ON co.customer_id = c.customer_id
JOIN product p ON co.product_id = p.product_id;
```

In this example, `co` is an alias for `customer_order`, `c` for `customer`, and `p` for `product`. These aliases are used to reference the respective tables in the `JOIN` conditions and when selecting columns.

##### 1. INNER JOIN

- **Purpose**: To find all orders along with their corresponding product descriptions and customer information.
- **Example Query**:

```
sqlCopy code
SELECT c.customer_name, p.description, p.price
FROM customer_order co
INNER JOIN customer c ON co.customer_id = c.customer_id
INNER JOIN product p ON co.product_id = p.product_id;
```

##### 2. LEFT JOIN

- **Purpose**: List all customers and their orders, including those who have not placed any orders.
- **Example Query**:

```
sqlCopy code
SELECT c.customer_name, p.description, p.price
FROM customer c
LEFT JOIN customer_order co ON c.customer_id = co.customer_id
LEFT JOIN product p ON co.product_id = p.product_id;
```

##### 3. Aggregating Data with JOINs

- **Purpose**: Calculate the total amount spent by each customer.
- **Example Query**:

```
sqlCopy code
SELECT c.customer_name, SUM(p.price) AS total_spent
FROM customer c
JOIN customer_order co ON c.customer_id = co.customer_id
JOIN product p ON co.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
```

### Using these JOINs

#### 9. Putting It All Together

- Since the databases cannot be joined, this section will focus on more complex queries within each database independently.
- **Example Query for Weather**:

```
sqlCopy code
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

#### 10. Conclusion

- Recap of the topics covered.
- Tips for further learning and troubleshooting common issues.