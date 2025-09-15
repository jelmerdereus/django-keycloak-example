## Django Keycloak tryout project
This project uses Django and Keycloak to authenticate users and implements a simple setup to extend for small projects.

### Components
- Django
- Keycloak
- Postgres

### Requirements
- Python 3.13
- Docker
- Docker Compose

### Run

#### Start Keycloak, Docker and Django
```bash
docker-compose up -d
```

#### Create a realm, user and django role
- Go to http://localhost:8080/admin/
- Create a realm in 'manage realms'
- Go to 'identity providers' and create a 'Keycloak OpenID Connect provider'
- The example endpoint is 'http://localhost:8080/realms/jaylabs/broker/keycloak-oidc/endpoint'
- Create a user
- Create a role 'django_general_user'

<br/>

### Environment variables
You can create the following environment variables in a `.env` file or in Kubernetes Configmaps or Secrets.
```
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=
DJANGO_SETTINGS_MODULE=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
KC_HOSTNAME=
KC_HOSTNAME_PORT=
KC_HOSTNAME_STRICT_BACKCHANNEL=
KEYCLOAK_ADMIN=
KEYCLOAK_ADMIN_PASSWORD=
KC_HEALTH_ENABLED=
KC_LOG_LEVEL=
KC_REALM=jaylabs
KC_CLIENT_ID=django-client
KC_CLIENT_SECRET=Qrmaem4FxlC1OpVY1GlbwM9rOwkWTtSd
KC_CLIENT_SCOPE=openid profile email
```