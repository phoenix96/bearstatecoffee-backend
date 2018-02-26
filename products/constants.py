CATEGORY_NOT_FOUND = 'The category to be updated/deleted was not found.'
CATEGORY_UPDATED = 'The category was successfully updated.'
INVALID_FIELDS = 'Details entered have invalid fields.'
CATEGORY_DELETED = 'The category was successfully deleted.'
PRODUCT_NOT_FOUND = 'The required product was not found.'
CATEGORY_ADDED = 'The category was successfully added.'
CATEGORY_ADDED_TO_PRODUCT = 'The category was successfully added to the product.'
CATEGORY_REMOVED_FROM_PRODUCT = 'The category was successfully removed from the product.'
PRODUCT_UPDATED = 'The product was successfully updated.'
PRODUCT_DELETED = 'The product was successfully deleted.'
COMBO_QUANTITY_ERROR = 'The total quantities of products in a combo must at least be two.'
COMBO_FIELD_ERROR = 'Name and Cost are necessary to add a combo.'
COMBO_PRODUCT_ERROR = 'One or more Product in the Combo does not exist.'
COMBO_ADDED = 'The combo was created successfully.'
COMBO_UPDATED = 'The combo was updated successfully.'
USER_NOT_FOUND = 'The user does not exist.'
SUBSCRIPTION_FIELD_ERROR = 'Product and Category are required fields to add a subscription'
CATEGORY_NOT_FOR_PRODUCT = 'The selected category is not available for this product.'
SUBSCRIPTION_ADDED = 'The subscription was successfully added.'
SUBSCRIPTION_NOT_FOUND = 'This subscription does not exist.'
SUBSCRIPTION_ACTIVE = 'This subscription is already active.'
SUBSCRIPTION_FINALIZED = 'This subscription has been successfully finalized.'
SUBSCRIPTION_DATE_ERROR = 'The new order date has to be at least 1 day ahead of today.'
SUBSCRIPTION_NOT_ACTIVE = 'This subscription is not currently active or was finished.'
SUBSCRIPTION_SHIFTED = 'This subscription was successfully shifted.'
SUBSCRIPTION_CANCELLED = 'This subscription has been cancelled.'
SUBSCRIPTION_ORDER_CONFIRMATION = 'Your order has been placed from your subscription.'
SUBSCRIPTION_SHIFT_BODY = 'Your subscription of product %s has been shifted to %s\n'
SUBSCRIPTION_SHIFT_SUBJECT = 'Shifted Subscription'
SUBSCRIPTION_CANCEL_SUBJECT = 'Subscription Cancelled'
SUBSCRIPTION_CANCEL_BODY = 'Your subscription of product %s has been cancelled.\n'
SHIFTING_REASON_NO_QUANTITY = 'The subscription is being shifted due to unavailability of the product currently.'
CANCEL_REASON_NO_PRODUCT = 'The subscription is being cancelled due to unavailability of the product.'
CANCEL_REASON_NO_PERIOD = 'The subscription is being cancelled due to removal of the chosen category option of that ' \
                          'product'
PRODUCT_NOT_FOR_SUBSCRIPTION = 'Product not available for subscriptions'
CATEGORY_CANT_BE_REMOVED = 'Category does\'nt exist for the product'
CATEGORY_CANT_BE_ADDED = 'Category is already added to the product'
# Important Messages To Be Returned In Response
ADD_TO_CART_VALIDATION = 'product_id or quantity missing.'
INVALID_PRODUCT = 'No product found.'
AVAILABLE_QUANTITY = 'Available quantity is '
INVALID_PRODUCT_CART = 'Product doesn\'t exists in cart.'
QUANTITY_NOT_AVAILABLE = 'Cart products not available to buy.'
PRODUCT_REMOVED = 'Product Removed.'

NOT_ALLOWED = 'You are not allowed to do this operation'

INVALID_ORDER = 'Order doesn\'t exists.'

ORDER_CONFIRMATION_EMAIL_BODY = 'Your order is confirmed amounting to %s  with Customer Order Id %s.\nProduct      ' \
                                'Quantity      Price\n'
ORDER_CONFIRMATION_EMAIL_BODY_PRODUCTS = '%s      %s      %s\n'
ORDER_CONFIRMATION_EMAIL_SUBJECT = 'Your Order is Confirmed.'

INITIATE_PAYMENT_VALIDATION = 'customer_order_id or payment_type missing'
PAYMENT_CONFIRMATION_VALIDATION = 'customer_order_id or payment_status or amount_paid missing'
CART_VALIDATION = 'product_id or quantity missing.'
