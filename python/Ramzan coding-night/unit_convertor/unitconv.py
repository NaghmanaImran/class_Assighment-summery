import streamlit as st

# Add custom CSS for animated background
def add_bg_animation():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }

        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        /* Additional styling for better contrast */
        .stSelectbox, .stNumberInput {
            background-color: rgba(255, 255, 255, 0.9) !important;
        }
        
        .stButton button {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #333 !important;
        }
        
        h1 {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .stSuccess, .stError {
            background-color: rgba(255, 255, 255, 0.9) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def length_conversion(value, from_unit, to_unit):
    # Base conversion to meters
    length_to_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    
    # Convert to base unit (meters) then to target unit
    meters = value * length_to_meters[from_unit]
    return meters / length_to_meters[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Base conversion to kilograms
    weight_to_kg = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Metric Tons": 1000
    }
    
    # Convert to base unit (kg) then to target unit
    kg = value * weight_to_kg[from_unit]
    return kg / weight_to_kg[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    # First convert to Celsius
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    else:  # Kelvin
        celsius = value - 273.15
    
    # Then convert to target unit
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    else:  # Kelvin
        return celsius + 273.15

def main():
    # Add the animated background
    add_bg_animation()
    
    st.title("Unit Converter")
    
    # Conversion type selection
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"]
    )
    
    # Units for each conversion type
    units = {
        "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", 
                  "Miles", "Yards", "Feet", "Inches"],
        "Weight": ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Tons"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }
    
    # Input value
    value = st.number_input("Enter value", value=0.0)
    
    # Unit selection
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units[conversion_type])
    with col2:
        to_unit = st.selectbox("To", units[conversion_type])
    
    # Perform conversion
    if st.button("Convert"):
        try:
            if conversion_type == "Length":
                result = length_conversion(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = weight_conversion(value, from_unit, to_unit)
            else:  # Temperature
                result = temperature_conversion(value, from_unit, to_unit)
            
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        except Exception as e:
            st.error("An error occurred during conversion. Please check your inputs.")

if __name__ == "__main__":
    main()
