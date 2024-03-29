import environ

env = environ.Env(
    SECRET_KEY=(str, 'secret_key'),
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(str, '*'),
    POSTGRES_DB=(str, 'postgres_db'),
    POSTGRES_USER=(str, 'postgres_db'),
    POSTGRES_PASSWORD=(str, 'postgres_db'),
    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_PORT=(int, None),
)