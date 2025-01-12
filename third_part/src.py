
import json

#-------------------------------------------------------------------------------------------------------------------------------------------------#

# TASK 1 
def parse_categories():
    categories = []

    def get_categories_recursive():
        # TODO: Your code here
        with open('categoriesjson\\categories.json', 'r') as j:
            data = j.read()
            Cate_data = json.loads(data)

        for key, value in Cate_data.items():
            data = value.get('content', {}).get('items', [])
            data2 = value.get('props', {}).get('items', {})
            if data and data2:
                d_1 = data2[-1].get('itemProps').get('href').split('/')[-2]
                href = data[-1].get('itemProps').get('href').replace('d_1', '').replace(' ', '')

                text = data[-1].get('itemProps').get('text')
                if data2[-1].get('highlight'):
                    categories.append([d_1, href.split('/')[-1].title().replace('-', ' '), text])

    get_categories_recursive()
    return categories

# print(parse_categories())