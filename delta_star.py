import streamlit as st

st.title("2305a21l58-PS5")

def DELTA_STAR(R12,R23,R13):
    R1=(R12*R13)/(R23+R23+R13)
    R2=(R12*R23)/(R12+R23+R13)
    R3=(R13*R23)/(R12+R23+R13)
    st.write(f"R1={R1:.2f} Ohms")
    st.write(f"R2={R2:.2f} Ohms")
    st.write(f"R3={R3:.2f} Ohms")  

    return R1,R2,R3

st.write("calculate the resistance values (R1,R2,R3)  of the STAR connection network for the given DELTA connection network having resistances R12,R23, and R31.")
col1,col2=st.columns(2)
with col1:
    R12=st.number_input("R12:Ohms",value=100)
    R23=st.number_input("R23:Ohms",value=100)
    R31=st.number_input("R31:Ohms",value=100)
    a=st.button("Compute")

with col2:
    if a:

        DELTA_STAR(R12,R23,R31)
