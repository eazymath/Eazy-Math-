import streamlit as st
import random
import sympy as sp

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random number for prime factors question
def generate_prime_question():
    number = random.randint(2, 250)
    st.write(f"Q1: List the prime factors of {number}:")
    user_input = st.text_input("Prime factors (e.g., 2,3,5):", key="q1")
    if st.button("Submit Q1"):
        prime_factors = [str(i) for i in range(2, number+1) if is_prime(i) and number % i == 0]
        if sorted(user_input.replace(" ", "").split(",")) == sorted(prime_factors):
            st.success("Correct!", icon="✅")
        else:
            st.error(f"Incorrect. The correct answer is: {', '.join(prime_factors)}", icon="❌")

# Generate a random expression for expanding and simplifying brackets
def generate_bracket_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.symbols('x')
    expression = (a*x + b) * (c*x + b)
    st.write(f"Q2: Expand and simplify the following expression: ({a}x + {b})({c}x + {b})")
    user_input = st.text_input("Your answer:", key="q2")
    if st.button("Submit Q2"):
        simplified_expr = sp.expand(expression)
        if sp.sympify(user_input.replace("^", "**")) == simplified_expr:
            st.success("Correct!", icon="✅")
        else:
            st.error(f"Incorrect. The correct answer is: {simplified_expr}", icon="❌")

# Generate a random percentage question
def generate_percentage_question():
    base = random.randint(100, 1000)
    percentage = random.randint(1, 100)
    st.write(f"Q3: What is {percentage}% of {base}?")
    user_input = st.text_input("Your answer:", key="q3")
    if st.button("Submit Q3"):
        correct_answer = (percentage / 100) * base
        if float(user_input) == correct_answer:
            st.success("Correct!", icon="✅")
        else:
            st.error(f"Incorrect. The correct answer is: {correct_answer}", icon="❌")

# Generate a random solve for X question
def generate_solve_for_x_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.symbols('x')
    equation = sp.Eq(a*x + b, c)
    st.write(f"Q4: Solve for x: {sp.latex(equation)}")
    user_input = st.text_input("Your answer for x:", key="q4")
    if st.button("Submit Q4"):
        correct_answer = sp.solve(equation, x)[0]
        if sp.sympify(user_input) == correct_answer:
            st.success("Correct!", icon="✅")
        else:
            st.error(f"Incorrect. The correct answer is: x = {correct_answer}", icon="❌")

# Main function to display all questions
def main():
    st.title("Math Practice Site")
    
    generate_prime_question()
    generate_bracket_question()
    generate_percentage_question()
    generate_solve_for_x_question()

if __name__ == "__main__":
    main()

