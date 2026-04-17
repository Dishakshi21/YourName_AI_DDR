import streamlit as st
from extractor.pdf_extractor import extract_pdf
from report.generator import generate_report

st.set_page_config(page_title="AI DDR Generator", layout="wide")

# 🎨 Balanced Dark + White UI
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3 {
        color: #FFFFFF;
    }

    /* White card blocks */
    .card {
        background-color: white;
        color: black;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    /* Button */
    .stButton button {
        background: linear-gradient(90deg, #6C63FF, #00C9A7);
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }

    /* File uploader */
    .stFileUploader {
        background-color: #1A1D24;
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 🧠 Header
st.markdown("""
# 🤖 AI DDR Generator  
### ⚡ Generate Smart Diagnostic Reports
""")

st.divider()

# 📂 Upload Section
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    inspection_file = st.file_uploader("📄 Upload Inspection Report")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    thermal_file = st.file_uploader("🌡️ Upload Thermal Report")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 🚀 Generate Button
if st.button("✨ Generate DDR Report", use_container_width=True):

    if inspection_file and thermal_file:

        with st.spinner("🔄 AI analyzing..."):

            text1, img1 = extract_pdf(inspection_file)
            text2, img2 = extract_pdf(thermal_file)

            combined_text = text1 + "\n\n" + text2
            all_images = img1 + img2

            report = generate_report(combined_text, all_images)

        st.success("✅ Report Generated!")

        st.divider()

        # 📄 REPORT (WHITE CARD)
        st.markdown("## 📄 DDR Report")

        st.markdown(
            f"""
            <div class="card">
            {report}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # 🖼️ Images (WHITE CARD)
        st.markdown("## 🖼️ Extracted Images")

        if all_images:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            cols = st.columns(3)
            for i, img in enumerate(all_images):
                cols[i % 3].image(img, use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.info("No images found.")

    else:
        st.warning("⚠️ Please upload both files")