"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
import mlab
from mongoengine import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

# Connect mlab
mlab.connect()

class Item(Document):
    image = StringField()
    title = StringField()
    price = FloatField()

class Profile(Document):
    image = StringField()
    title = StringField()
    age = FloatField()

# item1 = Item(image = "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/Bc/B4/swCYODnJGzU4cfprkDL-ifgzM1NNMNZY832oUV97ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC8wXC8wXC8yXC8yXC85XC81XC9DRklMUEQwMDIyOTUwX05SMDAwMl8xMDAuanBnIiwiZmEiOjEsImZmIjoxLCJmaCI6NjAxLCJmcSI6OTAsImZ0IjoxLCJmdyI6NDEwfQ~~.jpg",
#              title = "Slip on",
#              price = 456)
# item1.save()

# profile1 = Profile(image_profile = "http://file2.instiz.net/data/file2/2017/04/18/7/0/7/707bb2a82ea9e9bb1c2ea80447db7655.jpg",
#                 title_profile = "Shibaaaa",
#                 age_profile = "5")
# profile1.save()

image_profile = "http://kenh14cdn.com/k:r9LkQbF6VoiiUUdcKz6F7w8WhmMgcd/Image/2015/01/td1/TD2/365594eef01f3a296c1f79599a25bc315d607c57-b0b9f/ang-nara-tre-dep-hon-nhien-trong-loat-anh-moi-o-tuoi-34.jpg"
title_profile = "Jang Nara"
age_profile = "36"

profiles = [
    {
        "image_profile": "http://kenh14cdn.com/k:r9LkQbF6VoiiUUdcKz6F7w8WhmMgcd/Image/2015/01/td1/TD2/365594eef01f3a296c1f79599a25bc315d607c57-b0b9f/ang-nara-tre-dep-hon-nhien-trong-loat-anh-moi-o-tuoi-34.jpg",
        "title_profile": "Jang Nara",
        "age_profile": "36"
    },
    {
        "image_profile": "http://www.allkpop.com/upload/2014/05/af_org/Kim-Tae-Hee_1401210174_af_org.jpg",
        "title_profile": "Kim Tae-Hee",
        "age_profile": "37"
    },
    {
        "image_profile": "http://file2.instiz.net/data/file2/2017/04/18/7/0/7/707bb2a82ea9e9bb1c2ea80447db7655.jpg",
        "title_profile": "Shibaaa",
        "age_profile": "5"
    },
]
##
# Routing for your application.
##

# image = "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/SS/15/tOc-GNtQvb1ryMNA1Oxensn9K2VhyG1I4SguJnR7ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC85XC8wXC82XC83XC82XC8wXC9DRklMUEQ5MDY3NjBfTlIwMDAyXzEuanBnIiwiZmEiOjEsImZmIjoxLCJmaCI6NjAxLCJmcSI6OTAsImZ0IjoxLCJmdyI6NDEwfQ~~.jpg"
# title = "bodice"
# price = "1035$"

items = [
    {
        "image": "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/pk/LW/t3DZAL5YdGhawI0vFm-TLqKSGlTQzOpCfNUpeN57ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC85XC8wXC82XC83XC82XC8zXC9DRklMUEQ5MDY3NjNfTlIwMDAyXzEwMC5qcGciLCJmYSI6MSwiZmYiOjEsImZoIjo2MDEsImZxIjo5MCwiZnQiOjEsImZ3Ijo0MTB9.jpg",
        "title": "bodice",
        "price": "234$"
    },
    {
        "image": "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/kx/VK/Grj4NVrJjagbdhpfg40LwlAhOtDfjociKGw6ktl7ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC8wXC8wXC8yXC8yXC85XC81XC9DRklMUEQwMDIyOTU1X05SMDAwMl8xMDBfMS5qcGciLCJmYSI6MSwiZmYiOjEsImZoIjo2MDEsImZxIjo5MCwiZnQiOjEsImZ3Ijo0MTB9.jpg",
        "title": "Long night dress",
        "price": "813$"
    },
    {
        "image": "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/Bc/B4/swCYODnJGzU4cfprkDL-ifgzM1NNMNZY832oUV97ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC8wXC8wXC8yXC8yXC85XC81XC9DRklMUEQwMDIyOTUwX05SMDAwMl8xMDAuanBnIiwiZmEiOjEsImZmIjoxLCJmaCI6NjAxLCJmcSI6OTAsImZ0IjoxLCJmdyI6NDEwfQ~~.jpg",
        "title": "Slip on",
        "price": "456$"
    }
]

@app.route('/') #Home page
def index():
    return render_template("profile.html", profiles = Profile.objects())

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

# @app.route('/profile/')
# def data_profile():
#     return render_template("profile.html", profiles = Profile.objects())

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False)
