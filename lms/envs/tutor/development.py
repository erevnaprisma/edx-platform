# -*- coding: utf-8 -*-
import os
from lms.envs.devstack import *

####### Settings common to LMS and CMS
import json
import os

DEFAULT_FROM_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
SERVER_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
TECH_SUPPORT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
CONTACT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
BUGS_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
UNIVERSITY_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
PRESS_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
BULK_EMAIL_DEFAULT_FROM_EMAIL = "no-reply@" + ENV_TOKENS["LMS_BASE"]
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]
API_ACCESS_FROM_EMAIL = ENV_TOKENS["CONTACT_EMAIL"]

# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)
DATA_DIR = "/openedx/data/"
for store in MODULESTORE["default"]["OPTIONS"]["stores"]:
   store["OPTIONS"]["fs_root"] = DATA_DIR

# Get rid completely of coursewarehistoryextended, as we do not use the CSMH database
INSTALLED_APPS.remove("coursewarehistoryextended")
DATABASE_ROUTERS.remove(
    "openedx.core.lib.django_courseware_routers.StudentModuleHistoryExtendedRouter"
)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]
# Disable django/drf deprecation warnings
import logging
import warnings
from django.utils.deprecation import RemovedInDjango30Warning, RemovedInDjango31Warning
from rest_framework import RemovedInDRF310Warning, RemovedInDRF311Warning
warnings.simplefilter('ignore', RemovedInDjango30Warning)
warnings.simplefilter('ignore', RemovedInDjango31Warning)
warnings.simplefilter('ignore', RemovedInDRF310Warning)
warnings.simplefilter('ignore', RemovedInDRF311Warning)

# Email
EMAIL_USE_SSL = False
# Forward all emails from edX's Automated Communication Engine (ACE) to django.
ACE_ENABLED_CHANNELS = ["django_email"]
ACE_CHANNEL_DEFAULT_EMAIL = "django_email"
ACE_CHANNEL_TRANSACTIONAL_EMAIL = "django_email"
EMAIL_FILE_PATH = "/tmp/openedx/emails"

LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")

# Allow the platform to include itself in an iframe
X_FRAME_OPTIONS = "SAMEORIGIN"


JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "HkCtEFJ4oFrjIqd57KhoeBjT"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "OgmoquIJIVfI0Ue8SGEsOoX8VWam0PQSp4YkoY_yfF5BAsoNyNSYPAEdTk2I9YtLHuA7TOLYHdJE9W1GSJK2R1cC3aTgpPLAlhoxOLCR_M94MmzrxBD5crmfdoVhymtQMhU676OEzkLKmwNyUHxsAiCE2K4d9D8j7ryNzjKJer-UlWIioHrOSC_raQCNvl-hKIpmQV9DcCDN0NeGQGp7nnrnRo9coQJN1nKdGegcFZuuiPjiWYReUKn-fPlcO6E9QMbLCMbzmwdnmHpBCpawFL1I7egHhWoGf7Juyj36usJKxyhjYCuj_iftkMztvQgBIq6Ipy7ETppND2lXS1_WEQ",
        "n": "zk8krBQwkBaw7g-IJFg8pcu7paWYM04tRmdS-4s5P1I6bkePWGhEYWlf2bcpCikm5w9Bc3Bo-84UHamkXhL-SS48EFqCesf1Z0Gl7-BEZDCyUO0jow-NTTYX9FkQ4AQle4KvAtFw70TyU7dltBIHvemPh7y4POOkL_ee5S9WjyrYr-d-2o2MLzBOCpJzDUvE19MUCytmLZ06nt0iLMMYuyUzi42OdrgWksSYxOXSe-ms_5hWR0LNwlyj_tTqIej_9mTJS3mQR0z9tgOAgSSRlCxoMDWSi9uu8duIqVRRybmJVvBHv4i8Tzh0_NtDmbGCAm6AoITs5p4Fo5USQc-W4w",
        "p": "0V5ATd0luEhdue51YMyFbIyYLDojuH1YKwQ2hxwpH-SFr6ZVFiePvUfgrPkbuCyTUErpw4Vr6xGshWOZpj74AKNnv9zMaTxWak5x9ueHI1VS1_UUD1WXlqY8mUE6tSkzecxfW8kuv5ZwxWhJVmewCtKm_lIcctTO7kq5kqlY17M",
        "q": "_EJ5I9TuJwU1S9DpAtrif09MOTzA4QLH7rwvvpsJX_kym5IX1-YWQ9tVu566ZDZja2Fwge-vsGdFYvVLgiKkOd9F4f8dEHccOX9iXHs3Z5MUxpjUsSjtpuV5HkLFp08CMIp1q8TSW7qtLqvQfnrYfnziFpDRDjyRXi5XZVePrBE",
    }
)
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "zk8krBQwkBaw7g-IJFg8pcu7paWYM04tRmdS-4s5P1I6bkePWGhEYWlf2bcpCikm5w9Bc3Bo-84UHamkXhL-SS48EFqCesf1Z0Gl7-BEZDCyUO0jow-NTTYX9FkQ4AQle4KvAtFw70TyU7dltBIHvemPh7y4POOkL_ee5S9WjyrYr-d-2o2MLzBOCpJzDUvE19MUCytmLZ06nt0iLMMYuyUzi42OdrgWksSYxOXSe-ms_5hWR0LNwlyj_tTqIej_9mTJS3mQR0z9tgOAgSSRlCxoMDWSi9uu8duIqVRRybmJVvBHv4i8Tzh0_NtDmbGCAm6AoITs5p4Fo5USQc-W4w",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "HkCtEFJ4oFrjIqd57KhoeBjT"
    }
]

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT.lstrip("/")
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT.lstrip("/")

# Ora2 setting
ORA2_FILEUPLOAD_BACKEND = "s3"
FILE_UPLOAD_STORAGE_BUCKET_NAME = "openedxuploads"

AWS_S3_SIGNATURE_VERSION = "s3v4"
# Note that this might not work with runserver, where nginx is not running
AWS_S3_ENDPOINT_URL = "http://minio.local.overhang.io"
AWS_AUTO_CREATE_BUCKET = False # explicit is better than implicit
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_EXPIRE = 7 * 24 * 60 * 60  # 1 week: this is necessary to generate valid download urls
######## End of settings common to LMS and CMS

######## Common LMS settings
LOGIN_REDIRECT_WHITELIST = ["studio.local.overhang.io"]

# This url must not be None and should not be used anywhere
LEARNING_MICROFRONTEND_URL = "http://learn.openedx.org"

# Fix media files paths
PROFILE_IMAGE_BACKEND["options"]["location"] = os.path.join(
    MEDIA_ROOT, "profile-images/"
)

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

COURSE_CATALOG_VISIBILITY_PERMISSION = "see_in_catalog"
COURSE_ABOUT_VISIBILITY_PERMISSION = "see_about_page"

# Allow insecure oauth2 for local interaction with local containers
OAUTH_ENFORCE_SECURE = False

# Create folders if necessary
for folder in [DATA_DIR, LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE, ORA2_FILEUPLOAD_ROOT]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common LMS settings

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

SESSION_COOKIE_DOMAIN = ".local.overhang.io"

CMS_BASE = "studio.local.overhang.io:8001"
CMS_ROOT_URL = "http://{}".format(CMS_BASE)
LOGIN_REDIRECT_WHITELIST.append(CMS_BASE)

FEATURES['ENABLE_COURSEWARE_MICROFRONTEND'] = False

LOGGING["loggers"]["oauth2_provider"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}


