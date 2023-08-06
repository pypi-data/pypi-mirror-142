from api.dataset import Dataset
from api.category import Category
from api.app import App
from api import request
from exceptions.exceptions import InvalidCategoryID
from exceptions.exceptions import InvalidDatasetID

class Client:
    """
    Example:
    ```
    client = Client(api_key="YOUR_API_KEY")
    ```
    """
    
    def __init__(self, api_key:str):
        self.api_key = api_key
        request.key = self.api_key

    def get_dataset(self, id:str):
        """
        Returns dataset object.
        
        Example:
        ```
        print(get_dataset({"Id": "123"}).caption)
        ```
        """
        
        r = request.get(f'datasets?$filter=Id+eq+{id}')

        if r.status_code == 404:
            raise InvalidDatasetID(id)
        else:
            req = r.json()

            if isinstance(req, list):
                if len(req) > 1:
                    return list(map(lambda r: Dataset(r['Id'], r['VersionNumber'], r['ReleaseNumber'], r['Caption'], r['CategoryId'], r['DepartmentId'], r['PublishDate'], r['FullDescription'], r['Season'], r['LastUpdateDate'], r['Keywords'], r['ContainsGeodata'], r['ContainsAccEnvData'], r['IsForeign'], r['IsSeasonal'], r['IsArchive'], r['IsNew']), req))
                else:
                    r = req[0]
                    return Dataset(r['Id'], r['VersionNumber'], r['ReleaseNumber'], r['Caption'], r['CategoryId'], r['DepartmentId'], r['PublishDate'], r['FullDescription'], r['Season'], r['LastUpdateDate'], r['Keywords'], r['ContainsGeodata'], r['ContainsAccEnvData'], r['IsForeign'], r['IsSeasonal'], r['IsArchive'], r['IsNew'])
            elif isinstance(req, dict):
                r = req
                return Dataset(r['Id'], r['VersionNumber'], r['ReleaseNumber'], r['Caption'], r['CategoryId'], r['DepartmentId'], r['PublishDate'], r['FullDescription'], r['Season'], r['LastUpdateDate'], r['Keywords'], r['ContainsGeodata'], r['ContainsAccEnvData'], r['IsForeign'], r['IsSeasonal'], r['IsArchive'], r['IsNew'])

    def get_category(self, id:str):
        """
        Returns category object.
        
        Example:
        ```
        print(get_category({"Id": "123"}).caption)
        ```
        """

        r = request.get(f'categories?$filter=Id+eq+{id}')
        
        if r.status_code == 404:
            raise InvalidCategoryID(id)
        else:
            req = r.json()
            
            if isinstance(req, list):
                if len(req) > 1:
                    return list(map(lambda r: Category(r['Id'], r['Name'], r['EnglishName'], r['Description'], r['EnglishDescription'], r['Datasets'], r['Services']), req))
                else:
                    r = req[0]
                    return Category(r['Id'], r['Name'], r['EnglishName'], r['Description'], r['EnglishDescription'], r['Datasets'], r['Services'])
            elif isinstance(req, dict):
                r = req
                return Category(r['Id'], r['Name'], r['EnglishName'], r['Description'], r['EnglishDescription'], r['Datasets'], r['Services'])
    
    def get_datasets(self):
        """
        Returns objects of dataset.
        
        Example:
        ```
        print(get_datasets())
        ```
        """
        
        r = request.get('datasets')
        
        if r.status_code == 404:
            raise InvalidDatasetID(id)
        else:
            req = r.json()
            
            return list(map(lambda r: Dataset(r['Id'], r['VersionNumber'], r['ReleaseNumber'], r['Caption'], r['CategoryId'], r['DepartmentId'], r['PublishDate'], r['FullDescription'], r['Season'], r['LastUpdateDate'], r['Keywords'], r['ContainsGeodata'], r['ContainsAccEnvData'], r['IsForeign'], r['IsSeasonal'], r['IsArchive'], r['IsNew']), req))

    def get_categories(self):
        """
        Returns objects of category.
        
        Example:
        ```
        print(get_categories())
        ```
        """
        
        r = request.get('categories')
        
        if r.status_code == 404:
            raise InvalidCategoryID(id)
        else:
            req = r.json()
            
            return list(map(lambda r: Category(r['Id'], r['Name'], r['EnglishName'], r['Description'], r['EnglishDescription'], r['Datasets'], r['Services']), req))
    
    def get_app(self, id:str):
        """
        Returns dataset object.
        
        Example:
        ```
        print(get_dataset({"Id": "123"}).caption)
        ```
        """
        
        r = request.get(f'apps/{id}')

        if r.status_code == 404:
            raise InvalidDatasetID(id)
        else:
            req = r.json()

            if isinstance(req, list):
                if len(req) > 1:
                    return list(map(lambda r: App(r['Id'], r['Caption'], r['Description'], r['CategoryId'], r['PublishDate'], r['Developer'], r['Icon']), req))
                else:
                    r = req[0]
                    print(r)
                    return App(r['Id'], r['Caption'], r['Description'], r['CategoryId'], r['PublishDate'], r['Developer'], r['Icon'])
            elif isinstance(req, dict):
                r = req
                return App(r['Id'], r['Caption'], r['Description'], r['CategoryId'], r['PublishDate'], r['Developer'], r['Icon'])
    
    def get_apps(self):
        """
        Returns objects of dataset.
        
        Example:
        ```
        print(get_datasets())
        ```
        """
        
        r = request.get('apps')
        
        if r.status_code == 404:
            raise InvalidDatasetID(id)
        else:
            req = r.json()
            
            return list(map(lambda r: App(r['Id'], r['Caption'], r['Description'], r['CategoryId'], r['PublishDate'], r['Developer'], r['Icon']), req))