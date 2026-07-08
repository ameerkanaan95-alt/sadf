"""
Interactive 3D Globe — Highlighted Countries
=============================================
Run with:  streamlit run globe_app.py

Requires:  pip install streamlit plotly

The globe uses Plotly's orthographic projection, which is natively
draggable (click + drag to rotate) and zoomable (scroll wheel / pinch)
inside Streamlit — no extra code needed for the interactivity itself.
"""

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Co-sponsoring countries", layout="wide")

# ---------------------------------------------------------------------------
# Country list -> ISO-3166-1 alpha-3 codes (ISO-3 is far more reliable for
# Plotly's `locationmode="ISO-3"` matching than free-text country names).
# ---------------------------------------------------------------------------
COUNTRIES = {
    "Algeria": "DZA",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Australia": "AUS",
    "Austria": "AUT",
    "Bahrain": "BHR",
    "Bangladesh": "BGD",
    "Belgium": "BEL",
    "Bosnia and Herzegovina": "BIH",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Denmark": "DNK",
    "Ecuador": "ECU",
    "Estonia": "EST",
    "Finland": "FIN",
    "France": "FRA",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Hungary": "HUN",
    "Indonesia": "IDN",
    "Iraq": "IRQ",
    "Ireland": "IRL",
    "Italy": "ITA",
    "Japan": "JPN",
    "Jordan": "JOR",
    "Kuwait": "KWT",
    "Latvia": "LVA",
    "Lebanon": "LBN",
    "Libya": "LBY",
    "Luxembourg": "LUX",
    "Malta": "MLT",
    "Mexico": "MEX",
    "Moldova": "MDA",
    "Montenegro": "MNE",
    "Morocco": "MAR",
    "Netherlands": "NLD",
    "New Zealand": "NZL",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Oman": "OMN",
    "Pakistan": "PAK",
    "Palestine": "PSE",
    "Philippines": "PHL",
    "Poland": "POL",
    "Portugal": "PRT",
    "Qatar": "QAT",
    "Republic of Korea": "KOR",
    "Romania": "ROU",
    "Saudi Arabia": "SAU",
    "Singapore": "SGP",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Spain": "ESP",
    "Sudan": "SDN",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Syrian Arab Republic": "SYR",
    "Turkey": "TUR",
    "Ukraine": "UKR",
    "United Arab Emirates": "ARE",
    "United Kingdom": "GBR",
    "United States of America": "USA",
    "Yemen": "YEM",
}

names = list(COUNTRIES.keys())
codes = list(COUNTRIES.values())

# ---------------------------------------------------------------------------
# Fixed colors (no sidebar controls)
# ---------------------------------------------------------------------------
green_shade = "#2E7D32"
grey_shade = "#BDBDBD"
ocean_shade = "#EAF3FA"
show_labels = True

st.title("Co-sponsoring countries")
st.caption(
    "Drag to rotate • Scroll or pinch to zoom • Highlighted countries are shown in green"
)

# ---------------------------------------------------------------------------
# Build the figure
# ---------------------------------------------------------------------------
fig = go.Figure(
    data=go.Choropleth(
        locations=codes,
        z=[1] * len(codes),
        locationmode="ISO-3",
        colorscale=[[0, green_shade], [1, green_shade]],
        showscale=False,
        marker_line_color="white",
        marker_line_width=0.5,
        text=names,
        hovertemplate="%{text}<extra></extra>",
    )
)

fig.update_geos(
    projection_type="orthographic",
    showcountries=True,
    countrycolor="white",
    showland=True,
    landcolor=grey_shade,
    showocean=True,
    oceancolor=ocean_shade,
    showlakes=False,
    showcoastlines=False,
    bgcolor="rgba(0,0,0,0)",
)

fig.update_layout(
    height=750,
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor="rgba(0,0,0,0)",
    geo=dict(projection_rotation=dict(lon=10, lat=20, roll=0)),
)

st.plotly_chart(fig, width="stretch", config={"scrollZoom": True})

# ---------------------------------------------------------------------------
# Optional reference list
# ---------------------------------------------------------------------------
if show_labels:
    with st.expander(f"Highlighted countries ({len(names)})", expanded=False):
        cols = st.columns(3)
        for i, n in enumerate(sorted(names)):
            cols[i % 3].write(f"- {n}")