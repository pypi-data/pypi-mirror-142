from api.icon import Icon
from api import request

class App:
    """
    Default App object
    """
    
    def __init__(self, id:str, caption:str, description:str, category:str, publish_date:list, developer:list, icon:str):
        self.id = id
        self.caption = caption
        self.description = description
        self.category = category
        self.publish_date = publish_date
        self.developer = developer
    
    def get_icon(self):
        """
        Returns icon object.
        
        Example:
        ```
        get_app({"Id": "123"}).get_icon()
        ```
        """
        
        return Icon(bytes(request.get(f'apps/{self.id}/icon').content))
    
    def __repr__(self):
        return f"Category({self.id})"