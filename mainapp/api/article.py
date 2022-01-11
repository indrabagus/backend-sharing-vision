from flask import Blueprint,jsonify,request,url_for
from mainapp import db,api_url_prefix
from mainapp.models import Article
from mainapp.errors import bad_request

article_bp = Blueprint(
  'article',
  __name__,
  static_folder = 'statics',
  template_folder = 'template',
  url_prefix=api_url_prefix+'article'
)

class PaginationTool(object):
  @staticmethod
  def collection_to_dict(query,offset,limit,endpoint,itemfunc=None,**kwargs):
    resources = query.paginate(offset,limit,False)
    data = {
      'items' : [
        itemfunc(item) if itemfunc else item.to_dict() for item in resources.items
      ],
      'meta' : {
          'offset':offset,
          'limit':limit,
          'total_offset':resources.pages,
          'total_items':resources.total
      },
      'link': {
          'self': url_for(endpoint, offset=offset,limit=limit,**kwargs),
          'next': url_for(endpoint, offset=offset+1, limit=limit,
                          **kwargs) if resources.has_next else None,
          'prev':url_for(endpoint,offset=offset-1,limit=limit,
                          **kwargs) if resources.has_prev else None,
      }
    }
    return data

    

@article_bp.route('/',methods=['POST'])
def create_article():
    data = request.get_json() or {}
    if 'title' not in data or 'content' not in data or 'category' not in data or 'status' not in data :
        return bad_request("Should have 'content' and 'category' and 'status' element in JSON data input")
    article = Article()
    article.from_dict(data)
    db.session.add(article)
    db.session.commit()
    resp = jsonify(article.to_dict())
    resp.status_code=201
    resp.headers['Location'] = url_for('article.article_by_id',id=article.id)
    return resp


@article_bp.route('/<int:id>',methods=['GET'])
def article_by_id(id=-1):
    if id == -1:
        return bad_request("Unknown Article ID")
    article = Article.query.get_or_404(id)
    return jsonify(article.to_dict())


@article_bp.route('/<int:limit>/<int:offset>',methods=['GET'])
def article_pagination(limit,offset):
    data = PaginationTool.collection_to_dict(Article.query,offset,limit,'article.article_pagination')
    return jsonify(data)


@article_bp.route('/<int:id>',methods=['POST'])
def article_change(id=-1):
    if id == -1:
        return bad_request("Unknown Article ID")
    data = request.get_json() or {}
    if 'title' not in data or 'content' not in data or 'category' not in data or 'status' not in data :
        return bad_request("Should have 'content' and 'category' and 'status' element in JSON data input")
    article = Article.query.get_or_404(id)
    article.update_from_dict(data)
    db.session.commit()
    resp = jsonify(article.to_dict())
    resp.status_code=201
    return resp



@article_bp.route('/<int:id>',methods=['DELETE'])
def article_delete(id=-1):
    if id == -1:
        return bad_request("Unknown Article ID")
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({"status":"Success"})

