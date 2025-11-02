import mysql.connector as sql
import random

mycon = sql.connect(host='localhost',user='root',passwd='Guru@2007')
cursor = mycon.cursor()
cursor.execute('create database if not exists AGROZON')
cursor.execute('use agrozon')
cursor.execute('create table if not exists products(ProductID int primary key,ProductName varchar(50),Price int,Stock int,Description varchar(150),Seller varchar(30))')
cursor.execute('create table if not exists user_info(UserName varchar(20) primary key,Password varchar(30),PhoneNumber varchar(10),Address varchar(150))')
cursor.execute('create table if not exists deletedusers(UserName varchar(20) primary key)')

accounts={}
cursor.execute('select UserName,Password from user_info')
for i in cursor:
    accounts[i[0]] = i[1]
for i in accounts:
    cursor.execute('create table if not exists '+i+'(ProductID int primary key,ProductName varchar(50),Price int,Quantity int,Description varchar(150))')
signin_acc = ''

products = {}
cursor.execute('select * from products')
for i in cursor:
    products[i[0]] = {'Product Name': i[1], 'Price': i[2], 'Stock': i[3], 'Description': i[4], 'Seller': i[5]}

cart = {}
if signin_acc != '':
    cursor.execute('select * from '+signin_acc)
    for i in cursor:
        cart[i[0]] = {'Product Name': i[1],'Price':i[2],'Quantity':i[3],'Description': i[4]}
    
if products == {}:
    c = 0
else:
    cursor.execute('select max(productid) from products')
    for i in cursor:
        c = i[0]

deleted_acc = []
cursor.execute('select * from deletedusers')
for i in cursor:
    deleted_acc.append(i[0])
    
accounts_info = {}
cursor.execute('select * from user_info')
for i in cursor:
    accounts_info[i[0]] = {'Phone Number': i[2], 'Address': i[3]}
cursor.execute('create table if not exists orders(UserName varchar(30),ProductID int,ProductName varchar(50),Quantity int,Address varchar(150))')

print("*"*80)
print('*'+' '*78+'*')
print("*                                  ***AGROZON***                               *")
print('*'+' '*78+'*')
print("*"*80)
print('\n\n')
input("   PRESS ENTER TO CONTINUE")
for i in range(50):
    print('\n')

