import requests

def getUrlStatusCode(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.ConnectionError:
        return -1

def main():
    with open('urls.txt', 'r') as url_file, open('result.txt', 'w') as output:
        for url in url_file:
            print("Accessing %s ...\n" % url)
            url_status_code = getUrlStatusCode(url)
            output.write("url: %s" % url)
            output.write("code: %d\n\n" % url_status_code )

if __name__ == "__main__":
    main()
