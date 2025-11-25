import streamlit as st


def main():
    """A simple counter that increments when the button is clicked."""
    st.title("カウントアップボタン")
    st.write("ボタンをクリックするたびに数値が1ずつ増加します。")

    # Initialize the counter in the session state
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # Define button to increment the count
    if st.button("カウントアップ"):
        st.session_state.count += 1

    # Define button to reset the count
    if st.button("リセット"):
        st.session_state.count = 0

    # Display the current count
    st.metric(label="現在のカウント", value=st.session_state.count)


if __name__ == "__main__":
    main()