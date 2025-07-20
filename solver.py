import streamlit as st
import math

# Title
st.title("🧮 Quadratic Equation Solver")

st.markdown("### 📘 Solve any quadratic equation of the form:")
st.latex("ax^2 + bx + c = 0")

# Input fields
st.sidebar.header("Enter coefficients:")
a = st.sidebar.number_input("a (≠ 0)", value=1.0)
b = st.sidebar.number_input("b", value=0.0)
c = st.sidebar.number_input("c", value=0.0)

def discriminant(a,b,c):
    delta= (b**2)- 4 * a * c
    st.subheader("📊 Results")
    st.write(f"Discriminant (Δ) = `{delta}`")

    if delta > 0:
        x1 =((-b)+ math.sqrt(delta))/ (2*a) 
        x2 =((-b)- math.sqrt(delta))/ (2*a) 
        st.success("Two distinct real solutions:")
        st.write(f"x1 = {x1}")
        st.write(f"x2 = {x2}")

    elif delta ==0:
        x= (-b)/(2*a)
        st.info("One real (double) solution:")
        st.write(f"x = {x}")

    else:
         real = -b / (2 * a)
         imag = math.sqrt(-delta) / (2 * a)
         x1 = complex(real, imag)
         x2 = complex(real, -imag)
         st.warning("Two complex solutions:")
         st.write(f"x1 = {x1}")
         st.write(f"x2 = {x2}")
       
# Solve button
if st.button("🔍 Solve the Equation"):
    if a == 0:
        st.error("Coefficient 'a' must not be zero for a quadratic equation.")
    else:
        discriminant(a, b, c)


