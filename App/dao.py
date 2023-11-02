def get_categories():
    return [{
        "id" : 1,
        "name" : "Mobile"
    }, {
        "id" : 2,
        "name" : "Tablet"
    }]

def get_products(kw):
    product = [{
        "id" : 1,
        "name" : "Iphone 13",
        "price" : 2000000,
        "image" : "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png",
        "category_id" : 1
    },{
        "id" : 2,
        "name" : "Galaxy S23",
        "price" : 17000000,
        "image" : "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png",
        "category_id" : 1
    },{
        "id" : 3,
        "name" : "Tablet",
        "price" : 2350000,
        "image" : "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png",
        "category_id": 2
    },{
        "id" : 4,
        "name" : "Iphone 14",
        "price" : 2000000,
        "image" : "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png",
        "category_id" : 1
    },{
        "id" : 5,
        "name" : "Iphone 15",
        "price" : 2000000,
        "image" : "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png",
        "category_id" : 1
    }]

    if kw:
        product = [p for p in product if p['name'].find(kw) >= 0]
    return product
