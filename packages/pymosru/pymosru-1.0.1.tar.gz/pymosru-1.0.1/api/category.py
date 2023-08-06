from api import request
from api.icon import Icon

class Category:
    """
    Default Category object
    """
    
    def __init__(self, id:str, name:str, en_name:str, description:str, en_description:str, datasets:list, services:list):
        self.id = id
        self.name = name
        self.en_name = en_name
        self.description = description
        self.en_description = en_description
        self.datasets = datasets
        self.services = services
    
    def get_small_icon(self):
        """
        Returns icon object.
        
        Example:
        ```
        get_category({"Id": "123"}).get_small_icon()
        ```
        """
        
        return Icon(bytes(request.get(f'categories/{self.id}/icon/s').content))
    
    def get_icon(self):
        """
        Returns icon object.
        
        Example:
        ```
        get_category({"Id": "123"}).get_icon()
        ```
        """
        
        return Icon(bytes(request.get(f'categories/{self.id}/icon').content))
    
    def get_middle_icon(self):
        """
        Returns icon object.
        
        Example:
        ```
        get_category({"Id": "123"}).get_middle_icon()
        ```
        """
        
        return Icon(bytes(request.get(f'categories/{self.id}/icon/m').content))
    
    def __repr__(self):
        return f"Category({self.id})"