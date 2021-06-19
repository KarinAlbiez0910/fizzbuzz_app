from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


def generate_fizz_buzz_num(start_range, end_range):
    """
    This function determines the fizzbuzz values for a given range of numbers and creates an
    inner dictionary for each number and its fizzbuzz value, which is appended to the number_fizz_buzz
    list

    Arguments:
        start_range for numbers
        end_range for numbers

    Returns:
        number_fizz_buzz: list of dictionaries containing the respective number under the 'number' key
        and the fizzbuzz value under the 'fizzbuzz' key
    """
    number_fizz_buzz = []
    for num in range(start_range, end_range):
        if num % 3 == 0 and num % 5 == 0:
            value = "FizzBuzz"
        elif num % 3 == 0:
            value = 'Fizz'
        elif num % 5 == 0:
            value = 'Buzz'
        else:
            value = None
        number_fizzbuzz_inner_dict = {
                                        'number': num,
                                        'fizzbuzz': value
                                      }
        number_fizz_buzz.append(number_fizzbuzz_inner_dict)
    return number_fizz_buzz


number_fizzbuzz = generate_fizz_buzz_num(1, 101)


def get_placeholder_posts():
    """
    This function effectuates a get request to the API jsonplaceholder.typicode.com and assigns a placeholder
    title and body based on the number = the 'id' key in the API json data

    Returns:
        list containing dictionaries of placeholder posts
    """
    placeholder_posts = []
    for item in number_fizzbuzz:
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{item["number"]}')
        data = response.json()
        placeholder_post = {
                             'placeholder_post':
                             {'title': data.get('title'), 'body': data.get('body')}
                           }
        placeholder_posts.append(placeholder_post)
    return placeholder_posts


def generate_all_elements():
    """
    This function unites the number_fizz_buzz dictionaries and placeholder dictionaries

    Returns:
        list containing dictionaries with all the required elements
    """
    placeholders = get_placeholder_posts()
    number_fizzbuzz_placeholders = list(zip(number_fizzbuzz, placeholders))
    all_elements = []
    for item in number_fizzbuzz_placeholders:
        merged_dict_item = {**item[0], **item[1]}
        all_elements.append(merged_dict_item)
    return all_elements


all_elements_list = generate_all_elements()
# print(all_elements_list)


class FizzBuzzEntitities(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        # gets a list of the first ten entities, through path '/fizzbuzz-entities'
        first_ten_entities = all_elements_list[0:10]
        return {'entities': first_ten_entities}


class FizzBuzz(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self, num):
        # gets the fizzbuzz entry for the number entered through the path '/fizzbuzz/<int:num>'
        for item in all_elements_list:
            if item['number'] == num:
                return item


api.add_resource(FizzBuzzEntitities, '/fizzbuzz-entities')
api.add_resource(FizzBuzz, '/fizzbuzz/<int:num>')


if __name__ == '__main__':
    app.run()
