import codecs, re
path = r'c:\Users\jakkob\Desktop\WEB_STATIS\design-theme\theme\kartun\index.html'
with codecs.open(path, 'r', 'utf-8') as f:
    content = f.read()

new_sections_and_script = '''    <!-- 2. CHARACTERS SECTION (Comic Panel Grid) -->
    <section id="characters" class="py-24 bg-tn-blue border-b-8 border-tn-black relative z-10">
        <div class="absolute inset-0 bg-halftone opacity-20 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
            <div class="text-center mb-16 gsap-fade-up">
                <div class="inline-block bg-tn-yellow brutal-border px-6 py-2 rounded-full font-bold mb-4 shadow-comic transform -rotate-2">
                    PROFIL TOKOH
                </div>
                <h2 class="text-[60px] md:text-[80px] font-bangers text-white text-stroke mb-4 leading-none">PAHLAWAN <span class="text-tn-red">KITA</span></h2>
            </div>

            <!-- Comic Grid Layout -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6 auto-rows-min">
                
                <!-- Main Character (Spans 2 cols, 2 rows on desktop) -->
                <div class="md:col-span-2 md:row-span-2 bg-white brutal-border p-6 shadow-comic group hover:-translate-y-2 transition-transform cursor-crosshair gsap-fade-up">
                    <div class="h-64 bg-tn-yellow brutal-border mb-6 flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-halftone-light opacity-50"></div>
                         <i class="fa-solid fa-robot text-9xl text-tn-black group-hover:scale-110 transition-transform relative z-10"></i>
                         <div class="absolute bottom-4 right-4 bg-white px-3 py-1 font-bold text-sm brutal-border rotate-[-5deg]">#01</div>
                    </div>
                    <h3 class="text-5xl font-bangers mb-2">SI KUNING</h3>
                    <p class="font-bold text-lg mb-4 text-tn-black">Ahli strategi super jenius dengan obsesi aneh pada gadget berbentuk pisang.</p>
                    <div class="flex flex-wrap gap-2 font-bold text-sm">
                        <span class="bg-tn-red text-white px-3 py-1 brutal-border">INTEL: 99</span>
                        <span class="bg-tn-green text-tn-black px-3 py-1 brutal-border">SPEED: 85</span>
                    </div>
                </div>

                <!-- Side Character 1 -->
                <div class="md:col-span-2 bg-tn-red brutal-border p-6 shadow-comic flex items-center gap-6 group hover:-translate-y-2 transition-transform cursor-crosshair gsap-fade-up">
                    <div class="w-32 h-32 bg-white brutal-border flex items-center justify-center shrink-0 relative overflow-hidden rounded-full">
                        <div class="absolute inset-0 bg-halftone opacity-30"></div>
                        <i class="fa-solid fa-flask text-5xl text-tn-red relative z-10"></i>
                    </div>
                    <div>
                        <h3 class="text-4xl font-bangers text-white text-stroke mb-2">DR. MERAH</h3>
                        <p class="font-bold text-white leading-tight">Ilmuwan gila yang ramuannya selalu meledak (tapi kadang berguna).</p>
                    </div>
                </div>

                <!-- Side Character 2 -->
                <div class="md:col-span-1 bg-white brutal-border p-4 shadow-comic group hover:-translate-y-2 transition-transform cursor-crosshair gsap-fade-up">
                    <div class="h-40 bg-tn-green brutal-border mb-4 flex items-center justify-center relative overflow-hidden">
                        <i class="fa-solid fa-tree text-6xl text-white group-hover:rotate-12 transition-transform"></i>
                    </div>
                    <h3 class="text-3xl font-bangers text-center leading-none">KAPTEN<br>HIJAU</h3>
                </div>

                <!-- Action Panel -->
                <div class="md:col-span-1 bg-tn-black brutal-border p-4 shadow-comic flex items-center justify-center relative overflow-hidden group hover:-translate-y-2 transition-transform cursor-crosshair gsap-fade-up">
                    <div class="absolute inset-0 bg-halftone-light opacity-20"></div>
                    <span class="text-5xl font-bangers text-tn-yellow text-stroke transform -rotate-12 group-hover:scale-125 transition-transform duration-500">VS!</span>
                </div>

            </div>
        </div>
    </section>

    <!-- 3. EPISODES (Swiper Gallery) -->
    <section id="episodes" class="py-24 bg-tn-purple border-b-8 border-tn-black relative overflow-hidden">
        <!-- Background Decor -->
        <div class="absolute top-0 right-0 w-64 h-64 bg-tn-yellow rounded-full brutal-border transform translate-x-1/2 -translate-y-1/2 mix-blend-screen opacity-50"></div>
        
        <div class="max-w-[1400px] mx-auto px-4">
            <div class="flex justify-between items-end mb-12 px-4 sm:px-6 lg:px-8 gsap-fade-up">
                <div>
                    <h2 class="text-[60px] md:text-[80px] font-bangers text-white text-stroke leading-none">ISU <span class="text-tn-yellow">TERBARU</span></h2>
                </div>
                <!-- Custom Swiper Navigation -->
                <div class="hidden md:flex gap-4">
                    <button class="swiper-button-prev-custom w-14 h-14 bg-white brutal-border shadow-comic flex items-center justify-center text-2xl hover:bg-tn-yellow hover:-translate-y-1 transition-all z-10"><i class="fa-solid fa-arrow-left"></i></button>
                    <button class="swiper-button-next-custom w-14 h-14 bg-white brutal-border shadow-comic flex items-center justify-center text-2xl hover:bg-tn-yellow hover:-translate-y-1 transition-all z-10"><i class="fa-solid fa-arrow-right"></i></button>
                </div>
            </div>

            <!-- Swiper Container -->
            <div class="swiper episodeSwiper pb-16 pt-4 px-4 sm:px-6 lg:px-8 gsap-fade-up">
                <div class="swiper-wrapper">
                    
                    <!-- Slide 1 -->
                    <div class="swiper-slide">
                        <div class="bg-white brutal-border p-4 shadow-comic hover:shadow-comic-xl transition-shadow cursor-grab group">
                            <div class="w-full aspect-[3/4] bg-tn-red brutal-border mb-4 relative overflow-hidden flex items-center justify-center">
                                <div class="absolute inset-0 bg-halftone mix-blend-multiply opacity-40"></div>
                                <span class="font-bangers text-7xl text-white text-stroke transform -rotate-6 group-hover:scale-110 transition-transform">#01</span>
                                <div class="absolute top-4 left-4 bg-tn-yellow px-3 py-1 font-bold brutal-border text-xs transform -rotate-3">EDISI KOLEKTOR</div>
                            </div>
                            <h3 class="text-3xl font-bangers leading-none mb-2">BANGKITNYA MESIN</h3>
                            <p class="font-bold text-sm text-gray-600 line-clamp-2">Ketika toaster di rumah Dr. Merah mulai memiliki kesadaran sendiri.</p>
                        </div>
                    </div>

                    <!-- Slide 2 -->
                    <div class="swiper-slide">
                        <div class="bg-white brutal-border p-4 shadow-comic hover:shadow-comic-xl transition-shadow cursor-grab group">
                            <div class="w-full aspect-[3/4] bg-tn-blue brutal-border mb-4 relative overflow-hidden flex items-center justify-center">
                                <div class="absolute inset-0 bg-halftone mix-blend-multiply opacity-40"></div>
                                <span class="font-bangers text-7xl text-white text-stroke transform -rotate-6 group-hover:scale-110 transition-transform">#02</span>
                            </div>
                            <h3 class="text-3xl font-bangers leading-none mb-2">MISTERI HUTAN NEON</h3>
                            <p class="font-bold text-sm text-gray-600 line-clamp-2">Menyelidiki pohon bercahaya yang mengubah hewan menjadi mutant lambat.</p>
                        </div>
                    </div>

                    <!-- Slide 3 -->
                    <div class="swiper-slide">
                        <div class="bg-white brutal-border p-4 shadow-comic hover:shadow-comic-xl transition-shadow cursor-grab group">
                            <div class="w-full aspect-[3/4] bg-tn-green brutal-border mb-4 relative overflow-hidden flex items-center justify-center">
                                <div class="absolute inset-0 bg-halftone mix-blend-multiply opacity-40"></div>
                                <span class="font-bangers text-7xl text-white text-stroke transform -rotate-6 group-hover:scale-110 transition-transform">#03</span>
                            </div>
                            <h3 class="text-3xl font-bangers leading-none mb-2">SERANGAN PIZZA!</h3>
                            <p class="font-bold text-sm text-gray-600 line-clamp-2">Alien berbentuk pizza pepperoni menginvasi bumi dari langit.</p>
                        </div>
                    </div>

                    <!-- Slide 4 -->
                    <div class="swiper-slide">
                        <div class="bg-white brutal-border p-4 shadow-comic hover:shadow-comic-xl transition-shadow cursor-grab group">
                            <div class="w-full aspect-[3/4] bg-tn-black brutal-border mb-4 relative overflow-hidden flex items-center justify-center">
                                <div class="absolute inset-0 bg-halftone-light opacity-40"></div>
                                <span class="font-bangers text-7xl text-tn-yellow text-stroke transform -rotate-6 group-hover:scale-110 transition-transform">#04</span>
                                <div class="absolute top-4 left-4 bg-tn-red text-white px-3 py-1 font-bold brutal-border text-xs transform -rotate-3">BARU!</div>
                            </div>
                            <h3 class="text-3xl font-bangers leading-none mb-2">BAYANGAN MASA DEPAN</h3>
                            <p class="font-bold text-sm text-gray-600 line-clamp-2">Apakah ini akhir cerita, atau awal dari multiverse baru?</p>
                        </div>
                    </div>

                </div>
            </div>
            
        </div>
    </section>

    <!-- 4. FUN ZONE (Interactive Game Element) -->
    <section id="fun" class="py-32 bg-tn-yellow border-b-8 border-tn-black relative overflow-hidden">
        <div class="absolute inset-0 bg-halftone opacity-10"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            
            <div class="bg-white brutal-border shadow-comic-xl rounded-[2rem] p-8 md:p-16 relative">
                <!-- Decorative Tape -->
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 w-40 h-10 bg-white opacity-80 rotate-2"></div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                    <div class="gsap-fade-up">
                        <div class="inline-block bg-tn-blue text-white brutal-border px-4 py-1 font-bold mb-4 transform -rotate-2">ZONA INTERAKTIF</div>
                        <h2 class="text-5xl md:text-7xl font-bangers mb-6 leading-none text-tn-black">HANCURKAN TARGET!</h2>
                        <p class="text-xl font-bold mb-8 text-gray-700">Fitur bukan cuma hiasan. Tes refleksmu. Ketuk (atau klik) bom di sebelah secepat mungkin sebelum meledak secara otomatis!</p>
                        
                        <div class="flex items-center gap-4 bg-tn-paper brutal-border p-4 inline-flex">
                            <span class="font-bangers text-3xl">SKOR: <span id="game-score" class="text-tn-red">0</span></span>
                        </div>
                    </div>
                    
                    <!-- The Game Viewport -->
                    <div class="relative h-80 bg-tn-blue brutal-border rounded-2xl overflow-hidden cursor-crosshair border-8 border-tn-black shadow-inner flex items-center justify-center gsap-fade-up">
                        <div class="absolute inset-0 bg-halftone opacity-30 mix-blend-multiply"></div>
                        
                        <!-- The Target (Interactive) -->
                        <div id="interactive-target" class="absolute w-24 h-24 bg-tn-black rounded-full brutal-border flex items-center justify-center cursor-pointer transform hover:scale-110 transition-transform select-none">
                            <div class="absolute -top-4 left-1/2 w-2 h-6 bg-yellow-600"></div>
                            <i class="fa-solid fa-bomb text-white text-4xl"></i>
                        </div>
                        
                        <!-- Explosion FX (Hidden by default) -->
                        <div id="explosion-fx" class="absolute inset-0 pointer-events-none flex items-center justify-center opacity-0 scale-50 transition-all duration-200">
                            <svg viewBox="0 0 200 200" class="w-full h-full text-tn-yellow">
                                <path fill="currentColor" stroke="#1E1E24" stroke-width="4" d="M100,0 L120,60 L180,40 L150,90 L200,120 L140,140 L160,200 L110,160 L70,200 L80,140 L10,160 L50,110 L0,70 L60,80 L40,20 Z" />
                            </svg>
                            <span class="absolute font-bangers text-6xl text-tn-red text-stroke transform -rotate-12">BAM!</span>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- 5. JOIN / NEWSLETTER (Functional Form) -->
    <section id="join" class="py-32 bg-tn-black text-white relative zigzag-top">
        <div class="max-w-3xl mx-auto px-4 text-center gsap-fade-up">
            <h2 class="text-6xl md:text-[100px] font-bangers mb-6 text-tn-yellow drop-shadow-[4px_4px_0_#FFF]">JANGAN KETINGGALAN!</h2>
            <p class="text-2xl font-bold mb-12 font-comic text-gray-300">Daftar untuk akses komik premium dan cheat code rahasia.</p>
            
            <form id="subscribe-form" class="relative max-w-xl mx-auto">
                <div class="flex flex-col sm:flex-row gap-4 relative z-10">
                    <input type="email" id="email-input" placeholder="ALAMAT EMAILMU..." required class="flex-1 px-6 py-5 bg-white text-tn-black font-bold text-xl brutal-border shadow-comic focus:outline-none focus:shadow-comic-lg transition-all uppercase placeholder:text-gray-400">
                    <button type="submit" id="submit-btn" class="px-10 py-5 bg-tn-red text-white font-bangers text-3xl brutal-border shadow-comic hover:bg-tn-yellow hover:text-tn-black hover:-translate-y-1 hover:shadow-comic-lg transition-all active:translate-y-2 active:shadow-none">
                        KIRIM!
                    </button>
                </div>
                
                <!-- Success Message -->
                <div id="form-success" class="absolute top-0 left-0 w-full h-full bg-tn-green brutal-border flex items-center justify-center scale-y-0 origin-bottom transition-transform duration-300 ease-out z-20 shadow-comic">
                    <span class="font-bangers text-4xl text-tn-black">BERHASIL BERGABUNG! 🎉</span>
                </div>
            </form>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-white text-tn-black pt-24 pb-12 brutal-border-t relative overflow-hidden">
        <div class="absolute inset-0 bg-halftone-light opacity-30 pointer-events-none"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
                
                <div class="col-span-1 md:col-span-5">
                    <a href="#" class="flex items-center gap-3 mb-6 inline-flex">
                        <div class="w-12 h-12 bg-tn-black rounded-full brutal-border flex items-center justify-center text-tn-yellow text-xl transform -rotate-12">
                            <i class="fa-solid fa-bolt"></i>
                        </div>
                        <span class="text-5xl font-bangers tracking-wider uppercase mt-1">TOON<span class="text-tn-blue">WORLD</span></span>
                    </a>
                    <p class="font-bold text-lg text-gray-700 max-w-sm">
                        Dimensi interaktif tanpa foto asli, 100% dipenuhi oleh CSS, SVG, dan imajinasi liar dari pikiran cerdas.
                    </p>
                </div>
                
                <div class="col-span-1 md:col-span-3">
                    <h4 class="font-bangers text-3xl text-tn-red mb-6 border-b-4 border-tn-black pb-2 inline-block">MARKAS</h4>
                    <ul class="space-y-3 font-bold text-lg uppercase">
                        <li><a href="#" class="hover:text-tn-blue hover:ml-2 transition-all block">Buku Komik</a></li>
                        <li><a href="#" class="hover:text-tn-blue hover:ml-2 transition-all block">Karakter</a></li>
                        <li><a href="#" class="hover:text-tn-blue hover:ml-2 transition-all block">Merchandise</a></li>
                    </ul>
                </div>

                <div class="col-span-1 md:col-span-4">
                    <h4 class="font-bangers text-3xl text-tn-purple mb-6 border-b-4 border-tn-black pb-2 inline-block">SINYAL</h4>
                    <div class="flex gap-4">
                        <a href="#" class="w-14 h-14 bg-tn-yellow brutal-border shadow-comic hover:shadow-none hover:translate-y-1 hover:translate-x-1 flex items-center justify-center text-3xl transition-all"><i class="fa-brands fa-discord"></i></a>
                        <a href="#" class="w-14 h-14 bg-tn-blue text-white brutal-border shadow-comic hover:shadow-none hover:translate-y-1 hover:translate-x-1 flex items-center justify-center text-3xl transition-all"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#" class="w-14 h-14 bg-tn-red text-white brutal-border shadow-comic hover:shadow-none hover:translate-y-1 hover:translate-x-1 flex items-center justify-center text-3xl transition-all"><i class="fa-brands fa-instagram"></i></a>
                    </div>
                </div>

            </div>
            
            <div class="border-t-4 border-tn-black pt-8 flex flex-col md:flex-row justify-between items-center font-bold text-lg">
                <p>&copy; 2024 TOON WORLD. DIBUAT UNTUK KESERUAN.</p>
                <div class="flex gap-6 mt-4 md:mt-0 uppercase">
                    <a href="#" class="hover:text-tn-red">Privasi</a>
                    <a href="#" class="hover:text-tn-red">Syarat</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Back to Hub Bubble -->
    <a href="../../index.html" class="fixed bottom-6 right-6 w-16 h-16 bg-white text-[#d4af37] rounded-full flex items-center justify-center shadow-2xl hover:scale-110 hover:-translate-y-1 transition-all z-[9999] border-4 border-[#d4af37] shadow-[0_0_20px_rgba(212,175,55,0.4)] group">
        <i class="fa-solid fa-house text-2xl group-hover:text-yellow-600 transition-colors"></i>
    </a>

    <!-- SCRIPTS -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            gsap.registerPlugin(ScrollTrigger);

            // 1. Lenis Smooth Scroll Setup
            const lenis = new Lenis({
                duration: 1.2,
                easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
                direction: 'vertical',
                gestureDirection: 'vertical',
                smooth: true,
            });

            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);

            // 2. Hero GSAP Reveals
            gsap.from(".gsap-hero-el", {
                y: 50,
                opacity: 0,
                duration: 1,
                stagger: 0.15,
                ease: "back.out(1.5)",
                delay: 0.2
            });

            // 3. Mouse Parallax Effect for Hero Graphics
            const layers = document.querySelectorAll('.parallax-layer');
            const heroSection = document.getElementById('hero');

            heroSection.addEventListener('mousemove', (e) => {
                const x = (e.clientX - window.innerWidth / 2);
                const y = (e.clientY - window.innerHeight / 2);

                layers.forEach(layer => {
                    const speed = layer.getAttribute('data-speed');
                    const xOffset = x * speed;
                    const yOffset = y * speed;
                    
                    gsap.to(layer, {
                        x: xOffset,
                        y: yOffset,
                        duration: 0.5,
                        ease: "power1.out"
                    });
                });
            });

            // Recenter on mouse leave
            heroSection.addEventListener('mouseleave', () => {
                layers.forEach(layer => {
                    gsap.to(layer, { x: 0, y: 0, duration: 1, ease: "elastic.out(1, 0.3)" });
                });
            });

            // 4. Scroll Revels for other sections
            const fadeUpElements = gsap.utils.toArray('.gsap-fade-up');
            fadeUpElements.forEach(el => {
                gsap.from(el, {
                    y: 60,
                    opacity: 0,
                    duration: 0.8,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: el,
                        start: "top 85%",
                        toggleActions: "play none none reverse"
                    }
                });
            });

            // 5. SwiperJS Initialization for Episodes
            new Swiper('.episodeSwiper', {
                slidesPerView: 1.2,
                spaceBetween: 20,
                grabCursor: true,
                navigation: {
                    nextEl: '.swiper-button-next-custom',
                    prevEl: '.swiper-button-prev-custom',
                },
                breakpoints: {
                    640: { slidesPerView: 2.2, spaceBetween: 20 },
                    1024: { slidesPerView: 3.2, spaceBetween: 30 },
                    1280: { slidesPerView: 4, spaceBetween: 40 },
                }
            });

            // 6. Fun Zone Interactive Game Logic
            const target = document.getElementById('interactive-target');
            const explosion = document.getElementById('explosion-fx');
            const scoreEl = document.getElementById('game-score');
            const gameViewport = target.parentElement;
            let score = 0;
            
            function moveTarget() {
                // Ensure target stays within bounds
                const maxX = gameViewport.clientWidth - target.clientWidth;
                const maxY = gameViewport.clientHeight - target.clientHeight;
                
                const randomX = Math.floor(Math.random() * maxX);
                const randomY = Math.floor(Math.random() * maxY);
                
                // Add a slightly random rotation for cartoon feel
                const randomRot = Math.floor(Math.random() * 40) - 20;

                gsap.to(target, {
                    x: randomX,
                    y: randomY,
                    rotation: randomRot,
                    duration: 0.4,
                    ease: "back.out(1.5)",
                    clearProps: "transform" // Reset to allow absolute positioning to work smoothly next time
                });
                
                // We actually apply it via top/left for absolute positioning limits
                target.style.left = randomX + 'px';
                target.style.top = randomY + 'px';
                gsap.set(target, {x:0, y:0}); // reset GSAP translation
            }

            // Initial position
            setTimeout(moveTarget, 1000);

            target.addEventListener('click', () => {
                score += 10;
                scoreEl.textContent = score;

                // Animate Score Bump
                gsap.fromTo(scoreEl, 
                    { scale: 2, color: '#fcee0a' }, 
                    { scale: 1, color: '#FF4949', duration: 0.5, ease: "bounce.out" }
                );

                // Show Explosion
                gsap.fromTo(explosion, 
                    { opacity: 1, scale: 0.5 }, 
                    { opacity: 0, scale: 1.5, duration: 0.4, ease: "power2.out" }
                );
                
                // Immediately pick new spot
                moveTarget();
            });

            // Optional: Move it automatically every 2 seconds if not clicked (adds pressure)
            setInterval(moveTarget, 2000);

            // 7. Functional Newsletter Form Simulation
            const form = document.getElementById('subscribe-form');
            const successMsg = document.getElementById('form-success');
            
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const btn = document.getElementById('submit-btn');
                const originalText = btn.innerHTML;
                
                // Loading state
                btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
                btn.style.pointerEvents = 'none';

                // Simulate API call
                setTimeout(() => {
                    // Success state
                    gsap.to(successMsg, {
                        scaleY: 1,
                        opacity: 1,
                        duration: 0.4,
                        ease: "back.out(1.5)"
                    });
                    
                    form.reset();
                    
                    // Reset after 3 seconds
                    setTimeout(() => {
                        gsap.to(successMsg, {
                            scaleY: 0,
                            duration: 0.3,
                            ease: "power2.in"
                        });
                        btn.innerHTML = originalText;
                        btn.style.pointerEvents = 'auto';
                    }, 3000);

                }, 1000);
            });

        });
    </script>
</body>
</html>'''

# Replace from <section id="characters"> to the end of the file
# We will match from "<!-- 2. CHARACTERS SECTION" to the very end
content = re.sub(r'<!-- 2\. CHARACTERS SECTION.*?</html>', new_sections_and_script, content, flags=re.DOTALL)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(content)
