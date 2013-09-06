from flask import Flask, render_template, redirect, url_for
import random
from iamjeremiah import app
import pymongo
from iamjeremiah import utils
@app.route('/')
def home():
  pic = random.randrange(7)
  return render_template('home.html', pic=pic)
@app.route('/about')
def about_me():
  pic = random.randrange(7)
  return render_template('about_me.html', pic=pic)
@app.route('/blog')
def blog():
  pic = random.randrange(7)
  title_list = utils.post_listing_all()
  return render_template('linux.html', pic=pic, title_list=title_list)
@app.route('/blog/<post_name>')
def linux_post(post_name):
  if post_name == 'blog':
    return redirect(url_for('blog'))
  pic = random.randrange(7)
  title_list = utils.check_if_empty(post_name)
  if title_list:
    return render_template('linux_post.html', pic=pic, title_list=title_list)
  else:
    return render_template('page_not_found.html'), 404