##########################
def transfer():
    global c
    global products
    global accounts
    global accounts_info
    groceries={
    1:{'Product Name': 'African Horned Cucumber', 'Price': 110, 'Stock': 60, 'Description': 'African horned cucumber, with a mix of banana, cucumber, and kiwi flavors.', 'Seller': 'AGROZON'},
    2:{'Product Name': 'African Mango (Ojoba)', 'Price': 120, 'Stock': 60, 'Description': 'African mango (ojoba), large and fibrous fruit with a sweet, tropical taste.', 'Seller': 'AGROZON'},
    3:{'Product Name': 'Ajwain (Carom Seeds)', 'Price': 90, 'Stock': 200, 'Description': 'Ajwain seeds, used for digestive benefits and in spice blends.', 'Seller': 'AGROZON'},
    4:{'Product Name': 'Ajwain Seeds', 'Price': 30, 'Stock': 200, 'Description': 'Ajwain seeds, small seeds with a thyme-like flavor used in Indian snacks and as a digestive aid.', 'Seller': 'AGROZON'},
    5:{'Product Name': 'Almond Flour', 'Price': 250, 'Stock': 60, 'Description': 'Fine ground almond flour, perfect for gluten-free baking.', 'Seller': 'AGROZON'},
    6:{'Product Name': 'Almond Milk', 'Price': 150, 'Stock': 70, 'Description': 'Nutritious almond milk, dairy-free alternative.', 'Seller': 'AGROZON'},
    7:{'Product Name': 'Almond Milk Yogurt', 'Price': 130, 'Stock': 70, 'Description': 'Creamy almond milk yogurt, dairy-free and probiotic-rich.', 'Seller': 'AGROZON'},
    8:{'Product Name': 'Almond Yogurt', 'Price': 150, 'Stock': 40, 'Description': 'Creamy almond-based yogurt, dairy-free and probiotic-rich.', 'Seller': 'AGROZON'},
    9:{'Product Name': 'Almonds', 'Price': 500, 'Stock': 100, 'Description': 'Whole almonds, used in Indian sweets, desserts, and as a snack.', 'Seller': 'AGROZON'},
    10:{'Product Name': 'Alphonso Mango', 'Price': 200, 'Stock': 200, 'Description': 'King of mangoes, known for its sweetness and aroma.', 'Seller': 'AGROZON'},
    11:{'Product Name': 'Amchur Powder (Dry Mango Powder)', 'Price': 80, 'Stock': 150, 'Description': 'Amchur powder, adds tanginess to dishes, especially chaats and curries.', 'Seller': 'AGROZON'},
    12:{'Product Name': 'Asafoetida (Hing)', 'Price': 100, 'Stock': 100, 'Description': 'Asafoetida powder, enhances the flavor of dishes, especially in vegetarian cooking.', 'Seller': 'AGROZON'},
    13:{'Product Name': 'Ash Gourd (Petha)', 'Price': 40, 'Stock': 150, 'Description': 'Ash gourd (petha), mild-flavored and versatile vegetable used in soups, stews, and desserts.', 'Seller': 'AGROZON'},
    14:{'Product Name': 'Asian Mango (Alphonso)', 'Price': 1300, 'Stock': 40, 'Description': 'Asian mango (alphonso), known for its rich, sweet flavor and juicy flesh.', 'Seller': 'AGROZON'},
    15:{'Product Name': 'Atta (Whole Wheat Flour)', 'Price': 50, 'Stock': 180, 'Description': 'Atta (whole wheat flour), whole wheat flour used to make Indian breads like chapati and paratha.', 'Seller': 'AGROZON'},
    16:{'Product Name': 'Baby Purple Artichokes', 'Price': 675, 'Stock': 85, 'Description': 'Baby purple artichokes, tender and perfect for roasting.', 'Seller': 'AGROZON'},
    17:{'Product Name': 'Baby Rainbow Swiss Chard', 'Price': 450, 'Stock': 120, 'Description': 'Baby rainbow Swiss chard, tender leaves with a mild, earthy flavor.', 'Seller': 'AGROZON'},
    18:{'Product Name': 'Basmati Rice', 'Price': 120, 'Stock': 100, 'Description': 'Basmati rice, long-grain rice known for its fragrance and texture.', 'Seller': 'AGROZON'},
    19:{'Product Name': 'Basmati Rice (Premium)', 'Price': 150, 'Stock': 300, 'Description': 'Long-grain premium basmati rice, aromatic and fluffy when cooked.', 'Seller': 'AGROZON'},
    20:{'Product Name': 'Bay Leaf (Tej Patta)', 'Price': 40, 'Stock': 150, 'Description': 'Bay leaf (tej patta), aromatic leaf used in Indian cooking for flavoring.', 'Seller': 'AGROZON'},
    21:{'Product Name': 'Bay Leaf Powder', 'Price': 20, 'Stock': 100, 'Description': 'Ground bay leaf powder, adds subtle flavor to soups and sauces.', 'Seller': 'AGROZON'},
    22:{'Product Name': 'Bay Leaf Spice Powder', 'Price': 20, 'Stock': 100, 'Description': 'Ground bay leaf spice powder, adds subtle flavor to soups and sauces.', 'Seller': 'AGROZON'},
    23:{'Product Name': 'Bay Leaves', 'Price': 20, 'Stock': 100, 'Description': 'Dried bay leaves, aromatic and great for soups and stews.', 'Seller': 'AGROZON'},
    24:{'Product Name': 'Bay Leaves (Tej Patta)', 'Price': 50, 'Stock': 200, 'Description': 'Bay leaves, used in Indian cooking for their aromatic properties.', 'Seller': 'AGROZON'},
    25:{'Product Name': 'Besan (Gram Flour)', 'Price': 40, 'Stock': 250, 'Description': 'Besan (gram flour), ground chickpea flour used in Indian snacks and sweets.', 'Seller': 'AGROZON'},
    26:{'Product Name': 'Birds Eye Chili (Thai Chili)', 'Price': 90, 'Stock': 250, 'Description': "Bird's eye chili (Thai chili), small and fiery peppers used in Thai and Southeast Asian dishes to add intense heat.", 'Seller': 'AGROZON'},
    27:{'Product Name': 'Biryani Masala', 'Price': 100, 'Stock': 150, 'Description': 'Biryani masala, spice blend used to flavor biryani rice dishes.', 'Seller': 'AGROZON'},
    28:{'Product Name': 'Bitter Gourd (Karela)', 'Price': 30, 'Stock': 300, 'Description': 'Fresh bitter gourd, used in Indian cuisine for its health benefits.', 'Seller': 'AGROZON'},
    29:{'Product Name': 'Black Cardamom', 'Price': 120, 'Stock': 150, 'Description': 'Black cardamom pods, smoky flavor used in meat dishes and spice blends.', 'Seller': 'AGROZON'},
    30:{'Product Name': 'Black Cardamom (Badi Elaichi)', 'Price': 250, 'Stock': 100, 'Description': 'Black cardamom (badi elaichi), larger pods with a smoky flavor used in savory dishes and spice blends.', 'Seller': 'AGROZON'},
    31:{'Product Name': 'Black Mustard Seeds (Rai)', 'Price': 60, 'Stock': 300, 'Description': 'Black mustard seeds (rai), small seeds used in tempering for a nutty and slightly spicy flavor.', 'Seller': 'AGROZON'},
    32:{'Product Name': 'Black Peppercorns', 'Price': 120, 'Stock': 250, 'Description': 'Whole black peppercorns, used for seasoning and spice mixes.', 'Seller': 'AGROZON'},
    33:{'Product Name': 'Black Salt (Kala Namak)', 'Price': 60, 'Stock': 250, 'Description': 'Black salt, used in chaats and snacks for its distinct flavor.', 'Seller': 'AGROZON'},
    34:{'Product Name': 'Bottle Gourd (Lauki)', 'Price': 30, 'Stock': 300, 'Description': 'Fresh bottle gourd (lauki), used in Indian curries, sweets, and drinks.', 'Seller': 'AGROZON'},
    35:{'Product Name': 'Brinjal/Eggplant (Baingan)', 'Price': 25, 'Stock': 300, 'Description': 'Brinjal/eggplant (baingan), versatile vegetable used in Indian cooking for making curries, bharta, and snacks like baingan pakora.', 'Seller': 'AGROZON'},
    36:{'Product Name': 'Buddha Hand Citron', 'Price': 1200, 'Stock': 60, 'Description': 'Buddha hand citron, fragrant citrus fruit used for zest and decoration.', 'Seller': 'AGROZON'},
    37:{'Product Name': 'Cabbage (Patta Gobi)', 'Price': 30, 'Stock': 250, 'Description': 'Cabbage (patta gobi), nutritious and versatile vegetable used in Indian cooking for making curries, salads, and pickles.', 'Seller': 'AGROZON'},
    38:{'Product Name': 'Cacao Nibs', 'Price': 150, 'Stock': 40, 'Description': 'Crunchy cacao nibs, great for adding to smoothies and desserts.', 'Seller': 'AGROZON'},
    39:{'Product Name': 'Capsicum (Shimla Mirch)', 'Price': 30, 'Stock': 250, 'Description': 'Capsicum (shimla mirch), bell peppers used in Indian cooking for their sweet flavor and crunchy texture in curries and salads.', 'Seller': 'AGROZON'},
    40:{'Product Name': 'Cardamom Pods', 'Price': 80, 'Stock': 80, 'Description': 'Fragrant cardamom pods, great for adding flavor to desserts and curries.', 'Seller': 'AGROZON'},
    41:{'Product Name': 'Cardamom Powder', 'Price': 80, 'Stock': 80, 'Description': 'Ground cardamom powder, adds aromatic flavor to desserts and beverages.', 'Seller': 'AGROZON'},
    42:{'Product Name': 'Cardamom Spice Pods', 'Price': 80, 'Stock': 80, 'Description': 'Ground cardamom spice pods, adds aromatic flavor to desserts and beverages.', 'Seller': 'AGROZON'},
    43:{'Product Name': 'Carom Seeds (Ajwain)', 'Price': 90, 'Stock': 180, 'Description': 'Carom seeds (ajwain), small seeds with a strong, bitter taste used in Indian breads and snacks.', 'Seller': 'AGROZON'},
    44:{'Product Name': 'Cashew Butter', 'Price': 180, 'Stock': 40, 'Description': 'Smooth and creamy cashew butter, a nutritious spread.', 'Seller': 'AGROZON'},
    45:{'Product Name': 'Cashew Milk', 'Price': 120, 'Stock': 60, 'Description': 'Creamy cashew milk, dairy-free alternative for smoothies and cereals.', 'Seller': 'AGROZON'},
    46:{'Product Name': 'Cashew Nuts (Kaju)', 'Price': 400, 'Stock': 100, 'Description': 'Whole cashew nuts, used in Indian curries, sweets, and snacks.', 'Seller': 'AGROZON'},
    47:{'Product Name': 'Cassia Bark (Indian Cinnamon)', 'Price': 100, 'Stock': 150, 'Description': 'Cassia bark, similar to cinnamon, used in spice blends and desserts.', 'Seller': 'AGROZON'},
    48:{'Product Name': 'Cauliflower (Phool Gobi)', 'Price': 40, 'Stock': 200, 'Description': 'Cauliflower (phool gobi), versatile vegetable used in Indian cooking for making curries, stir-fries, and snacks like pakoras.', 'Seller': 'AGROZON'},
    49:{'Product Name': 'Chaat Masala', 'Price': 80, 'Stock': 150, 'Description': 'Chaat masala, tangy spice blend used in street food and snacks.', 'Seller': 'AGROZON'},
    50:{'Product Name': 'Champagne Grapes', 'Price': 600, 'Stock': 60, 'Description': 'Champagne grapes, small and sweet with a hint of tartness.', 'Seller': 'AGROZON'},
    51:{'Product Name': 'Chana Dal', 'Price': 80, 'Stock': 120, 'Description': 'Chana dal, split chickpeas used in Indian cooking to make dal and snacks like pakoras.', 'Seller': 'AGROZON'},
    52:{'Product Name': 'Chana Masala', 'Price': 80, 'Stock': 150, 'Description': 'Chana masala spice blend, used to prepare chickpea curry.', 'Seller': 'AGROZON'},
    53:{'Product Name': 'Cherimoya (Custard Apple)', 'Price': 500, 'Stock': 60, 'Description': 'Cherimoya (custard apple), creamy fruit with a tropical taste.', 'Seller': 'AGROZON'},
    54:{'Product Name': 'Chia Seed Pudding', 'Price': 120, 'Stock': 50, 'Description': 'Creamy chia seed pudding, packed with omega-3s.', 'Seller': 'AGROZON'},
    55:{'Product Name': 'Chia Seeds', 'Price': 250, 'Stock': 50, 'Description': 'Nutrient-dense chia seeds, rich in omega-3 fatty acids.', 'Seller': 'AGROZON'},
    56:{'Product Name': 'Chicken Masala', 'Price': 100, 'Stock': 150, 'Description': 'Chicken masala spice blend, used to prepare chicken curries and dishes.', 'Seller': 'AGROZON'},
    57:{'Product Name': 'Chili Flakes', 'Price': 30, 'Stock': 120, 'Description': 'Crushed chili flakes, adds heat and flavor to dishes.', 'Seller': 'AGROZON'},
    58:{'Product Name': 'Chili Flakes (Indian)', 'Price': 80, 'Stock': 150, 'Description': 'Indian chili flakes, adds heat and flavor to dishes like pizzas and pastas.', 'Seller': 'AGROZON'},
    59:{'Product Name': 'Chili Pepper Flakes', 'Price': 30, 'Stock': 120, 'Description': 'Crushed chili pepper flakes, adds heat and flavor to dishes.', 'Seller': 'AGROZON'},
    60:{'Product Name': 'Chili Pepper Powder', 'Price': 30, 'Stock': 120, 'Description': 'Spicy chili pepper powder, perfect for Tex-Mex and Indian dishes.', 'Seller': 'AGROZON'},
    61:{'Product Name': 'Chili Powder', 'Price': 30, 'Stock': 120, 'Description': 'Spicy chili powder blend, perfect for Tex-Mex and Indian dishes.', 'Seller': 'AGROZON'},
    62:{'Product Name': 'Chinese Five Spice Powder', 'Price': 80, 'Stock': 200, 'Description': 'Chinese five spice powder, blend of five spices including star anise, cloves, cinnamon, Sichuan pepper, and fennel seeds used in Chinese cooking.', 'Seller': 'AGROZON'},
    63:{'Product Name': 'Chinese Rice Vinegar', 'Price': 100, 'Stock': 250, 'Description': 'Chinese rice vinegar, mild and slightly sweet vinegar made from fermented rice used in Chinese cooking.', 'Seller': 'AGROZON'},
    64:{'Product Name': 'Chinese Sesame Oil', 'Price': 90, 'Stock': 200, 'Description': 'Chinese sesame oil, aromatic oil made from roasted sesame seeds used in Chinese cooking for flavoring stir-fries, noodles, and marinades.', 'Seller': 'AGROZON'},
    65:{'Product Name': 'Chironji Seeds', 'Price': 100, 'Stock': 150, 'Description': 'Chironji seeds, used in Indian sweets and desserts for their nutty flavor.', 'Seller': 'AGROZON'},
    66:{'Product Name': 'Cinnamon Powder', 'Price': 50, 'Stock': 120, 'Description': 'Ground cinnamon powder, versatile spice for baking and cooking.', 'Seller': 'AGROZON'},
    67:{'Product Name': 'Cinnamon Sticks', 'Price': 60, 'Stock': 120, 'Description': 'Whole cinnamon sticks, perfect for infusing flavor in beverages and dishes.', 'Seller': 'AGROZON'},
    68:{'Product Name': 'Cinnamon Sticks (Dalchini)', 'Price': 150, 'Stock': 200, 'Description': 'Cinnamon sticks (dalchini), aromatic bark used whole or ground in sweet and savory dishes.', 'Seller': 'AGROZON'},
    69:{'Product Name': 'Cloves', 'Price': 180, 'Stock': 150, 'Description': 'Whole cloves, aromatic and used in curries, rice dishes, and desserts.', 'Seller': 'AGROZON'},
    70:{'Product Name': 'Cloves (Laung)', 'Price': 180, 'Stock': 150, 'Description': 'Cloves (laung), aromatic flower buds used in Indian cuisine for their warm, sweet flavor.', 'Seller': 'AGROZON'},
    71:{'Product Name': 'Cluster Beans (Gavar)', 'Price': 40, 'Stock': 250, 'Description': 'Fresh cluster beans, used in Indian curries and stir-fries.', 'Seller': 'AGROZON'},
    72:{'Product Name': 'Cluster Beans (Gawar Phali)', 'Price': 60, 'Stock': 100, 'Description': 'Cluster beans (gawar phali), crunchy and slightly bitter beans used in Indian curries and stir-fries.', 'Seller': 'AGROZON'},
    73:{'Product Name': 'Coconut (Fresh)', 'Price': 50, 'Stock': 300, 'Description': 'Fresh coconut, grated or whole, used in Indian sweets and savory dishes.', 'Seller': 'AGROZON'},
    74:{'Product Name': 'Coconut (Nariyal)', 'Price': 40, 'Stock': 200, 'Description': 'Coconut (nariyal), versatile fruit used in various forms in Indian cooking, from coconut milk to grated coconut in sweets.', 'Seller': 'AGROZON'},
    75:{'Product Name': 'Coconut Almond Butter', 'Price': 180, 'Stock': 50, 'Description': 'Creamy blend of coconut and almond butter, perfect for spreads.', 'Seller': 'AGROZON'},
    76:{'Product Name': 'Coconut Cream', 'Price': 150, 'Stock': 60, 'Description': 'Rich and creamy coconut cream, ideal for curries and desserts.', 'Seller': 'AGROZON'},
    77:{'Product Name': 'Coconut Flour Pancake Mix', 'Price': 120, 'Stock': 60, 'Description': 'Gluten-free coconut flour pancake mix, easy to prepare.', 'Seller': 'AGROZON'},
    78:{'Product Name': 'Coconut Milk', 'Price': 120, 'Stock': 60, 'Description': 'Creamy coconut milk, ideal for curries and smoothies.', 'Seller': 'AGROZON'},
    79:{'Product Name': 'Coconut Milk (Canned)', 'Price': 80, 'Stock': 150, 'Description': 'Canned coconut milk, used in curries, desserts, and drinks.', 'Seller': 'AGROZON'},
    80:{'Product Name': 'Coconut Milk Powder', 'Price': 100, 'Stock': 60, 'Description': 'Convenient coconut milk powder, great for curries and smoothies.', 'Seller': 'AGROZON'},
    81:{'Product Name': 'Coconut Oil', 'Price': 100, 'Stock': 60, 'Description': 'Versatile coconut oil, ideal for cooking, skincare, and haircare.', 'Seller': 'AGROZON'},
    82:{'Product Name': 'Coconut Sugar', 'Price': 80, 'Stock': 200, 'Description': 'Coconut sugar, natural sweetener used in Indian sweets and drinks.', 'Seller': 'AGROZON'},
    83:{'Product Name': 'Coconut Water with Pulp', 'Price': 120, 'Stock': 60, 'Description': 'Refreshing coconut water with pulp, hydrating and nutritious.', 'Seller': 'AGROZON'},
    84:{'Product Name': 'Coconut Yogurt', 'Price': 120, 'Stock': 70, 'Description': 'Creamy coconut-based yogurt, dairy-free and probiotic-rich.', 'Seller': 'AGROZON'},
    85:{'Product Name': 'Cold-Pressed Flaxseed Oil', 'Price': 180, 'Stock': 50, 'Description': 'Nutrient-rich cold-pressed flaxseed oil, high in omega-3 fatty acids.', 'Seller': 'AGROZON'},
    86:{'Product Name': 'Cold-Pressed Hemp Seed Oil', 'Price': 220, 'Stock': 50, 'Description': 'Nutrient-rich cold-pressed hemp seed oil, high in omega-3 and omega-6 fatty acids.', 'Seller': 'AGROZON'},
    87:{'Product Name': 'Cold-Pressed Olive Oil', 'Price': 180, 'Stock': 30, 'Description': 'Extra virgin olive oil, perfect for salads and cooking.', 'Seller': 'AGROZON'},
    88:{'Product Name': 'Cold-Pressed Pumpkin Seed Oil', 'Price': 200, 'Stock': 30, 'Description': 'Nutrient-rich cold-pressed pumpkin seed oil, high in antioxidants.', 'Seller': 'AGROZON'},
    89:{'Product Name': 'Cold-Pressed Walnut Oil', 'Price': 250, 'Stock': 40, 'Description': 'Nutrient-rich cold-pressed walnut oil, ideal for dressings and dips.', 'Seller': 'AGROZON'},
    90:{'Product Name': 'Coriander Chutney (Dhania Chutney)', 'Price': 70, 'Stock': 150, 'Description': 'Coriander chutney (dhania chutney), tangy and spicy condiment made from fresh coriander leaves, served with snacks and sandwiches.', 'Seller': 'AGROZON'},
    91:{'Product Name': 'Coriander Leaves (Cilantro)', 'Price': 20, 'Stock': 400, 'Description': 'Fresh coriander leaves (cilantro), used as a garnish and in chutneys.', 'Seller': 'AGROZON'},
    92:{'Product Name': 'Coriander Powder (Dhania Powder)', 'Price': 30, 'Stock': 250, 'Description': 'Coriander powder (dhania powder), ground coriander seeds used to flavor curries, soups, and marinades.', 'Seller': 'AGROZON'},
    93:{'Product Name': 'Coriander Seeds', 'Price': 50, 'Stock': 300, 'Description': 'Whole coriander seeds, used in spice blends and curry powders.', 'Seller': 'AGROZON'},
    94:{'Product Name': 'Coriander Seeds (Dhania)', 'Price': 70, 'Stock': 300, 'Description': 'Coriander seeds (dhania), citrusy and nutty seeds used whole or ground in curries, pickles, and spice blends.', 'Seller': 'AGROZON'},
    95:{'Product Name': 'Cumin Powder', 'Price': 40, 'Stock': 100, 'Description': 'Ground cumin powder, essential for Indian and Middle Eastern cuisines.', 'Seller': 'AGROZON'},
    96:{'Product Name': 'Cumin Powder (Jeera Powder)', 'Price': 40, 'Stock': 200, 'Description': 'Cumin powder (jeera powder), ground cumin seeds used as a seasoning in Indian dishes and spice blends.', 'Seller': 'AGROZON'},
    97:{'Product Name': 'Cumin Seed Powder', 'Price': 40, 'Stock': 100, 'Description': 'Ground cumin seed powder, essential for Indian and Middle Eastern cuisines.', 'Seller': 'AGROZON'},
    98:{'Product Name': 'Cumin Seeds', 'Price': 40, 'Stock': 100, 'Description': 'Whole cumin seeds, essential for Indian and Middle Eastern cuisines.', 'Seller': 'AGROZON'},
    99:{'Product Name': 'Cumin Seeds (Jeera)', 'Price': 80, 'Stock': 250, 'Description': 'Cumin seeds (jeera), earthy and slightly spicy seeds used whole or ground in Indian curries, rice dishes, and snacks.', 'Seller': 'AGROZON'},
    100:{'Product Name': 'Cupuaçu', 'Price': 1000, 'Stock': 70, 'Description': 'Cupuaçu, tropical fruit with a creamy pulp and chocolatey aroma.', 'Seller': 'AGROZON'},
    101:{'Product Name': 'Curry Leaves', 'Price': 30, 'Stock': 300, 'Description': 'Fresh curry leaves, used in South Indian cooking for flavoring.', 'Seller': 'AGROZON'},
    102:{'Product Name': 'Curry Leaves (Kadi Patta)', 'Price': 20, 'Stock': 250, 'Description': 'Curry leaves (kadi patta), aromatic leaves used in South Indian and Sri Lankan cooking for flavoring.', 'Seller': 'AGROZON'},
    103:{'Product Name': 'Curry Powder', 'Price': 100, 'Stock': 150, 'Description': 'Curry powder blend, a mix of spices for preparing curry dishes.', 'Seller': 'AGROZON'},
    104:{'Product Name': 'Dark Chocolate', 'Price': 80, 'Stock': 70, 'Description': 'Rich and indulgent dark chocolate, high in cocoa content.', 'Seller': 'AGROZON'},
    105:{'Product Name': 'Dates (Khajoor)', 'Price': 80, 'Stock': 200, 'Description': 'Fresh dates, sweet and chewy, used in Indian sweets and desserts.', 'Seller': 'AGROZON'},
    106:{'Product Name': 'Desiccated Coconut', 'Price': 70, 'Stock': 120, 'Description': 'Desiccated coconut, dried and grated coconut used in baking, sweets, and curries.', 'Seller': 'AGROZON'},
    107:{'Product Name': 'Dragon Fruit', 'Price': 1000, 'Stock': 40, 'Description': 'Exotic dragon fruit, known for its vibrant colors and refreshing taste.', 'Seller': 'AGROZON'},
    108:{'Product Name': 'Dried Basil', 'Price': 25, 'Stock': 100, 'Description': 'Dried basil flakes, versatile herb for Italian dishes and salads.', 'Seller': 'AGROZON'},
    109:{'Product Name': 'Dried Fenugreek Leaves (Kasuri Methi)', 'Price': 70, 'Stock': 200, 'Description': 'Dried fenugreek leaves, used in Indian dishes for flavor and aroma.', 'Seller': 'AGROZON'},
    110:{'Product Name': 'Dried Fruits Mix', 'Price': 150, 'Stock': 100, 'Description': 'Assorted dried fruits mix, used as snacks and in Indian desserts.', 'Seller': 'AGROZON'},
    111:{'Product Name': 'Dried Mango Powder (Amchur)', 'Price': 50, 'Stock': 120, 'Description': 'Dried mango powder (amchur), tangy spice made from dried unripe mangoes, used in Indian cuisine.', 'Seller': 'AGROZON'},
    112:{'Product Name': 'Dried Mango Slices (Aam Papad)', 'Price': 80, 'Stock': 150, 'Description': 'Dried mango slices, sweet and tangy snack in Indian households.', 'Seller': 'AGROZON'},
    113:{'Product Name': 'Dried Oregano', 'Price': 25, 'Stock': 120, 'Description': 'Aromatic dried oregano, essential for Mediterranean dishes.', 'Seller': 'AGROZON'},
    114:{'Product Name': 'Dried Oregano Leaves', 'Price': 25, 'Stock': 120, 'Description': 'Dried oregano leaves, aromatic herb for Mediterranean dishes.', 'Seller': 'AGROZON'},
    115:{'Product Name': 'Dried Oregano Spice', 'Price': 25, 'Stock': 120, 'Description': 'Dried oregano spice, aromatic herb for Mediterranean dishes.', 'Seller': 'AGROZON'},
    116:{'Product Name': 'Drumsticks (Moringa)', 'Price': 60, 'Stock': 150, 'Description': 'Fresh drumsticks, used in South Indian and Bengali curries.', 'Seller': 'AGROZON'},
    117:{'Product Name': 'Drumsticks (Shinga)', 'Price': 50, 'Stock': 120, 'Description': 'Drumsticks (shinga), long, green pods used in South Indian and Bengali cuisine.', 'Seller': 'AGROZON'},
    118:{'Product Name': 'Durian', 'Price': 1300, 'Stock': 20, 'Description': 'King of fruits, durian, known for its strong odor and creamy texture.', 'Seller': 'AGROZON'},
    119:{'Product Name': 'Extra Virgin Coconut Oil', 'Price': 150, 'Stock': 60, 'Description': 'Cold-pressed extra virgin coconut oil, versatile for cooking and skincare.', 'Seller': 'AGROZON'},
    120:{'Product Name': 'Feijoa (Pineapple Guava)', 'Price': 1000, 'Stock': 70, 'Description': 'Feijoa (pineapple guava), aromatic fruit with a tropical taste.', 'Seller': 'AGROZON'},
    121:{'Product Name': 'Fennel Seed Powder', 'Price': 40, 'Stock': 100, 'Description': 'Ground fennel seed powder, aromatic spice for cooking and teas.', 'Seller': 'AGROZON'},
    122:{'Product Name': 'Fennel Seed Spice', 'Price': 40, 'Stock': 100, 'Description': 'Ground fennel seed spice, aromatic and great for teas and cooking.', 'Seller': 'AGROZON'},
    123:{'Product Name': 'Fennel Seeds', 'Price': 40, 'Stock': 100, 'Description': 'Whole fennel seeds, aromatic and great for teas and cooking.', 'Seller': 'AGROZON'},
    124:{'Product Name': 'Fennel Seeds (Saunf)', 'Price': 70, 'Stock': 200, 'Description': 'Fennel seeds, used as a mouth freshener and in spice blends.', 'Seller': 'AGROZON'},
    125:{'Product Name': 'Fenugreek Leaves (Kasuri Methi)', 'Price': 40, 'Stock': 200, 'Description': 'Fenugreek leaves (kasuri methi), dried leaves with a slightly bitter taste used in Indian cooking for flavoring.', 'Seller': 'AGROZON'},
    126:{'Product Name': 'Fenugreek Leaves (Methi)', 'Price': 40, 'Stock': 200, 'Description': 'Fresh fenugreek leaves, used in Indian curries and parathas.', 'Seller': 'AGROZON'},
    127:{'Product Name': 'Fenugreek Seeds', 'Price': 70, 'Stock': 200, 'Description': 'Fenugreek seeds, used in spice blends and for medicinal purposes.', 'Seller': 'AGROZON'},
    128:{'Product Name': 'Fenugreek Seeds (Methi Dana)', 'Price': 60, 'Stock': 300, 'Description': 'Fenugreek seeds (methi dana), bitter and nutty seeds used in Indian and Middle Eastern cooking for flavoring curries, pickles, and spice blends.', 'Seller': 'AGROZON'},
    129:{'Product Name': 'Fish Curry Masala', 'Price': 100, 'Stock': 150, 'Description': 'Fish curry masala, spice blend used to prepare fish curries.', 'Seller': 'AGROZON'},
    130:{'Product Name': 'Fish Sauce', 'Price': 120, 'Stock': 180, 'Description': 'Fish sauce, salty and savory condiment made from fermented fish used as a seasoning in Thai and Southeast Asian cuisines.', 'Seller': 'AGROZON'},
    131:{'Product Name': 'Free-Range Chicken', 'Price': 400, 'Stock': 30, 'Description': 'Certified organic free-range chicken, raised with care.', 'Seller': 'AGROZON'},
    132:{'Product Name': 'Free-Range Chicken Eggs', 'Price': 6, 'Stock': 200, 'Description': 'Farm-fresh free-range chicken eggs, high in protein.', 'Seller': 'AGROZON'},
    133:{'Product Name': 'Free-Range Duck Eggs', 'Price': 8, 'Stock': 150, 'Description': 'Rich and flavorful free-range duck eggs, great for baking and cooking.', 'Seller': 'AGROZON'},
    134:{'Product Name': 'Free-Range Eggs', 'Price': 5, 'Stock': 200, 'Description': 'Farm-fresh free-range eggs from happy hens.', 'Seller': 'AGROZON'},
    135:{'Product Name': 'Free-Range Goose Eggs', 'Price': 10, 'Stock': 100, 'Description': 'Rich and creamy free-range goose eggs, perfect for baking.', 'Seller': 'AGROZON'},
    136:{'Product Name': 'Free-Range Quail Eggs', 'Price': 12, 'Stock': 50, 'Description': 'Delicate and flavorful free-range quail eggs, great for appetizers.', 'Seller': 'AGROZON'},
    137:{'Product Name': 'Free-Range Quail Meat', 'Price': 300, 'Stock': 25, 'Description': 'Tender and flavorful free-range quail meat, great for gourmet dishes.', 'Seller': 'AGROZON'},
    138:{'Product Name': 'Free-Range Rabbit Meat', 'Price': 500, 'Stock': 20, 'Description': 'Tender and lean free-range rabbit meat, versatile for various dishes.', 'Seller': 'AGROZON'},
    139:{'Product Name': 'Free-Range Turkey', 'Price': 450, 'Stock': 25, 'Description': 'Organic free-range turkey, perfect for holiday feasts.', 'Seller': 'AGROZON'},
    140:{'Product Name': 'Fresh Almonds', 'Price': 350, 'Stock': 100, 'Description': 'Premium quality almonds, sourced from California.', 'Seller': 'AGROZON'},
    141:{'Product Name': 'Fresh Blueberries', 'Price': 180, 'Stock': 80, 'Description': 'Sweet and juicy fresh blueberries, packed with antioxidants.', 'Seller': 'AGROZON'},
    142:{'Product Name': 'Fresh Curry Leaves (Kadi Patta)', 'Price': 20, 'Stock': 300, 'Description': 'Fresh curry leaves (kadi patta), aromatic leaves used in South Indian and Sri Lankan cooking for flavoring.', 'Seller': 'AGROZON'},
    143:{'Product Name': 'Galangal', 'Price': 150, 'Stock': 180, 'Description': 'Galangal, rhizome with a pungent and peppery flavor used in Thai and Southeast Asian cooking, especially in curries and soups.', 'Seller': 'AGROZON'},
    144:{'Product Name': 'Garam Masala', 'Price': 120, 'Stock': 150, 'Description': 'Garam masala spice blend, used as a finishing spice in many Indian dishes.', 'Seller': 'AGROZON'},
    145:{'Product Name': 'Garlic', 'Price': 30, 'Stock': 300, 'Description': 'Fresh garlic cloves, used in Indian curries, marinades, and sauces.', 'Seller': 'AGROZON'},
    146:{'Product Name': 'Garlic (Lehsun)', 'Price': 20, 'Stock': 300, 'Description': 'Garlic (lehsun), pungent bulb used in Indian cooking for its flavor and health benefits.', 'Seller': 'AGROZON'},
    147:{'Product Name': 'Ghee', 'Price': 120, 'Stock': 40, 'Description': 'Pure clarified butter, ideal for cooking and flavoring.', 'Seller': 'AGROZON'},
    148:{'Product Name': 'Ginger', 'Price': 40, 'Stock': 250, 'Description': 'Fresh ginger root, used in Indian cooking for flavoring and health benefits.', 'Seller': 'AGROZON'},
    149:{'Product Name': 'Ginger (Adrak)', 'Price': 40, 'Stock': 200, 'Description': 'Ginger (adrak), aromatic and pungent root used in Indian cooking for its spicy and medicinal properties.', 'Seller': 'AGROZON'},
    150:{'Product Name': 'Gluten-Free Pasta', 'Price': 100, 'Stock': 100, 'Description': 'Corn and rice blend gluten-free pasta, easy to cook.', 'Seller': 'AGROZON'},
    151:{'Product Name': 'Golden Kiwifruit', 'Price': 950, 'Stock': 50, 'Description': 'Golden kiwifruit, sweeter than green kiwis with a tropical flavor.', 'Seller': 'AGROZON'},
    152:{'Product Name': 'Grass-Fed Bison Burgers', 'Price': 800, 'Stock': 15, 'Description': 'Juicy grass-fed bison burgers, lean and full of flavor.', 'Seller': 'AGROZON'},
    153:{'Product Name': 'Grass-Fed Butter', 'Price': 120, 'Stock': 80, 'Description': 'Rich and flavorful grass-fed butter, perfect for cooking and baking.', 'Seller': 'AGROZON'},
    154:{'Product Name': 'Grass-Fed Goat Cheese', 'Price': 180, 'Stock': 50, 'Description': 'Nutty and tangy grass-fed goat cheese, perfect for salads and sandwiches.', 'Seller': 'AGROZON'},
    155:{'Product Name': 'Grass-Fed Gouda Cheese', 'Price': 200, 'Stock': 40, 'Description': 'Rich and nutty grass-fed Gouda cheese, aged to perfection.', 'Seller': 'AGROZON'},
    156:{'Product Name': 'Grass-Fed Lamb Chops', 'Price': 700, 'Stock': 15, 'Description': 'Tender grass-fed lamb chops, perfect for gourmet meals.', 'Seller': 'AGROZON'},
    157:{'Product Name': 'Grass-Fed Lamb Shank', 'Price': 750, 'Stock': 15, 'Description': 'Flavorful grass-fed lamb shank, ideal for slow cooking.', 'Seller': 'AGROZON'},
    158:{'Product Name': 'Greek Style Yogurt', 'Price': 100, 'Stock': 80, 'Description': 'Creamy and thick Greek style yogurt, high in protein.', 'Seller': 'AGROZON'},
    159:{'Product Name': 'Greek Yogurt', 'Price': 60, 'Stock': 60, 'Description': 'Thick and creamy Greek yogurt, high in protein.', 'Seller': 'AGROZON'},
    160:{'Product Name': 'Green Cardamom', 'Price': 800, 'Stock': 100, 'Description': 'Green cardamom pods, aromatic and used in both sweet and savory dishes.', 'Seller': 'AGROZON'},
    161:{'Product Name': 'Green Cardamom (Choti Elaichi)', 'Price': 300, 'Stock': 100, 'Description': 'Green cardamom (choti elaichi), small pods with a sweet and floral flavor used in Indian sweets, chai, and rice dishes.', 'Seller': 'AGROZON'},
    162:{'Product Name': 'Green Chili (Fresh)', 'Price': 20, 'Stock': 350, 'Description': 'Fresh green chili peppers, used in Indian cooking for heat and flavor.', 'Seller': 'AGROZON'},
    163:{'Product Name': 'Green Chili Peppers (Hari Mirch)', 'Price': 20, 'Stock': 400, 'Description': 'Green chili peppers (hari mirch), spicy peppers used fresh or dried in Indian cooking for heat.', 'Seller': 'AGROZON'},
    164:{'Product Name': 'Green Chilies (Hari Mirch)', 'Price': 30, 'Stock': 250, 'Description': 'Green chilies (hari mirch), spicy peppers used to add heat and flavor to Indian curries, snacks, and pickles.', 'Seller': 'AGROZON'},
    165:{'Product Name': 'Green Papaya (Papita)', 'Price': 50, 'Stock': 200, 'Description': 'Fresh green papaya, used in salads, curries, and pickles.', 'Seller': 'AGROZON'},
    166:{'Product Name': 'Green Peas (Hari Matar)', 'Price': 30, 'Stock': 250, 'Description': 'Green peas (hari matar), sweet and tender peas used in Indian cooking for making curries, pulao, and snacks.', 'Seller': 'AGROZON'},
    167:{'Product Name': 'Green Tea Leaves', 'Price': 120, 'Stock': 80, 'Description': 'Premium loose green tea leaves, antioxidant-rich.', 'Seller': 'AGROZON'},
    168:{'Product Name': 'Ground Cinnamon', 'Price': 50, 'Stock': 120, 'Description': 'Ground cinnamon, versatile spice for baking and cooking.', 'Seller': 'AGROZON'},
    169:{'Product Name': 'Ground Cinnamon Spice', 'Price': 50, 'Stock': 120, 'Description': 'Ground cinnamon spice, versatile spice for baking and cooking.', 'Seller': 'AGROZON'},
    170:{'Product Name': 'Ground Nutmeg', 'Price': 40, 'Stock': 120, 'Description': 'Ground nutmeg, warm and aromatic spice for sweet and savory dishes.', 'Seller': 'AGROZON'},
    171:{'Product Name': 'Ground Nutmeg Powder', 'Price': 40, 'Stock': 120, 'Description': 'Ground nutmeg powder, warm and aromatic spice for sweet and savory dishes.', 'Seller': 'AGROZON'},
    172:{'Product Name': 'Ground Paprika', 'Price': 30, 'Stock': 120, 'Description': 'Ground paprika, adds color and mild heat to dishes.', 'Seller': 'AGROZON'},
    173:{'Product Name': 'Ground Saffron', 'Price': 300, 'Stock': 10, 'Description': 'Ground saffron, adds rich color and flavor to rice and seafood dishes.', 'Seller': 'AGROZON'},
    174:{'Product Name': 'Ground Saffron Spice', 'Price': 350, 'Stock': 10, 'Description': 'Ground saffron spice, luxurious spice for rice dishes and desserts.', 'Seller': 'AGROZON'},
    175:{'Product Name': 'Heirloom Cherry Tomatoes', 'Price': 550, 'Stock': 105, 'Description': 'Colorful heirloom cherry tomatoes, bursting with sweet and tangy flavors.', 'Seller': 'AGROZON'},
    176:{'Product Name': 'Himalayan Pink Salt', 'Price': 20, 'Stock': 150, 'Description': 'Pure and natural Himalayan pink salt, rich in minerals.', 'Seller': 'AGROZON'},
    177:{'Product Name': 'Honey Roasted Almonds', 'Price': 250, 'Stock': 50, 'Description': 'Crunchy almonds coated in honey, a delightful snack.', 'Seller': 'AGROZON'},
    178:{'Product Name': 'Honey Roasted Cashews', 'Price': 280, 'Stock': 40, 'Description': 'Crunchy cashews coated in honey, a delicious snack.', 'Seller': 'AGROZON'},
    179:{'Product Name': 'Idli Rice', 'Price': 50, 'Stock': 200, 'Description': 'Idli rice, short-grain parboiled rice used to make South Indian idlis, a staple breakfast item.', 'Seller': 'AGROZON'},
    180:{'Product Name': 'Indian Ajwain Seeds', 'Price': 90, 'Stock': 200, 'Description': 'Indian ajwain seeds, small seeds with a strong, bitter taste used in Indian breads, snacks, and spice blends for their digestive properties.', 'Seller': 'AGROZON'},
    181:{'Product Name': 'Indian Asafoetida (Hing)', 'Price': 180, 'Stock': 120, 'Description': 'Indian asafoetida (hing), pungent spice used in Indian vegetarian cooking for its onion-like flavor.', 'Seller': 'AGROZON'},
    182:{'Product Name': 'Indian Bay Leaf (Tej Patta)', 'Price': 80, 'Stock': 200, 'Description': 'Indian bay leaf (tej patta), aromatic leaves used in Indian cooking for adding flavor to curries, biryanis, and rice dishes.', 'Seller': 'AGROZON'},
    183:{'Product Name': 'Indian Bay Leaves (Tej Patta)', 'Price': 80, 'Stock': 200, 'Description': 'Indian bay leaves (tej patta), aromatic leaves used in Indian cooking for adding flavor to curries, biryanis, and rice dishes.', 'Seller': 'AGROZON'},
    184:{'Product Name': 'Indian Black Cardamom (Badi Elaichi)', 'Price': 250, 'Stock': 100, 'Description': 'Indian black cardamom (badi elaichi), larger pods with a smoky flavor used in savory dishes and spice blends in Indian cooking.', 'Seller': 'AGROZON'},
    185:{'Product Name': 'Indian Black Mustard Seeds (Rai)', 'Price': 60, 'Stock': 300, 'Description': 'Indian black mustard seeds (rai), small seeds used in tempering for a nutty and slightly spicy flavor in Indian cuisine.', 'Seller': 'AGROZON'},
    186:{'Product Name': 'Indian Black Salt (Kala Namak)', 'Price': 100, 'Stock': 180, 'Description': 'Indian black salt (kala namak), pungent rock salt used in Indian cooking for chaats, chutneys, and snacks.', 'Seller': 'AGROZON'},
    187:{'Product Name': 'Indian Carom Seeds (Ajwain)', 'Price': 90, 'Stock': 180, 'Description': 'Indian carom seeds (ajwain), small seeds with a strong, bitter taste used in Indian breads and snacks for their digestive properties.', 'Seller': 'AGROZON'},
    188:{'Product Name': 'Indian Cinnamon Bark (Dalchini)', 'Price': 180, 'Stock': 150, 'Description': 'Indian cinnamon bark (dalchini), aromatic bark used in Indian cooking for adding flavor to sweets, curries, and rice dishes.', 'Seller': 'AGROZON'},
    189:{'Product Name': 'Indian Cinnamon Sticks (Dalchini)', 'Price': 150, 'Stock': 200, 'Description': 'Indian cinnamon sticks (dalchini), aromatic bark used whole or ground in sweet and savory dishes in Indian cooking.', 'Seller': 'AGROZON'},
    190:{'Product Name': 'Indian Cloves (Laung)', 'Price': 180, 'Stock': 150, 'Description': 'Indian cloves (laung), aromatic flower buds used in Indian cooking for their warm, sweet flavor.', 'Seller': 'AGROZON'},
    191:{'Product Name': 'Indian Coriander Seeds (Dhania)', 'Price': 70, 'Stock': 300, 'Description': 'Indian coriander seeds (dhania), citrusy and nutty seeds used whole or ground in curries, pickles, and spice blends in Indian cuisine.', 'Seller': 'AGROZON'},
    192:{'Product Name': 'Indian Cumin Seeds (Jeera)', 'Price': 80, 'Stock': 250, 'Description': 'Indian cumin seeds (jeera), earthy and slightly spicy seeds used whole or ground in Indian curries, rice dishes, and snacks.', 'Seller': 'AGROZON'},
    193:{'Product Name': 'Indian Curry Leaves', 'Price': 50, 'Stock': 200, 'Description': 'Indian curry leaves, aromatic leaves used in South Indian cooking to add flavor to curries, chutneys, and stir-fries.', 'Seller': 'AGROZON'},
    194:{'Product Name': 'Indian Fenugreek Leaves (Kasuri Methi)', 'Price': 120, 'Stock': 200, 'Description': 'Indian fenugreek leaves (kasuri methi), herb with a slightly bitter taste used in Indian curries, breads, and snacks.', 'Seller': 'AGROZON'},
    195:{'Product Name': 'Indian Gooseberry (Amla)', 'Price': 60, 'Stock': 250, 'Description': 'Fresh Indian gooseberry, high in vitamin C and used in Ayurvedic medicine.', 'Seller': 'AGROZON'},
    196:{'Product Name': 'Indian Green Cardamom (Choti Elaichi)', 'Price': 300, 'Stock': 100, 'Description': 'Indian green cardamom (choti elaichi), aromatic pods used in Indian sweets, chai, and rice dishes for their sweet and floral flavor.', 'Seller': 'AGROZON'},
    197:{'Product Name': 'Indian Long Pepper (Pipli)', 'Price': 100, 'Stock': 180, 'Description': 'Indian long pepper (pipli), spicy and pungent spice used in Indian cooking for flavoring curries, pickles, and spice blends.', 'Seller': 'AGROZON'},
    198:{'Product Name': 'Indian Long Pepper (Pippali)', 'Price': 100, 'Stock': 250, 'Description': 'Indian long pepper (pippali), spicy and pungent spice used in Indian cooking for flavoring curries, pickles, and spice blends.', 'Seller': 'AGROZON'},
    199:{'Product Name': 'Indian Mace (Javitri)', 'Price': 200, 'Stock': 150, 'Description': 'Indian mace (javitri), outer covering of nutmeg seed with a similar but milder flavor, used in spice blends and savory dishes.', 'Seller': 'AGROZON'},
    200:{'Product Name': 'Indian Mustard Seeds (Sarson)', 'Price': 60, 'Stock': 300, 'Description': 'Indian mustard seeds (sarson), mild and slightly sweet seeds used in pickles, sauces, and spice mixes in Indian cuisine.', 'Seller': 'AGROZON'},
    201:{'Product Name': 'Indian Saffron (Kesar)', 'Price': 500, 'Stock': 50, 'Description': 'Indian saffron (kesar), aromatic threads used to add color and flavor to Indian sweets, rice dishes, and drinks.', 'Seller': 'AGROZON'},
    202:{'Product Name': 'Indian Star Anise (Chakra Phool)', 'Price': 120, 'Stock': 200, 'Description': 'Indian star anise (chakra phool), star-shaped spice used in Indian cooking for adding flavor to biryanis, masalas, and desserts.', 'Seller': 'AGROZON'},
    203:{'Product Name': 'Indian Stone Flower (Dagad Phool)', 'Price': 150, 'Stock': 200, 'Description': 'Indian stone flower (dagad phool), lichen used in Indian cooking for its earthy and aromatic flavor in spice blends and masalas.', 'Seller': 'AGROZON'},
    204:{'Product Name': 'Indian Tamarind (Imli)', 'Price': 80, 'Stock': 200, 'Description': 'Indian tamarind (imli), sour fruit used in Indian cooking for its tartness in chutneys, curries, and sauces.', 'Seller': 'AGROZON'},
    205:{'Product Name': 'Indian White Poppy Seeds (Khus Khus)', 'Price': 100, 'Stock': 250, 'Description': 'Indian white poppy seeds (khus khus), mild and nutty seeds used in Indian sweets, gravies, and spice blends.', 'Seller': 'AGROZON'},
    206:{'Product Name': 'Jabuticaba (Brazilian Grape Tree)', 'Price': 1000, 'Stock': 70, 'Description': 'Jabuticaba, grape-like fruit with a sweet, juicy pulp.', 'Seller': 'AGROZON'},
    207:{'Product Name': 'Jackfruit (Kathal)', 'Price': 80, 'Stock': 150, 'Description': 'Fresh jackfruit, used in savory dishes, curries, and desserts.', 'Seller': 'AGROZON'},
    208:{'Product Name': 'Jaggery', 'Price': 80, 'Stock': 200, 'Description': 'Jaggery, unrefined cane sugar used in sweets and desserts.', 'Seller': 'AGROZON'},
    209:{'Product Name': 'Jaggery (Gur)', 'Price': 100, 'Stock': 200, 'Description': 'Jaggery (gur), unrefined cane sugar used in Indian cooking for its caramel-like flavor and sweetness.', 'Seller': 'AGROZON'},
    210:{'Product Name': 'Jamaican Ackee', 'Price': 1200, 'Stock': 50, 'Description': 'Jamaican ackee, exotic fruit with a buttery texture and mild flavor.', 'Seller': 'AGROZON'},
    211:{'Product Name': 'Japanese Mango (Kesar)', 'Price': 1200, 'Stock': 30, 'Description': 'Rare Japanese mango (kesar), known for its sweet, creamy flesh.', 'Seller': 'AGROZON'},
    212:{'Product Name': 'Japanese Mirin', 'Price': 120, 'Stock': 180, 'Description': 'Japanese mirin, sweet rice wine used in Japanese cuisine for adding sweetness and depth of flavor to sauces, glazes, and marinades.', 'Seller': 'AGROZON'},
    213:{'Product Name': 'Japanese Rice Vinegar', 'Price': 80, 'Stock': 200, 'Description': 'Japanese rice vinegar, mild and slightly sweet vinegar made from fermented rice used in Japanese cooking.', 'Seller': 'AGROZON'},
    214:{'Product Name': 'Japanese Soy Sauce (Shoyu)', 'Price': 100, 'Stock': 200, 'Description': 'Japanese soy sauce (shoyu), fermented sauce made from soybeans, wheat, salt, and koji mold used as a seasoning in Japanese cooking.', 'Seller': 'AGROZON'},
    215:{'Product Name': 'Kaffir Lime Leaves', 'Price': 80, 'Stock': 100, 'Description': 'Kaffir lime leaves, aromatic leaves used in Thai and Indian cuisine.', 'Seller': 'AGROZON'},
    216:{'Product Name': 'Kesar (Saffron)', 'Price': 1000, 'Stock': 50, 'Description': 'High-quality saffron threads, known for its color, flavor, and aroma.', 'Seller': 'AGROZON'},
    217:{'Product Name': 'Kiwano (Horned Melon)', 'Price': 1200, 'Stock': 30, 'Description': 'Unique kiwano (horned melon), with a blend of cucumber, kiwi, and banana flavors.', 'Seller': 'AGROZON'},
    218:{'Product Name': 'Kokum', 'Price': 150, 'Stock': 100, 'Description': 'Kokum, dried fruit used in coastal Indian cuisine for its souring properties.', 'Seller': 'AGROZON'},
    219:{'Product Name': 'Kokum Butter', 'Price': 120, 'Stock': 100, 'Description': 'Kokum butter, extracted from the seeds of kokum fruit and used in culinary and cosmetic applications for its moisturizing properties.', 'Seller': 'AGROZON'},
    220:{'Product Name': 'Korean Red Chili Powder (Gochugaru)', 'Price': 120, 'Stock': 180, 'Description': 'Korean red chili powder (gochugaru), coarse ground chili flakes used in Korean cuisine, especially for making kimchi and spicy dishes.', 'Seller': 'AGROZON'},
    221:{'Product Name': 'Korean Soybean Paste (Doenjang)', 'Price': 150, 'Stock': 150, 'Description': 'Korean soybean paste (doenjang), fermented paste made from soybeans and salt used in Korean soups, stews, and marinades.', 'Seller': 'AGROZON'},
    222:{'Product Name': 'Ladyfinger (Bhindi)', 'Price': 30, 'Stock': 300, 'Description': 'Fresh ladyfinger (okra), used in Indian curries and as a side dish.', 'Seller': 'AGROZON'},
    223:{'Product Name': 'Lemongrass', 'Price': 100, 'Stock': 200, 'Description': 'Lemongrass, herb with a lemony flavor used in Thai and Southeast Asian cooking, especially in curries, soups, and teas.', 'Seller': 'AGROZON'},
    224:{'Product Name': 'Lemons', 'Price': 10, 'Stock': 400, 'Description': 'Fresh lemons, used in Indian cooking for tanginess and flavoring.', 'Seller': 'AGROZON'},
    225:{'Product Name': 'Lime Pickle (Nimbu ka Achar)', 'Price': 80, 'Stock': 100, 'Description': 'Lime pickle (nimbu ka achar), tangy and spicy pickle made from lime, enjoyed with Indian meals.', 'Seller': 'AGROZON'},
    226:{'Product Name': 'Lychee', 'Price': 1100, 'Stock': 50, 'Description': 'Lychee, sweet and fragrant fruit with a juicy flesh.', 'Seller': 'AGROZON'},
    227:{'Product Name': 'Mace (Javitri)', 'Price': 150, 'Stock': 100, 'Description': 'Mace, outer covering of nutmeg seed, used in spice blends and savory dishes.', 'Seller': 'AGROZON'},
    228:{'Product Name': 'Mangaba', 'Price': 1200, 'Stock': 60, 'Description': 'Mangaba, tropical fruit with a creamy texture and tangy-sweet flavor.', 'Seller': 'AGROZON'},
    229:{'Product Name': 'Mango Chutney', 'Price': 120, 'Stock': 50, 'Description': 'Sweet and tangy mango chutney, ideal for pairing with cheeses.', 'Seller': 'AGROZON'},
    230:{'Product Name': 'Mango Ginger (Amba Haldi)', 'Price': 100, 'Stock': 180, 'Description': 'Mango ginger (amba haldi), rhizome with a tangy and aromatic flavor used in Indian cooking for pickles, chutneys, and spice blends.', 'Seller': 'AGROZON'},
    231:{'Product Name': 'Mango Pickle (Aam ka Achar)', 'Price': 100, 'Stock': 80, 'Description': 'Mango pickle (aam ka achar), spicy and tangy pickle made from raw mangoes, a staple in Indian households.', 'Seller': 'AGROZON'},
    232:{'Product Name': 'Mango Powder (Amchur)', 'Price': 80, 'Stock': 200, 'Description': 'Dried mango powder, adds sourness to dishes like chaats and curries.', 'Seller': 'AGROZON'},
    233:{'Product Name': 'Mangosteen', 'Price': 1100, 'Stock': 40, 'Description': 'Tropical mangosteen, with sweet and tangy segments inside.', 'Seller': 'AGROZON'},
    234:{'Product Name': 'Meat Masala', 'Price': 120, 'Stock': 150, 'Description': 'Meat masala spice blend, used to prepare meat curries and dishes.', 'Seller': 'AGROZON'},
    235:{'Product Name': 'Mint Chutney (Pudina Chutney)', 'Price': 80, 'Stock': 120, 'Description': 'Mint chutney (pudina chutney), refreshing condiment made from fresh mint leaves, served with kebabs and snacks.', 'Seller': 'AGROZON'},
    236:{'Product Name': 'Mint Leaves (Pudina)', 'Price': 30, 'Stock': 300, 'Description': 'Fresh mint leaves, used in chutneys, raita, and as a garnish.', 'Seller': 'AGROZON'},
    237:{'Product Name': 'Miracle Fruit (Synsepalum dulcificum)', 'Price': 1200, 'Stock': 60, 'Description': 'Miracle fruit, berry that alters sour flavors to taste sweet.', 'Seller': 'AGROZON'},
    238:{'Product Name': 'Mixed Vegetable Pickle', 'Price': 120, 'Stock': 60, 'Description': 'Mixed vegetable pickle, assortment of seasonal vegetables pickled with spices, a popular accompaniment.', 'Seller': 'AGROZON'},
    239:{'Product Name': 'Moong Dal', 'Price': 70, 'Stock': 150, 'Description': 'Moong dal, split mung beans used in Indian cooking to make dal, khichdi, and desserts.', 'Seller': 'AGROZON'},
    240:{'Product Name': 'Mustard Oil (Sarson Ka Tel)', 'Price': 150, 'Stock': 200, 'Description': 'Mustard oil (sarson ka tel), pungent oil used in Indian cooking for frying, tempering, and pickling.', 'Seller': 'AGROZON'},
    241:{'Product Name': 'Mustard Seeds', 'Price': 35, 'Stock': 100, 'Description': 'Whole mustard seeds, great for pickling and adding to sauces.', 'Seller': 'AGROZON'},
    242:{'Product Name': 'Mustard Seeds (Rai)', 'Price': 50, 'Stock': 250, 'Description': 'Mustard seeds (rai), small seeds used for tempering and pickling in Indian cuisine.', 'Seller': 'AGROZON'},
    243:{'Product Name': 'Natural Almond Butter', 'Price': 200, 'Stock': 40, 'Description': 'Smooth and creamy almond butter, no added sugars or oils.', 'Seller': 'AGROZON'},
    244:{'Product Name': 'Nigella Seeds (Kalonji)', 'Price': 60, 'Stock': 250, 'Description': 'Nigella seeds, used in spice blends and pickles for their distinctive flavor.', 'Seller': 'AGROZON'},
    245:{'Product Name': 'Nutmeg', 'Price': 120, 'Stock': 150, 'Description': 'Whole nutmeg, used in spice blends and desserts for its warm, sweet flavor.', 'Seller': 'AGROZON'},
    246:{'Product Name': 'Nutmeg Powder', 'Price': 40, 'Stock': 120, 'Description': 'Ground nutmeg powder, warm and aromatic spice for sweet and savory dishes.', 'Seller': 'AGROZON'},
    247:{'Product Name': 'Nutmeg Spice Powder', 'Price': 40, 'Stock': 120, 'Description': 'Ground nutmeg spice powder, warm and aromatic for sweet and savory dishes.', 'Seller': 'AGROZON'},
    248:{'Product Name': 'Oat Milk', 'Price': 80, 'Stock': 120, 'Description': 'Creamy oat milk, dairy-free alternative for coffee and baking.', 'Seller': 'AGROZON'},
    249:{'Product Name': 'Okra (Bhindi)', 'Price': 40, 'Stock': 200, 'Description': 'Okra (bhindi), slimy yet nutritious vegetable used in Indian cooking for making curries, stir-fries, and snacks like bhindi masala.', 'Seller': 'AGROZON'},
    250:{'Product Name': 'Onion (Pyaz)', 'Price': 15, 'Stock': 400, 'Description': 'Onion (pyaz), versatile vegetable used as a base ingredient in Indian curries, salads, and snacks.', 'Seller': 'AGROZON'},
    251:{'Product Name': 'Onions', 'Price': 15, 'Stock': 500, 'Description': 'Fresh onions, essential in Indian cooking for flavoring and as a base ingredient.', 'Seller': 'AGROZON'},
    252:{'Product Name': 'Organic Apples', 'Price': 80, 'Stock': 120, 'Description': 'Crisp organic apples, perfect for snacks and baking.', 'Seller': 'AGROZON'},
    253:{'Product Name': 'Organic Applesauce', 'Price': 60, 'Stock': 100, 'Description': 'Pure organic applesauce, no added sugars or preservatives.', 'Seller': 'AGROZON'},
    254:{'Product Name': 'Organic Asparagus', 'Price': 80, 'Stock': 80, 'Description': 'Fresh organic asparagus spears, great for grilling and stir-fries.', 'Seller': 'AGROZON'},
    255:{'Product Name': 'Organic Avocado', 'Price': 50, 'Stock': 80, 'Description': 'Creamy organic avocado, great for guacamole and salads.', 'Seller': 'AGROZON'},
    256:{'Product Name': 'Organic Baby Carrots', 'Price': 30, 'Stock': 100, 'Description': 'Sweet and tender organic baby carrots, perfect for snacking.', 'Seller': 'AGROZON'},
    257:{'Product Name': 'Organic Baby Eggplant', 'Price': 675, 'Stock': 95, 'Description': 'Organic baby eggplant, small and tender, ideal for grilling and roasting.', 'Seller': 'AGROZON'},
    258:{'Product Name': 'Organic Baby Spinach', 'Price': 50, 'Stock': 80, 'Description': 'Tender organic baby spinach, perfect for salads and smoothies.', 'Seller': 'AGROZON'},
    259:{'Product Name': 'Organic Basil', 'Price': 25, 'Stock': 150, 'Description': 'Fresh organic basil leaves, perfect for pesto and garnishes.', 'Seller': 'AGROZON'},
    260:{'Product Name': 'Organic Basil Leaves', 'Price': 25, 'Stock': 150, 'Description': 'Fresh organic basil leaves, perfect for pesto and garnishes.', 'Seller': 'AGROZON'},
    261:{'Product Name': 'Organic Basil Powder', 'Price': 25, 'Stock': 150, 'Description': 'Organic basil powder, perfect for seasoning and garnishing dishes.', 'Seller': 'AGROZON'},
    262:{'Product Name': 'Organic Beef Steak', 'Price': 500, 'Stock': 20, 'Description': 'Prime cut organic beef steak, tender and flavorful.', 'Seller': 'AGROZON'},
    263:{'Product Name': 'Organic Beetroot', 'Price': 60, 'Stock': 90, 'Description': 'Fresh organic beetroot, perfect for salads and roasting.', 'Seller': 'AGROZON'},
    264:{'Product Name': 'Organic Bell Peppers', 'Price': 60, 'Stock': 80, 'Description': 'Colorful organic bell peppers, great for salads and stir-fries.', 'Seller': 'AGROZON'},
    265:{'Product Name': 'Organic Bison Jerky', 'Price': 350, 'Stock': 40, 'Description': 'Tender organic bison jerky, a protein-packed snack.', 'Seller': 'AGROZON'},
    266:{'Product Name': 'Organic Bison Meat', 'Price': 600, 'Stock': 20, 'Description': 'Lean and flavorful organic bison meat, great for grilling.', 'Seller': 'AGROZON'},
    267:{'Product Name': 'Organic Bison Ribeye Steak', 'Price': 900, 'Stock': 10, 'Description': 'Juicy organic bison ribeye steak, perfect for grilling.', 'Seller': 'AGROZON'},
    268:{'Product Name': 'Organic Bison Sausages', 'Price': 700, 'Stock': 15, 'Description': 'Savory organic bison sausages, perfect for breakfast or grilling.', 'Seller': 'AGROZON'},
    269:{'Product Name': 'Organic Black Beans', 'Price': 80, 'Stock': 60, 'Description': 'Rich and creamy organic black beans, high in fiber.', 'Seller': 'AGROZON'},
    270:{'Product Name': 'Organic Blackberries', 'Price': 180, 'Stock': 30, 'Description': 'Juicy organic blackberries, perfect for snacking and desserts.', 'Seller': 'AGROZON'},
    271:{'Product Name': 'Organic Blood Oranges', 'Price': 100, 'Stock': 70, 'Description': 'Juicy organic blood oranges, rich in antioxidants and vitamins.', 'Seller': 'AGROZON'},
    272:{'Product Name': 'Organic Blue Corn Tortilla Chips', 'Price': 80, 'Stock': 60, 'Description': 'Crispy blue corn tortilla chips, perfect for dipping.', 'Seller': 'AGROZON'},
    273:{'Product Name': 'Organic Blueberries', 'Price': 180, 'Stock': 50, 'Description': 'Sweet and antioxidant-rich organic blueberries, perfect for snacks.', 'Seller': 'AGROZON'},
    274:{'Product Name': 'Organic Boysenberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic boysenberries, a cross between raspberry, blackberry, and loganberry.', 'Seller': 'AGROZON'},
    275:{'Product Name': 'Organic Broccoli', 'Price': 35, 'Stock': 90, 'Description': 'Fresh organic broccoli florets, packed with vitamins.', 'Seller': 'AGROZON'},
    276:{'Product Name': 'Organic Brown Rice', 'Price': 250, 'Stock': 50, 'Description': 'High-quality organic brown rice, rich in nutrients and fiber.', 'Seller': 'AGROZON'},
    277:{'Product Name': 'Organic Cacao Nibs', 'Price': 120, 'Stock': 60, 'Description': 'Crunchy organic cacao nibs, perfect for adding to smoothies and desserts.', 'Seller': 'AGROZON'},
    278:{'Product Name': 'Organic Cantaloupe', 'Price': 100, 'Stock': 80, 'Description': 'Sweet and refreshing organic cantaloupe melon, perfect for snacks.', 'Seller': 'AGROZON'},
    279:{'Product Name': 'Organic Cauliflower', 'Price': 45, 'Stock': 80, 'Description': 'Fresh organic cauliflower, versatile for roasting or mashing.', 'Seller': 'AGROZON'},
    280:{'Product Name': 'Organic Cheddar Cheese', 'Price': 180, 'Stock': 50, 'Description': 'Sharp and flavorful organic cheddar cheese, great for snacking.', 'Seller': 'AGROZON'},
    281:{'Product Name': 'Organic Cloudberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic cloudberries, golden berries with a tart flavor.', 'Seller': 'AGROZON'},
    282:{'Product Name': 'Organic Coconut Flour', 'Price': 120, 'Stock': 80, 'Description': 'Gluten-free organic coconut flour, ideal for baking.', 'Seller': 'AGROZON'},
    283:{'Product Name': 'Organic Coconut Water', 'Price': 100, 'Stock': 70, 'Description': 'Refreshing organic coconut water, hydrating and electrolyte-rich.', 'Seller': 'AGROZON'},
    284:{'Product Name': 'Organic Coriander Powder', 'Price': 30, 'Stock': 120, 'Description': 'Ground organic coriander powder, versatile spice for cooking.', 'Seller': 'AGROZON'},
    285:{'Product Name': 'Organic Coriander Seeds', 'Price': 30, 'Stock': 120, 'Description': 'Whole organic coriander seeds, versatile spice for cooking.', 'Seller': 'AGROZON'},
    286:{'Product Name': 'Organic Cottage Cheese', 'Price': 90, 'Stock': 60, 'Description': 'Smooth and creamy organic cottage cheese, high in protein.', 'Seller': 'AGROZON'},
    287:{'Product Name': 'Organic Cranberries', 'Price': 140, 'Stock': 70, 'Description': 'Sweet and tart organic cranberries, perfect for baking and snacking.', 'Seller': 'AGROZON'},
    288:{'Product Name': 'Organic Cucumber', 'Price': 40, 'Stock': 90, 'Description': 'Crisp organic cucumber, great for salads and snacks.', 'Seller': 'AGROZON'},
    289:{'Product Name': 'Organic Curry Leaves', 'Price': 70, 'Stock': 80, 'Description': 'Fresh organic curry leaves, essential for South Indian cooking.', 'Seller': 'AGROZON'},
    290:{'Product Name': 'Organic Curry Powder', 'Price': 70, 'Stock': 80, 'Description': 'Versatile organic curry powder blend, perfect for curries and marinades.', 'Seller': 'AGROZON'},
    291:{'Product Name': 'Organic Dill', 'Price': 25, 'Stock': 80, 'Description': 'Fresh organic dill, ideal for pickling and seafood dishes.', 'Seller': 'AGROZON'},
    292:{'Product Name': 'Organic Dried Sage', 'Price': 20, 'Stock': 80, 'Description': 'Dried organic sage, aromatic herb for seasoning meats and sauces.', 'Seller': 'AGROZON'},
    293:{'Product Name': 'Organic Dried Sage Leaves', 'Price': 20, 'Stock': 80, 'Description': 'Dried organic sage leaves, aromatic herb for seasoning meats and sauces.', 'Seller': 'AGROZON'},
    294:{'Product Name': 'Organic Duck Meat', 'Price': 550, 'Stock': 20, 'Description': 'Flavorful organic duck meat, ideal for roasting and grilling.', 'Seller': 'AGROZON'},
    295:{'Product Name': 'Organic Eggs', 'Price': 7, 'Stock': 150, 'Description': 'Certified organic eggs from pasture-raised hens.', 'Seller': 'AGROZON'},
    296:{'Product Name': 'Organic Elk Jerky', 'Price': 400, 'Stock': 25, 'Description': 'Tender organic elk jerky, a protein-packed snack.', 'Seller': 'AGROZON'},
    297:{'Product Name': 'Organic Elk Meat', 'Price': 650, 'Stock': 20, 'Description': 'Lean and tender organic elk meat, perfect for roasts and steaks.', 'Seller': 'AGROZON'},
    298:{'Product Name': 'Organic Feta Cheese', 'Price': 150, 'Stock': 40, 'Description': 'Tangy organic feta cheese, ideal for salads and Mediterranean dishes.', 'Seller': 'AGROZON'},
    299:{'Product Name': 'Organic Free-Range Chicken', 'Price': 400, 'Stock': 25, 'Description': 'Certified organic free-range chicken, raised with care.', 'Seller': 'AGROZON'},
    300:{'Product Name': 'Organic Garlic', 'Price': 30, 'Stock': 80, 'Description': 'Fresh organic garlic bulbs, essential for cooking.', 'Seller': 'AGROZON'},
    301:{'Product Name': 'Organic Garlic Flakes', 'Price': 40, 'Stock': 100, 'Description': 'Organic garlic flakes, convenient for seasoning and cooking.', 'Seller': 'AGROZON'},
    302:{'Product Name': 'Organic Garlic Powder', 'Price': 40, 'Stock': 100, 'Description': 'Organic garlic powder, convenient for seasoning and cooking.', 'Seller': 'AGROZON'},
    303:{'Product Name': 'Organic Garlic Spice', 'Price': 40, 'Stock': 100, 'Description': 'Organic garlic spice, convenient for seasoning and cooking.', 'Seller': 'AGROZON'},
    304:{'Product Name': 'Organic Ginger Flakes', 'Price': 40, 'Stock': 150, 'Description': 'Organic ginger flakes, convenient for seasoning and brewing tea.', 'Seller': 'AGROZON'},
    305:{'Product Name': 'Organic Ginger Powder', 'Price': 40, 'Stock': 150, 'Description': 'Organic ginger powder, convenient for seasoning and brewing tea.', 'Seller': 'AGROZON'},
    306:{'Product Name': 'Organic Ginger Root', 'Price': 40, 'Stock': 150, 'Description': 'Fresh organic ginger root, ideal for cooking and brewing tea.', 'Seller': 'AGROZON'},
    307:{'Product Name': 'Organic Goji Berries', 'Price': 850, 'Stock': 80, 'Description': 'Organic goji berries, known for their antioxidant properties and sweet-tart flavor.', 'Seller': 'AGROZON'},
    308:{'Product Name': 'Organic Golden Kiwi', 'Price': 120, 'Stock': 80, 'Description': 'Sweet and tangy organic golden kiwi, rich in Vitamin C.', 'Seller': 'AGROZON'},
    309:{'Product Name': 'Organic Gooseberries', 'Price': 900, 'Stock': 80, 'Description': 'Organic gooseberries, tart and packed with vitamins.', 'Seller': 'AGROZON'},
    310:{'Product Name': 'Organic Greek Yogurt', 'Price': 80, 'Stock': 100, 'Description': 'Thick and tangy organic Greek yogurt, high in probiotics.', 'Seller': 'AGROZON'},
    311:{'Product Name': 'Organic Hemp Milk', 'Price': 90, 'Stock': 80, 'Description': 'Creamy organic hemp milk, rich in omega fatty acids and vitamins.', 'Seller': 'AGROZON'},
    312:{'Product Name': 'Organic Hemp Seeds', 'Price': 180, 'Stock': 50, 'Description': 'Nutrient-dense organic hemp seeds, rich in omega fatty acids.', 'Seller': 'AGROZON'},
    313:{'Product Name': 'Organic Huckleberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic huckleberries, tart and perfect for pies and jams.', 'Seller': 'AGROZON'},
    314:{'Product Name': 'Organic Kale', 'Price': 30, 'Stock': 100, 'Description': 'Fresh organic kale, nutrient-packed superfood.', 'Seller': 'AGROZON'},
    315:{'Product Name': 'Organic Kiwano', 'Price': 150, 'Stock': 60, 'Description': 'Exotic organic kiwano fruit, also known as horned melon.', 'Seller': 'AGROZON'},
    316:{'Product Name': 'Organic Kiwi Berries', 'Price': 200, 'Stock': 40, 'Description': 'Sweet and tangy organic kiwi berries, bite-sized treats.', 'Seller': 'AGROZON'},
    317:{'Product Name': 'Organic Lemongrass', 'Price': 25, 'Stock': 80, 'Description': 'Fresh organic lemongrass stalks, aromatic and great for teas and Thai dishes.', 'Seller': 'AGROZON'},
    318:{'Product Name': 'Organic Lemongrass Powder', 'Price': 30, 'Stock': 80, 'Description': 'Organic lemongrass powder, convenient for seasoning and tea infusions.', 'Seller': 'AGROZON'},
    319:{'Product Name': 'Organic Lemongrass Tea Leaves', 'Price': 25, 'Stock': 150, 'Description': 'Organic lemongrass tea leaves, refreshing and soothing.', 'Seller': 'AGROZON'},
    320:{'Product Name': 'Organic Lemons', 'Price': 70, 'Stock': 100, 'Description': 'Juicy organic lemons, perfect for zest and juice.', 'Seller': 'AGROZON'},
    321:{'Product Name': 'Organic Lingonberries', 'Price': 180, 'Stock': 50, 'Description': 'Tart and flavorful organic lingonberries, great for sauces and jams.', 'Seller': 'AGROZON'},
    322:{'Product Name': 'Organic Loganberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic loganberries, a hybrid of blackberry and raspberry with a tart flavor.', 'Seller': 'AGROZON'},
    323:{'Product Name': 'Organic Mango Chunks', 'Price': 150, 'Stock': 60, 'Description': 'Frozen organic mango chunks, convenient for smoothies and desserts.', 'Seller': 'AGROZON'},
    324:{'Product Name': 'Organic Mangoes', 'Price': 100, 'Stock': 70, 'Description': 'Sweet and juicy organic mangoes, bursting with flavor.', 'Seller': 'AGROZON'},
    325:{'Product Name': 'Organic Marionberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic marionberries, a type of blackberry with a sweet-tart flavor.', 'Seller': 'AGROZON'},
    326:{'Product Name': 'Organic Mint Leaves', 'Price': 25, 'Stock': 150, 'Description': 'Fresh organic mint leaves, ideal for teas, salads, and desserts.', 'Seller': 'AGROZON'},
    327:{'Product Name': 'Organic Mint Powder', 'Price': 25, 'Stock': 150, 'Description': 'Organic mint powder, convenient for teas, desserts, and sauces.', 'Seller': 'AGROZON'},
    328:{'Product Name': 'Organic Mint Spice', 'Price': 25, 'Stock': 150, 'Description': 'Organic mint spice, perfect for teas, desserts, and sauces.', 'Seller': 'AGROZON'},
    329:{'Product Name': 'Organic Miso Paste', 'Price': 100, 'Stock': 80, 'Description': 'Traditional organic miso paste, great for soups and marinades.', 'Seller': 'AGROZON'},
    330:{'Product Name': 'Organic Mixed Berries', 'Price': 250, 'Stock': 40, 'Description': 'Frozen organic mixed berries, perfect for smoothies and desserts.', 'Seller': 'AGROZON'},
    331:{'Product Name': 'Organic Mixed Greens', 'Price': 70, 'Stock': 80, 'Description': 'Fresh organic mixed greens, ready for salads.', 'Seller': 'AGROZON'},
    332:{'Product Name': 'Organic Mixed Nuts', 'Price': 300, 'Stock': 40, 'Description': 'Premium organic mixed nuts, a nutritious snack.', 'Seller': 'AGROZON'},
    333:{'Product Name': 'Organic Mixed Salad Greens', 'Price': 70, 'Stock': 60, 'Description': 'Fresh organic mixed salad greens, ready to enjoy.', 'Seller': 'AGROZON'},
    334:{'Product Name': 'Organic Mozzarella Cheese', 'Price': 160, 'Stock': 50, 'Description': 'Smooth and stretchy organic mozzarella cheese, perfect for pizzas.', 'Seller': 'AGROZON'},
    335:{'Product Name': 'Organic Mulberries', 'Price': 200, 'Stock': 30, 'Description': 'Sweet and chewy organic mulberries, packed with antioxidants.', 'Seller': 'AGROZON'},
    336:{'Product Name': 'Organic Mushrooms', 'Price': 50, 'Stock': 90, 'Description': 'Fresh organic mushrooms, great for soups and sauces.', 'Seller': 'AGROZON'},
    337:{'Product Name': 'Organic Orange Juice', 'Price': 120, 'Stock': 80, 'Description': 'Freshly squeezed organic orange juice, rich in Vitamin C.', 'Seller': 'AGROZON'},
    338:{'Product Name': 'Organic Parsley', 'Price': 20, 'Stock': 150, 'Description': 'Fresh organic parsley leaves, perfect for garnishing.', 'Seller': 'AGROZON'},
    339:{'Product Name': 'Organic Parsley Flakes', 'Price': 20, 'Stock': 150, 'Description': 'Dried organic parsley flakes, perfect for garnishing dishes.', 'Seller': 'AGROZON'},
    340:{'Product Name': 'Organic Parsley Powder', 'Price': 20, 'Stock': 150, 'Description': 'Organic parsley powder, perfect for seasoning and garnishing dishes.', 'Seller': 'AGROZON'},
    341:{'Product Name': 'Organic Peanut Butter', 'Price': 180, 'Stock': 50, 'Description': 'Creamy organic peanut butter, made from roasted peanuts.', 'Seller': 'AGROZON'},
    342:{'Product Name': 'Organic Pears', 'Price': 80, 'Stock': 100, 'Description': 'Sweet and juicy organic pears, great for snacks and desserts.', 'Seller': 'AGROZON'},
    343:{'Product Name': 'Organic Plums', 'Price': 80, 'Stock': 90, 'Description': 'Sweet and juicy organic plums, packed with vitamins and fiber.', 'Seller': 'AGROZON'},
    344:{'Product Name': 'Organic Pomegranates', 'Price': 160, 'Stock': 60, 'Description': 'Juicy organic pomegranates, packed with antioxidants and vitamins.', 'Seller': 'AGROZON'},
    345:{'Product Name': 'Organic Quinoa', 'Price': 300, 'Stock': 40, 'Description': 'Gluten-free whole grain quinoa, rich in protein and fiber.', 'Seller': 'AGROZON'},
    346:{'Product Name': 'Organic Raspberries', 'Price': 150, 'Stock': 60, 'Description': 'Sweet and tangy organic raspberries, rich in antioxidants.', 'Seller': 'AGROZON'},
    347:{'Product Name': 'Organic Raw Honey', 'Price': 200, 'Stock': 40, 'Description': 'Pure organic raw honey, unprocessed and full of natural goodness.', 'Seller': 'AGROZON'},
    348:{'Product Name': 'Organic Red Currants', 'Price': 850, 'Stock': 70, 'Description': 'Organic red currants, tart and perfect for jams and desserts.', 'Seller': 'AGROZON'},
    349:{'Product Name': 'Organic Red Lentils', 'Price': 120, 'Stock': 100, 'Description': 'Nutritious organic red lentils, great for soups and stews.', 'Seller': 'AGROZON'},
    350:{'Product Name': 'Organic Red Quinoa', 'Price': 280, 'Stock': 50, 'Description': 'Nutty and flavorful organic red quinoa, rich in protein and fiber.', 'Seller': 'AGROZON'},
    351:{'Product Name': 'Organic Rhubarb', 'Price': 80, 'Stock': 90, 'Description': 'Tart and tangy organic rhubarb, ideal for pies and jams.', 'Seller': 'AGROZON'},
    352:{'Product Name': 'Organic Ricotta Cheese', 'Price': 120, 'Stock': 60, 'Description': 'Smooth and creamy organic ricotta cheese, perfect for pasta dishes.', 'Seller': 'AGROZON'},
    353:{'Product Name': 'Organic Rosemary', 'Price': 30, 'Stock': 80, 'Description': 'Fragrant organic rosemary, perfect for roasts and marinades.', 'Seller': 'AGROZON'},
    354:{'Product Name': 'Organic Rosemary Leaves', 'Price': 30, 'Stock': 80, 'Description': 'Dried organic rosemary leaves, aromatic herb for roasts and marinades.', 'Seller': 'AGROZON'},
    355:{'Product Name': 'Organic Rosemary Powder', 'Price': 30, 'Stock': 80, 'Description': 'Ground organic rosemary powder, aromatic herb for roasts and marinades.', 'Seller': 'AGROZON'},
    356:{'Product Name': 'Organic Sage', 'Price': 20, 'Stock': 150, 'Description': 'Fresh organic sage leaves, great for seasoning meats and sauces.', 'Seller': 'AGROZON'},
    357:{'Product Name': 'Organic Saskatoon Berries', 'Price': 850, 'Stock': 80, 'Description': 'Organic saskatoon berries, similar to blueberries with a nutty flavor.', 'Seller': 'AGROZON'},
    358:{'Product Name': 'Organic Seaweed Snacks', 'Price': 80, 'Stock': 120, 'Description': 'Crispy organic seaweed snacks, packed with minerals and nutrients.', 'Seller': 'AGROZON'},
    359:{'Product Name': 'Organic Soy Milk', 'Price': 90, 'Stock': 60, 'Description': 'Nutrient-rich organic soy milk, dairy-free alternative.', 'Seller': 'AGROZON'},
    360:{'Product Name': 'Organic Soy Yogurt', 'Price': 80, 'Stock': 80, 'Description': 'Creamy and dairy-free organic soy yogurt, high in probiotics.', 'Seller': 'AGROZON'},
    361:{'Product Name': 'Organic Spinach', 'Price': 40, 'Stock': 120, 'Description': 'Fresh organic spinach leaves, packed with vitamins and minerals.', 'Seller': 'AGROZON'},
    362:{'Product Name': 'Organic Strawberries', 'Price': 120, 'Stock': 70, 'Description': 'Juicy organic strawberries, perfect for desserts and smoothies.', 'Seller': 'AGROZON'},
    363:{'Product Name': 'Organic Tahini', 'Price': 160, 'Stock': 60, 'Description': 'Smooth and nutty organic tahini, great for dressings and dips.', 'Seller': 'AGROZON'},
    364:{'Product Name': 'Organic Tarragon', 'Price': 20, 'Stock': 100, 'Description': 'Fresh organic tarragon, adds a hint of licorice flavor to dishes.', 'Seller': 'AGROZON'},
    365:{'Product Name': 'Organic Tarragon Leaves', 'Price': 20, 'Stock': 150, 'Description': 'Dried organic tarragon leaves, adds a hint of licorice flavor to dishes.', 'Seller': 'AGROZON'},
    366:{'Product Name': 'Organic Tarragon Spice', 'Price': 20, 'Stock': 150, 'Description': 'Organic tarragon spice, adds a hint of licorice flavor to dishes.', 'Seller': 'AGROZON'},
    367:{'Product Name': 'Organic Tayberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic tayberries, a cross between raspberry and blackberry with a sweet-tart flavor.', 'Seller': 'AGROZON'},
    368:{'Product Name': 'Organic Thyme', 'Price': 20, 'Stock': 150, 'Description': 'Aromatic organic thyme leaves, great for seasoning meats and vegetables.', 'Seller': 'AGROZON'},
    369:{'Product Name': 'Organic Thyme Leaves', 'Price': 20, 'Stock': 150, 'Description': 'Aromatic organic thyme leaves, great for seasoning meats and vegetables.', 'Seller': 'AGROZON'},
    370:{'Product Name': 'Organic Thyme Powder', 'Price': 20, 'Stock': 150, 'Description': 'Ground organic thyme powder, versatile spice for cooking.', 'Seller': 'AGROZON'},
    371:{'Product Name': 'Organic Tofu', 'Price': 120, 'Stock': 60, 'Description': 'Silken organic tofu, versatile for stir-fries and desserts.', 'Seller': 'AGROZON'},
    372:{'Product Name': 'Organic Tomato Sauce', 'Price': 70, 'Stock': 60, 'Description': 'Smooth and flavorful organic tomato sauce, perfect for pasta.', 'Seller': 'AGROZON'},
    373:{'Product Name': 'Organic Tomatoes', 'Price': 60, 'Stock': 80, 'Description': 'Ripe organic tomatoes, perfect for salads and cooking.', 'Seller': 'AGROZON'},
    374:{'Product Name': 'Organic Turmeric Powder', 'Price': 50, 'Stock': 100, 'Description': 'Ground organic turmeric powder, known for its anti-inflammatory properties.', 'Seller': 'AGROZON'},
    375:{'Product Name': 'Organic Yogurt', 'Price': 70, 'Stock': 100, 'Description': 'Creamy organic yogurt, made from grass-fed cow milk.', 'Seller': 'AGROZON'},
    376:{'Product Name': 'Organic Youngberries', 'Price': 850, 'Stock': 80, 'Description': 'Organic youngberries, hybrid of blackberry, raspberry, and dewberry with a sweet-tart flavor.', 'Seller': 'AGROZON'},
    377:{'Product Name': 'Organic Zucchini', 'Price': 60, 'Stock': 90, 'Description': 'Fresh organic zucchini, versatile for cooking and grilling.', 'Seller': 'AGROZON'},
    378:{'Product Name': 'Palm Sugar', 'Price': 100, 'Stock': 200, 'Description': 'Palm sugar, natural sweetener made from palm sap used in Thai and Southeast Asian desserts, curries, and sauces.', 'Seller': 'AGROZON'},
    379:{'Product Name': 'Panch Phoron', 'Price': 100, 'Stock': 150, 'Description': 'Panch phoron, Bengali five-spice blend used for tempering.', 'Seller': 'AGROZON'},
    380:{'Product Name': 'Pandan Leaves', 'Price': 50, 'Stock': 200, 'Description': 'Pandan leaves, used in South Asian cooking for flavoring desserts and rice dishes.', 'Seller': 'AGROZON'},
    381:{'Product Name': 'Paneer Masala', 'Price': 90, 'Stock': 150, 'Description': 'Paneer masala spice blend, used to prepare paneer (Indian cottage cheese) dishes.', 'Seller': 'AGROZON'},
    382:{'Product Name': 'Papad', 'Price': 50, 'Stock': 200, 'Description': 'Indian papadums, crispy snack served with meals.', 'Seller': 'AGROZON'},
    383:{'Product Name': 'Papaya (Hawaiian Solo)', 'Price': 1000, 'Stock': 70, 'Description': 'Hawaiian solo papaya, sweet and creamy fruit with orange flesh.', 'Seller': 'AGROZON'},
    384:{'Product Name': 'Paprika', 'Price': 30, 'Stock': 120, 'Description': 'Vibrant paprika powder, adds color and flavor to dishes.', 'Seller': 'AGROZON'},
    385:{'Product Name': 'Paprika Ground Powder', 'Price': 30, 'Stock': 120, 'Description': 'Ground paprika powder, adds color and flavor to dishes.', 'Seller': 'AGROZON'},
    386:{'Product Name': 'Paprika Powder', 'Price': 30, 'Stock': 120, 'Description': 'Ground paprika powder, adds color and flavor to dishes.', 'Seller': 'AGROZON'},
    387:{'Product Name': 'Paprika Spice Blend', 'Price': 30, 'Stock': 120, 'Description': 'Paprika spice blend, adds color and flavor to dishes.', 'Seller': 'AGROZON'},
    388:{'Product Name': 'Paprika Spice Powder', 'Price': 30, 'Stock': 120, 'Description': 'Ground paprika spice powder, adds color and flavor to dishes.', 'Seller': 'AGROZON'},
    389:{'Product Name': 'Passion Fruit', 'Price': 900, 'Stock': 60, 'Description': 'Passion fruit, with aromatic seeds and tangy-sweet flavor.', 'Seller': 'AGROZON'},
    390:{'Product Name': 'Pav Bhaji Masala', 'Price': 80, 'Stock': 150, 'Description': 'Pav bhaji masala, spice blend used in Mumbai street food pav bhaji.', 'Seller': 'AGROZON'},
    391:{'Product Name': 'Peanuts', 'Price': 80, 'Stock': 200, 'Description': 'Raw peanuts, used in Indian snacks, sweets, and as a garnish.', 'Seller': 'AGROZON'},
    392:{'Product Name': 'Pepino Melon (Solanum muricatum)', 'Price': 1200, 'Stock': 60, 'Description': 'Pepino melon, pear-shaped fruit with a sweet and refreshing taste.', 'Seller': 'AGROZON'},
    393:{'Product Name': 'Pickle Masala', 'Price': 70, 'Stock': 150, 'Description': 'Pickle masala, spice blend used to prepare Indian pickles.', 'Seller': 'AGROZON'},
    394:{'Product Name': 'Pineberries', 'Price': 800, 'Stock': 80, 'Description': 'Pineberries, white strawberries with a pineapple-like flavor.', 'Seller': 'AGROZON'},
    395:{'Product Name': 'Pistachios (Pista)', 'Price': 300, 'Stock': 100, 'Description': 'Whole pistachios, used in Indian sweets and desserts.', 'Seller': 'AGROZON'},
    396:{'Product Name': 'Poha (Flattened Rice)', 'Price': 40, 'Stock': 250, 'Description': 'Poha (flattened rice), used in Indian breakfast dishes like poha and upma.', 'Seller': 'AGROZON'},
    397:{'Product Name': 'Pointed Gourd (Parwal)', 'Price': 50, 'Stock': 120, 'Description': 'Pointed gourd (parwal), slender vegetable with a slightly bitter taste, used in North Indian and Bengali cuisine.', 'Seller': 'AGROZON'},
    398:{'Product Name': 'Pomegranate Seeds (Anardana)', 'Price': 90, 'Stock': 200, 'Description': 'Dried pomegranate seeds, used as a souring agent in Indian cooking.', 'Seller': 'AGROZON'},
    399:{'Product Name': 'Poppy Seeds (Khus Khus)', 'Price': 120, 'Stock': 150, 'Description': 'Poppy seeds, used in Indian cuisine for thickening and adding texture.', 'Seller': 'AGROZON'},
    400:{'Product Name': 'Potato (Aloo)', 'Price': 20, 'Stock': 350, 'Description': 'Potato (aloo), widely used vegetable in Indian cooking for making curries, snacks, and biryanis.', 'Seller': 'AGROZON'},
    401:{'Product Name': 'Potatoes', 'Price': 20, 'Stock': 400, 'Description': 'Fresh potatoes, versatile vegetable used in Indian curries, snacks, and side dishes.', 'Seller': 'AGROZON'},
    402:{'Product Name': 'Puffed Lotus Seeds (Makhana)', 'Price': 120, 'Stock': 150, 'Description': 'Puffed lotus seeds (makhana), used in Indian snacks and sweets.', 'Seller': 'AGROZON'},
    403:{'Product Name': 'Puffed Rice (Murmura)', 'Price': 20, 'Stock': 300, 'Description': 'Puffed rice (murmura), used in Indian snacks like bhel puri and chivda.', 'Seller': 'AGROZON'},
    404:{'Product Name': 'Pumpkin (Kaddu)', 'Price': 40, 'Stock': 250, 'Description': 'Fresh pumpkin, used in Indian curries, sweets, and savory dishes.', 'Seller': 'AGROZON'},
    405:{'Product Name': 'Purple Brussels Sprouts', 'Price': 625, 'Stock': 95, 'Description': 'Colorful purple Brussels sprouts, mild and slightly sweet.', 'Seller': 'AGROZON'},
    406:{'Product Name': 'Purple Mangosteen', 'Price': 1000, 'Stock': 70, 'Description': 'Purple mangosteen, known for its purple rind and sweet, tangy flesh.', 'Seller': 'AGROZON'},
    407:{'Product Name': 'Purple Potatoes', 'Price': 600, 'Stock': 100, 'Description': 'Nutrient-rich purple potatoes, with a creamy texture and earthy flavor.', 'Seller': 'AGROZON'},
    408:{'Product Name': 'Quinoa Flour', 'Price': 200, 'Stock': 50, 'Description': 'Gluten-free flour made from quinoa, ideal for baking.', 'Seller': 'AGROZON'},
    409:{'Product Name': 'Rainbow Carrots', 'Price': 475, 'Stock': 115, 'Description': 'Colorful rainbow carrots, sweet and crunchy, perfect for roasting.', 'Seller': 'AGROZON'},
    410:{'Product Name': 'Raisins (Kishmish)', 'Price': 120, 'Stock': 200, 'Description': 'Golden raisins, used in Indian sweets, desserts, and savory dishes.', 'Seller': 'AGROZON'},
    411:{'Product Name': 'Rambutan', 'Price': 1200, 'Stock': 60, 'Description': 'Rambutan, exotic fruit with hairy red skin and sweet, juicy flesh.', 'Seller': 'AGROZON'},
    412:{'Product Name': 'Rasam Powder', 'Price': 90, 'Stock': 150, 'Description': 'Rasam powder, spice blend used in South Indian rasam soup.', 'Seller': 'AGROZON'},
    413:{'Product Name': 'Rava (Semolina)', 'Price': 40, 'Stock': 200, 'Description': 'Rava (semolina), coarse wheat flour used to make South Indian dishes like upma and halwa.', 'Seller': 'AGROZON'},
    414:{'Product Name': 'Raw Almonds', 'Price': 300, 'Stock': 40, 'Description': 'Premium raw almonds, great for snacking or baking.', 'Seller': 'AGROZON'},
    415:{'Product Name': 'Raw Cashews', 'Price': 280, 'Stock': 40, 'Description': 'Premium raw cashews, great for snacking or cooking.', 'Seller': 'AGROZON'},
    416:{'Product Name': 'Raw Honey', 'Price': 150, 'Stock': 60, 'Description': 'Pure, unprocessed honey collected from local apiaries.', 'Seller': 'AGROZON'},
    417:{'Product Name': 'Raw Mango (Kachcha Aam)', 'Price': 30, 'Stock': 200, 'Description': 'Raw mango (kachcha aam), tangy and sour mango used in pickles and chutneys.', 'Seller': 'AGROZON'},
    418:{'Product Name': 'Raw Organic Brazil Nuts', 'Price': 400, 'Stock': 30, 'Description': 'Premium raw organic Brazil nuts, rich in selenium and healthy fats.', 'Seller': 'AGROZON'},
    419:{'Product Name': 'Raw Organic Macadamia Nuts', 'Price': 450, 'Stock': 30, 'Description': 'Premium raw organic macadamia nuts, buttery and delicious.', 'Seller': 'AGROZON'},
    420:{'Product Name': 'Raw Organic Pistachios', 'Price': 380, 'Stock': 40, 'Description': 'Premium raw organic pistachios, great for snacking.', 'Seller': 'AGROZON'},
    421:{'Product Name': 'Raw Pistachios', 'Price': 350, 'Stock': 30, 'Description': 'Premium raw pistachios, great for snacking or adding to dishes.', 'Seller': 'AGROZON'},
    422:{'Product Name': 'Raw Walnuts', 'Price': 300, 'Stock': 30, 'Description': 'Premium raw walnuts, great for salads and baking.', 'Seller': 'AGROZON'},
    423:{'Product Name': 'Red Banana', 'Price': 400, 'Stock': 70, 'Description': 'Red banana, sweeter and creamier than yellow bananas.', 'Seller': 'AGROZON'},
    424:{'Product Name': 'Red Chili (Fresh)', 'Price': 30, 'Stock': 300, 'Description': 'Fresh red chili peppers, used in Indian cooking for spiciness.', 'Seller': 'AGROZON'},
    425:{'Product Name': 'Red Chili Flakes', 'Price': 40, 'Stock': 250, 'Description': 'Red chili flakes, crushed dried red chilies used as a seasoning and for adding heat to dishes in Indian cuisine.', 'Seller': 'AGROZON'},
    426:{'Product Name': 'Red Chili Garlic Chutney', 'Price': 60, 'Stock': 200, 'Description': 'Red chili garlic chutney, spicy and garlicky condiment made from red chilies and garlic, used in Indian street food.', 'Seller': 'AGROZON'},
    427:{'Product Name': 'Red Chili Powder', 'Price': 70, 'Stock': 200, 'Description': 'Ground red chili powder, adds heat and color to dishes.', 'Seller': 'AGROZON'},
    428:{'Product Name': 'Red Chili Powder (Lal Mirch Powder)', 'Price': 50, 'Stock': 150, 'Description': 'Red chili powder (lal mirch powder), ground red chilies used to add heat and color to Indian dishes.', 'Seller': 'AGROZON'},
    429:{'Product Name': 'Red Chilli Powder (Lal Mirch Powder)', 'Price': 60, 'Stock': 300, 'Description': 'Red chilli powder (lal mirch powder), ground dried red chillies used to add heat and color to Indian dishes.', 'Seller': 'AGROZON'},
    430:{'Product Name': 'Red Pineapple', 'Price': 700, 'Stock': 60, 'Description': 'Red pineapple, sweeter and juicier than regular pineapple.', 'Seller': 'AGROZON'},
    431:{'Product Name': 'Red Pitahaya (Red Dragon Fruit)', 'Price': 1000, 'Stock': 70, 'Description': 'Red pitahaya (red dragon fruit), vibrant fruit with a sweet and refreshing taste.', 'Seller': 'AGROZON'},
    432:{'Product Name': 'Rice Flour', 'Price': 40, 'Stock': 250, 'Description': 'Rice flour, used in Indian sweets, snacks, and as a gluten-free alternative.', 'Seller': 'AGROZON'},
    433:{'Product Name': 'Ridge Gourd (Torai)', 'Price': 30, 'Stock': 250, 'Description': 'Ridge gourd (torai), mild-flavored and nutritious vegetable used in Indian cooking for making curries, chutneys, and stir-fries.', 'Seller': 'AGROZON'},
    434:{'Product Name': 'Ridge Gourd (Turai)', 'Price': 35, 'Stock': 250, 'Description': 'Fresh ridge gourd, used in Indian curries and chutneys.', 'Seller': 'AGROZON'},
    435:{'Product Name': 'Romanesco Cauliflower', 'Price': 650, 'Stock': 90, 'Description': 'Romanesco cauliflower, with a striking fractal pattern and nutty flavor.', 'Seller': 'AGROZON'},
    436:{'Product Name': 'Sabudana (Tapioca Pearls)', 'Price': 60, 'Stock': 200, 'Description': 'Sabudana (tapioca pearls), used in Indian fasting dishes and desserts.', 'Seller': 'AGROZON'},
    437:{'Product Name': 'Saffron (Kesar)', 'Price': 500, 'Stock': 50, 'Description': 'Saffron (kesar), aromatic threads used to add color and flavor to Indian sweets, rice dishes, and drinks.', 'Seller': 'AGROZON'},
    438:{'Product Name': 'Saffron Powder', 'Price': 350, 'Stock': 10, 'Description': 'Ground saffron powder, luxurious spice for rice dishes and desserts.', 'Seller': 'AGROZON'},
    439:{'Product Name': 'Saffron Threads', 'Price': 300, 'Stock': 10, 'Description': 'Luxurious saffron threads, adds rich color and flavor to dishes.', 'Seller': 'AGROZON'},
    440:{'Product Name': 'Sago Seeds (Sabudana)', 'Price': 50, 'Stock': 250, 'Description': 'Sago seeds (sabudana), used in Indian fasting dishes like sabudana khichdi.', 'Seller': 'AGROZON'},
    441:{'Product Name': 'Sambar Powder', 'Price': 90, 'Stock': 150, 'Description': 'Sambar powder, spice blend used in South Indian sambar dishes.', 'Seller': 'AGROZON'},
    442:{'Product Name': 'Santol (Cotton Fruit)', 'Price': 1200, 'Stock': 60, 'Description': 'Santol (cotton fruit), sweet and sour fruit with juicy segments.', 'Seller': 'AGROZON'},
    443:{'Product Name': 'Sesame Oil (Gingelly Oil)', 'Price': 250, 'Stock': 100, 'Description': 'Sesame oil, flavorful oil used in cooking and for medicinal purposes.', 'Seller': 'AGROZON'},
    444:{'Product Name': 'Sesame Seeds (Til)', 'Price': 50, 'Stock': 250, 'Description': 'Sesame seeds (til), used in Indian sweets, snacks, and savory dishes.', 'Seller': 'AGROZON'},
    445:{'Product Name': 'Sesame Seeds (White)', 'Price': 100, 'Stock': 200, 'Description': 'White sesame seeds, used in Indian sweets and savory dishes.', 'Seller': 'AGROZON'},
    446:{'Product Name': 'Shaoxing Wine (Chinese Cooking Wine)', 'Price': 150, 'Stock': 150, 'Description': 'Shaoxing wine (Chinese cooking wine), fermented rice wine used in Chinese cooking for adding depth of flavor to stir-fries, braises, and marinades.', 'Seller': 'AGROZON'},
    447:{'Product Name': 'Shrimp Paste (Belacan)', 'Price': 150, 'Stock': 150, 'Description': 'Shrimp paste (belacan), fermented condiment made from shrimp used in Southeast Asian cooking to add umami flavor to dishes.', 'Seller': 'AGROZON'},
    448:{'Product Name': 'Sichuan Peppercorns', 'Price': 120, 'Stock': 180, 'Description': 'Sichuan peppercorns, numbing spice with citrusy and floral notes used in Sichuan and Chinese cuisine for adding heat and flavor to dishes.', 'Seller': 'AGROZON'},
    449:{'Product Name': 'Snake Gourd (Chichinda)', 'Price': 40, 'Stock': 200, 'Description': 'Fresh snake gourd, used in Indian curries and stir-fries.', 'Seller': 'AGROZON'},
    450:{'Product Name': 'Sooji (Semolina)', 'Price': 30, 'Stock': 300, 'Description': 'Sooji (semolina), coarse flour used in Indian sweets and savory dishes.', 'Seller': 'AGROZON'},
    451:{'Product Name': 'Soursop (Graviola)', 'Price': 1200, 'Stock': 50, 'Description': 'Soursop (graviola), known for its creamy texture and sweet-sour flavor.', 'Seller': 'AGROZON'},
    452:{'Product Name': 'Spinach (Palak)', 'Price': 25, 'Stock': 350, 'Description': 'Fresh spinach (palak), used in Indian curries, soups, and as a side dish.', 'Seller': 'AGROZON'},
    453:{'Product Name': 'Star Anise', 'Price': 120, 'Stock': 150, 'Description': 'Star anise, distinctive spice used in biryanis and spice blends.', 'Seller': 'AGROZON'},
    454:{'Product Name': 'Star Anise (Chakra Phool)', 'Price': 180, 'Stock': 120, 'Description': 'Star anise (chakra phool), star-shaped spice with a licorice-like flavor used in Indian cooking, especially in biryanis and masalas.', 'Seller': 'AGROZON'},
    455:{'Product Name': 'Star Anise (Chakriphool)', 'Price': 100, 'Stock': 120, 'Description': 'Star anise (chakriphool), star-shaped spice with a licorice-like flavor used in Indian cooking.', 'Seller': 'AGROZON'},
    456:{'Product Name': 'Starfruit (Carambola)', 'Price': 1000, 'Stock': 70, 'Description': 'Starfruit (carambola), with a tangy flavor and star-like shape.', 'Seller': 'AGROZON'},
    457:{'Product Name': 'Steel-Cut Oats', 'Price': 60, 'Stock': 100, 'Description': 'Nutritious steel-cut oats, ideal for hearty breakfasts.', 'Seller': 'AGROZON'},
    458:{'Product Name': 'Tamarind (Imli)', 'Price': 80, 'Stock': 200, 'Description': 'Tamarind (imli), sour fruit used in Indian cuisine for its tangy flavor in chutneys, curries, and sauces.', 'Seller': 'AGROZON'},
    459:{'Product Name': 'Tamarind Chutney', 'Price': 100, 'Stock': 100, 'Description': 'Tamarind chutney, sweet and sour condiment made from tamarind, used in chaats and snacks.', 'Seller': 'AGROZON'},
    460:{'Product Name': 'Tamarind Paste', 'Price': 120, 'Stock': 150, 'Description': 'Tamarind paste, adds tanginess to dishes like sambar and chutneys.', 'Seller': 'AGROZON'},
    461:{'Product Name': 'Tamarind Pulp (Imli Pulp)', 'Price': 60, 'Stock': 150, 'Description': 'Tamarind pulp (imli pulp), concentrated tamarind paste used to add sourness to Indian curries and chutneys.', 'Seller': 'AGROZON'},
    462:{'Product Name': 'Tandoori Masala', 'Price': 120, 'Stock': 150, 'Description': 'Tandoori masala, spice blend used to marinate meats and vegetables for tandoori cooking.', 'Seller': 'AGROZON'},
    463:{'Product Name': 'Thai Basil', 'Price': 100, 'Stock': 120, 'Description': 'Thai basil, herb with a sweet and slightly spicy flavor used in Thai curries, stir-fries, and salads.', 'Seller': 'AGROZON'},
    464:{'Product Name': 'Thai Fish Sauce (Nam Pla)', 'Price': 100, 'Stock': 250, 'Description': 'Thai fish sauce (nam pla), fermented condiment made from fish and salt used as a seasoning in Thai cooking for adding savory umami flavor to dishes.', 'Seller': 'AGROZON'},
    465:{'Product Name': 'Thai Palm Sugar (Nam Tan Peep)', 'Price': 120, 'Stock': 180, 'Description': 'Thai palm sugar (nam tan peep), natural sweetener made from palm sap used in Thai desserts, curries, and sauces for its caramel-like flavor.', 'Seller': 'AGROZON'},
    466:{'Product Name': 'Thai Tamarind Paste', 'Price': 90, 'Stock': 200, 'Description': 'Thai tamarind paste, concentrated pulp made from tamarind fruit used in Thai cooking for adding tartness.', 'Seller': 'AGROZON'},
    467:{'Product Name': 'Tindora (Ivy Gourd)', 'Price': 40, 'Stock': 250, 'Description': 'Fresh tindora (ivy gourd), used in Indian curries and stir-fries.', 'Seller': 'AGROZON'},
    468:{'Product Name': 'Tomato (Tamatar)', 'Price': 25, 'Stock': 300, 'Description': 'Tomato (tamatar), essential ingredient in Indian cooking for making curries, chutneys, and salads.', 'Seller': 'AGROZON'},
    469:{'Product Name': 'Tomatoes', 'Price': 20, 'Stock': 400, 'Description': 'Fresh tomatoes, used in Indian curries, salads, and as a base for sauces.', 'Seller': 'AGROZON'},
    470:{'Product Name': 'Toor Dal', 'Price': 80, 'Stock': 120, 'Description': 'Toor dal, split pigeon peas used in Indian cooking to make dal and sambhar.', 'Seller': 'AGROZON'},
    471:{'Product Name': 'Turmeric Powder', 'Price': 25, 'Stock': 120, 'Description': 'Ground turmeric powder, known for its anti-inflammatory properties.', 'Seller': 'AGROZON'},
    472:{'Product Name': 'Turmeric Powder (Haldi)', 'Price': 50, 'Stock': 250, 'Description': 'Turmeric powder (haldi), bright yellow spice with earthy flavor used in Indian cooking for its color and health benefits.', 'Seller': 'AGROZON'},
    473:{'Product Name': 'Turmeric Root', 'Price': 30, 'Stock': 100, 'Description': 'Fresh turmeric root, known for its health benefits and culinary uses.', 'Seller': 'AGROZON'},
    474:{'Product Name': 'Turmeric Root (Fresh Haldi)', 'Price': 80, 'Stock': 100, 'Description': 'Turmeric root (fresh haldi), fresh turmeric used in Indian cooking for its medicinal properties and flavor.', 'Seller': 'AGROZON'},
    475:{'Product Name': 'Turmeric Root Powder', 'Price': 30, 'Stock': 100, 'Description': 'Ground turmeric root powder, known for its health benefits.', 'Seller': 'AGROZON'},
    476:{'Product Name': 'Turmeric Root Spice', 'Price': 30, 'Stock': 100, 'Description': 'Ground turmeric root spice, known for its health benefits and culinary uses.', 'Seller': 'AGROZON'},
    477:{'Product Name': 'Turmeric Spice Powder', 'Price': 30, 'Stock': 100, 'Description': 'Ground turmeric spice powder, known for its health benefits.', 'Seller': 'AGROZON'},
    478:{'Product Name': 'Urad Dal', 'Price': 90, 'Stock': 100, 'Description': 'Urad dal, split black gram used in Indian cooking to make dal, dosa batter, and snacks like vadas.', 'Seller': 'AGROZON'},
    479:{'Product Name': 'Vanilla Bean Extract', 'Price': 150, 'Stock': 50, 'Description': 'Pure vanilla bean extract, adds rich flavor to baked goods and desserts.', 'Seller': 'AGROZON'},
    480:{'Product Name': 'Vanilla Beans', 'Price': 100, 'Stock': 50, 'Description': 'Whole vanilla beans, aromatic and perfect for desserts and infusions.', 'Seller': 'AGROZON'},
    481:{'Product Name': 'Vanilla Extract', 'Price': 150, 'Stock': 50, 'Description': 'Pure vanilla extract, adds rich flavor to baked goods and desserts.', 'Seller': 'AGROZON'},
    482:{'Product Name': 'Vietnamese Fish Sauce (Nuoc Mam)', 'Price': 150, 'Stock': 150, 'Description': 'Vietnamese fish sauce (nuoc mam), fermented condiment made from fish and salt used in Vietnamese cooking as a seasoning and dipping sauce.', 'Seller': 'AGROZON'},
    483:{'Product Name': 'Vietnamese Rice Paper', 'Price': 100, 'Stock': 200, 'Description': 'Vietnamese rice paper, thin and translucent sheets made from rice flour and water used for making spring rolls and other Vietnamese dishes.', 'Seller': 'AGROZON'},
    484:{'Product Name': 'Vietnamese Rice Vermicelli', 'Price': 120, 'Stock': 180, 'Description': 'Vietnamese rice vermicelli, thin noodles made from rice flour used in Vietnamese cuisine for soups, salads, and noodle dishes.', 'Seller': 'AGROZON'},
    485:{'Product Name': 'Walnuts', 'Price': 600, 'Stock': 100, 'Description': 'Whole walnuts, used in Indian sweets, desserts, and as a snack.', 'Seller': 'AGROZON'},
    486:{'Product Name': 'Watermelon Radish', 'Price': 525, 'Stock': 110, 'Description': 'Vibrant watermelon radish, with a mild peppery flavor and striking appearance.', 'Seller': 'AGROZON'},
    487:{'Product Name': 'White Asparagus', 'Price': 600, 'Stock': 100, 'Description': 'Tender white asparagus, delicate in flavor and texture.', 'Seller': 'AGROZON'},
    488:{'Product Name': 'White Poppy Seeds (Khus Khus)', 'Price': 100, 'Stock': 200, 'Description': 'White poppy seeds (khus khus), mild and nutty seeds used in Indian sweets, gravies, and spice mixes.', 'Seller': 'AGROZON'},
    489:{'Product Name': 'Whole Bay Leaves', 'Price': 20, 'Stock': 100, 'Description': 'Whole bay leaves, aromatic and essential for soups and stews.', 'Seller': 'AGROZON'},
    490:{'Product Name': 'Whole Black Pepper', 'Price': 50, 'Stock': 100, 'Description': 'Whole black peppercorns, essential for grinding fresh pepper.', 'Seller': 'AGROZON'},
    491:{'Product Name': 'Whole Black Pepper Powder', 'Price': 50, 'Stock': 100, 'Description': 'Ground black pepper powder, essential for seasoning.', 'Seller': 'AGROZON'},
    492:{'Product Name': 'Whole Black Peppercorns', 'Price': 50, 'Stock': 100, 'Description': 'Whole black peppercorns, essential for grinding fresh pepper.', 'Seller': 'AGROZON'},
    493:{'Product Name': 'Whole Cinnamon Bark', 'Price': 60, 'Stock': 120, 'Description': 'Whole cinnamon bark, perfect for infusing flavor in beverages and dishes.', 'Seller': 'AGROZON'},
    494:{'Product Name': 'Whole Cinnamon Sticks', 'Price': 60, 'Stock': 120, 'Description': 'Whole cinnamon sticks, perfect for infusing flavor in beverages and dishes.', 'Seller': 'AGROZON'},
    495:{'Product Name': 'Whole Clove Seeds', 'Price': 70, 'Stock': 80, 'Description': 'Whole clove seeds, aromatic spice used in both sweet and savory dishes.', 'Seller': 'AGROZON'},
    496:{'Product Name': 'Whole Clove Spice', 'Price': 70, 'Stock': 80, 'Description': 'Whole clove spice, aromatic and used in both sweet and savory dishes.', 'Seller': 'AGROZON'},
    497:{'Product Name': 'Whole Cloves', 'Price': 70, 'Stock': 80, 'Description': 'Whole cloves, aromatic spice used in both sweet and savory dishes.', 'Seller': 'AGROZON'},
    498:{'Product Name': 'Whole Fennel Seeds', 'Price': 40, 'Stock': 100, 'Description': 'Whole fennel seeds, aromatic and great for teas and cooking.', 'Seller': 'AGROZON'},
    499:{'Product Name': 'Whole Grain Bread', 'Price': 50, 'Stock': 80, 'Description': 'Nutritious whole grain bread, freshly baked.', 'Seller': 'AGROZON'},
    500:{'Product Name': 'Whole Grain Pasta', 'Price': 80, 'Stock': 80, 'Description': 'Nutritious whole grain pasta, great for wholesome meals.', 'Seller': 'AGROZON'},
    501:{'Product Name': 'Whole Milk', 'Price': 90, 'Stock': 100, 'Description': 'Rich and creamy whole milk, great for drinking and cooking.', 'Seller': 'AGROZON'},
    502:{'Product Name': 'Whole Red Chilies (Sabut Lal Mirch)', 'Price': 70, 'Stock': 300, 'Description': 'Whole red chillies (sabut lal mirch), dried red chillies used for tempering and in spice blends in Indian cooking.', 'Seller': 'AGROZON'},
    503:{'Product Name': 'Whole Vanilla Beans', 'Price': 120, 'Stock': 50, 'Description': 'Whole vanilla beans, aromatic and perfect for desserts and infusions.', 'Seller': 'AGROZON'},
    504:{'Product Name': 'Whole Wheat Flour', 'Price': 80, 'Stock': 100, 'Description': 'Stone-ground whole wheat flour, ideal for baking.', 'Seller': 'AGROZON'},
    505:{'Product Name': 'Whole Wheat Flour (Atta)', 'Price': 30, 'Stock': 300, 'Description': 'Whole wheat flour (atta), used in Indian breads like chapati and paratha.', 'Seller': 'AGROZON'},
    506:{'Product Name': 'Wild-Caught Salmon Fillet', 'Price': 350, 'Stock': 20, 'Description': 'Premium wild-caught salmon fillet, rich in omega-3s.', 'Seller': 'AGROZON'},
    507:{'Product Name': 'Yellow Dragon Fruit', 'Price': 1100, 'Stock': 50, 'Description': 'Yellow dragon fruit, sweeter and milder than the red variety.', 'Seller': 'AGROZON'},
    508:{'Product Name': 'Yellow Mustard Powder', 'Price': 35, 'Stock': 100, 'Description': 'Yellow mustard powder, great for making mustard sauces and dressings.', 'Seller': 'AGROZON'},
    509:{'Product Name': 'Yellow Mustard Seeds', 'Price': 35, 'Stock': 80, 'Description': 'Yellow mustard seeds, ideal for pickling and making mustard sauce.', 'Seller': 'AGROZON'},
    510:{'Product Name': 'Yellow Mustard Seeds (Sarson)', 'Price': 60, 'Stock': 200, 'Description': 'Yellow mustard seeds (sarson), mild and slightly sweet seeds used in pickles, sauces, and spice mixes in Indian cuisine.', 'Seller': 'AGROZON'},
    511:{'Product Name': 'Yellow Pitahaya (Yellow Dragon Fruit)', 'Price': 1000, 'Stock': 70, 'Description': 'Yellow pitahaya (yellow dragon fruit), sweet and refreshing.', 'Seller': 'AGROZON'},
    512:{'Product Name': 'Yellow Watermelon', 'Price': 700, 'Stock': 90, 'Description': 'Yellow watermelon, sweet and refreshing, perfect for hot summer days.', 'Seller': 'AGROZON'},
    513: {'Product Name': 'yuvan yogurt', 'Price': 10, 'Stock': 100000, 'Description': 'tasty', 'Seller': 'YUVAN'},
    514: {'Product Name': 'siva salts', 'Price': 10, 'Stock': 100, 'Description': 'tasty', 'Seller': 'SIVA'},
    515: {'Product Name': 'manish meat masala', 'Price': 12, 'Stock': 12, 'Description': 'good for meat', 'Seller': 'ABISEK'},
    516: {'Product Name': 'asim coffee powder', 'Price': 90, 'Stock': 100, 'Description': 'fine coffee powder', 'Seller': 'ASIM'},
    517: {'Product Name': 'ram rice cake', 'Price': 20, 'Stock': 1000, 'Description': 'best in the market', 'Seller': 'YUVAN'},
    518: {'Product Name': 'kidney beans', 'Price': 10, 'Stock': 92, 'Description': 'i mean if you want to', 'Seller': 'BADHRI'},
    519: {'Product Name': 'yuvan icecreams', 'Price': 100, 'Stock': 406, 'Description': 'vanga friends vanga', 'Seller': 'YUVAN'}
}

    users = {
    'ASIM': 'AsimIsmail@123',
    'DEEPESH': 'iroots',
    'MANISH': '123456',
    'NITHIN': 'password@1',
    'YUVAN': 'abcdef',
    'ABISEK': 'P.abisek'
}
    
    userinfo = {
    'ASIM': {'Phone Number': '9629794101', 'Address': 'Shanti Nagar,19 Street,Tirunelveli'},
    'DEEPESH': {'Phone Number': '9845984589', 'Address': ''},
    'MANISH': {'Phone Number': '9845984589', 'Address': ''},
    'NITHIN': {'Phone Number': '8072606096', 'Address': 'No.32,Rajaji Nagar,KTC Nagar'},
    'YUVAN': {'Phone Number': '9994755902', 'Address': ''},
    'ABISEK': {'Phone Number': '9486657570', 'Address': 'Near Jeba Garden'}
}
 
    for i in groceries:
        if i not in products.keys():
            t = str(groceries[i].values())
            t = t[13:-2]
            prod = str(i)+','+t
            cursor.execute('insert into PRODUCTS values('+prod+')')
            products[i] = {'Product Name': groceries[i]['Product Name'], 'Price': groceries[i]['Price'],'Stock': groceries[i]['Stock'], 'Description': groceries[i]['Description'], 'Seller': groceries[i]['Seller']}    
    if products == {}:
         c = 0
    else:
        cursor.execute('select max(productid) from products')
        for i in cursor:
            c = i[0]

    for i in users:
        if i not in accounts.keys():
            accounts[i]=users[i]
            accounts_info[i] = userinfo[i]
            t = (i,users[i],userinfo[i]['Phone Number'],userinfo[i]['Address'])
            cursor.execute('insert into user_info values'+str(t))
            cursor.execute('create table if not exists '+i+'(ProductID int primary key,ProductName varchar(50),Price int,Quantity int,Description varchar(150))')
    if 'AGROZON' not in deleted_acc:
        deleted_acc.append('AGROZON')
        cursor.execute("insert into deletedusers values('AGROZON')")
                   
