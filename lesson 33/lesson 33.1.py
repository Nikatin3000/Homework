import requests

url1 = 'https://uk.wikipedia.org/robots.txt'
url2 = 'https://twitter.com/robots.txt'

response = requests.get(url1)
response2 = requests.get(url2)

if response.status_code == 200:
    content = response.text

    with open('robots_wiki.txt', 'wb') as file1:
        file1.write(response.content)
        print("file downloaded and saved successfully.")
else:
    print("Failed to download file.")

if response2.status_code == 200:
    content2 = response2.text

    with open('robots_twitter.txt', 'wb') as file2:
        file2.write(response2.content)
        print("file downloaded and saved successfully.")
else:
    print("Failed to download file.")
