account = "63435e96e54f9c12e91c9745"
location = "641a44cc7ccad44aefcda1ec"

products = pcli.products.list_all(q={"account" : account, })


for product in products:
    