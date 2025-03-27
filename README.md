# project_01

Password Manager
----------------

prerequisites
- AIM user and role
- .env file
- .gitignore

src/password_manager.py
- Hold the script, writing to the console, prompting for user input
- [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it

infrastructure deployment
- boto3 > aws Secrets Manager
- create roles and permissions
- secretsmanager:PutSecretValue permission

src/util/util_funcs
- list passwords
- retrieve passwords
- write new password_manager
- delete password

test utility functions
- test each util function

test password_manager 
- test for overall functionality

other considerations
- error handling


  to implement:
  error handling
  empty inoput mhandling
  doc strings
  update secrets - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/update_secret.html
  randomasier - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/get_random_password.html
