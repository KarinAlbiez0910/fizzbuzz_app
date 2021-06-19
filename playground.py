import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
response.raise_for_status()
data = response.json()
#print(data)

output = [{'number': 1, 'fizzbuzz': None},
          {'number': 2, 'fizzbuzz': None},
          {'number': 3, 'fizzbuzz': 'Fizz'},
          {'number': 4, 'fizzbuzz': None},
          {'number': 5, 'fizzbuzz': 'Buzz'},
          {'number': 6, 'fizzbuzz': 'Fizz'},
          {'number': 7, 'fizzbuzz': None},
          {'number': 8, 'fizzbuzz': None},
          {'number': 9, 'fizzbuzz': 'Fizz'},
          {'number': 10, 'fizzbuzz': 'Buzz'}]

for item in output:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/101')
    data = response.json()
    placeholder_post = {'placeholder_post':
                          {'title': data['title'],
                          'body' : data['body']}
                      }
    print(data)
