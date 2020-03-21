from django import forms

#these are the list of choices. They are called in the model and are presented
#to the user on the frontend

AD_TYPE_CHOICES = (
    ('selling', "I am selling"),
    ('buying', "I am buying"),
)

FOR_SALE_BY_CHOICES = (
    ('owner', "Owner"),
    ('business', "Business"),
)

PRICE_CHOICES=(
    ('listed price', "Listed Price"),
    ('free', "Free"),
    ('please contact', "Please Contact"),
    ('swap or trade', "Swap / Trade"),
)

CATEGORY_CHOICES = [
    ('Real Estate', (
            ('for rent', 'For Rent'),
            ('for sale', 'For Sale'),
            ('real estate services', 'Real Estate Services'),
        )
    ),
    ('Cars and Vehicles', (
            ('cars and trucks', 'Cars And Trucks'),
            ('classic cars', 'Classic Cars'),
            ('vehicle parts', 'Vehicle Parts'),
            ('tires', 'Tires'),
            ('vehicle accessories', 'Vehicle Accessories'),
            ('motorcycles', 'Motorcycles'),
            ('atvs and snowmobiles', 'ATVs and Snowmobiles'),
            ('boats and watercraft', 'Boats and Watercraft'),
            ('rvs, campers, trailers', 'RVs, Campers and Trailers'),
            ('heavy equipment', 'Heavy Equipment'),
            ('other','other')
        )
    ),
    ('Buy and Sell', (
            ('arts and collectibles', 'Arts and Collectibles'),
            ('audio', 'Audio'),
            ('baby items', 'Baby Items'),
            ('bikes','Bikes'),
            ('books','Books'),
            ('business and industrial','Business and Industrial'),
            ('cameras and camcorders','Cameras and Camcorders'),
            ('cds, dvds and blu rays','CDs, DVDs, and Blu-Ray'),
            ('clothing','Clothing'),
            ('computers','Computers'),
            ('computer accessories','Computer Accessories'),
            ('electronics','Electronics'),
            ('free stuff','Free Stuff'),
            ('furniture','Furniture'),
            ('garage sales','Garage Sales'),
            ('health and special needs','Health and Special Needs'),
            ('hobbies and crafts','Hobbies and Crafts'),
            ('home appliances','Home Appliances'),
            ('home indoor', 'Home - Indoor'),
            ('home outdoor and garden', 'Home - Outdoor and Garden'),
            ('home renovation materials','Home Renovation Materials'),
            ('jewellery and watches','Jewellery and Watches'),
            ('phones', 'Phones'),
            ('sporting goods and exercise','Sporting Goods and Exercise'),
            ('tickers','Tickets'),
            ('tools','Tools'),
            ('toys and games','Toys and Games'),
            ('tvs and video','TVs and Video'),
            ('video games','Video Games and Consoles'),
            ('other','Other')
        )
    ),
]


SEARCH_FILTER=(
    ('all categories',"All Categories"),
    ('real estate', "Real Estate"),
    ('cars and vehicles', "Cars and Vehicles"),
    ('buy and sell', "Buy and Sell"),
)