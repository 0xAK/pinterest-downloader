import argparse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    parser = argparse.ArgumentParser(description='Download an image from a Pinterest URL.')
    parser.add_argument('url', metavar='URL', type=str, help='The Pinterest URL of the image to download')
    args = parser.parse_args()

    # WebDriver
    driver = webdriver.Chrome()
    driver.get(args.url)  # cli url

    # img url
    selector = driver.find_element(By.ID, 'pin-image-preload')
    img_url = selector.get_attribute('href')
    print(img_url)

    # img name
    url = img_url
    parts = url.split("/")
    name = parts[-1]
    print(name)

    # img download
    response = requests.get(img_url)

    if response.status_code == 200:  
            filename = name
            with open(filename, 'wb') as file:
                file.write(response.content)
                print(f"Image downloaded as {filename}")
    else:
            print("Failed to download the image.")

if __name__ == '__main__':
    main()

#0xAK