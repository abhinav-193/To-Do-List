from flask import Flask, render_template, url_for
from website import create_app
from sawo import createTemplate, getContext, verifyToken

app = create_app()




if __name__== "__main__":
    app.run(debug=True)