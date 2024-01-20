## README
> [!IMPORTANT] Was running into HTTP 500 issues when it came to validating emails, but that should be resolved with [this commit](https://github.com/sandau-dev/cvat/commit/3070fb0afa650f1e33e74475279b2d22423fb79d). However, issues may still arise when creating users using the `provision_users.py` script.

Make sure that a `users.csv` exists in the `scripts` directory. Ensure there is an entry in `users.csv` for all users that are going to be added. The `users.csv` file follows this format:

| username   | email             | password1 | password2 | first_name | last_name | groups  | is_staff | is_superuser | is_active | organization | org_role |
|------------|-------------------|-----------|-----------|------------|-----------|---------|----------|--------------|-----------|--------------|----------|
| myusername | myemail@email.com | abc123    | abc123    | Jane       | Doe       | mygroup | True     | False        | True      | myorg        | worker   |

> [!NOTE] The current `users.csv` can be found [here](https://sandaudev-my.sharepoint.com/:x:/r/personal/matt_sandau_dev/Documents/Customer/asBuilt/users.csv?d=w0db64c0dc85f444c9d158fe3dbfcc248&csf=1&web=1&e=sqzWvk) (you will most likely need to request access)

Install the CVAT SDK Python package
```shell
pip install cvat-sdk
```

Set up the environment variables. Examples below:
```bash
export CVAT_HOST="https://cvat-instance.sandau.dev"
export CVAT_ADMIN_USERNAME="supadupauser"
export CVAT_ADMIN_PASSWORD="noonewouldeverguessthis"
export CVAT_ORGANIZATION="mycustomersorg"  # This would be organization that is set up for the customer within CVAT
```

Run the provisioner
```shell
python3 provision_users.py
```
