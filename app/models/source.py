class Source:
    '''
    News class to define News Objects
    '''

    def __init__(self, source, author, title, description, url, image_url, publish_time):

        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publish_time = publish_time