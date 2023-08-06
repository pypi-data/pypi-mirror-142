DEBUG = True
SECRET_KEY = "testkeytestkey"
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "tuhls.core",
    "tuhls.invoice",
    "example",
]
AUTH_USER_MODEL = "example.User"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
