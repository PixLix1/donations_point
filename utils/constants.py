SHIPPING_ADDRESS = 1
BILLING_ADDRESS = 2
ACTIVATION_AVAILABILITY = {
    'unit': 'minutes',
    'value': 30,
}
ACTIVATION_AVAILABILITY_DICT = {
    ACTIVATION_AVAILABILITY['unit']: ACTIVATION_AVAILABILITY['value']
}

# product status
ACTIVE_STATUS = 1
REQUESTED_STATUS = 2
INACTIVE_STATUS = 3

# # order status
# OPEN_STATUS = 1  # submitted
# APPROVED_STATUS = 2  # approved by product owner
# REJECTED_STATUS = 3  # other orders, same product automatically rejected if 1 order approved for product
# SHIPMENT_STATUS = 4  # product has been shipped to requestor
# CLOSED_STATUS = 5  # requestor/(shipping company?) confirms product pick-up
