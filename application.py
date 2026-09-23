from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone

application = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartNest - Smart Home</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        html {
            scroll-behavior: smooth;
        }

        body {
            background:
                radial-gradient(circle at top left, rgba(6,182,212,0.12), transparent 30%),
                radial-gradient(circle at top right, rgba(99,102,241,0.12), transparent 25%),
                #020617;
        }

        .glass {
            background: rgba(15, 23, 42, 0.72);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(148, 163, 184, 0.12);
        }

        .product-card {
            transition: 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-8px);
        }
    </style>
</head>

<body class="text-white">

<!-- NAVBAR -->
<header class="sticky top-0 z-50 bg-slate-950/90 backdrop-blur-xl border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-indigo-500 flex items-center justify-center">
                🏠
            </div>

            <div>
                <h1 class="font-bold text-xl">
                    Smart<span class="text-cyan-400">Nest</span>
                </h1>
                <p class="text-xs text-slate-500">SMART HOME SOLUTIONS</p>
            </div>
        </div>

        <nav class="hidden md:flex gap-8 text-sm text-slate-400">
            <a href="#products" class="hover:text-cyan-400">Products</a>
            <a href="#services" class="hover:text-cyan-400">Services</a>
            <a href="#about" class="hover:text-cyan-400">About</a>
            <a href="#contact" class="hover:text-cyan-400">Contact</a>
        </nav>

        <button onclick="showCart()"
                class="bg-slate-900 border border-slate-700 px-4 py-2 rounded-xl">
            🛒 Cart <span id="cartCount">0</span>
        </button>

    </div>
</header>


<!-- HERO -->
<section class="min-h-[85vh] flex items-center">

    <div class="max-w-7xl mx-auto px-6 py-20 w-full">

        <div class="grid lg:grid-cols-2 gap-16 items-center">

            <div>

                <span class="inline-block px-4 py-2 rounded-full
                             bg-cyan-500/10
                             border border-cyan-500/20
                             text-cyan-400 text-sm mb-6">
                    ✨ The Future of Smart Living
                </span>

                <h2 class="text-5xl md:text-7xl font-black leading-tight">

                    Make Your Home

                    <span class="text-transparent bg-clip-text
                                 bg-gradient-to-r from-cyan-400 to-indigo-500">
                        Smarter.
                    </span>

                </h2>

                <p class="text-slate-400 text-lg mt-6 max-w-xl leading-relaxed">
                    Modern smart ceiling fans, intelligent lighting,
                    home security and automation solutions designed
                    for the connected home.
                </p>

                <div class="flex gap-4 mt-8">

                    <a href="#products"
                       class="px-7 py-4 rounded-xl
                              bg-gradient-to-r from-cyan-500 to-indigo-500
                              font-bold hover:scale-105 transition">
                        Shop Now →
                    </a>

                    <a href="#services"
                       class="px-7 py-4 rounded-xl
                              border border-slate-700
                              bg-slate-900
                              hover:bg-slate-800 transition">
                        Our Services
                    </a>

                </div>

                <div class="flex gap-10 mt-12">

                    <div>
                        <h3 class="text-2xl font-bold">500+</h3>
                        <p class="text-slate-500 text-sm">Smart Homes</p>
                    </div>

                    <div>
                        <h3 class="text-2xl font-bold">4.9/5</h3>
                        <p class="text-slate-500 text-sm">Customer Rating</p>
                    </div>

                    <div>
                        <h3 class="text-2xl font-bold">24/7</h3>
                        <p class="text-slate-500 text-sm">Support</p>
                    </div>

                </div>

            </div>


            <!-- HERO IMAGE -->
            <div>

                <div class="glass rounded-3xl p-5 shadow-2xl">

                    <img
                        src="https://images.unsplash.com/photo-1558008258-3256797b43f3?auto=format&fit=crop&w=1200&q=80"
                        alt="Smart Home"
                        class="w-full h-[420px] object-cover rounded-2xl">

                    <div class="p-4">

                        <p class="text-cyan-400 text-sm">
                            Featured
                        </p>

                        <h3 class="text-2xl font-bold mt-1">
                            Complete Smart Home
                        </h3>

                        <p class="text-slate-400 mt-2">
                            Lighting • Security • Automation • Climate
                        </p>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>


