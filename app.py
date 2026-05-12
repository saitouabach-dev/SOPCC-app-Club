import streamlit as st

# --- CONFIGURATION DU DESIGN ---
st.set_page_config(page_title="SOPCC App", page_icon="⚽", layout="wide")

# Appliquer le vert SOPCC
st.markdown("""
    <style>
    .stButton>button {
        background-color: #008143;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .main {
        background-color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
st.title("⚽ SOPCC - Gestionnaire de Séances")
st.write("Bienvenue dans votre interface de création Football et Futsal.")

# --- ONGLETS PRINCIPAUX ---
tab1, tab2, tab3 = st.tabs(["📂 Import & Tri", "📋 Créateur de Séance", "📊 Dashboard"])

with tab1:
    st.header("Éditeur de Base (Scanner)")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("SECTION FOOTBALL"):
            st.session_state.mode = "FOOTBALL"
    with col2:
        if st.button("SECTION FUTSAL"):
            st.session_state.mode = "FUTSAL"
            
    st.divider()
    
    uploaded_file = st.file_uploader("Importer un PDF d'exercices", type="pdf")
    
    if uploaded_file:
        st.success(f"Fichier {uploaded_file.name} reçu ! Prêt pour le tri.")
        # Ici on ajoutera la connexion à ton Agent 1 plus tard

with tab2:
    st.header("Générer une nouvelle séance")
    st.info("Cette section sera connectée au Méthodologue.")

with tab3:
    st.header("Suivi du Club")
    st.write("Lien SportEasy / FFF à venir ici.")
