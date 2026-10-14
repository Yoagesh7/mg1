import sys
import shutil

new_contact_section = '''<!-- ========================================== -->
  <!-- 12. AUDIT PROPOSAL & CONTACT FORM SECTION  -->
  <!-- ========================================== -->
  <section class="py-24 bg-gradient-to-b from-slate-50 via-white to-slate-50 border-t border-slate-200/80" id="contact">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-16 reveal-on-scroll">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 text-white text-[11px] font-semibold tracking-wider uppercase shadow-xs mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Audit Practice Desk</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-3.5">
          Connect with our Senior Audit Partners
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed font-light">
          Submit your audit inquiry, RFP document, or request an initial exploratory meeting. All communications are governed by strict auditor confidentiality agreements.
        </p>
      </div>

      <!-- Main Bento Grid Layout: Modern Classic Boxes -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Left Column: Desk Information Bento Boxes (5 Cols) -->
        <div class="lg:col-span-5 space-y-5 reveal-on-scroll">
          
          <!-- Box 1: Official Practice Location -->
          <div class="group bg-white rounded-2xl p-6 sm:p-7 border border-slate-200/90 shadow-xs hover:border-slate-900 hover:shadow-md transition-all duration-300">
            <div class="flex items-center justify-between mb-4">
              <div class="w-10 h-10 rounded-xl bg-slate-900 text-white flex items-center justify-center flex-shrink-0 shadow-xs group-hover:scale-105 transition-transform">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              </div>
              <span class="text-[11px] font-bold uppercase tracking-widest text-slate-400 group-hover:text-slate-700 transition-colors">Location</span>
            </div>
            <div class="text-xs font-semibold uppercase tracking-wider text-blue-600 mb-1">Official Practice Location</div>
            <h3 class="text-base font-bold text-slate-900 tracking-tight">MG Audit / Tax Experts &amp; Advisory</h3>
            <p class="text-xs sm:text-sm text-slate-500 mt-1.5 leading-relaxed font-normal">
              Saravanampatti, Coimbatore, Tamil Nadu 641035
            </p>
            <div class="mt-5 pt-4 border-t border-slate-100">
              <a href="https://www.google.com/maps/place/MG+Audit+%2F+Tax+Experts+%26+Advisory+%2F+Tax+Consultancy/@11.0752631,76.9967702,17z/data=!4m8!3m7!1s0x3ba8f7562a0dad57:0xf6207fc8f814c8a6!8m2!3d11.0752631!4d76.9967702!9m1!1b1!16s%2Fg%2F11v637175p!18m1!1e1?entry=ttu&amp;g_ep=EgoyMDI2MDQwMS4wIKXMDSoASAFQAw%3D%3D" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-between w-full py-2.5 px-4 rounded-xl bg-slate-50 hover:bg-slate-900 text-slate-700 hover:text-white font-medium text-xs border border-slate-200 hover:border-slate-900 transition-all duration-200 group/link">
                <span class="font-semibold">Open in Google Maps</span>
                <span class="group-hover/link:translate-x-1 transition-transform">&rarr;</span>
              </a>
            </div>
          </div>

          <!-- Box 2: Direct Contact Channels (Clean Split Box) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <!-- Inquiries Box -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs hover:border-slate-900 hover:shadow-xs transition-all duration-300">
              <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center mb-3">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
              </div>
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1">Practice Inquiries</span>
              <a href="mailto:audit@mgassociates.in" class="text-xs sm:text-sm font-bold text-slate-900 hover:text-blue-600 transition-colors break-all">
                audit@mgassociates.in
              </a>
            </div>

            <!-- Statutory Desk Box -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs hover:border-slate-900 hover:shadow-xs transition-all duration-300">
              <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center mb-3">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1">Statutory Desk</span>
              <a href="tel:+914222345678" class="text-xs sm:text-sm font-bold text-slate-900 hover:text-emerald-600 transition-colors whitespace-nowrap">
                +91 422 234 5678
              </a>
            </div>
          </div>

          <!-- Box 3: Assurance & Ethics Guarantee Badge Box -->
          <div class="bg-slate-900 rounded-2xl p-5 sm:p-6 text-white border border-slate-800 shadow-sm relative overflow-hidden">
            <div class="relative z-10 flex items-start gap-4">
              <div class="w-9 h-9 rounded-xl bg-white/10 text-emerald-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
              </div>
              <div>
                <h4 class="text-xs font-bold uppercase tracking-widest text-slate-300">ICAI Ethics &amp; Confidentiality</h4>
                <p class="text-xs text-slate-300 mt-1 leading-relaxed font-light">
                  All RFP documents and exploratory inquiries are protected under non-disclosure protocols and statutory confidentiality frameworks.
                </p>
              </div>
            </div>
          </div>

        </div>

        <!-- Right Column: Audit RFP & Consultation Request Form Card (7 Cols) -->
        <div class="lg:col-span-7 reveal-on-scroll">
          <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200/90 shadow-sm hover:border-slate-300 transition-all duration-300">
            
            <div class="flex items-center justify-between pb-6 mb-6 border-b border-slate-100">
              <div>
                <h3 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight">Audit RFP &amp; Consultation Request</h3>
                <p class="text-xs sm:text-sm text-slate-500 mt-1">Receive a tailored audit roadmap and proposal within 24 hours.</p>
              </div>
              <span class="hidden sm:inline-flex items-center px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-[11px] font-semibold">
                Fast Response • 24h
              </span>
            </div>

            <form id="auditInquiryForm" onsubmit="handleFormSubmit(event)" class="space-y-5">
              
              <!-- Company & Contact Person Row -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Company / Entity Name *</label>
                  <input required type="text" id="companyName" placeholder="e.g. Acme Technologies Pvt Ltd" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 placeholder:text-slate-400 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none"/>
                </div>
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Contact Person &amp; Designation *</label>
                  <input required type="text" id="contactName" placeholder="e.g. Rajesh Kumar (CFO)" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 placeholder:text-slate-400 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none"/>
                </div>
              </div>

              <!-- Email & Phone Row -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Corporate Email Address *</label>
                  <input required type="email" id="contactEmail" placeholder="rajesh@acmetech.com" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 placeholder:text-slate-400 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none"/>
                </div>
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Direct Phone / Mobile *</label>
                  <input required type="tel" id="contactPhone" placeholder="+91 98765 43210" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 placeholder:text-slate-400 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none"/>
                </div>
              </div>

              <!-- Audit Type & Turnover Selects -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Type of Audit Required *</label>
                  <select id="formAuditType" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none cursor-pointer">
                    <option value="Statutory Audit (Sec 139/143)">Statutory Audit (Sec 139/143)</option>
                    <option value="Tax Audit (Sec 44AB)">Tax Audit (Sec 44AB)</option>
                    <option value="Internal Audit & ICFR">Internal Audit &amp; ICFR</option>
                    <option value="Forensic / Investigative Audit">Forensic / Investigative Audit</option>
                    <option value="Information Systems (ITGC) Audit">Information Systems (ITGC) Audit</option>
                    <option value="Financial Due Diligence">Financial Due Diligence</option>
                    <option value="Bank / Stock Audit">Bank / Stock Audit</option>
                  </select>
                </div>
                <div>
                  <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Annual Turnover Range *</label>
                  <select id="formTurnover" class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none cursor-pointer">
                    <option value="Below ₹5 Cr">Below &#8377;5 Crores</option>
                    <option value="₹5 Cr - ₹50 Cr">&#8377;5 Cr - &#8377;50 Crores</option>
                    <option value="₹50 Cr - ₹250 Cr">&#8377;50 Cr - &#8377;250 Crores</option>
                    <option value="Above ₹250 Cr">Above &#8377;250 Crores</option>
                  </select>
                </div>
              </div>

              <!-- Message / Details -->
              <div>
                <label class="block text-[11px] font-bold text-slate-700 uppercase tracking-wider mb-1.5">Engagement Details / Specific Requirements</label>
                <textarea rows="3" id="formMessage" placeholder="Specify financial year, multi-location audit, ERP software (SAP, Oracle, Tally), or specific audit scope..." class="w-full rounded-xl border border-slate-200 bg-slate-50/50 py-2.5 px-3.5 text-sm text-slate-900 placeholder:text-slate-400 focus:bg-white focus:border-slate-900 focus:ring-1 focus:ring-slate-900 transition-all outline-none resize-none"></textarea>
              </div>

              <!-- Checkbox -->
              <div class="flex items-start gap-2.5 pt-1">
                <input type="checkbox" id="confidentialityAck" required class="mt-0.5 rounded border-slate-300 text-slate-900 focus:ring-slate-900 cursor-pointer"/>
                <label for="confidentialityAck" class="text-xs text-slate-500 leading-relaxed cursor-pointer select-none">
                  I agree to confidentiality terms governed by ICAI code of professional ethics.
                </label>
              </div>

              <!-- Submit Button -->
              <button type="submit" class="w-full py-3.5 px-6 rounded-xl bg-slate-900 hover:bg-black text-white font-bold text-xs uppercase tracking-widest transition-all duration-200 shadow-sm hover:shadow-md flex items-center justify-center gap-2 group/submit">
                <span>Submit Audit Inquiry &amp; Request RFP</span>
                <span class="group-hover/submit:translate-x-1 transition-transform">&rarr;</span>
              </button>

            </form>

            <div id="formSuccessToast" class="hidden mt-5 p-4 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs">
              <div class="flex items-center gap-2 mb-1">
                <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span class="font-bold">Proposal Request Received Successfully!</span>
              </div>
              <p class="pl-6 text-slate-600 font-light">
                Your reference inquiry ID is <span class="font-mono font-bold text-slate-900" id="inquiryIdDisplay">MGA-AUD-2024</span>. Our Engagement Partner will review your details and reach out within 24 business hours.
              </p>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  '''

with open('html.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- ========================================== -->\n  <!-- 12. AUDIT PROPOSAL & CONTACT FORM SECTION  -->\n  <!-- ========================================== -->'
end_marker = '<!-- ========================================== -->\n  <!-- 13. MAIN FOOTER                           -->\n  <!-- ========================================== -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('Error: markers not found!')
    sys.exit(1)

updated_text = text[:start_idx] + new_contact_section + text[end_idx:]

with open('html.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

# Also synchronize to index.html
shutil.copyfile('html.html', 'index.html')

print('Successfully updated contact section in html.html and index.html')
