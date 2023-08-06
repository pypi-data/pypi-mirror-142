from api import request
from api.icon import Icon

class Dataset:
    """
    Default Dataset object
    """
    
    def __init__(self, id:str, version:str, release:str, caption:str, category:str, department:str, publish_date:str, description:str, season:str, last_update:str, tags:list, geodata:bool, accenv:bool, foreign:bool, seasonal:bool, archive:bool, new:bool):
        self.id = id
        self.version = version
        self.release = release
        self.caption = caption
        self.category = category
        self.department = department
        self.publish_date = publish_date
        self.description = description
        self.season = season
        self.last_update = last_update
        self.tags = tags
        self.geodata = geodata
        self.accenv = accenv
        self.foreign = foreign
        self.seasonal = seasonal
        self.archive = archive
        self.new = new
    
    def get_small_icon(self, category_color:bool=False):
        """
        Returns icon object.
        
        Example:
        ```
        get_dataset({"Id": "123"}).get_small_icon()
        ```
        """
        
        if category_color:
            return Icon(bytes(request.get(f'datasets/{self.id}/Image').content))
        else:
            return Icon(bytes(request.get(f'datasets/{self.id}/icon/s').content))
    
    def get_icon(self, category_color:bool=False):
        """
        Returns icon object.
        
        Example:
        ```
        get_dataset({"Id": "123"}).get_icon()
        ```
        """
        
        if category_color:
            return Icon(bytes(request.get(f'datasets/{self.id}/Image').content))
        else:
            return Icon(bytes(request.get(f'datasets/{self.id}/icon').content))
    
    def get_middle_icon(self, category_color:bool=False):
        """
        Returns icon object.
        
        Example:
        ```
        get_dataset({"Id": "123"}).get_middle_icon()
        ```
        """
        
        if category_color:
            return Icon(bytes(request.get(f'datasets/{self.id}/Image').content))
        else:
            return Icon(bytes(request.get(f'datasets/{self.id}/icon/m').content))
    
    def __repr__(self):
        return f"Dataset({self.id})"