
def create_module(app,**kwargs):
    from .about import about_bp
    from .article import article_bp
    app.register_blueprint(about_bp)
    app.register_blueprint(article_bp)