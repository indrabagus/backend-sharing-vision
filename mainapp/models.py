from mainapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200))
  content = db.Column(db.Text)
  category = db.Column(db.String(128))
  created_date = db.Column(db.DateTime,default=datetime.utcnow)
  updated_date = db.Column(db.DateTime,default=datetime.utcnow)
  status = db.Column(db.Enum('publish','draft','thrash'),nullable=False,server_default="draft")

  def __repr__(self):
    return '< Article {} >'.format(self.title)

  def from_dict(self,data):
    for field in ['title','content','category','status']:
      setattr(self,field,data[field])

  def update_from_dict(self,data):
    self.from_dict(data)
    self.updated_date = datetime.utcnow()


  def to_dict(self):
    data = {
      'id' : self.id,
      'title':self.title,
      'content':self.content,
      'category':self.category,
      'created_date':str(self.created_date),
      'updated_date':str(self.updated_date),
      'status':self.status
    }
    return data