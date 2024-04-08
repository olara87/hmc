import os

DO_STORAGES_ACCESS_KEY_ID=os.environ.get("DO_STORAGES_ACCESS_KEY_ID")
DO_STORAGES_SECRET_ACCESS_KEY=os.environ.get("DO_STORAGES_SECRET_ACCESS_KEY")
DO_STORAGES_STORAGE_BUCKET_NAME='django-k8s'
DO_STORAGES_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com"
DO_STORAGES_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
DO_STORAGES_LOCATION="https://django-k8s.nyc3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "django_k8s.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'django_k8s.cdn.backends.StaticRootS3BotoStorage'