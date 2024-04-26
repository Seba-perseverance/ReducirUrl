import pyshorteners
import streamlit as St

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

St.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered")
St.image("images/www.png", use_column_width=True)
St.title("URL Shortener")
URL = St.text_input("Enter the URL")
if St.button("Generate new URL"):
    St.write("URL Shortened:", shorten_url(URL))