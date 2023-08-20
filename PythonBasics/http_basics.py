user_query = 'как стать бэкенд-разработчиком'

# Replace spaces with %20 in the query
query_words = user_query.split()  # Split the query into words
encoded_query = '%20'.join(query_words)  # Join words with %20 as separator

# Construct the URL
url = f'https://yandex.ru/search/?text={encoded_query}'

print(url)