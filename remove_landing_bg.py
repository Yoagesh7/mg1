import shutil

def remove_landing_bg_elements(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove the HTML background orb divs & geometric accent badges from hero
    target_html_block = """    <!-- Animated Floating Background Elements (Down Left and Right) -->
    <div class="absolute bottom-6 left-6 sm:left-12 w-72 sm:w-96 h-72 sm:h-96 bg-gradient-to-tr from-blue-500/15 via-indigo-500/10 to-transparent rounded-full blur-3xl pointer-events-none ambient-orb-left"></div>
    <div class="absolute bottom-4 right-6 sm:right-12 w-80 sm:w-[420px] h-80 sm:h-[420px] bg-gradient-to-bl from-cyan-400/15 via-blue-600/10 to-transparent rounded-full blur-3xl pointer-events-none ambient-orb-right"></div>
    
    <!-- Geometric Accent Badges (Floating Down Left & Right) -->
    <div class="hidden lg:flex items-center gap-3 absolute bottom-12 left-10 p-3 rounded-2xl bg-white/80 backdrop-blur-md border border-slate-200/80 shadow-lg pointer-events-none ambient-orb-left z-10">
      <div class="w-8 h-8 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-xs">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
      </div>
      <div>
        <span class="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">ICAI SQC-1 Verified</span>
        <span class="text-xs font-bold text-slate-800">100% Assurance Quality</span>
      </div>
    </div>

    <div class="hidden lg:flex items-center gap-3 absolute bottom-12 right-10 p-3 rounded-2xl bg-white/80 backdrop-blur-md border border-slate-200/80 shadow-lg pointer-events-none ambient-orb-right z-10">
      <div class="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-xs">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
      </div>
      <div>
        <span class="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">JET Analytics Engine</span>
        <span class="text-xs font-bold text-slate-800">Zero Sampling Gaps</span>
      </div>
    </div>"""

    if target_html_block in text:
        text = text.replace(target_html_block, "")
        print(f"Removed HTML bg elements from {filename}")
    else:
        print(f"Warning: HTML bg block not matched exactly in {filename}")

    # 2. Also clean up the unused CSS keyframes for floatOrbLeft and floatOrbRight
    target_css_block = """    /* Floating Ambient Background Elements for Landing Page */
    @keyframes floatOrbLeft {
      0%, 100% {
        transform: translate(0, 0) scale(1);
      }
      50% {
        transform: translate(25px, -35px) scale(1.08);
      }
    }
    @keyframes floatOrbRight {
      0%, 100% {
        transform: translate(0, 0) scale(1);
      }
      50% {
        transform: translate(-30px, 40px) scale(1.12);
      }
    }
    .ambient-orb-left {
      animation: floatOrbLeft 12s ease-in-out infinite;
      will-change: transform;
    }
    .ambient-orb-right {
      animation: floatOrbRight 14s ease-in-out infinite;
      will-change: transform;
    }"""

    if target_css_block in text:
        text = text.replace(target_css_block, "")
        print(f"Removed CSS keyframes from {filename}")
    else:
        print(f"Warning: CSS keyframes block not matched in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

remove_landing_bg_elements('html.html')
shutil.copyfile('html.html', 'index.html')
print("Synchronized to index.html")
