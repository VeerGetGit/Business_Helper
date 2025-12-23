import streamlit as st
import requests

st.set_page_config(page_title="AI Architecture Generator", layout="wide")

st.title("AI Requirement → Technical Architecture Tool")

requirement = st.text_area(
    "Enter Business Requirement",
    height=200,
    placeholder="Example: Build a web app with authentication and CRUD features"
)

if st.button("Generate Architecture"):
    if not requirement.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Architects are analyzing..."):
            response = requests.post(
                "http://localhost:5000/generate",
                json={"requirement": requirement}
            )

        if response.status_code != 200:
            st.error("Backend error")
            st.text(response.text)
            st.stop()

        try:
            result = response.json()
        except Exception:
            st.error("Invalid JSON returned by backend")
            st.text(response.text)
            st.stop()

        if "error" in result:
            st.error(result["error"])
            st.text(result.get("raw_output", ""))
            st.stop()

        st.success("Architecture Generated")

        st.subheader("Assumptions")
        st.write(result["assumptions"])

        st.subheader("Missing Requirements")
        st.write(result["missing_requirements"])

        st.subheader("Modules")
        st.json(result["modules"])

        st.subheader("Database Schema")
        st.json(result["database_schema"])

        st.subheader("Pseudo Code")
        st.json(result["pseudo_code"])

        st.subheader("Architecture Diagram (Mermaid)")
        st.code(result["architecture_diagram"])