<!-- PRODUCTS -->
<section id="products" class="max-w-7xl mx-auto px-6 py-20">

    <div class="mb-12">

        <p class="text-cyan-400 uppercase text-sm">
            Our Products
        </p>

        <h2 class="text-4xl font-bold mt-2">
            Smart Home Products
        </h2>

        <p class="text-slate-400 mt-3">
            Upgrade your home with modern connected devices.
        </p>

    </div>


    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">


        <!-- PRODUCT 1 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="Smart Light">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Lighting
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart LED Ceiling Light
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    Dimmable Wi-Fi ceiling light with mobile
                    and voice control.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $129
                        </span>

                        <span class="text-slate-500 line-through ml-2">
                            $159
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart LED Ceiling Light')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 2 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1540932239986-30128078f3c5?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="Smart Fan">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Ceiling Fans
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart Ceiling Fan Pro
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    Energy-efficient smart fan with remote
                    and mobile control.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $189
                        </span>

                        <span class="text-slate-500 line-through ml-2">
                            $229
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart Ceiling Fan Pro')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 3 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="RGB Lighting">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Lighting
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart RGB Ceiling Panel
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    RGB smart panel with millions of colors
                    and scheduling.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $149
                        </span>

                        <span class="text-slate-500 line-through ml-2">
                            $179
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart RGB Ceiling Panel')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 4 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1558008258-3256797b43f3?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="Motion Sensor">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Security
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart Motion Sensor
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    Motion detection for smart lighting
                    and home security.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $49
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart Motion Sensor')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 5 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="Air Sensor">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Climate
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart Air Quality Sensor
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    Monitor temperature, humidity and
                    indoor air quality.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $89
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart Air Quality Sensor')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 6 -->
        <div class="product-card glass rounded-3xl overflow-hidden">

            <img
                src="https://images.unsplash.com/photo-1558008258-3256797b43f3?auto=format&fit=crop&w=900&q=80"
                class="w-full h-56 object-cover"
                alt="Smart Hub">

            <div class="p-6">

                <span class="text-cyan-400 text-xs uppercase">
                    Automation
                </span>

                <h3 class="text-xl font-bold mt-2">
                    Smart Home Hub
                </h3>

                <p class="text-slate-400 text-sm mt-3">
                    Central hub for controlling all your
                    smart home devices.
                </p>

                <div class="flex justify-between items-center mt-6">

                    <div>
                        <span class="text-2xl font-bold">
                            $199
                        </span>
                    </div>

                    <button
                        onclick="buyProduct('Smart Home Hub')"
                        class="bg-cyan-500 hover:bg-cyan-400
                               text-slate-950
                               font-bold
                               px-5 py-3 rounded-xl">
                        Buy Now
                    </button>

                </div>

            </div>

        </div>

    </div>

</section>


<!-- SERVICES -->
<section id="services"
         class="border-y border-slate-800
                bg-slate-950/50">

    <div class="max-w-7xl mx-auto px-6 py-20">

        <p class="text-indigo-400 text-sm uppercase">
            Our Services
        </p>

        <h2 class="text-4xl font-bold mt-2">
            Complete Smart Home Services
        </h2>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10">

            <div class="glass rounded-2xl p-6">
                <div class="text-4xl">🔧</div>
                <h3 class="text-xl font-bold mt-5">
                    Installation
                </h3>
                <p class="text-slate-400 mt-3 text-sm">
                    Professional smart device installation.
                </p>
            </div>

            <div class="glass rounded-2xl p-6">
                <div class="text-4xl">💡</div>
                <h3 class="text-xl font-bold mt-5">
                    Lighting Automation
                </h3>
                <p class="text-slate-400 mt-3 text-sm">
                    Smart lighting scenes and schedules.
                </p>
            </div>

            <div class="glass rounded-2xl p-6">
                <div class="text-4xl">📱</div>
                <h3 class="text-xl font-bold mt-5">
                    Device Integration
                </h3>
                <p class="text-slate-400 mt-3 text-sm">
                    Connect your smart devices together.
                </p>
            </div>

            <div class="glass rounded-2xl p-6">
                <div class="text-4xl">🛡️</div>
                <h3 class="text-xl font-bold mt-5">
                    Home Security
                </h3>
                <p class="text-slate-400 mt-3 text-sm">
                    Smart sensors and security automation.
                </p>
            </div>

        </div>

    </div>

</section>


<!-- ABOUT -->
<section id="about" class="max-w-7xl mx-auto px-6 py-20">

    <div class="glass rounded-3xl p-10">

        <p class="text-cyan-400 text-sm uppercase">
            Smart Technology
        </p>

        <h2 class="text-4xl font-bold mt-2">
            One Home. One Smart Ecosystem.
        </h2>

        <p class="text-slate-400 mt-5 max-w-3xl leading-relaxed">
            Control your lights, ceiling fans, security sensors
            and other smart appliances from your phone.
            Build automation routines that make everyday life
            easier and more energy efficient.
        </p>

    </div>

</section>


<!-- CONTACT -->
<section id="contact" class="max-w-7xl mx-auto px-6 pb-20">

    <div class="rounded-3xl p-10
                bg-gradient-to-r from-cyan-500 to-indigo-600">

        <h2 class="text-4xl font-bold">
            Ready to make your home smarter?
        </h2>

        <p class="mt-4 text-white/80">
            Talk to our team about your smart home project.
        </p>

        <a href="mailto:hello@smartnest.com"
           class="inline-block mt-6 bg-white text-slate-950
                  px-6 py-3 rounded-xl font-bold">
            Contact Us
        </a>

    </div>

</section>


<!-- FOOTER -->
<footer class="border-t border-slate-800">

    <div class="max-w-7xl mx-auto px-6 py-8
                flex justify-between flex-wrap gap-4">

        <p class="text-slate-500 text-sm">
            © 2026 SmartNest Smart Home Solutions
        </p>

        <p class="text-slate-500 text-sm">
            Powered by AWS Elastic Beanstalk + Flask
        </p>

    </div>

</footer>


<script>

let cartCount = 0;

function buyProduct(productName) {

    cartCount++;

    document.getElementById("cartCount").innerText = cartCount;

    alert(productName + " added to cart!");

}

function showCart() {

    if (cartCount === 0) {

        alert("Your cart is empty.");

    } else {

        alert("Your cart has " + cartCount + " item(s).");

    }

}

</script>

</body>
</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML_TEMPLATE
    )


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "service": "SmartNest Flask Application",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


if __name__ == "__main__":

    application.run(
        host="0.0.0.0",
        port=5000
    )