def sign_in():
    print('USERNAME CANNOT BE CHANGED AFTERWARDS')
    while True:
        name = input('Enter your username: ').upper()
        if name not in accounts and name not in deleted_acc and len(name)>0 and len(name)<30 and name.isalpha() and name not in ['orders','products','user_info']:
            break
        else:
            print('Username is already taken or Invalid')
  
    while True:
        phone_number = input('Enter phone number: ')
        if len(phone_number)==10 and phone_number.isdigit():
            break
        else:
            print('Not a real phone number')

    while True:
        address = input('Enter address: ')
        if len(address) < 150:
            break
        else:
            print('Address is too long')      

    tempdict = {'Phone Number':phone_number,'Address':address} 
    while True:
        password=input("Enter your password(for your new account):")
        if len(password) > 5 and len(password) < 30:
            break
        elif len(password) >= 30:
            print('Password is too long')            
        else:
            print('Password should be more than 5 characters')
      
    accounts[name]=password
    accounts_info[name] = tempdict
    t = (name,password,phone_number,address)
    cursor.execute('insert into user_info values'+str(t))
    cursor.execute('create table if not exists '+name+'(ProductID int primary key,ProductName varchar(50),Price int,Quantity int,Description varchar(150))')
    print()
    print("Enter your login details")
    print()
    login()
  
