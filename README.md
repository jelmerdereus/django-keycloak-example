# STATUS: starting project, not usable yet

## TODO

- create templates for Django to display roles / claims
- automate Keycloak default config with realm and role and example user
- create a Docker Compose setup that just sets up everything
- update README

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
- Go to 'clients' and choose a type OpenID Connect with a name 'django-keycloak'
- Enable 'client authentication' and 'authorization'
- valid redirect URL and post logout url: '*'
- web origins: http://localhost:8000
- Save and go to the 'credentials' tab. Copy the client secret into the .env file at 'DJANGO_KC_SECRET'
- Go to 'realm roles' and create roles: 'django_generic_access' and 'django_special_test'
- Go to 'Groups' and create a group 'django_special_group' and add the roles
- Go to 'users' and create a user with this group assigned, and set an initial password
- Go to the client 'django-keycloak' and open the scope 'django-keycloak-dedicated'
- Add a mapper from the predefined mappers: 'realm roles'
- Open the mapper and enable 'Add to userinfo'
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
KC_REALM=
KC_CLIENT_ID=django-client
KC_CLIENT_SECRET=
```