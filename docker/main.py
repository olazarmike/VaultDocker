import hvac
import os

client = hvac.Client()
client = hvac.Client(
    url='https://localhost:8200',
    token=os.environ['VAULT_TOKEN']
)
client.is_authenticated()

#crear una tabla
config_response = client.secrets.activedirectory.configure(
    binddn='username@domain.fqdn', # A upn or DN can be used for this value, Vault resolves the user to a dn silently
    bindpass='***********',
    url='ldaps://domain.fqdn',
    userdn='CN=Users,DN=domain,DN=fqdn',
    upndomain='domain.fqdn',
    ttl=60,
    max_ttl=120
)


#crear rol
role_response = client.secrets.activedirectory.create_or_update_role(
    name='sql-service-account',
    service_account_name='svc-sqldb-petshop@domain.fqdn',
    ttl=60)

#lista de todos los roles
all_roles = client.secrets.activedirectory.list_roles()
print(config_response)