import requests

def download_images(url,directory, file_name):

    try:
        image_content = requests.get(url)

        if image_content.status_code == 200:

            with open(f"{directory}/{file_name}.png","wb") as capture:
                capture.write(image_content.content)

            print(f"Your file is available: {directory}/{file_name}.png")

    except Exception:
        print("Download Failed!")

if __name__ == '__main__':
    #input_url = input("Please input image url: ")
    #input_dir = input("Please input directory to download image: ")
    #file_name = input("Enter file name: ")
    #download_images(url=input_url, directory=input_dir, file_name=file_name)
    download_images()


