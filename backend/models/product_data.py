"""
Mock product data for the E-Commerce Recommendation System.
This serves as our in-memory product catalog.
"""

PRODUCTS = [
     # ─────────────────────────────────────────────────────────────
    # ELECTRONICS (20 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 1,
        "name": "Sony WH-1000XM5 Headphones",
        "category": "Electronics",
        "brand": "Sony",
        "price": 349.99,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
        "description": "Industry-leading noise cancelling with Auto NC Optimizer. Crystal-clear hands-free calling with 4 beamforming microphones.",
        "features": ["noise_cancelling", "wireless", "long_battery"]
    },
    {
        "id": 2,
        "name": "Apple MacBook Air M3",
        "category": "Electronics",
        "brand": "Apple",
        "price": 1099.00,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400",
        "description": "Supercharged by M3 chip. Up to 18 hours of battery life. Stunningly thin design with a brilliant Liquid Retina display.",
        "features": ["portable", "high_performance", "long_battery"]
    },
    {
        "id": 4,
        "name": "Samsung Galaxy S24 Ultra",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 1299.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400",
        "description": "Galaxy AI is here. Search like never before, built-in S Pen, 200MP camera with nightography and 100x Space Zoom.",
        "features": ["high_performance", "camera", "AI"]
    },
    {
        "id": 8,
        "name": "Apple iPad Pro 13-inch M4",
        "category": "Electronics",
        "brand": "Apple",
        "price": 1299.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400",
        "description": "Thin. Light. Phenomenally powerful. The new iPad Pro, powered by the blazingly fast M4 chip with Ultra Retina XDR display.",
        "features": ["portable", "high_performance", "creative"]
    },
    {
        "id": 10,
        "name": "Sony PlayStation 5",
        "category": "Electronics",
        "brand": "Sony",
        "price": 499.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400",
        "description": "Experience lightning-fast loading with an ultra-high speed SSD, deeper immersion with haptic feedback and adaptive triggers.",
        "features": ["gaming", "high_performance", "4K"]
    },
    {
        "id": 11,
        "name": "Bose QuietComfort Ultra Earbuds",
        "category": "Electronics",
        "brand": "Bose",
        "price": 299.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1590658268037-6bf12f032f55?w=400",
        "description": "World-class noise cancellation and Immersive Audio. CustomTune sound calibration personalized to your ears.",
        "features": ["noise_cancelling", "wireless", "compact"]
    },
    {
        "id": 13,
        "name": "Canon EOS R6 Mark II Camera",
        "category": "Electronics",
        "brand": "Canon",
        "price": 2499.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400",
        "description": "Full-frame mirrorless camera with 24.2MP, up to 40 fps electronic shutter, and advanced subject detection AF.",
        "features": ["camera", "high_performance", "professional"]
    },
    {
        "id": 15,
        "name": "Samsung 65\" OLED 4K Smart TV",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 1799.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400",
        "description": "Experience pure blacks and vivid colors with Samsung OLED. Neural Quantum Processor 4K with Dolby Atmos sound.",
        "features": ["4K", "smart", "OLED"]
    },
    {
        "id": 20,
        "name": "Logitech MX Master 3S Mouse",
        "category": "Electronics",
        "brand": "Logitech",
        "price": 99.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400",
        "description": "Advanced wireless mouse with ultra-fast scrolling, 8K DPI tracking, and quiet clicks. Ergonomic design for all-day comfort.",
        "features": ["ergonomic", "wireless", "precise"]
    },
    {
        "id": 21,
        "name": "Apple AirPods Pro 2nd Gen",
        "category": "Electronics",
        "brand": "Apple",
        "price": 249.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400",
        "description": "Active Noise Cancellation up to 2x more powerful. Adaptive Audio for seamless transitions between environments.",
        "features": ["noise_cancelling", "wireless", "spatial_audio"]
    },
    {
        "id": 22,
        "name": "Dell XPS 15 Laptop",
        "category": "Electronics",
        "brand": "Dell",
        "price": 1799.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=400",
        "description": "15.6-inch OLED display with Intel Core i9, 32GB RAM and NVIDIA RTX 4070. InfinityEdge display with 3.5K resolution.",
        "features": ["high_performance", "OLED", "portable"]
    },
    {
        "id": 23,
        "name": "GoPro Hero 12 Black",
        "category": "Electronics",
        "brand": "GoPro",
        "price": 399.99,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400",
        "description": "5.3K60 + 4K120 video, HyperSmooth 6.0 stabilization, waterproof to 33ft without housing. Built-in GPS and Bluetooth.",
        "features": ["waterproof", "4K", "stabilization"]
    },
    {
        "id": 24,
        "name": "Kindle Paperwhite 16GB",
        "category": "Electronics",
        "brand": "Amazon",
        "price": 149.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1592434134753-a70baf7979d5?w=400",
        "description": "300 ppi glare-free display, adjustable warm light, waterproof, and up to 12 weeks of battery. Now with faster page turns.",
        "features": ["lightweight", "long_battery", "waterproof"]
    },
    {
        "id": 25,
        "name": "DJI Mini 4 Pro Drone",
        "category": "Electronics",
        "brand": "DJI",
        "price": 759.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400",
        "description": "Under 249g foldable drone with 4K/60fps HDR video, omnidirectional obstacle sensing, and 34-min max flight time.",
        "features": ["4K", "portable", "obstacle_sensing"]
    },
    {
        "id": 26,
        "name": "LG UltraWide 34\" Monitor",
        "category": "Electronics",
        "brand": "LG",
        "price": 699.99,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
        "description": "34-inch curved QHD IPS display with 160Hz refresh rate and 1ms response time. HDR400 with USB-C 90W power delivery.",
        "features": ["curved", "high_refresh", "ultrawide"]
    },
    {
        "id": 27,
        "name": "Razer DeathAdder V3 Pro",
        "category": "Electronics",
        "brand": "Razer",
        "price": 159.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=400",
        "description": "Wireless gaming mouse with 30K DPI optical sensor, 90-hour battery life, and ultra-lightweight 63g design.",
        "features": ["gaming", "wireless", "lightweight"]
    },
    {
        "id": 28,
        "name": "Anker 65W GaN Charger",
        "category": "Electronics",
        "brand": "Anker",
        "price": 45.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1609592424673-1b5e71e6de4d?w=400",
        "description": "3-port compact charger with 2x USB-C and 1x USB-A. GaN technology for 50% smaller size with intelligent power distribution.",
        "features": ["compact", "fast_charging", "multi_port"]
    },
    {
        "id": 29,
        "name": "Samsung 990 Pro 2TB SSD",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 179.99,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1597852074816-d933c7d2b988?w=400",
        "description": "PCIe 4.0 NVMe SSD with sequential read speeds up to 7,450 MB/s. Optimized thermal control for sustained peak performance.",
        "features": ["fast", "high_capacity", "durable"]
    },
    {
        "id": 30,
        "name": "Philips Hue Starter Kit",
        "category": "Electronics",
        "brand": "Philips",
        "price": 199.99,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
        "description": "Smart lighting starter kit with 3 color bulbs and Hue Bridge. 16 million colors and voice control with Alexa and Google Home.",
        "features": ["smart", "color_changing", "voice_control"]
    },
    {
        "id": 31,
        "name": "Meta Quest 3 VR Headset",
        "category": "Electronics",
        "brand": "Meta",
        "price": 499.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?w=400",
        "description": "Mixed reality headset with Snapdragon XR2 Gen 2, 4K+ display, and pancake lenses. Access to 500+ VR and MR titles.",
        "features": ["VR", "mixed_reality", "wireless"]
    },
 
    # ─────────────────────────────────────────────────────────────
    # CLOTHING (15 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 5,
        "name": "Levi's 501 Original Fit Jeans",
        "category": "Clothing",
        "brand": "Levi's",
        "price": 69.50,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=400",
        "description": "The iconic straight fit with an authentic look. Sits at the waist with a regular fit through the thigh and straight leg.",
        "features": ["classic", "durable", "comfortable"]
    },
    {
        "id": 9,
        "name": "The North Face Thermoball Jacket",
        "category": "Clothing",
        "brand": "The North Face",
        "price": 230.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400",
        "description": "Lightweight synthetic insulation that continues to insulate even when wet. Packable design for outdoor adventures.",
        "features": ["warm", "lightweight", "waterproof"]
    },
    {
        "id": 14,
        "name": "Patagonia Better Sweater Fleece",
        "category": "Clothing",
        "brand": "Patagonia",
        "price": 139.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400",
        "description": "Soft, comfortable fleece made from 100% recycled polyester. Fair Trade Certified sewn with a full-zip design.",
        "features": ["sustainable", "comfortable", "warm"]
    },
    {
        "id": 16,
        "name": "Nike Dri-FIT Training T-Shirt",
        "category": "Clothing",
        "brand": "Nike",
        "price": 35.00,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
        "description": "Sweat-wicking technology moves moisture away for quicker evaporation. Keeps you dry during high-intensity workouts.",
        "features": ["breathable", "lightweight", "athletic"]
    },
    {
        "id": 32,
        "name": "Ralph Lauren Polo Shirt",
        "category": "Clothing",
        "brand": "Ralph Lauren",
        "price": 98.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400",
        "description": "Classic piqué polo crafted from soft 100% cotton. Ribbed collar and cuffs with embroidered pony detail.",
        "features": ["classic", "cotton", "versatile"]
    },
    {
        "id": 33,
        "name": "Zara Oversized Blazer",
        "category": "Clothing",
        "brand": "Zara",
        "price": 119.00,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1594938298603-c8148c4b5b08?w=400",
        "description": "Relaxed-fit blazer in textured fabric with notched lapels. Single-button closure, padded shoulders, and two front pockets.",
        "features": ["trendy", "versatile", "office_wear"]
    },
    {
        "id": 34,
        "name": "Champion Reverse Weave Hoodie",
        "category": "Clothing",
        "brand": "Champion",
        "price": 65.00,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400",
        "description": "Iconic reverse weave construction resists vertical shrinkage. Made from heavyweight fleece with a kangaroo pocket.",
        "features": ["comfortable", "durable", "casual"]
    },
    {
        "id": 35,
        "name": "Uniqlo Ultra Light Down Jacket",
        "category": "Clothing",
        "brand": "Uniqlo",
        "price": 79.90,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=400",
        "description": "Packable down jacket that folds into its own pocket. 90/10 down fill with DWR coating for light water resistance.",
        "features": ["lightweight", "packable", "warm"]
    },
    {
        "id": 36,
        "name": "Lululemon Align Leggings 25\"",
        "category": "Clothing",
        "brand": "Lululemon",
        "price": 128.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400",
        "description": "Buttery-soft Nulu fabric for a barely-there feel. Weightless, sweat-wicking design for yoga, pilates, and everyday wear.",
        "features": ["comfortable", "flexible", "moisture_wicking"]
    },
    {
        "id": 37,
        "name": "Carhartt WIP Michigan Chore Jacket",
        "category": "Clothing",
        "brand": "Carhartt",
        "price": 160.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1548126032-079a0fb0099d?w=400",
        "description": "Heritage workwear jacket in washed canvas fabric. Four front pockets and a blanket-lined interior for warmth.",
        "features": ["durable", "workwear", "warm"]
    },
    {
        "id": 38,
        "name": "Tommy Hilfiger Classic Chinos",
        "category": "Clothing",
        "brand": "Tommy Hilfiger",
        "price": 79.50,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400",
        "description": "Slim-fit chinos in stretch cotton blend for added comfort. Flat-front design with belt loops and two front slash pockets.",
        "features": ["slim_fit", "stretch", "versatile"]
    },
    {
        "id": 39,
        "name": "H&M Linen Button-Down Shirt",
        "category": "Clothing",
        "brand": "H&M",
        "price": 29.99,
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400",
        "description": "Relaxed-fit linen blend shirt in a washed finish. Button-down collar, chest pocket, and roll-up sleeves with a tab.",
        "features": ["breathable", "casual", "summer"]
    },
    {
        "id": 40,
        "name": "Arc'teryx Beta AR Jacket",
        "category": "Clothing",
        "brand": "Arc'teryx",
        "price": 799.00,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1605025002018-a7e04c5b2e15?w=400",
        "description": "GORE-TEX Pro shell jacket for alpine climbing and mountaineering. Waterproof, breathable, and fully seam-taped construction.",
        "features": ["waterproof", "breathable", "mountaineering"]
    },
    {
        "id": 41,
        "name": "Everlane Slim Fit Dress Pants",
        "category": "Clothing",
        "brand": "Everlane",
        "price": 88.00,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1594938298603-c8148c4b5b08?w=400",
        "description": "Clean, modern trousers in a performance stretch fabric that resists wrinkles. Machine washable for easy care.",
        "features": ["wrinkle_resistant", "stretch", "office_wear"]
    },
    {
        "id": 42,
        "name": "Gucci GG Wool Scarf",
        "category": "Clothing",
        "brand": "Gucci",
        "price": 320.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1601924921557-45e6dea0a157?w=400",
        "description": "Classic GG jacquard pattern woven in fine Italian wool and silk blend. Fringe edges with signature stripe detailing.",
        "features": ["luxury", "wool", "designer"]
    },
 
    # ─────────────────────────────────────────────────────────────
    # FOOTWEAR (10 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 3,
        "name": "Nike Air Max 270",
        "category": "Footwear",
        "brand": "Nike",
        "price": 150.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
        "description": "Nike's first lifestyle Air Max with the biggest heel Air unit yet for a super-soft ride that feels as great as it looks.",
        "features": ["comfortable", "stylish", "durable"]
    },
    {
        "id": 7,
        "name": "Adidas Ultraboost Light",
        "category": "Footwear",
        "brand": "Adidas",
        "price": 190.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400",
        "description": "The lightest Ultraboost ever. Light BOOST midsole delivers an incredible energy return for your daily run.",
        "features": ["lightweight", "comfortable", "running"]
    },
    {
        "id": 18,
        "name": "New Balance 990v6",
        "category": "Footwear",
        "brand": "New Balance",
        "price": 199.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400",
        "description": "Made in USA with premium materials and FuelCell midsole technology. The 990 series remains the gold standard in running.",
        "features": ["premium", "comfortable", "made_in_usa"]
    },
    {
        "id": 43,
        "name": "Converse Chuck Taylor All Star",
        "category": "Footwear",
        "brand": "Converse",
        "price": 65.00,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1494496195158-c3bc66c7f2ed?w=400",
        "description": "The original basketball shoe turned cultural icon. Canvas upper with vulcanized rubber outsole for timeless style.",
        "features": ["classic", "casual", "versatile"]
    },
    {
        "id": 44,
        "name": "Birkenstock Arizona Sandals",
        "category": "Footwear",
        "brand": "Birkenstock",
        "price": 110.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400",
        "description": "Two-strap sandal with anatomically shaped cork-latex footbed. Contoured arch support and deep heel cup for all-day comfort.",
        "features": ["comfortable", "orthopedic", "casual"]
    },
    {
        "id": 45,
        "name": "Timberland 6-Inch Premium Boots",
        "category": "Footwear",
        "brand": "Timberland",
        "price": 220.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
        "description": "Waterproof nubuck leather upper with seam-sealed construction. Insulated with 400g PrimaLoft and lugged rubber outsole.",
        "features": ["waterproof", "durable", "warm"]
    },
    {
        "id": 46,
        "name": "Vans Old Skool Skate Shoes",
        "category": "Footwear",
        "brand": "Vans",
        "price": 75.00,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400",
        "description": "Original skate shoe with a suede and canvas upper. Waffle sole for superior grip and the iconic jazz stripe design.",
        "features": ["skate", "casual", "durable"]
    },
    {
        "id": 47,
        "name": "ASICS Gel-Kayano 30",
        "category": "Footwear",
        "brand": "ASICS",
        "price": 160.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400",
        "description": "Maximum support running shoe with GEL technology in heel and forefoot. PureGEL cushioning for soft landings on long runs.",
        "features": ["running", "support", "cushioned"]
    },
    {
        "id": 48,
        "name": "Dr. Martens 1460 Boots",
        "category": "Footwear",
        "brand": "Dr. Martens",
        "price": 170.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1520639888713-7851133b1ed0?w=400",
        "description": "Classic 8-eyelet lace-up boot in smooth leather with iconic yellow welt stitching and air-cushioned AirWair sole.",
        "features": ["durable", "iconic", "versatile"]
    },
    {
        "id": 49,
        "name": "On Cloudrunner 2",
        "category": "Footwear",
        "brand": "On",
        "price": 149.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1587563871167-1ee9c731aefb?w=400",
        "description": "Stability running shoe with CloudTec Phase cushioning and Helion superfoam. Waterproof version available for all conditions.",
        "features": ["running", "stability", "cushioned"]
    },
 
    # ─────────────────────────────────────────────────────────────
    # HOME (10 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 6,
        "name": "Dyson V15 Detect Vacuum",
        "category": "Home",
        "brand": "Dyson",
        "price": 749.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
        "description": "Intelligently optimizes suction and run time. Reveals invisible dust with a precisely-angled laser on the cleaner head.",
        "features": ["powerful", "smart", "cordless"]
    },
    {
        "id": 12,
        "name": "IKEA KALLAX Shelf Unit",
        "category": "Home",
        "brand": "IKEA",
        "price": 89.99,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
        "description": "Versatile shelving that can be placed on the floor or mounted on the wall. Compatible with a range of inserts and boxes.",
        "features": ["modular", "affordable", "versatile"]
    },
    {
        "id": 17,
        "name": "KitchenAid Artisan Stand Mixer",
        "category": "Home",
        "brand": "KitchenAid",
        "price": 449.99,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1594385208974-2f8bb07b1c1c?w=400",
        "description": "Iconic tilt-head stand mixer with 10 speeds and 5-quart stainless steel bowl. Over 10 optional hub-powered attachments.",
        "features": ["powerful", "versatile", "durable"]
    },
    {
        "id": 19,
        "name": "Instant Pot Duo Plus 6-Quart",
        "category": "Home",
        "brand": "Instant Pot",
        "price": 89.95,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=400",
        "description": "9-in-1 multi-use cooker: pressure cook, slow cook, rice cooker, steamer, sauté, yogurt maker, warmer, and sterilizer.",
        "features": ["multi_function", "affordable", "time_saving"]
    },
    {
        "id": 50,
        "name": "Nespresso Vertuo Next Coffee Maker",
        "category": "Home",
        "brand": "Nespresso",
        "price": 179.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400",
        "description": "Centrifusion brewing technology reads capsule barcodes for perfect extraction. Makes 5 cup sizes from espresso to carafe.",
        "features": ["convenient", "fast", "compact"]
    },
    {
        "id": 51,
        "name": "Dyson Purifier Hot+Cool",
        "category": "Home",
        "brand": "Dyson",
        "price": 649.99,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400",
        "description": "Purifies, heats, and cools. HEPA H13 filter captures 99.97% of particles. Air Multiplier technology for whole-room circulation.",
        "features": ["air_purifier", "heater", "smart"]
    },
    {
        "id": 52,
        "name": "Casper Wave Hybrid Snow Mattress",
        "category": "Home",
        "brand": "Casper",
        "price": 2495.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=400",
        "description": "Zoned ergonomic support with Snow Technology for cooler sleep. AirScape foam and 1000+ springs for pressure relief.",
        "features": ["cooling", "ergonomic", "premium"]
    },
    {
        "id": 53,
        "name": "Vitamix 5200 Blender",
        "category": "Home",
        "brand": "Vitamix",
        "price": 499.95,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=400",
        "description": "Aircraft-grade stainless steel blades create friction heat to blend hot soups. Variable speed control for any texture.",
        "features": ["powerful", "durable", "versatile"]
    },
    {
        "id": 54,
        "name": "Roomba j9+ Robot Vacuum",
        "category": "Home",
        "brand": "iRobot",
        "price": 899.99,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
        "description": "Smart home robot that automatically empties itself for 60 days. Obstacle avoidance navigates around pet bowls and shoes.",
        "features": ["smart", "self_emptying", "mapping"]
    },
    {
        "id": 55,
        "name": "Le Creuset Dutch Oven 5.5 Qt",
        "category": "Home",
        "brand": "Le Creuset",
        "price": 399.95,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1584990347449-39ce96c08bca?w=400",
        "description": "Enameled cast iron for superior heat retention. Works on all cooktops including induction. Oven-safe to 500°F.",
        "features": ["durable", "heat_retention", "versatile"]
    },
 
    # ─────────────────────────────────────────────────────────────
    # BEAUTY (13 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 56,
        "name": "Charlotte Tilbury Pillow Talk Lipstick",
        "category": "Beauty",
        "brand": "Charlotte Tilbury",
        "price": 38.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1586495777744-4e6232bf2176?w=400",
        "description": "Iconic nude-pink shade with a hydrating matte finish. Enriched with vitamin E and hyaluronic acid for all-day comfort.",
        "features": ["hydrating", "long_lasting", "iconic"]
    },
    {
        "id": 57,
        "name": "Dyson Airwrap Complete Styler",
        "category": "Beauty",
        "brand": "Dyson",
        "price": 599.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1522338242992-e1a54906a8da?w=400",
        "description": "Styles and dries simultaneously using the Coanda effect. No extreme heat, multiple attachments for curls, waves, and smooth blowouts.",
        "features": ["no_heat_damage", "versatile", "professional"]
    },
    {
        "id": 58,
        "name": "La Mer Crème de la Mer Moisturizer",
        "category": "Beauty",
        "brand": "La Mer",
        "price": 365.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400",
        "description": "Legendary moisturizer with Miracle Broth. Instantly relieves dryness, reduces the look of fine lines and wrinkles.",
        "features": ["anti_aging", "luxury", "moisturizing"]
    },
    {
        "id": 59,
        "name": "Fenty Beauty Pro Filt'r Foundation",
        "category": "Beauty",
        "brand": "Fenty Beauty",
        "price": 40.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400",
        "description": "Soft matte foundation in 50 shades. Oil-free, long-wear formula that controls shine for up to 24 hours.",
        "features": ["full_coverage", "long_lasting", "inclusive"]
    },
    {
        "id": 60,
        "name": "Olaplex No.3 Hair Perfector",
        "category": "Beauty",
        "brand": "Olaplex",
        "price": 30.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1526045612212-70caf35c14df?w=400",
        "description": "At-home treatment that reduces breakage and visibly strengthens hair. Reconnects broken disulfide bonds in damaged hair.",
        "features": ["repairing", "strengthening", "at_home_treatment"]
    },
    {
        "id": 61,
        "name": "SK-II Facial Treatment Essence",
        "category": "Beauty",
        "brand": "SK-II",
        "price": 185.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1617897903246-719242758050?w=400",
        "description": "90% PITERA essence improves skin texture and radiance. Helps skin look younger and crystal clear with regular use.",
        "features": ["brightening", "anti_aging", "luxury"]
    },
    {
        "id": 62,
        "name": "Rare Beauty Soft Pinch Blush",
        "category": "Beauty",
        "brand": "Rare Beauty",
        "price": 22.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1607748862156-7c548e7e98f4?w=400",
        "description": "Weightless, blendable liquid blush that gives a natural flush. A little goes a long way with this highly-pigmented formula.",
        "features": ["lightweight", "buildable", "natural_finish"]
    },
    {
        "id": 63,
        "name": "Tatcha The Water Cream",
        "category": "Beauty",
        "brand": "Tatcha",
        "price": 72.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400",
        "description": "Oil-free pore-minimizing moisturizer inspired by Japanese superfoods. Bursts on contact to release skin-clarifying botanicals.",
        "features": ["oil_free", "pore_minimizing", "hydrating"]
    },
    {
        "id": 64,
        "name": "MAC Cosmetics Prep + Prime Fix+",
        "category": "Beauty",
        "brand": "MAC Cosmetics",
        "price": 32.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400",
        "description": "Multitasking spray refreshes skin and sets makeup. Can be used as skincare, eyeshadow intensifier, or makeup setting spray.",
        "features": ["multi_use", "setting", "hydrating"]
    },
    {
        "id": 65,
        "name": "The Ordinary Niacinamide 10%",
        "category": "Beauty",
        "brand": "The Ordinary",
        "price": 11.90,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
        "description": "High-strength vitamin and mineral formula that reduces blemishes and congestion. Balances visible sebum activity.",
        "features": ["affordable", "effective", "pore_minimizing"]
    },
    {
        "id": 66,
        "name": "Estée Lauder Advanced Night Repair Serum",
        "category": "Beauty",
        "brand": "Estée Lauder",
        "price": 115.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
        "description": "Award-winning serum synchronized with skin's natural nighttime repair. Reduces lines, wrinkles, and uneven skin tone.",
        "features": ["anti_aging", "repairing", "brightening"]
    },
    {
        "id": 67,
        "name": "Benefit Cosmetics Brow Pencil",
        "category": "Beauty",
        "brand": "Benefit Cosmetics",
        "price": 26.00,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1512207736890-6ffed8a84e8d?w=400",
        "description": "Ultra-fine precision pencil with a spoolie brush. Creates natural-looking hair strokes for fuller, defined brows.",
        "features": ["precise", "natural_finish", "long_lasting"]
    },
    {
        "id": 68,
        "name": "Tom Ford Black Orchid Perfume",
        "category": "Beauty",
        "brand": "Tom Ford",
        "price": 175.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1541643600914-78b084683702?w=400",
        "description": "Luxurious and sensual fragrance with black truffle, ylang-ylang, and patchouli. A rich Oriental floral for day or evening.",
        "features": ["luxury", "long_lasting", "intense"]
    },
 
    # ─────────────────────────────────────────────────────────────
    # SPORTS (12 products)
    # ─────────────────────────────────────────────────────────────
    {
        "id": 69,
        "name": "Peloton Bike+",
        "category": "Sports",
        "brand": "Peloton",
        "price": 2495.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1534787238916-9ba6764efd4f?w=400",
        "description": "Auto-follow resistance adjusts to match instructor cues. Rotating 24\" HD touchscreen streams 10,000+ on-demand classes.",
        "features": ["smart", "streaming", "high_performance"]
    },
    {
        "id": 70,
        "name": "Hydro Flask 32oz Wide Mouth Bottle",
        "category": "Sports",
        "brand": "Hydro Flask",
        "price": 44.95,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400",
        "description": "TempShield double-wall insulation keeps drinks cold for 24 hours, hot for 12 hours. 18/8 pro-grade stainless steel.",
        "features": ["insulated", "durable", "BPA_free"]
    },
    {
        "id": 71,
        "name": "Garmin Forerunner 965 GPS Watch",
        "category": "Sports",
        "brand": "Garmin",
        "price": 599.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
        "description": "Premium running smartwatch with AMOLED display, training readiness score, and morning report. Up to 31 days battery life.",
        "features": ["GPS", "long_battery", "training_metrics"]
    },
    {
        "id": 72,
        "name": "Yeti Rambler 20oz Tumbler",
        "category": "Sports",
        "brand": "Yeti",
        "price": 34.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=400",
        "description": "Double-wall vacuum insulation and 18/8 stainless steel. Keeps drinks ice cold or hot. Dishwasher safe with MagSlider lid.",
        "features": ["insulated", "durable", "dishwasher_safe"]
    },
    {
        "id": 73,
        "name": "Theragun Prime Massage Gun",
        "category": "Sports",
        "brand": "Therabody",
        "price": 299.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400",
        "description": "5 speeds, 16mm amplitude for deep muscle treatment. Smart app integration with guided routines for warm-up and recovery.",
        "features": ["recovery", "smart", "portable"]
    },
    {
        "id": 74,
        "name": "Lululemon Mat 5mm Yoga Mat",
        "category": "Sports",
        "brand": "Lululemon",
        "price": 88.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400",
        "description": "Natural rubber base for grip, moisture-wicking microfiber top. Dense 5mm cushioning for joint support on hard floors.",
        "features": ["grip", "cushioned", "eco_friendly"]
    },
    {
        "id": 75,
        "name": "Bowflex SelectTech 552 Dumbbells",
        "category": "Sports",
        "brand": "Bowflex",
        "price": 429.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1571731956672-f2b94d7dd0cb?w=400",
        "description": "Adjusts from 5 to 52 lbs with a turn of the dial. Replaces 15 sets of weights. Compact design for home gym.",
        "features": ["adjustable", "space_saving", "versatile"]
    },
    {
        "id": 76,
        "name": "Wilson Pro Staff RF97 Tennis Racket",
        "category": "Sports",
        "brand": "Wilson",
        "price": 249.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400",
        "description": "Roger Federer's signature racket. Braided Basalt fiber and Kaarbon construction for improved flexibility and vibration dampening.",
        "features": ["professional", "control", "durable"]
    },
    {
        "id": 77,
        "name": "Trek Domane SL 6 Road Bike",
        "category": "Sports",
        "brand": "Trek",
        "price": 3499.99,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
        "description": "Carbon endurance road bike with IsoSpeed decoupler for compliance over rough roads. Shimano 105 Di2 electronic groupset.",
        "features": ["carbon", "smooth_ride", "professional"]
    },
    {
        "id": 78,
        "name": "Fitbit Charge 6 Fitness Tracker",
        "category": "Sports",
        "brand": "Fitbit",
        "price": 159.95,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400",
        "description": "Heart rate tracking, ECG app, and built-in GPS. Google Maps and Wallet integration. Up to 7 days battery life.",
        "features": ["GPS", "heart_rate", "sleep_tracking"]
    },
    {
        "id": 79,
        "name": "Coleman 6-Person Camping Tent",
        "category": "Sports",
        "brand": "Coleman",
        "price": 149.99,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=400",
        "description": "Sets up in 10 minutes with pre-attached poles. WeatherTec system with patented welded floors and inverted seams.",
        "features": ["waterproof", "easy_setup", "spacious"]
    },
    {
        "id": 80,
        "name": "Osprey Atmos AG 65 Backpack",
        "category": "Sports",
        "brand": "Osprey",
        "price": 310.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400",
        "description": "Anti-Gravity suspension system for exceptional airflow and weight distribution. Integrated raincover and StraightJacket compression.",
        "features": ["ergonomic", "ventilated", "durable"]
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# Derived lookups — O(1) access used by DataLoader and recommendation engine
# ─────────────────────────────────────────────────────────────────────────────
 
PRODUCT_BY_ID: dict[int, dict] = {p["id"]: p for p in PRODUCTS}
 
ALL_PRODUCT_IDS: list[int] = [p["id"] for p in PRODUCTS]
 
CATEGORIES: list[str] = sorted(set(p["category"] for p in PRODUCTS))
 
BRANDS: list[str] = sorted(set(p["brand"] for p in PRODUCTS))
 
# Products grouped by category for quick filtering
PRODUCTS_BY_CATEGORY: dict[str, list[dict]] = {}
for _p in PRODUCTS:
    PRODUCTS_BY_CATEGORY.setdefault(_p["category"], []).append(_p)
 
# All unique feature tags across the catalog
ALL_FEATURES: list[str] = sorted(set(
    feature
    for p in PRODUCTS
    for feature in p["features"]
))