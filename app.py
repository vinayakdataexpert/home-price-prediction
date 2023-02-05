import streamlit as st
import pickle
import pandas as pd


st.title('Bengalore Home Price Prediction')

location = ['other', ' Devarachikkanahalli', '1st Phase JP Nagar', '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar', '9th Phase JP Nagar', 'Abbigere', 'Akshaya Nagar', 'Ambalipura', 'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Balagere', 'Banashankari', 'Banashankari Stage III', 'Banashankari Stage V', 'Banaswadi', 'Bannerghatta Road', 'Basavangudi', 'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bommanahalli', 'Bommasandra', 'Bommasandra Industrial Area', 'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkalasandra', 'Choodasandra', 'Devanahalli', 'Dodda Nekkundi', 'Doddathoguru', 'Domlur', 'EPIP Zone', 'Electronic City', 'Electronic City Phase II', 'Electronics City Phase 1', 'Frazer Town', 'Garudachar Palya', 'Gottigere', 'Green Glen Layout', 'Gubbalala', 'Gunjur', 'HBR Layout', 'HRBR Layout', 'HSR Layout', 'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura', 'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara', 'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli', 'Hosur Road', 'Hulimavu', 'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur', 'Jalahalli', 'Jigani', 'KR Puram', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura', 'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura', 'Kammasandra', 'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Kasavanhalli', 'Kathriguppe', 'Kaval Byrasandra', 'Kengeri', 'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli', 'Kogilu', 'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate', 'Kumaraswami Layout', 'Kundalahalli', 'Lakshminarayana Pura', 'Lingadheeranahalli', 'Mahadevpura', 'Mallasandra', 'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Munnekollal', 'Murugeshpalya', 'Mysore Road', 'Nagarbhavi', 'Nagavara', 'Neeladri Nagar', 'OMBR Layout', 'Old Airport Road', 'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur', 'Parappana Agrahara', 'Poorna Pragna Layout', 'R.T. Nagar', 'Rachenahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra', 'Sahakara Nagar', 'Sanjay nagar', 'Sarjapur', 'Sarjapur  Road', 'Sarjapura - Attibele Road', 'Sector 7 HSR Layout', 'Seegehalli', 'Singasandra', 'Somasundara Palya', 'Sonnenahalli', 'Subramanyapura', 'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya', 'Thubarahalli', 'Tumkur Road', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Vidyaranyapura', 'Vijayanagar', 'Vittasandra', 'Whitefield', 'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yeshwanthpur']


file = open('model.pkl', 'rb')
model = pickle.load(file)

location_input = st.selectbox('Select the Location', location)

total_sqft = st.number_input('Enter Square Feet')
bathroom = st.number_input('Enter Number of Bathroom')
bhk = st.number_input('Enter Number of Bedroom')

if st.button('Predict'):
    input_df = pd.DataFrame({'location': [location_input], 'total_sqft': [total_sqft], 'bath': [bathroom], 'bhk': [bhk]})
    
    if total_sqft == 0.00 or bathroom == 0.00 or bhk == 0.00:
        result = "Please type Valid Sqare feet,Bathroom BHK"
        st.header(result)
    else:
        result = model.predict(input_df)
        result = round(result)
        st.header("₹" + str(result*100000))

# py -m streamlit run app.py   To run this app.py
