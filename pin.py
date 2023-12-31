import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description='Download an image from a Pinterest URL.')
    parser.add_argument('url', metavar='URL', type=str, help='The Pinterest URL of the image to download')
    args = parser.parse_args()

    url = args.url
    print(url)
    parts = url.split("/")
    print(parts)
    name = parts[-2]
    namejpg = name + '.jpg'
    print(name)
    response = requests.get('https://www.pinterest.com/oembed.json?url=https://www.pinterest.com/pin/'+name+'/&amp;ref=oembed-discovery')
    data = response.json()
    thumbnail_url = data.get('thumbnail_url')
    print("Thumbnail URL:", thumbnail_url)

    parts2 = thumbnail_url.split("/")
    print(parts2)
    u1 = parts2[-1]
    u2 = parts2[-2]
    u3 = parts2[-3]
    u4 = parts2[-4]

    Hq_Image_URL = (f'https://i.pinimg.com/originals/{u4}/{u3}/{u2}/{u1}')
    print(Hq_Image_URL)

 # img download
    response = requests.get(Hq_Image_URL)

    if response.status_code == 200:  
            filename = namejpg
            with open(filename, 'wb') as file:
                file.write(response.content)
                print(f"Image downloaded as {filename}")
    else:
            print("Failed to download the image.")

if __name__ == '__main__':
    main()

#0xAK
