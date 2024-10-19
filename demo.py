import streamlit as st
from st_audiorec import st_audiorec


st.set_page_config(page_title="streamlit_audio_recorder")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    st.title('🗣️ speaker verification')
    st.markdown('')
    st.write('\n\n')

    wav_audio_data = st_audiorec() 

    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')


if __name__ == '__main__':
    # call main function
    audiorec_demo_app()
