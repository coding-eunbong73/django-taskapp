#### create project with pycharm default (with virtual environment)
    input the name of the project


#### how to activate/deactivate virtual environment 
    venv/scripts/activate | deactivate

#### django install in virtual environment 
    pip install django
    pip install django-crispy-forms

#### project create
    django-admin startproject taskproject
    cd taskproject
    python manage.py startapp taskapp
    
#### setting ( taskproject.settings.py )
    taskapp 등록   (INSTALLED_APPS)
    static-url 설정 ( STATICFILES_DIRS = [ BASE_DIR / "static"] )
    static 디렉토리 생성 ( taskapp 하위에 static, templates, templates/page, templates/common,  생성 )
    static/styles.css 파일 생성
    url.py에 미디어파일 처리설정 
        from django.conf.urls.static import static, 
        urlpattern + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### model 정의 (models.py)
    python manage.py makemigrations
    python manage.py migrate

#### 관련 library
    pip install django-crispy-forms
    taskproject.settings.py, crispy-forms등록 (INSTALLED_APPS)  [ https://django-crispy-forms.readthedocs.io/en/latest/install.html]
    taskproject.settings.py, CRISPY_TEMPLATE_PACK = 'bootstrap4'
    flatpickr css,js template setting

#### 실행
    python manage.py runserver

    
    