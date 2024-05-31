import streamlit as st
import numpy as np

st.title("Laptop Price Predictor")

company = st.selectbox(label="Select the company of your laptop",options=('Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'Fujitsu', 'HP', 'Huawei', 'LG', 'Lenovo', 'MSI', 'Mediacom', 'Microsoft', 'Razer', 'Samsung', 'Toshiba', 'Vero', 'XiaomiGoogle'))

typename = st.selectbox(label="Select the type of your laptop",options=('2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation'))

cpu = st.selectbox("Select the CPU your laptop uses",options=('AMD A10-Series', 'AMD A12-Series', 'AMD A4-Series', 'AMD A6-Series', 'AMD A8-Series', 'AMD A9-Series', 'AMD E-Series', 'AMD Fx', 'AMD Ryzen 1600', 'AMD Ryzen 1700', 'Intel Atom', 'Intel Celeron Dual Core', 'Intel Celeron Quad Core', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core m', 'Intel Pentium Dual Core', 'Intel Pentium Quad Core', 'Intel Xeon', 'Samsung Cortex'))

ram = st.text_input(label="Enter the size of your laptop's RAM")
ram = ram.strip()
if ram == "":
    ram = 0
else:
    ram = int(ram)

gpu = st.selectbox(label="Select the GPU your laptop uses",options=('AMD', 'ARM', 'Intel', 'Nvidia'))

opsys = st.selectbox(label="Enter the operating system your laptop uses",options=('Windows', 'Chrome OS', 'No OS', 'Android', 'Linux', 'Mac'))

weight = st.text_input("Enter your laptop's weight")
if weight == "":
    weight = 0
else:
    weight = float(ram)

touchscreen = st.radio(label="Is your laptop a touchscreen one?", options=["Yes", "No"])

ips = st.radio(label="Does your screen use In-Plane Switching (IPS) technology?", options=["Yes", "No"])

hdd = st.selectbox(label="Select the size of Hard Disk Drive",options=("0", "1", "8", "16", "32", "128", "180", "240", "256", "500", "512", "1024", "2048"))
hdd = int(hdd)
ssd = st.selectbox(label="Select the size of Solid State Drive",options=("0", "1", "8", "16", "32", "128", "180", "240", "256", "500", "512", "1024", "2048"))
ssd = int(ssd)

screenlength = st.text_input(label="Enter the length of the screen")
if screenlength == "":
    screenlength = 0
else:
    screenlength = float(screenlength)

screenwidth = st.text_input(label="Enter the width of the screen")
if screenwidth == "":
    screenwidth = 0
else:
    screenwidth = float(screenwidth)

inches = st.text_input(label="Enter the number of inches for the screen")
if inches == "":
    inches = 0
else:
    inches = float(inches)

ppi = np.sqrt(screenlength * screenlength + screenwidth * screenwidth)/inches

#model = 
if st.button(label="Predict Price"):
    st.write(company)
    st.write(typename)
    st.write(cpu)
    st.write(ram)
    st.write(gpu)
    st.write(opsys)
    st.write(weight)
    st.write(touchscreen)
    st.write(ips)
    st.write(ssd)
    st.write(hdd)
    st.write(ppi)
    st.write("")