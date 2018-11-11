class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,image_url,publish_date,content,source):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publish_date = publish_date
        self.content = content
        self.source = source    