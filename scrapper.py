from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords": "Sequence Diagram UML", "limit":400, "print_urls":True, 'output_directory':
    '/Users/josefernandotavares/Documents/downloads', 'chromedriver': '/Users/josefernandotavares/Documents/GitHub/UML_automatic_classification/bin/chromedriver'}
paths = response.download(arguments)
print(paths)