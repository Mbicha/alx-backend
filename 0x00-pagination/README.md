## 0x00-pagination

Pagination involves splitting data into pages. Let's say we have 1000000 rows in a database, showing all this data at the time will cause traffic and scolling through the data will be tedious. That's why the data is splitted in small chunks of range of rows per page.

# Resources
- REST API Design: Pagination - https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination
- HATEOAS - https://en.wikipedia.org/wiki/HATEOAS

# AUTHOR
Charles Mbithi Rhoda (mbithicharlse@gmail.com) - Alx Student

# Files and Directories

|**File**                                      | **Description**                                                   |
|----------------------------------------------|-------------------------------------------------------------------|
|[Helper Fun](./0-simple_helper_function.py)   |Tuple of page and page size.                                       |
| **1-main.py, 1-simple_pagination.py**         | Simple pagination                        |
| **2-main.py, 2-hypermedia_pagination.py**     | Hypermedia pagination                    |
| **3-main.py, 3-hypermedia_del_pagination.py** | Deletion-resilient hypermedia pagination |
| **Popular_Baby_Names.csv**                    | Dataset                                  |
