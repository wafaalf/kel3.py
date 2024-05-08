import streamlit as st

st.header('Perhitungan Kadar Cl menggunakan cara Mohr', divider='rainbow')

st.write('Kelompok 3 LPK')
st.write('Arya Pratama W.P (2360077)')
st.write('Asriyanti Lestari (2360078)')
st.write('Azka Afriyuni Suwito (2360084)')
st.write('Shintya Ingrid M.M (2360262)')
st.write('Wafa Alifiah (2360287)')


Volume_AgNO3= st.number_input('masukkan Volume AgNO3 (mL)',format='%.2f')
st.write('the first number is',Volume_AgNO3)

Normalitas_AgNO3= st.number_input('masukkan Normalitas AgNO3 (mgrek/mL)',format='%.4f')
st.write('the second number is',Normalitas_AgNO3)

BE_Cl= st.number_input('masukkan BE Cl dalam (mg/mgrek)',format='%.1f')
st.write('the third number is',BE_Cl)

Volume_Sampel= st.number_input('masukkan Volume Sampel (mL)',format='%.0f')
st.write('the fourth number is',Volume_Sampel)

Perhitungan_Kadar_Cl= (Volume_AgNO3 * Normalitas_AgNO3 * BE_Cl * 0.001 * 100) / Volume_Sampel
st.write(f'(Volume AgNO3 {Volume_AgNO3} x Normalitas AgNO3 {Normalitas_AgNO3} x BE Cl {BE_Cl} x {0.001} X {100}) : Volume_sampel {Volume_Sampel} = {Perhitungan_Kadar_Cl}')

st.success(f'Persentase kadar Cl adalah {Perhitungan_Kadar_Cl:.2f}%(b/v)')