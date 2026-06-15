import streamlit as st

from agents.coordinator_agent import (
    CoordinatorAgent
)

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="PharmaMind",
    page_icon="💊",
    layout="wide"
)

# ====================================
# STYLING
# ====================================

st.markdown(
    """
    <style>

    .main {
        background-color: white;
    }

    .stMetric {
        background-color: #F5FAFF;
        border: 1px solid #D6EAF8;
        padding: 15px;
        border-radius: 10px;
    }

    .block-container {
        padding-top: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ====================================
# SEARCH VARIABLES
# ====================================

if "products" not in st.session_state:

    st.session_state.products = []

if "substitutes" not in st.session_state:

    st.session_state.substitutes = []

if "api_name" not in st.session_state:

    st.session_state.api_name = ""

if "substitute_count" not in st.session_state:

    st.session_state.substitute_count = 0

manufacturer_count = 0

if st.session_state.products:

    import pandas as pd

    products_df = pd.DataFrame(
        st.session_state.products
    )

    manufacturer_count = (
        products_df[
            "Manufacturer"
        ]
        .nunique()
    )

# ====================================
# HEADER
# ====================================

st.title("💊 PharmaMind")

st.caption(
    "Pharma Market Intelligence Platform"
)

st.divider()

# ====================================
# SEARCH SECTION
# ====================================

st.subheader(
    "Search API / Salt Composition"
)

col1, col2 = st.columns([4, 1])

with col1:

    api_name = st.text_input(
    "API Name",
    placeholder=
    "Enter API name (Example: Betamethasone)",
    label_visibility="collapsed"
)

with col2:

    search_btn = st.button(
        "🔍 Analyze",
        use_container_width=True
    )

# ====================================
# RUN ANALYSIS
# ====================================

if search_btn:

    if api_name:

        with st.spinner(
            "Analyzing market data..."
        ):

            agent = (
                CoordinatorAgent()
            )

            result = (
                agent.run(
                    api_name
                )
            )

            st.session_state.products = (
                result["products"]
            )

            st.session_state.substitutes = (
                result["substitutes"]
            )

            st.session_state.substitute_count = (
                len(
                    result["substitutes"]
                )
            )

            st.session_state.api_name = (
                api_name
            )

        st.success(
            f"Found {len(st.session_state.products)} products"
        )

    else:

        st.warning(
            "Please enter an API name."
        )

# ====================================
# SIDEBAR
# ====================================

with st.sidebar:

    st.title("💊 PharmaMind")

    st.caption(
        "Pharma Market Intelligence Platform"
    )

    st.divider()

    st.subheader(
        "🏠 Navigation"
    )

    st.write("📊 Dashboard")
    st.write("💊 Products")
    st.write("🏭 Manufacturers")
    st.write("🔄 Substitutes")
    st.write("🤖 AI Assistant")

    st.divider()

    st.subheader(
        "🌐 Data Sources"
    )

    st.write("✅ 1mg")
    st.write("✅ Apollo Pharmacy")

    st.divider()

    st.subheader(
        "🧠 AI Services"
    )

    st.write(
        "🔍 Product Discovery"
    )

    st.write(
        "🏭 Manufacturer Intelligence"
    )

    st.write(
        "🔄 Substitute Intelligence"
    )

    st.write(
        "⭐ Recommendation Engine"
    )

    st.write(
        "📈 Market Insights"
    )

    st.divider()

    st.subheader(
        "📋 Search Summary"
    )

    st.write(
        f"API: {st.session_state.api_name if st.session_state.api_name else 'Not Selected'}"
    )

    st.write(
    f"Products: {len(st.session_state.products)}"
)

    st.write(
        f"Manufacturers: {manufacturer_count}"
        )

    st.write(
    f"Substitutes: {st.session_state.substitute_count}"
)

    st.divider()

    st.caption(
        "Version 1.0"
    )

# ====================================
# KPI CARDS
# ====================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💊 Products",
    len(st.session_state.products)
)

manufacturer_count = 0

if st.session_state.products:

    import pandas as pd

    products_df = pd.DataFrame(
        st.session_state.products
    )

    manufacturer_count = (
        products_df[
            "Manufacturer"
        ]
        .nunique()
    )

col2.metric(
    "🏭 Manufacturers",
    manufacturer_count
)

substitute_count = 0


col3.metric(
    "🔄 Substitutes",
    st.session_state.substitute_count
)


st.divider()

# ====================================
# TABS
# ====================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "📊 Overview",
        "💊 Products",
        "🏭 Manufacturers",
        "🔄 Substitutes",
        "🤖 AI Assistant",
        "📈 Market Insights"
    ]
)

with tab1:

    st.subheader(
        "Market Overview"
    )

    st.info(
        "Search an API to view market intelligence."
    )

with tab2:

    st.subheader(
        "Products"
    )

    if st.session_state.products:

        import pandas as pd

        products_df = pd.DataFrame(
            st.session_state.products
        )

        st.dataframe(
        products_df,
        use_container_width=True,
        hide_index=True
    )

    else:

        st.info(
            "No products available."
        )

with tab3:

    st.subheader(
        "Manufacturers"
    )

    if st.session_state.products:

        import pandas as pd

        products_df = pd.DataFrame(
            st.session_state.products
        )

        manufacturer_df = (
            products_df
            .groupby(
                "Manufacturer"
            )
            .agg(
                {
                    "Brand Name": "count",
                    "API": lambda x: ", ".join(
                        x.dropna()
                        .unique()[:5]
                    )
                }
            )
            .reset_index()
        )

        manufacturer_df.columns = [
    "Manufacturer",
    "Product Count",
    "APIs"
]

        total_products = (
            manufacturer_df[
                "Product Count"
            ]
            .sum()
        )
        
        manufacturer_df[
            "Market Share %"
        ] = round(
            (
                manufacturer_df[
                    "Product Count"
                ]
                / total_products
            ) * 100,
            2
        )
        manufacturer_df = (
    manufacturer_df[
        [
            "Manufacturer",
            "Product Count",
            "Market Share %",
            "APIs"
        ]
    ]
)

        manufacturer_df = (
            manufacturer_df
            .sort_values(
                "Product Count",
                ascending=False
            )
        )

        st.dataframe(
            manufacturer_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No manufacturer data available."
        )
with tab4:

    st.subheader(
        "Substitutes"
    )

    if st.session_state.substitutes:

        import pandas as pd

        substitutes_df = pd.DataFrame(
            st.session_state.substitutes
        )

        st.dataframe(
            substitutes_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No substitutes available."
        )

   

with tab5:

    st.subheader(
        "PharmaMind Assistant"
    )

    st.chat_input(
        "Ask PharmaMind..."
    )
    
with tab6:

    st.subheader(
        "Market Insights"
    )

    if st.session_state.products:

        import pandas as pd

        products_df = pd.DataFrame(
            st.session_state.products
        )

        total_products = len(
            products_df
        )

        total_manufacturers = (
            products_df[
                "Manufacturer"
            ]
            .nunique()
        )

        top_manufacturer = (
            products_df[
                "Manufacturer"
            ]
            .value_counts()
            .index[0]
        )

        top_dosage_form = (
            products_df[
                "Dosage Form"
            ]
            .value_counts()
            .index[0]
        )

        top_api = (
            products_df[
                "API"
            ]
            .value_counts()
            .index[0]
        )

        st.metric(
            "Total Products",
            total_products
        )

        st.metric(
            "Total Manufacturers",
            total_manufacturers
        )

        st.metric(
            "Total Substitutes",
            st.session_state.substitute_count
        )

        st.write(
            f"🏭 Top Manufacturer: {top_manufacturer}"
        )

        st.write(
            f"💊 Most Common Dosage Form: {top_dosage_form}"
        )

        st.write(
            f"🧪 Most Common API: {top_api}"
        )

    else:

        st.info(
            "Search an API first."
        )