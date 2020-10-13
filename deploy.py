import pickle
import streamlit as st

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)





def main():
    st.title("Credit card default prediction model")
    lim_bal = st.text_input("Limit Balance","Type Here")
    education = st.text_input("Education level","Type Here")
    marriage = st.text_input("Marital status","Type Here")
    age = st.text_input("Customer age","Type Here")
    pay1 = st.text_input("September payment status","Type Here")
    bill1 = st.text_input("Bill statement september","Type Here")
    bill2 = st.text_input("Bill statement august","Type Here")
    bill3 = st.text_input("Bill statement july","Type Here")
    bill4 = st.text_input("Bill statement june","Type Here")
    bill5 = st.text_input("Bill statement may","Type Here")
    bill6 = st.text_input("Bill statement april","Type Here")
    payamt1 = st.text_input("amount statement september","Type Here")
    payamt2 = st.text_input("amount statement august","Type Here")
    payamt3 = st.text_input("amount statement july","Type Here")
    payamt4 = st.text_input("amount statement june","Type Here")
    payamt5 = st.text_input("amount statement may","Type Here")
    payamt6 = st.text_input("amount statement april","Type Here")

    if st.button("Predict"):
        result = classifier.predict([[lim_bal, education, marriage, age, pay1, bill1,bill2,bill3,bill4,bill5,bill6,payamt1,payamt2,payamt3,payamt4,payamt5,payamt6]])
        print(result)
        st.success("The output is {}".format(result))

if __name__ == "__main__":
    main()