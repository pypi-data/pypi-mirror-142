import requests
import os

class MagentoApi:

    rest_path = '/rest/default/V1'

    def __init__(self, url=None, access_token=None):
        self.url = os.environ.get('MAGENTO_REST_BASE_URL', url)
        self.headers = {"Authorization": "Bearer " + os.environ.get('MAGENTO_REST_ACCESS_TOKEN', access_token)}

    def product_api(self, sku):
        """Makes a call to a Magento 2 REST API at
        /rest/default/V1/products/{sku}

        Args:
            sku (str): The product SKU to query.

        Returns:
            Response: Information on product with given SKU.
        """
        endpoint = self.rest_path + '/products/' + str(sku)
        return self.__call_api_get(endpoint)

    def product_media_api(self, sku):
        """Makes a call to a Magento 2 REST API at
        /rest/default/V1/products/{sku}/media/

        Args:
            sku (str): The product SKU to query.

        Returns:
            Response: Information on product media for given SKU.
        """
        endpoint = self.rest_path + '/products/' + str(sku) + '/media/'
        return self.__call_api_get(endpoint)

    def categories_api(self):
        """Makes a call to a Magento 2 REST API at
        /rest/default/V1/categories/

        Returns:
            Response: Information on categories for the website.
        """
        endpoint = self.rest_path + '/categories/'
        return self.__call_api_get(endpoint)

    def categories_products_api(self, category_id):
        """Makes a call to a Magento 2 REST API at
        /rest/default/V1/categories/{category_id}/products/

        Args:
            category_id (int): The category ID to query.

        Returns:
            Response: Information on products in the given category.
        """
        endpoint = (self.rest_path + '/categories/' + str(category_id)
                    + '/products/')
        return self.__call_api_get(endpoint)

    def guest_cart_create(self):
        """Makes a call to a Magento 2 REST API at
        /rest/default/V1/guest-carts/

        Returns:
            Response: The guest cart ID
        """
        endpoint = (self.rest_path + '/guest-carts/')
        return self.__call_api_post(endpoint)

    def guest_cart_get(self, cart_id):
        """Makes a call to a Mageto 2 REST API at
        /rest/default/V1/guest-carts/{cart_id}

        Args:
            cart_id (str): The guest cart ID

        Returns:
            Response: Information about the guest cart with the given ID.
        """
        endpoint = (self.rest_path + '/guest-carts/' + str(cart_id))
        return self.__call_api_get(endpoint)

    def guest_cart_add_product(self, cart_id, items):

        endpoint = (self.rest_path + '/guest-carts/' + str(cart_id) + '/')
        return self.__call_api_post(endpoint, json=items)

    def custom(self, endpoint):
        """Makes a call to a custom endpoint.

        Args:
            endpoint (str): The full REST API endpoint and variables you want
            to use.

        Returns:
            Response: Whatever the custom API returns.
        """
        return self.__call_api_get(endpoint)

    def __call_api_get(self, endpoint):
        return requests.get(self.url + endpoint, headers=self.headers)

    def __call_api_post(self, endpoint):
        return requests.post(self.url + endpoint, headers=self.headers)
