from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
from store import logic
from store.models import Product


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

#
# class LogicTestCase(TestCase):
#
#     def test_search_product(self):
#         """
#         Search product
#         :return: Product array : stored_product, stored_category, product_id, stored_grade, stored_categories
#         """
#         response = logic.get_product('3017620429484')
#
#         product = "Nutella"
#         category = "spreads"
#         code = "3017620429484"
#         grade = "e"
#         categories = "['en:breakfasts', 'en:spreads', 'en:sweet-spreads', 'fr:pates-a-tartiner', " \
#                      "'en:chocolate-spreads', 'en:hazelnut-spreads'," \
#                      " 'en:cocoa-and-hazelnuts-spreads', 'es:Pâtes à tartiner']"
#
#         product_array = [product, category, code, grade, categories]
#         self.assertQuerysetEqual(response, tuple(product_array))
#
#
    # def test_in_database(product_id):
    #     """
    #     Check if in database
    #     :param product_id: product id
    #     :return: product
    #     """
    #     stored_products = Product.objects.filter(code=product_id).count()
    #
    #     for stored_product in range(stored_products):
    #         if stored_product > 1:
    #             print(f"The product seems to have more than one existence")
    #             print("Destroy...")
    #             stored_product.delete()
    #         elif stored_product == 1:
    #             print(f"The product is already in database : {product_id} (logic)")
    #             return stored_product
    #         else:
    #             print(f"The product will be saved : {product_id} (logic)")
    #             return False
    #
    # def test_count_products(category, grade, code=0):
    #     """
    #     Counting substitutes
    #     :param category:
    #     :param grade:
    #     :param code:
    #     :return: substitutes amount
    #     """
    #     if code:
    #         return Product.objects.filter(category=category, grade__lt=grade).count()
    #     else:
    #         return Product.objects.filter(category=category, grade__lt=grade).exclude(code=code).count()
    #
    # def test_get_product(product_id):
    #     """
    #     Get product array
    #     :param product_id: Requested product
    #     :return: product_array : Product, Category, Code, Grade, List of categories
    #     """
    #     if in_database(product_id):
    #         product_object = Product.objects.get(code=product_id)
    #         product = in_database(product_id)
    #         category = product_object.category
    #         categories = product_object.categories
    #         grade = product_object.grade
    #         code = product_object.code
    #         print(product_object, product, category)
    #         return product, category, code, grade, categories
    #
    #     else:
    #         product_array = save_product(product_id)
    #
    #         if product_array is not None:
    #             product = product_array[0]
    #             category = product_array[1]
    #             categories = product_array[2]
    #             grade = product_array[3]
    #             code = product_array[4]
    #             print(product, category)
    #             return product, category, code, grade, categories
    #         else:
    #             return None
    #
    # def test_retrieve_or_save_products(category, categories, minimal_grade, product_code):
    #     """
    #     Check if substitutes are available
    #     :param category:
    #     :param categories:
    #     :param minimal_grade:
    #     :param product_code:
    #     :return: category amount
    #     """
    #     if count_products(category, minimal_grade, product_code) < 6:
    #         url = get_url_for_category(category)
    #         if url:
    #             if fetch_products(url, category, minimal_grade, product_code):
    #
    #                 if count_products(category, minimal_grade, product_code) > 6:
    #                     get_substitutes(category, categories, product_code, minimal_grade)
    #
    #         else:
    #             return None
    #     else:
    #         return count_products(category, minimal_grade, product_code)
    #
    # def test_get_substitutes(category, categories, product_code, minimal_grade):
    #     """
    #     Get substitutes for product
    #     :param category: The requested category
    #     :param categories: The requested list of categories
    #     :param product_code: The product code
    #     :param minimal_grade: The minimal grade
    #     :return:
    #     """
    #
    #     print("get substitutes (logic)")
    #
    #     if type(categories) == str:
    #         print("Categories is a string")
    #         print(f"{categories}")
    #
    #         categories = list_categories(categories)
    #         print("Categories is a list")
    #         print(categories)
    #
    #     subs = Product.objects.filter(categories__icontains=category, grade__lt=minimal_grade).exclude(
    #         code=product_code)
    #     print("Subs match filter")
    #     print(f"{subs}")
    #
    #     filters = get_filters(category, categories, minimal_grade, product_code)
    #     print("filters")
    #
    #     subs = apply_filter(subs, filters, category, categories, minimal_grade, product_code)
    #     print("subs after filter")
    #     print(f"{subs}")
    #     return subs
    #
    # def test_fetch_products(url, category, minimal_grade, product_code):
    #     """
    #     Fetch substitutes
    #     :param url: Products url
    #     :param category: Products category
    #     :param minimal_grade: Minimal grade
    #     :param product_code: Product code
    #     :return:
    #     """
    #     substitutes = []
    #
    #     page_range, product_range = calculate_parsing_loops(url)
    #
    #     for page in range(page_range):
    #         if page is 0:
    #             data = requests.get(f"{url}.json")
    #         else:
    #             data = requests.get(f"{url}/{page}.json")
    #
    #         print(f"{url}/{page}.json")
    #         substitutes_page = data.json()
    #
    #         for product in range(product_range):
    #             parsed_product = substitutes_page['products'][product]
    #
    #             if "nutrition_grades" in parsed_product:
    #                 grade = parsed_product['nutrition_grades']
    #
    #                 # if grade < mini:
    #                 if grade < minimal_grade:
    #
    #                     if "code" in parsed_product:
    #
    #                         if in_database(parsed_product["code"]):
    #                             substitutes.append(parsed_product)
    #                         else:
    #                             try:
    #                                 save_product(parsed_product["code"])
    #                                 substitutes.append(parsed_product)
    #                             except IndexError:
    #                                 pass
    #
    #         if count_products(category, minimal_grade, product_code) < 6:
    #
    #             if page > 3:
    #
    #                 if count_products(category, minimal_grade, product_code) < 0:
    #                     print(len(substitutes))
    #                     break
    #                 else:
    #                     pass
    #
    #             if page < 5:
    #                 page += 1
    #             else:
    #                 if len(substitutes) == 0:
    #                     return None
    #         else:
    #             print(len(substitutes))
    #             break
    #
    #     return True
    #
    # def test_fetch_product_array(product):
    #     """
    #     Fetch product array
    #     :param product:
    #     :return: product array
    #     """
    #     categories, image, name, code, grade, nutriments = 0, 0, 0, 0, 0, 0
    #
    #     if 'categories_hierarchy' in product:
    #         categories = product['categories_hierarchy']
    #
    #     if 'image_url' in product:
    #         image = product['image_url']
    #
    #     if 'product_name' in product:
    #         name = product['product_name']
    #
    #     if 'code' in product:
    #         code = product['code']
    #
    #     if 'nutrition_grades' in product:
    #         grade = product['nutrition_grades']
    #
    #     if 'nutriments' in product:
    #         nutriments = product['nutriments']
    #
    #     if categories and image and name and grade and nutriments:
    #         return [categories, image, name, code, grade, nutriments]
    #     else:
    #         return None
    #
    # def test_save_product(product_id):
    #     """
    #     Save product
    #     :param product_id: Requested product
    #     :return: Product array : Product queryset, Category, List of categories, Grade, Id
    #     """
    #     page = f"https://world.openfoodfacts.org/api/v0/product/{product_id}.json"
    #     print(f"Save product : {page} (logic)")
    #
    #     data = requests.get(page).json()
    #     if data:
    #
    #         if data['product']:
    #             product = data['product']
    #
    #             try:
    #                 product_array = fetch_product_array(product)
    #                 if product_array is not None:
    #                     categories = product_array[0]
    #                     image = product_array[1]
    #                     name = product_array[2]
    #                     code = product_array[3]
    #                     grade = product_array[4]
    #                     nutriments = product_array[5]
    #                     print(f"...{categories}...")
    #                     print(f"...{image}...")
    #                     print(f"...{name}...")
    #                     print(f"...{code}...")
    #                     print(f"...{grade}...")
    #                     print(f"...{nutriments}...")
    #                     try:
    #                         category = get_main_category(categories)
    #                         print(f"...{category}...")
    #                     except ValueError:
    #                         return None
    #
    #                     if category:
    #
    #                         try:
    #                             product = Product(name=name, image=image, category=category, categories=categories,
    #                                               grade=grade, nutriments=nutriments, code=code)
    #                             print(f"Saving the product ... {name} (logic)")
    #                             product.save()
    #
    #                             stored_product = Product.objects.filter(code=code)
    #                             return stored_product, category, categories, grade, code
    #
    #                         except IndexError:
    #                             return None
    #                 else:
    #                     return None
    #
    #             except IndexError:
    #                 return None
    #
    #     else:
    #         return None
    #
    # def test_calculate_parsing_loops(url):
    #     """
    #     Calculating parsing loops
    #     :param url: Counter url
    #     :return: page range and product range
    #     """
    #     data = requests.get(f"{url}.json")
    #     substitutes_page = data.json()
    #
    #     page_range = 1
    #     if substitutes_page['count'] < 6:
    #         product_range = substitutes_page['count']
    #
    #     else:
    #         product_range = 20
    #
    #         # We don't fetch the last page ( < 20 products)
    #         page_range = (substitutes_page['count'] // 20) - 1
    #
    #     return page_range, product_range
    #
    # def test_get_filters(category, categories, minimal_grade, product_code):
    #     """
    #     Get filters
    #     :param category:
    #     :param categories: List of categories
    #     :param minimal_grade: Minimal grade
    #     :param product_code: Product Code
    #     :return:
    #     """
    #
    #     filters = []
    #     subs = None
    #     for cat in categories:
    #
    #         if cat not in stopwords:
    #             subs = Product.objects.filter(categories__icontains=cat, grade__lt=minimal_grade).exclude(
    #                 code=product_code)
    #
    #             if subs:
    #                 filters.append(cat)
    #
    #     if not subs.exists():
    #         print("There is no substitutes yet...")
    #         print("We will be fetching few ones")
    #         retrieve_or_save_products(category, categories, minimal_grade, product_code)
    #
    #     filters = sorted(filters, reverse=True)
    #     return filters
    #
    # def test_apply_filter(substitutes_list, filters_to_apply, category, categories, minimal_grade, product_code):
    #     """
    #     Apply filters
    #     :param substitutes_list: substitutes_list
    #     :param filters_to_apply: The filters we can apply
    #     :param category: The product category
    #     :param minimal_grade: The minimal grade
    #     :param product_code: The product code
    #     :return:
    #     """
    #     for k, v in enumerate(filters_to_apply):
    #
    #         subs_before_filtering = len(substitutes_list)
    #
    #         if subs_before_filtering > 9:
    #
    #             print(f"Il y a {len(substitutes_list)} produits ... Filtre : {v} !")
    #             subs_with_filter = substitutes_list.filter(categories__icontains=v)
    #
    #             if subs_with_filter.count() >= 6:
    #                 substitutes_list = subs_with_filter
    #                 print(f"Après le filtre : {v} il y a  maintenant {len(substitutes_list)} produits ...")
    #
    #             else:
    #                 print(f"This filter seems to be great but unfilled with products...")
    #                 if subs_before_filtering - subs_with_filter.count() > 20:
    #                     print("Let's go fetching ones !")
    #                     retrieve_or_save_products(v, categories, minimal_grade, product_code)
    #         else:
    #             if k == 1:
    #                 print(f" Applying filters seems to return too few substitutes ...Fetching other ones !")
    #                 retrieve_or_save_products(category, categories, minimal_grade, product_code)
    #             else:
    #                 break
    #
    #     return substitutes_list[:6]
    #
    # def test_get_url_for_category(category):
    #     """
    #     Getting URL by following the open food facts redirection
    #     :param category:
    #     :return: url
    #     """
    #     print(f"Get substitutes for {category}")
    #     url = f"https://fr.openfoodfacts.org/category/{category}"
    #     try:
    #         # Getting the id
    #         req = requests.get(url)
    #         if req.history:
    #             print("Request was redirected")
    #             if req.status_code == 200:
    #                 url = req.url
    #             else:
    #                 url = None
    #         else:
    #             print("Request was not redirected")
    #             url = f"{url}"
    #
    #         print(f"It did works !  with {category} (get_product:logic) ")
    #         return url
    #
    #     except KeyError:
    #         print(f"It doesn't work with {category} (get_product:logic)")
    #         return None
    #
    # def test_get_main_category(product_categories):
    #     """
    #     Counting categories
    #     :param product_categories:
    #     :return: best category for the product
    #     """
    #     # Counting words in categories
    #
    #     categories = clean_categories(product_categories)
    #
    #     category = ''
    #     mini = 0
    #
    #     for cat in categories:
    #         value = categories.count(cat)
    #         if value > mini:
    #             if cat not in stopwords and len(cat) > 2:
    #                 mini = value
    #                 category = cat
    #
    #     return category
    #
    # def test_list_categories(categories):
    #     """
    #     Listing categories string
    #     :param categories: String
    #     :return: categories : List
    #     """
    #     # Remove iso codes
    #     categories = re.sub(r'..:', '', categories)
    #
    #     # Remove hooks
    #     categories = categories.replace('[', '')
    #     categories = categories.replace(']', '')
    #
    #     # Split string
    #     categories = categories.split(",")
    #
    #     # Back
    #     categories = ''.join(categories)
    #
    #     # Remove quotes
    #     categories = categories.replace("'", '')
    #
    #     # Split string
    #     categories = categories.split(' ')
    #     return categories
    #
    # def test_clean_categories(product_categories):
    #     """
    #     Cleaning categories
    #     :param product_categories: list
    #     :return: list without caret or iso codes
    #     """
    #     categories = []
    #
    #     for category in product_categories:
    #         category = re.sub(r'-', ' ', category)
    #         category = re.sub(r'..:', '', category)
    #         categories.append(category)
    #     categories = ' '.join(categories).split()
    #     return categories
    #
