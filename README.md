## App design

The function generate_fizz_buzz_num is in charge of creating the fizzbuzz value according to
the rules of the fizzbuzz game (https://en.wikipedia.org/wiki/Fizz_buzz) for a range of numbers that 
can be passed in as the arguments of the function. A dictionary containing each number
and the fizzbuzz value is generated within the function and added to a list number_fizz_buzz.

The function get_placeholder_posts is in charge of making a get request to the API 
jsonplaceholder.typicode.com and gets the values for "title" and "body" based on the
number which is evaluated as the 'id' key within the API data. Furthermore, the
function generates a dictionary for each number's title and body, which is appended to
a list named placeholder_posts.

The function generate_all_elements combines the number fizzbuzz and the placeholder
dictionaries into one dictionary structure and all of the combined dictionaries are
appended to a list called all_elements.

The API is generated via the Flask and Flask-Restful Frameworks and the following
endpoints are implemented:

1. api.add_resource(FizzBuzzEntitities, '/fizzbuzz-entities'):

Configured to access the first ten fizzbuzz entities:

![](./fizzbuzz_entities_request.jpg)

2. api.add_resource(FizzBuzz, '/fizzbuzz/<int:num>'):

Configured to access the entity corresponding to the number entered in the
variable part of the path, <int:num>: 


![](./single_fizzbuzz_request.jpg)

These two get requests have been carried out through the Postman interface
(https://www.postman.com/product/api-versioning/).


## How to run the Python project
In order to run the project, please be sure to install the libraries as
indicated in the requirements.txt file and run the file

app.py
