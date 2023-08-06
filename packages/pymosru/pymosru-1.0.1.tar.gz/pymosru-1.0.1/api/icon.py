class Icon:
    """
    Default Icon object
    """
    
    def __init__(self, data:bytes):
        self.data = data
    
    def save(self, path:str):
        """
        Saves icon.
        
        Example:
        ```
        get_category({"Id": "123"}).get_icon().save("test1.png")
        get_dataset({"Id": "123"}).get_icon().save("test2.png")
        ```
        """
        
        with open(path, 'wb') as icon:
            icon.write(self.data)
    
    def __repr__(self):
        return f"Icon({abs(self.__hash__())})"