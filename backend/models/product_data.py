"""
Mock product data for the E-Commerce Recommendation System.
This serves as our in-memory product catalog.
"""

PRODUCTS = [
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
        "id": 3,
        "name": "Nike Air Max 270",
        "category": "Footwear",
        "brand": "Nike",
        "price": 150.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
        "description": "Nike's first lifestyle Air Max featuring the biggest heel Air unit yet for a super-soft ride that feels as great as it looks.",
        "features": ["comfortable", "stylish", "durable"]
    },
    {
        "id": 4,
        "name": "Samsung Galaxy S24 Ultra",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 1299.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400",
        "description": "Galaxy AI is here. Search like never before, Icons communicate in an epic way, notes now Icons make themselves.",
        "features": ["high_performance", "camera", "AI"]
    },
    {
        "id": 5,
        "name": "Levi's 501 Original Fit Jeans",
        "category": "Clothing",
        "brand": "Levi's",
        "price": 69.50,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=400",
        "description": "The iconic straight fit with an authentic look and feel. Sits at the waist with a regular fit through the thigh.",
        "features": ["classic", "durable", "comfortable"]
    },
    {
        "id": 6,
        "name": "Dyson V15 Detect Vacuum",
        "category": "Home",
        "brand": "Dyson",
        "price": 749.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400",
        "description": "Intelligently optimizes suction and run time. Reveals invisible dust with a precisely-angled laser.",
        "features": ["powerful", "smart", "cordless"]
    },
    {
        "id": 7,
        "name": "Adidas Ultraboost Light",
        "category": "Footwear",
        "brand": "Adidas",
        "price": 190.00,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400",
        "description": "The lightest Ultraboost ever. Features Light BOOST midsole for an incredible step-in comfort.",
        "features": ["lightweight", "comfortable", "running"]
    },
    {
        "id": 8,
        "name": "Apple iPad Pro 13-inch M4",
        "category": "Electronics",
        "brand": "Apple",
        "price": 1299.00,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400",
        "description": "Thin. Light. Phenomenally powerful. The new iPad Pro, powered by the blazingly fast M4 chip.",
        "features": ["portable", "high_performance", "creative"]
    },
    {
        "id": 9,
        "name": "The North Face Thermoball Jacket",
        "category": "Clothing",
        "brand": "The North Face",
        "price": 230.00,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400",
        "description": "Lightweight synthetic insulation that continues to insulate even when wet. Perfect for outdoor adventures.",
        "features": ["warm", "lightweight", "waterproof"]
    },
    {
        "id": 10,
        "name": "Sony PlayStation 5",
        "category": "Electronics",
        "brand": "Sony",
        "price": 499.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400",
        "description": "Experience lightning-fast loading, deeper immersion with haptic feedback, adaptive triggers, and 3D Audio.",
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
        "id": 12,
        "name": "IKEA KALLAX Shelf Unit",
        "category": "Home",
        "brand": "IKEA",
        "price": 89.99,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
        "description": "Versatile shelving unit that can be placed on the floor or mounted on the wall. Choose to use with or without inserts.",
        "features": ["modular", "affordable", "versatile"]
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
        "id": 14,
        "name": "Patagonia Better Sweater",
        "category": "Clothing",
        "brand": "Patagonia",
        "price": 139.00,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400",
        "description": "A soft, comfortable fleece made from 100% recycled polyester. Fair Trade Certified sewn.",
        "features": ["sustainable", "comfortable", "warm"]
    },
    {
        "id": 15,
        "name": "Samsung 65\" OLED 4K Smart TV",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 1799.99,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400",
        "description": "Experience pure blacks and vivid colors with Samsung OLED technology. Neural Quantum Processor 4K delivers stunning picture.",
        "features": ["4K", "smart", "OLED"]
    },
    {
        "id": 16,
        "name": "Nike Dri-FIT Training T-Shirt",
        "category": "Clothing",
        "brand": "Nike",
        "price": 35.00,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
        "description": "Sweat-wicking technology moves moisture away from your skin for quicker evaporation. Helps keep you dry and comfortable.",
        "features": ["breathable", "lightweight", "athletic"]
    },
    {
        "id": 17,
        "name": "KitchenAid Stand Mixer",
        "category": "Home",
        "brand": "KitchenAid",
        "price": 449.99,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1594385208974-2f8bb07b1c1c?w=400",
        "description": "The iconic tilt-head stand mixer with 10 speeds and 5-quart stainless steel bowl. Over 10 optional hub-powered attachments.",
        "features": ["powerful", "versatile", "durable"]
    },
    {
        "id": 18,
        "name": "New Balance 990v6",
        "category": "Footwear",
        "brand": "New Balance",
        "price": 199.99,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400",
        "description": "The latest evolution of the iconic 990 series. Made in USA with premium materials and FuelCell midsole technology.",
        "features": ["premium", "comfortable", "made_in_usa"]
    },
    {
        "id": 19,
        "name": "Instant Pot Duo Plus 6-Quart",
        "category": "Home",
        "brand": "Instant Pot",
        "price": 89.95,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=400",
        "description": "9-in-1 electric pressure cooker: pressure cook, slow cook, rice cooker, steamer, sauté, yogurt maker, warmer, and sterilizer.",
        "features": ["multi_function", "affordable", "time_saving"]
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
    }
]

# Available categories and brands (derived from products)
CATEGORIES = list(set(p["category"] for p in PRODUCTS))
BRANDS = list(set(p["brand"] for p in PRODUCTS))
