import streamlit as st
def largest_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

st.title("Find the largest number")

st.write("Enter three numbers below to get largest of them")

n1 = st.number_input("Enter first number")
n2 = st.number_input("Enter second number")
n3 = st.number_input("Enter third number")

if st.button("Find Largest"):
    op = largest_num(n1, n2,n3)
    st.success(f"The largest number is : {op}")