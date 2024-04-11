## Introduction To SQLiteStudio and SQL

If you haven’t already dowloaded and installed SQLiteStudio, do so now. Go ahead and start SQLiteStudio. 

### Tour of SQLiteStudio

#### Panes

This is the SQLiteStudio window.

<img src="images/SQLiteStudioWindow.png" alt="SQLiteStudio Window" style="zoom:50%;" />

It is divided into a few main panes. On the left is the Databases pane. It shows any databases that you have added. Yours is probably empty at the moment (we’ll fix that soon!).

 To the right of the Databases pane are two panes, an upper one that has “Query | History” at the top, and a lower one that has “Grid view | Form view” at the top. If you look closely, you’ll see that these 2 panes are actually part of a window called “SQL editor 1” that lives within the SQLiteStudio application window.

At the bottom of everything is the Status pane. It shows how long your query took to execute or an error message if there is was an error in your code when you tried to run it. If you don’t have the status pane, you can toggle it on or off under the View menu item in the top menu bar. Note that you can also toggle other things on and off and further customize your interface.

#### Accessing a database

In order to access the data in a database, we need to “add” the database and then “connect” to it. Well use this concept of establishing a connection to a database again later, when we learn to use SQL from Python. For this exercise, we’re going to use the rexon_metals.db dataset that’s in the Canvas module. As we’ll soon see for ourselves, it contains customer, order, and product information for the fictional Rexon Metals company.

##### Add a database

To add the database, you can use either the Databases menu in the menu bar, or you can hit the little “Add a database” button above the Databases pane (the little steel barrel with a green plus sign on it). Once you add the database, it will appear in your Databases pane every time you open SQLiteStudio until you remove it.

* Databases -> Add a database
* Navigate to your database file and open it

##### Connect to the database

Now it’s time to connect to the database.  This is somewhat equivalent to reading a file into Pandas (or Excel or R or whatever); it opens the file so that you can interact with it. To connect with the database, first, select it in the database pane. Then you can either hit “Connect to the database” under the Databases menu in the top menu bar, or you can hit the little “Connect to database” button just above the Databases pane (a little plug going into an extension cord).

* Select the database in the Databases pane
* Databases -> Connect to database

The database will remain connected until you disconnect it. It will remain connected even if you quit and re-start SQLiteStudio, so you can pick up working right where you left off.

##### Looking at the database structure

You can explore the structure of the database in the Databases pane. If you have successfully added and connected the rexon_metals.db file, you will see that it now has a little expand/collapse button next to it’s icon in the databases pane. If you click it, you’ll see that the database contains *Tables* and *Views.*

###### Tables



###### Views (and Triggers)



---

### Basic SQL

Because SQL is a special purpose language, its use is quite limited. Specifically, it used only to *interact with database files*. Here, “database files” does not refer to “a file that somebody called a ‘data base’ in a meeting.” or whatever, but rather a specific file type that adheres to the specifications of being an actual *database file*. For us, these will have the extension “.db” or “.sqlite”.

#### `SELECT` and `FROM`

Now that we’ve attached a database, let’s do some SQL! Let’s see what products Rexon Metals offers – you never know what you might need! 

Type this in the SQL editor pane.

```sqlite
SELECT * FROM PRODUCT;
```

and hit the “Execute query” button (the little right-pointing blue arrow).

And – poof! – the product table appears in the pane beneath the editor pane. Just like a Pandas dataframe, the table has column names across the top to label the variables, and variable values running down the rows.

In the statement above, the splat (*) is shorthand for “all the columns”. So an English version of the above query would be “Give me all the columns from the product table.” The semicolon is not actually needed in – and only in – SQLiteStudio, but *a semicolon is required to terminate a statement* in general, so it’s better to just keep in the habit of doing it.

Let’s just get a couple columns. Do do this, we just specify the column names after the select keyword (instead of the splat).

```sql
SELECT DESCRIPTION, PRICE  

FROM PRODUCT;
```

And now you should 

Take a minute to play around with the formatting in the above statement. Can you put each word on a separate line? Can you put them all on one line? What happens if you omit the comma?

---

Try this: 

* Look at the whole customer table
* Look at just the names and home states in the customer table

---

#### `WHERE`

By using the `WHERE` keyword, we can specify criteria for the rows. Like this:

```sqlite
SELECT DESCRIPTION, PRICE 
FROM PRODUCT
WHERE PRICE > 10;
```

And now you should just see the products that cost more than $10.

SQL is very tolerant about how you express numbers.

---

Try this:

* Make the 10 into a decimal number. What happens?
* Use, in turn, `ten`, `"10"`, and `“ten”`. What works and what doesn’t?

---

So it seems that, as long as a number is represented numerically (rather than in words), things work, even if the number is in quotes.

You can specify more than one logical condition for `WHERE`. 

---

Try this: See if you can get the product description and price of items that cost more than \$5 and less than \$10.

---

#### Derived Columns

You can make new columns in your view based on existing columns. For example, let’s say that sales tax is 8%. We could see how much tax would be charged for each item like this:

```sqlite
SELECT PRICE, PRICE * 0.08 AS TAX
FROM PRODUCT
```

---

Try this: Make a view that shows the price and a total price (the price plus the tax).

---

#### Exporting View Data



#### Saving a View