########### 
def login():
    while True:
        userID_input=input("Enter your username: ").upper()
        break
    pass_input=input("Enter your password:")
    if userID_input in accounts.keys() and accounts[userID_input]== pass_input:
        print("Enter password again to verify")
        pass_input2=input("Enter your password:")
        if accounts[userID_input]!= pass_input2:
            print()
            print("Wrong Password")
            print()
            login_portal()
        else:
            print()
            print('Succesful Login!')
            global signin_acc
            signin_acc = userID_input
            cursor.execute('select * from '+signin_acc)
            for i in cursor:
                cart[i[0]] = {'Product Name': i[1],'Price':i[2],
                                'Quantity':i[3],'Description': i[4]}
            print('Welcome',signin_acc)
            input('Press Enter to Continue')
            for i in range(40):
                print('\n')
            main()                    
    else: 
        print("Invalid Details")
        print('''1.Try again
2.Sign in''')
        while True:
            accnotfound_choice =(input("enter the choice:"))
            if(accnotfound_choice =='1'):
                login()
                break
            elif(accnotfound_choice =='2'):
                sign_in()
                break
            else:
                print('Not a valid option')

###########
def login_portal():
    if signin_acc == '':
        print(' ____________________________________________________')
        print('|                                                    |')
        print('|-------------------*LOGIN_PORTAL*-------------------|')
        print('|____________________________________________________|')
        print()
        print('''Do you have a account on AGROZON?
1.Yes
2.No''')
        while True:
            LoginPortal_prompt=(input("Enter the choice:"))
            if LoginPortal_prompt == '1' or LoginPortal_prompt == '2':
                break
            else:
                print('Not a valid option')
        if(LoginPortal_prompt =='1'):
            print()
            login()
        if(LoginPortal_prompt =='2'):
            print()
            sign_in()
    else:
        main()
        

