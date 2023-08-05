Property Price Register
=======================

Easy way of interacting with property price register. Includes forward geocoding data so you can get cleaned addresses with latitude, longitude and the score of the match. I'm not paying for a forward geocoding service so as I use the free trial I'll update the data.

To enter a debugger with access to all sale data run `make load` (if working from the repo) or `load_property_price_register` if you have installed the package and you will have access to the variable `sales` which contains everything

Note that this data is fairly dirty, as more sources of data are brought in the data will become cleaner as time goes on. This is due to property price register having bad names and the forward geocoding not always being perfect.

Installation
------------

`pip install property-price-register`
