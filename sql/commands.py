ADD_TEST_PRODUCT = '''
    INSERT INTO oc_product (
        product_id, 
        sku, 
        upc, 
        ean, 
        jan, 
        isbn, 
        mpn, 
        location, 
        stock_status_id, 
        manufacturer_id, 
        tax_class_id, 
        model, 
        quantity, 
        price,
        date_added,
        date_modified 
    )
    VALUES (1, 'sku', 'upc', 'ean', 'jan', 'isbn', 'mpn', 'location', 7, 8, 9, '[test]model', 300, 19.99, NOW(), NOW())
    '''
ADD_TEST_PRODUCT_DESCRIPTION = '''
    INSERT INTO oc_product_description (
        product_id, 
        language_id,
        name,
        description,
        meta_title,
        tag,
        meta_description,
        meta_keyword
    )
    VALUES (1, 1, '[test]product', '[test]description', '[test]meta', '[test]tag', '[test]meta_desc', '[test]meta_key');
'''
CLEAR_TEST_PRODUCT = '''
    DELETE FROM oc_product
    WHERE product_id = {id};
'''
CLEAR_TEST_DESCRIPTION = '''
    DELETE FROM oc_product_description
    WHERE product_id = {id};
'''
CLEAR_TEST_PRODUCT_STORE = '''
    DELETE FROM oc_product_to_store
    WHERE product_id = {id};
'''
GET_ID_BY_MODEL = '''
    SELECT product_id FROM oc_product
    WHERE model = '{model}'
'''


def clean_up(connection, cursor, product_id):
    cursor.execute(CLEAR_TEST_PRODUCT.format(id=product_id))
    cursor.execute(CLEAR_TEST_DESCRIPTION.format(id=product_id))
    cursor.execute(CLEAR_TEST_PRODUCT_STORE.format(id=product_id))
    connection.commit()
    connection.close()