###########

def buy():
    templ = []
    print('-----------------*BUY_PRODUCTS*---------------------')
    print()
    print('Some Available Products: ')
    print(' ----------------------------------------------------------------------')
    print('|                   Product Name                   |Price    |Stock    |')
    print(' ----------------------------------------------------------------------')
    for i in range(15):
        while True:
            j = random.randrange(1,max(products.keys())+1)
            if j in templ:
                pass
            else:
                templ.append(j)
                break
        t1 = str(j)+(' '*(9-len(str(j))))
        t2 = products[j]['Product Name']+(' '*(50-len(products[j]['Product Name'])))
        t3 = str(products[j]['Price'])+(' '*(9-len(str(products[j]['Price']))))
        t4 = str(products[j]['Stock'])+(' '*(9-len(str(products[j]['Stock']))))
        print('|',t2,'|',t3,'|',t4,'|',sep='')   
    print(' ----------------------------------------------------------------------')
    print()
    prodbuy = input('Enter what you would like to buy: ').lower()
    print()
    buy_func(products,prodbuy)
    main()

def buy_func(lst,prod):
    l = []
    flag = 0
    f1 = 0
    for i in products:
        if prod in products[i]['Product Name'].lower() and products[i]['Seller'] != signin_acc and products[i]['Stock'] != 0:
            l.append(str(i))
    if l == []:
        print('There are no such items')
        print()
    else:
        print(' --------------------------------------------------------------------------------')
        print('|ProductID|                   Product Name                   |Price    |Stock    |')
        print(' --------------------------------------------------------------------------------')
        for i in l:
            i = int(i)
            t1 = str(i)+(' '*(9-len(str(i))))
            t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
            t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
            t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
            print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
        print(' --------------------------------------------------------------------------------')
        while True:
            print()
            buyprod = input("Enter the product number you want to buy(Enter 'q' if you want to go back): ")
            if (buyprod.isdigit() and (buyprod in l)):
                f1 = 1
                break
            elif buyprod == 'q':
                break
            else:
                print('Not a valid option','\n')
        if f1 == 1:
            print('Description:',products[int(buyprod)]['Description'])
            while True:
                print('Do you want to buy this product?')
                CHOICE = input('Enter y or n: ')
                if CHOICE == 'y':
                    flag = 1
                    break
                elif CHOICE == 'n':
                    break
                else:
                    print('Not a valid option')
        if buyprod.isdigit() and flag == 1:
            buyprod = int(buyprod)
            while True:
                try:
                    quan = int(input('Enter the quantity of products: '))
                    if quan > lst[buyprod]['Stock'] or quan <= 0:
                        print('Quantity cannot be more than stock or less than 0')
                    else:
                        print()
                        print('Added to cart')
                        print()
                        lst[buyprod]['Stock'] -= quan
                        cursor.execute('update products set stock=stock- '+str(quan)+' where ProductID='+str(buyprod))
                        tempdict = {'Product Name': lst[buyprod]['Product Name'], 'Price': lst[buyprod]['Price'],
                                    'Quantity': quan, 'Description': lst[buyprod]['Description']}
                        if buyprod not in cart:
                            cart[buyprod] = {'Product Name': lst[buyprod]['Product Name'],'Price':quan*lst[buyprod]['Price'],
                                             'Quantity':quan,'Description': lst[buyprod]['Description']}
                            t = str(cart[buyprod].values())
                            t = t[13:-2]
                            prod = str(buyprod)+','+t
                            cursor.execute('insert into '+signin_acc+' values('+prod+')')                            
                        else:
                            cart[buyprod]['Quantity'] += quan
                            cursor.execute('update '+signin_acc+' set quantity=quantity+'+str(quan)+' where ProductID='+str(buyprod))
                        break
                except ValueError:
                    print('Invalid value')
        elif buyprod == 'q':
            print()
            pass
    

