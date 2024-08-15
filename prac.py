import streamlit as st

# Try to import sympy and provide error feedback if it fails
try:
    import sympy as sp
    sympy_installed = True
except ModuleNotFoundError:
    sympy_installed = False

# Title of the app
st.title("Eazy Math: Quadratic Formula Practice")

if not sympy_installed:
    st.error("Sympy is not installed. Please install it using 'pip install sympy' and try running the app again.")
else:
    # Function to generate a quadratic equation
    def generate_quadratic_equation():
        a, b, c = sp.symbols('a b c')
        x = sp.symbols('x')
        equation = a*x**2 + b*x + c
        return equation

    # Function to solve the quadratic equation
    def solve_quadratic_equation(a, b, c):
        x = sp.symbols('x')
        solution = sp.solve(a*x**2 + b*x + c, x)
        return solution

    # User input for coefficients
    st.write("Enter the coefficients for the quadratic equation (ax² + bx + c = 0):")
    a = st.number_input("Enter coefficient a:", value=1.0)
    b = st.number_input("Enter coefficient b:", value=0.0)
    c = st.number_input("Enter coefficient c:", value=0.0)

    # Generate and display the quadratic equation
    equation = generate_quadratic_equation()
    st.write(f"The quadratic equation is: {sp.latex(a*sp.symbols('x')**2 + b*sp.symbols('x') + c)} = 0")

    # Solve and display the solution
    if st.button("Solve"):
        solution = solve_quadratic_equation(a, b, c)
        st.write(f"The solution for x is: {solution}")

        # Provide positive feedback if the solution is found
        if solution:
            st.success("Great! The equation has been solved.")
        else:
            st.error("Oops! There was an issue solving the equation.")
