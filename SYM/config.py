# Constants (User configurable)

FULL_NAME_AND_EMAIL = 'Mohamed Abuaita <mabuaita@yahoo.com>'  # For Dockerfile/POV-Ray builds.
APP_NAME = 's3syncsym'  # Used to generate derivative names unique to the application.

DOCKERHUB_USER = 'mabuaita'
DOCKERHUB_EMAIL = 'mabuaita@yahoo.com'
DOCKERHUB_REPO = 'ci'
DOCKERHUB_TAG = DOCKERHUB_USER + '/' + DOCKERHUB_REPO + ':' + APP_NAME

AWS_REGION = 'us-west-2'
AWS_PROFILE = 'default'  # The same profile used by your AWS CLI installation

SSH_KEY_NAME = 'mddx-prod-20180328.pem'  # Expected to be in ~/.ssh
ECS_CLUSTER = 'ecsS3Sync'