###########                     
def sell():
    global c
    while True:
        print('-----------------*SELL_MENU*---------------------')
        print()
        print('''What would you like to do?
1.Sell Products
2.Manage Products
3.Go Back''')
        choice1 = input('Enter a choice: ')
        if choice1 == '1':
            print('-----------------*SELL_PRODUCTS*---------------------')
            print()
            print()
            prodname = input('Enter the product name: ')
            while True:
                try:
                    price = int(input('Enter price per unit: '))
                    if price <= 0:
                        print('Price should be greater than Rs.0')
                    elif len(str(price)) > 9:
                        print('Price is out of range')
                    else:
                        break
                except ValueError:
                    print('Price should be an integer')
            while True:
                try:
                    stock = int(input('Enter Stock: '))
                    if stock <= 0:
                        print('Stock should be greater than 0')
                    elif len(str(stock)) > 9:
                        print('Stock is out of range')
                    else:
                        break
                except ValueError:
                    print('Stock should be in numbers')
            while True:
                descrip = input('Enter description(optional): ')
                if len(descrip) > 150:
                    print('Description cannot be more than 150 characters long')
                else:
                    break
            products[c+1] = {'Product Name':prodname,'Price':price,'Stock':stock,'Description':descrip,'Seller':signin_acc}
            t = str(products[c+1].values())
            t = t[13:-2]
            prod = str(c+1)+','+t
            cursor.execute('insert into products values('+str(c+1)+','+t+')')
            c += 1
            print('Product Added!')
            print()
        elif choice1 == '2':
            print()
            manage_prod()
        elif choice1 == '3':
            print()
            main()
            break
        else:
            print('Not a valid option')
                
                
    
        

