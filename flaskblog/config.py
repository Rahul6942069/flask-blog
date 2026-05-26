import os

class Config:
	SECRET_KEY='e1d1d9db5ef47d80cd3dbd203a57fd0f'
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	MAIL_SERVER='smtp.googlemail.com'
	MAIL_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=os.environ.get('EMAIL_USER')
	MAIL_PASSWORD=os.environ.get('EMAIL_PASS')