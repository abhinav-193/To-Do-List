from io import BytesIO
from os import name
from flask import Blueprint, app, render_template, redirect,request, jsonify, make_response, send_file
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Pdf, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home')
@login_required
def home():
    
    
    print(current_user)
    

    
    return render_template("index.html", user=current_user)

@views.route('/about')
@login_required
def about():
    

    
    return render_template("about.html", user=current_user)

@views.route('/contacts')
@login_required
def contact():
    

    
    return render_template("cntct.html", user=current_user)

@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        pdf_url = request.files.get('pdf')
        description= request.form.get('description')
        branch = request.form.get('BRANCH')
        

        new_upload = Pdf(data= pdf_url.read() , user_id= current_user.id ,description=description, branch = branch, name= pdf_url.filename)
        db.session.add(new_upload)
        db.session.commit()
    

    
    return render_template("upload.html", user=current_user)

@views.route('/download')
@login_required
def download():

    pdf= Pdf.query.all()
    print(len(pdf))
    

    
    return render_template("download.html", user=current_user, pdfs= Pdf.query.all(), user_list= User.query.all())


@views.route('/downloads/<int:id>', methods=['GET'])
@login_required
def download_file(id):
    pdf = Pdf.query.filter_by(id=id).first()
    pdf.no_of_upvotes +=1
    db.session.commit()
    return send_file(BytesIO(pdf.data), as_attachment=True, attachment_filename=pdf.name)
    

    
from models import Config
from sawo import getContext

def login(request):
    config = Config.objects.order_by('-api_key')[:1]
    context = {
        "sawo" = getContext(config,<route>) #the route where you will recieve
                the payload sent by sdk    
    }
