key_id = 'rzp_live_j32x9sULoq2kWI'
key_secret = 'PIGHg8hrrjvpl4myURpqjHfS'

import razorpay
client = razorpay.Client(auth=(key_id, key_secret))


data = {
    'amount' : 100*100,
    "currency" : "INR",
    "receipt" : "SrikanthSri",
    "notes" : {
        "name" : "Srikanth" ,
        "payment_for" : "Python Course"
    }
}

# server orderid
order = client.order.create(data=data)
print(order)

"""{'id': 'order_K7uzlro4ZCHfGX', 'entity': 'order', 'amount': 10000,
 'amount_paid': 0,
 'amount_due': 10000,
 'currency': 'INR', 'receipt': 'SrikanthSri', 'offer_id': None, 'status': 'created', 'attempts': 0,
 'notes': {'name': 'Srikanth', 'payment_for': 'Python Course'}, 'created_at': 1661005230}
"""



"""datadict = {
  "razorpay_payment_id": "pay_29QQoUBi66xm2f",
  "razorpay_order_id": "order_9A33XWu170gUtm",
  "razorpay_signature": "9ef4dffbfd84f1318f6739a3ce19f9d85851857ae648f114332d8401e0949a3d"
}

ver = client.utility.verify_payment_signature(datadict)
print(ver)

"""