import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_recommender.settings")

import django
django.setup()

from reviews.models import Product 


def save_Product_from_row(Product_row):
    Product = Product()
    Product.id = Product_row[0]
    Product.name = Product_row[1]
    Product.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        Products_df = pd.read_csv(sys.argv[1])
        print Products_df

        Products_df.apply(
            save_Product_from_row,
            axis=1
        )

        print "There are {} Products".format(Product.objects.count())
        
    else:
        print "Please, provide Product file path"