def manage_prod():
    while True:
        k = 0
        for i in products:
            if products[i]['Seller'] == signin_acc:
                    k += 1
        if k == 0:
            print('You have no products')
            print()
            break
        print('-----------------*MANAGE_PRODUCTS*---------------------')
        print()
        print('''What would you like to do
1.View Products
2.Delete Product
3.Increase Stock
4.Increase Price
5.Change Description
6.Check Sales
7.Go Back''')
        choice2 = input('Enter the numerical value: ')
        if choice2 == '1':
            print('-----------------*VIEW_PRODUCTS*---------------------')
            print()
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc and signin_acc != 'AGROZON':                    
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
        elif choice2 == '2':
            print()
            l = []
            print('-----------------*REMOVE_PRODUCTS*---------------------')
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc:
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            delprodchoice = input('Enter The product number which you want to delete: ')
            if delprodchoice in l:
                while True:
                    print('Product Name',products[int(delprodchoice)]['Product Name'],sep=':')
                    print()
                    print('Are you sure you want to delete this product?')
                    CHOICE = input("Enter 'y' or 'n': ")
                    if CHOICE == 'y':
                        products.pop(int(delprodchoice))
                        cursor.execute('delete from products where ProductID = '+delprodchoice)
                        print('Item successfully deleted')
                        print()
                        break
                    elif CHOICE == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice2 == '3':
            print()
            l = []
            print('-----------------*INCREASE_STOCK*---------------------')
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc:
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            incrstockchoice = input('Enter The product number which you want to increase the stock: ')
            if incrstockchoice in l:
                while True:
                    print('Product Name',products[int(incrstockchoice)]['Product Name'],sep=':')
                    print('Stock',products[int(incrstockchoice)]['Stock'],sep=':')
                    print()
                    print('Is this the product you want to increase stock?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                stockincr = int(input('Enter the amount of stock you want to add: '))
                                break
                            except ValueError:
                                print('Not a valid option')
                        products[int(incrstockchoice)]['Stock'] += stockincr
                        cursor.execute('update products set stock=stock+ '+str(stockincr)+' where ProductID='+incrstockchoice)
                        print('Stock successfully added')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice2 == '4':
            print()
            l = []
            print('-----------------*INCREASE_PRICE*---------------------')
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc:
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            incrpricechoice = input('Enter The product number which you want to increase the price: ')
            if incrpricechoice in l:
                while True:
                    print('Product Name',products[int(incrpricechoice)]['Product Name'],sep=':')
                    print('Price',products[int(incrpricechoice)]['Description'],sep=':')
                    print()
                    print('Is this the product you want to increase price?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                priceincr = int(input('Enter the changed price: '))
                                if priceincr <= 0:
                                    print('Price cannot be less than 0')
                                else:
                                    break
                            except ValueError:
                                print('Not a valid option')
                        products[int(incrpricechoice)]['Price'] = priceincr
                        cursor.execute('update products set price='+str(priceincr)+' where ProductID='+incrpricechoice)
                        print('Price successfully changed')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice2 == '5':
            print()
            l = []
            print('-----------------*CHANGE_DESCRIPTION*---------------------')
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc:
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            descrchoice = input('Enter The product number which you want to change the description: ')
            if descrchoice in l:
                while True:
                    print('Product Name',products[int(descrchoice)]['Product Name'],sep=':')
                    print('Description',products[int(descrchoice)]['Description'],sep=':')
                    print()
                    print('Is this the product you want to change description?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                descchange = input('Enter the changed description: ')
                                if len(descchange) > 150:
                                    print('Description cannot be more than 150 characters long')
                                else:
                                    break
                            except ValueError:
                                print('Not a valid option')
                        products[int(descrchoice)]['Price'] = descchange
                        cursor.execute("update products set description='"+descchange+"' where ProductID="+descrchoice)
                        print('Description successfully changed')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice2 == '6':
            print('-----------------*SALES*---------------------')
            cursor.execute('select orders.Productid,orders.ProductName,Price*Quantity,Seller from orders,products where products.productid=orders.productid')
            sumprofit = 0
            for i in cursor:
                if i[3] == signin_acc:
                    sumprofit += i[2]
            print()
            print('Total balance: Rs.',sumprofit)
            print()
        elif choice2 == '7':
            print()
            break
        else:
            print('Not a valid option')
    
    
def cart_menu():
    global cart
    while True:
        if cart == {}:
            print('Cart is Empty')
            print()
            main()
            break
        else:
            print('-----------------*CART_MENU*---------------------')
            print()
            print('''What would you like to do
1.View Products
2.Remove Products from cart
3.Checkout
4.Go Back''')
            cart_prompt = input('Enter your choice(numerical value): ')
            if cart_prompt == '1':
                print()
                print('-----------------*VIEW_CART*---------------------')
                print()
                s = 0
                print(' ----------------------------------------------------------------------------------')
                print('|ProductID|                   Product Name                   |Total Price|Quantity |')
                print(' ----------------------------------------------------------------------------------')
                for i in cart:
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = cart[i]['Product Name']+(' '*(50-len(cart[i]['Product Name'])))
                    t3 = str(cart[i]['Price'])+(' '*(11-len(str(cart[i]['Price']))))
                    t4 = str(cart[i]['Quantity'])+(' '*(9-len(str(cart[i]['Quantity']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')
                    s += cart[i]['Price']
                print(' ----------------------------------------------------------------------------------')
                print('Total Sum of Products: ',s)                    
                print()
            elif cart_prompt == '2':
                print()
                print('-----------------*REMOVE_PRODUCTS*---------------------')
                print()
                print(' ----------------------------------------------------------------------------------')
                print('|ProductID|                   Product Name                   |Total Price|Quantity |')
                print(' ----------------------------------------------------------------------------------')
                for i in cart:
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = cart[i]['Product Name']+(' '*(50-len(cart[i]['Product Name'])))
                    t3 = str(cart[i]['Price'])+(' '*(11-len(str(cart[i]['Price']))))
                    t4 = str(cart[i]['Quantity'])+(' '*(9-len(str(cart[i]['Quantity']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')
                print(' ----------------------------------------------------------------------------------')
                while True:
                    remove = input('Enter the product number which you want to remove: ')
                    if remove.isdigit():
                        if int(remove) in cart:
                            break
                        else:
                            print('Not a valid option')
                    else:
                        print('Not a valid option')
                print()
                while True:
                    print(cart[int(remove)])
                    print('Is this the product you want to remove')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    print()
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                quandecr = int(input('Enter the quantity of products you want to remove: '))
                                if quandecr < 0 or quandecr > cart[int(remove)]['Quantity']:
                                    print('Quantity cannot be decreased by less than 0 or less than old quantity')
                                else:
                                    break
                            except ValueError:
                                print('Not a valid option')
                        cart[int(remove)]['Quantity'] -= quandecr
                        products[int(remove)]['Stock'] += quandecr
                        cursor.execute('update products set stock=stock+ '+str(quandecr)+' where ProductID='+remove)
                        cursor.execute('update '+signin_acc+' set quantity=quantity- '+str(quandecr)+' where ProductID='+remove)
                        pr = products[int(remove)]['Price']
                        cart[int(remove)]['Price'] -= quandecr*pr
                        cursor.execute('update '+signin_acc+' set price=quantity* '+str(pr)+' where ProductID='+remove)
                        if cart[int(remove)]['Quantity'] == 0:
                            cart.pop(int(remove))
                            cursor.execute('delete from '+signin_acc+' where productid='+remove)
                        print('Products successfully removed')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        break
                    else:
                        print('Not a valid option')
                        
            elif cart_prompt == '3':
                print()
                print('-----------------*CHECKOUT*---------------------')
                print()
                total=0
                temp_cart=[]
                for product in cart:
                    qty=cart[product]['Quantity']
                    price=int(cart[product]['Price']/qty)
                    pname=cart[product]['Product Name']
                    cost=price*qty
                    order='Product name:'+str(pname)+'|'+'Quantity:'+str(qty)+'|'+'Price:'+str(price)+'|'+'Cost:'+str(cost)
                    temp_cart.append(order)
                    total=total+cost                  
                print("|ITEMS IN CART:")
                print()
                o = 1
                for i in temp_cart:
                    print(o,'.',i,sep='')
                    o += 1
                print("|---------------------------------------------------------------------------|")
                print("| Amount          :",total)
                print("|---------------------------------------------------------------------------|")
                input(" Press Enter to continue")
                for i in range(50):
                    print('\n')
                print('''
1.Cash on Delivery
2.NET BANKING''')
                pay_flag=1
                while pay_flag==1:
                    PAYMENT=input('Enter the payment method(enter the numerical value):')
                    if PAYMENT=='1':
                        print()
                        while True:
                            Address = input('Enter your delivery address: ')
                            if len(Address) > 150:
                                print('Address is too long')
                            else:
                                break
                        pay_flag=0
                        print(" ")
                        print('''Your Shipment will be Delivered within 36 hours of Order in between 9 am to 6 pm;
                              For further enquiries contact: 9486657570''')
                        input("Press Enter to Continue")
                        for i in cart:
                            t = (signin_acc,i,cart[i]['Product Name'],cart[i]['Quantity'],Address)
                            cursor.execute('insert into orders values'+str(t))
                            cursor.execute('delete from '+signin_acc+' where ProductId='+str(i))
                        cart = {}
                        break
                    if PAYMENT=='2':
                        print()
                        while True:
                            Address = input('Enter your delivery address: ')
                            if len(Address) > 150:
                                print('Address is too long')
                            else:
                                break
                        print()
                        print("Which bank do you wish to select for payment?")
                        print("1.ICICI Bank")
                        print("2.Axis Bank")
                        print("3.Canara Bank")
                        print("4.TMB")
                        print("5.Punjab & Sind Bank")
                        print("6.HDFC Bank")
                        print("7.State Bank of India")

                        while True:
                            bankch=input("Which bank would you like to proceed?")
                            if bankch in ('1','2','3','4','5','6','7'):
                                break
                            else:
                                print('Not a valid option')
                                
                        while True:
                            global cvv
                            cvv = input('Enter your CVV: ')
                            if len(cvv) == 3 and cvv.isdigit():
                                break
                            else:
                                print('Not a valid value')
                                
                        pass_temop=input("Enter password:")
                        print("CVV:", cvv)
                        print("PASSWORD:", pass_temop)
                        print("OTP will be generated")

                        random23=random.randint(1000,9999)
                        print(random23)
                        while True:
                            otp23=input("Please enter OTP:")
                            if otp23==str(random23):
                                print("PAYMENT DONE")
                                break    
                            else:                 
                                print("Please enter the correct OTP")
                                continue    
                        else:
                            print("Invalid choice")  
                        print(" ")
                        print('''Your Shipment will be Delivered within 36 hours of Order in between 9 am to 6 pm;
                              For further enquiries contact: 9486657570''')
                        input("Press Enter to Continue")
                        for i in cart:
                            t = (signin_acc,i,cart[i]['Product Name'],cart[i]['Quantity'],Address)
                            cursor.execute('insert into orders values'+str(t))
                            cursor.execute('delete from '+signin_acc+' where ProductId='+str(i))
                        cart = {}
                        break    
                    else:
                        print("Invalid payment method")
                main()
                break    
            elif cart_prompt == '4':
                print()
                main()
                break
            else:
                print('Not a valid option')

def profile():
    print('-----------------*PROFILE_SETTINGS*---------------------')
    print()
    while True:
        print('''What would you like to do
1.Change Password
2.Change Phone Number
3.Change Address
4.Go Back''')
        profile_prompt = input('Enter your choice(numerical value): ')
        if profile_prompt == '1':
            print()
            print('-----------------*CHANGE_PASSWORD*---------------------')
            print()
            password = input('Enter your current password: ')
            if accounts[signin_acc] == password:
                pass
            else:
                print('Invalid')
                profile()
                break
            while True:
                passchange = input('Enter new password: ')
                if len(passchange) > 5:
                    break
                else:
                    print('Password should be more than 5 characters')                
            passchange2 = input('Enter new password again: ')
            if passchange == passchange2:
                accounts[signin_acc] = passchange
                cursor.execute("update user_info set password= '"+passchange+"' where username='"+signin_acc+"'")
                print('Password succesfully changed')
                print()
            else:
                print('Invalid')
                profile()
                break
        elif profile_prompt == '2':
            print()
            print('-----------------*CHANGE_PHONE_NUMBER*---------------------')
            print()
            while True:
                phonechange = input('Enter new Phone Number: ')
                if len(phonechange) == 10:
                    break
                else:
                    print('Invalid Phone Number')                
            accounts_info[signin_acc]['Phone Number'] = phonechange
            cursor.execute("update user_info set PhoneNumber= '"+phonechange+"' where username='"+signin_acc+"'")
            print('Phone Number succesfully changed')
            print()
        elif profile_prompt == '3':
            print()
            print('-----------------*CHANGE_ADDRESS*---------------------')
            print()
            while True:
                addchange = input('Enter new Address: ')
                if len(addchange) < 150:
                    break
                else:
                    print('Address is too long')                           
            accounts_info[signin_acc]['Address'] = addchange
            cursor.execute("update user_info set Address= '"+addchange+"' where username='"+signin_acc+"'")
            print('Address succesfully changed')
            print()
        elif profile_prompt == '4':
            print()
            main()
            break
        else:
            print('Not a valid option')

###########
def main():
    global signin_acc
    print('-----------------*MAIN_MENU*---------------------')
    print()
    print('''What would you like to do
    1.Buy
    2.Sell
    3.Cart and Checkout
    4.Profile Settings
    5.Sign Out and Close Program''')
    while True:
        BuyOrSell = input('Enter choice: ')
        if BuyOrSell == '1':
            print()
            buy()
            break
        elif BuyOrSell == '2':
            print()
            sell()
            break
        elif BuyOrSell == '3':
            print()
            cart_menu()
            break
        elif BuyOrSell == '4':
            print()
            profile()
            break
        elif BuyOrSell == '5':
            print()
            signin_acc = ''
            start()
            break
        else:
            print('Not a valid option')

def agrozon():
    userid = input('Enter username: ')
    password = input('Enter password: ')
    if userid == 'AGROZON' and password == 'admin':
        print('Welcome Admin')
        input('Press Enter to Continue')
        for i in range(40):
            print('\n')
        admin_main()
    else:
        print()
        print('Invalid Details')
        print()
        start()

def admin_main():
    while True:
        print('---------------*ADMIN_MENU*---------------')
        print()
        print('''1.View Customers
2.View Sellers
3.Manage Products
4.Ban Users
5.Exit''')
        choice = input('Enter a choice: ')
        if choice == '1':
            print()
            cursor.execute('select username from user_info')
            print(' --------------------')
            print('|UserName            |')
            print(' --------------------')
            for i in cursor:
                print('|',i[0]+(' '*(20-len(i[0]))),'|',sep='')
            print(' --------------------')
            print()
        elif choice == '2':
            print()
            cursor.execute("select seller,count(seller) from products where seller!='AGROZON' group by seller")
            print(' -----------------------------------------')
            print('|Seller              | Number of Products |')
            print(' -----------------------------------------')
            for i in cursor:
                print('|',i[0]+(' '*(20-len(i[0]))),'|',str(i[1])+(' '*(20-len(str(i[1])))),'|',sep='')
            print(' -----------------------------------------')
            print()
        elif choice == '3':
            print()
            manage_prod_admin()
            print()
        elif choice == '4':
            print()
            l = []
            cursor.execute('select username from user_info')
            print(' --------------------')
            print('|UserName            |')
            print(' --------------------')
            for i in cursor:
                print('|',i[0]+(' '*(20-len(i[0]))),'|',sep='')
                l.append(i[0])
            print(' --------------------')
            print()
            remove_user = input('Enter the account you want to delete: ').upper()
            if remove_user in l:
                while True:
                    print('UserName',remove_user,sep=':')
                    print()
                    print('Are you sure you want to delete this user?')
                    CHOICE = input("Enter 'y' or 'n': ")
                    if CHOICE == 'y':
                        a = 0
                        accounts.pop(remove_user)
                        accounts_info.pop(remove_user)
                        deleted_acc.append(remove_user)
                        for i in products:
                            if products[i]['Seller'] == remove_user:
                                a = 1
                        if a == 1:
                            l = []
                            print('Deleted products: ')
                            print()
                            print(' --------------------------------------------------------------------------------')
                            print('|ProductID|                   Product Name                   |Price    |Stock    |')
                            print(' --------------------------------------------------------------------------------')
                            for i in products:
                                if products[i]['Seller'] == remove_user:
                                    i = int(i)
                                    t1 = str(i)+(' '*(9-len(str(i))))
                                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')
                                    l.append(i)
                            for i in l:
                                products.pop(i)
                            print(' --------------------------------------------------------------------------------')
                            print()
                        cursor.execute("insert into deletedusers values('{}')".format(remove_user))
                        cursor.execute("delete from user_info where UserName = '{}'".format(remove_user))
                        cursor.execute("delete from products where Seller = '{}'".format(remove_user))
                        print('User successfully deleted')
                        print()
                        break
                    elif CHOICE == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
                
        elif choice == '5':
            print()
            start()
            break
        else:
            print('Not a valid option')

def manage_prod_admin():
    while True:
        print('-----------------*MANAGE_PRODUCTS*---------------------')
        print()
        print('''1.View Products
2.Change Stock
3.Change Price
4.Change Description
5.Remove Product
6.Go Back''')
        choice = input('Enter a choice: ')
        if choice == '1':
            print()
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                i = int(i)
                t1 = str(i)+(' '*(9-len(str(i))))
                t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
        elif choice == '2':
            print()
            l = []
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == 'AGROZON':
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            print('-----------------*CHANGE_STOCK*---------------------')
            print()
            incrstockchoice = input('Enter The product number which you want to increase the stock: ')
            if incrstockchoice in l:
                while True:
                    print('Product Name',products[int(incrstockchoice)]['Product Name'],sep=':')
                    print('Stock',products[int(incrstockchoice)]['Stock'],sep=':')
                    print()
                    print('Is this the product you want to increase stock?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                stockincr = int(input('Enter the amount of stock you want to add: '))
                                break
                            except ValueError:
                                print('Not a valid option')
                        products[int(incrstockchoice)]['Stock'] += stockincr
                        cursor.execute('update products set stock=stock+ '+str(stockincr)+' where ProductID='+incrstockchoice)
                        print('Stock successfully added')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice == '3':
            print()
            l = []
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == 'AGROZON':
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            print('-----------------*CHANGE_PRICE*---------------------')
            print()
            incrpricechoice = input('Enter The product number which you want to increase the price: ')
            if incrpricechoice in l:
                while True:
                    print('Product Name',products[int(incrpricechoice)]['Product Name'],sep=':')
                    print('Price',products[int(incrpricechoice)]['Description'],sep=':')
                    print()
                    print('Is this the product you want to increase price?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                priceincr = int(input('Enter the changed price: '))
                                if priceincr <= 0:
                                    print('Price cannot be less than 0')
                                else:
                                    break
                            except ValueError:
                                print('Not a valid option')
                        products[int(incrpricechoice)]['Price'] = priceincr
                        cursor.execute('update products set price='+str(priceincr)+' where ProductID='+incrpricechoice)
                        print('Price successfully changed')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice == '4':
            print()
            l = []
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                if products[i]['Seller'] == signin_acc:
                    l.append(str(i))
                    i = int(i)
                    t1 = str(i)+(' '*(9-len(str(i))))
                    t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                    t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                    t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                    print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            print('-----------------*CHANGE_DESCRIPTION*---------------------')
            print()
            descrchoice = input('Enter The product number which you want to change the description: ')
            if descrchoice in l:
                while True:
                    print('Product Name',products[int(descrchoice)]['Product Name'],sep=':')
                    print('Description',products[int(descrchoice)]['Description'],sep=':')
                    print()
                    print('Is this the product you want to change description?')
                    CHOICE2 = input("Enter 'y' or 'n': ")
                    if CHOICE2 == 'y':
                        while True:
                            try:
                                descchange = input('Enter the changed description: ')
                                if len(descchange) > 150:
                                    print('Description cannot be more than 150 characters long')
                                else:
                                    break
                            except ValueError:
                                print('Not a valid option')
                        products[int(descrchoice)]['Price'] = descchange
                        cursor.execute("update products set description='"+descchange+"' where ProductID="+descrchoice)
                        print('Description successfully changed')
                        print()
                        break
                    elif CHOICE2 == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice == '5':
            l = []
            print(' --------------------------------------------------------------------------------')
            print('|ProductID|                   Product Name                   |Price    |Stock    |')
            print(' --------------------------------------------------------------------------------')
            for i in products:
                l.append(str(i))
                i = int(i)
                t1 = str(i)+(' '*(9-len(str(i))))
                t2 = products[i]['Product Name']+(' '*(50-len(products[i]['Product Name'])))
                t3 = str(products[i]['Price'])+(' '*(9-len(str(products[i]['Price']))))
                t4 = str(products[i]['Stock'])+(' '*(9-len(str(products[i]['Stock']))))
                print('|',t1,'|',t2,'|',t3,'|',t4,'|',sep='')            
            print(' --------------------------------------------------------------------------------')
            print()
            print('-----------------*REMOVE_PRODUCTS*---------------------')
            print()
            delprodchoice = input('Enter The product number which you want to delete: ')
            if delprodchoice in l:
                while True:
                    print('Product Name',products[int(delprodchoice)]['Product Name'],sep=':')
                    print()
                    print('Are you sure you want to delete this product?')
                    CHOICE = input("Enter 'y' or 'n': ")
                    if CHOICE == 'y':
                        products.pop(int(delprodchoice))
                        cursor.execute('delete from products where ProductID = '+delprodchoice)
                        print('Item successfully deleted')
                        print()
                        break
                    elif CHOICE == 'n':
                        print()
                        break
                    else:
                        print('Not a valid option')
            else:
                print('Not a valid option')
        elif choice == '6':
            break
        else:
            print('Not a valid option')
    
def start():
    global signin_acc
    print(' ____________________________________')
    print('|                                    |')
    print('|---------------*MENU*---------------|')
    print('|____________________________________|')
    print()
    print('''Select an option
1.Admin
2.Customer
3.Exit''')
    while True:
        prompt = input('Enter your choice: ')
        if prompt == '1':
            print()
            agrozon()
            break
        elif prompt == '2':
            print()
            login_portal() 
            break
        elif prompt == '3':
            print()
            print('Thank you for using our app!')
            mycon.commit()
            mycon.close()
            break
        else:
            print('Not a valid option')
     
transfer()
start()


   
   


