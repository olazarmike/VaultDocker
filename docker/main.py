import hvac

client = hvac.Client(url='https://localhost:8200')
client.is_authenticated()

# Authenticate to Vault using client.auth.x

# Not all these settings may apply to your setup, refer to Vault
# documentation for context of what to use here

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