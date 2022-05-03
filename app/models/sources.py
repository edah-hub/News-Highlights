class Sources:
    """
    class with sources object
    """
    def __init__(self, id, name, url, country, description):
        """
        This method allows us to instantiate an instance.
        """
        self.id = id
        self.name = name
        self.url = url
        self.country = country
        self.description = description