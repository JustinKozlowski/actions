# CICD_Examples

The following folders can be used for 
testing out GitHub Actions Cicd Pipelines as well as basic
DevOps Practices

To use this repository, simply uncomment sections of the
`.github-actions.yml` file in the `/.github/workflows` directory.

### `/hello_world`
This folder contains the simplest .github-actions.yml to run a
pipeline with GitHubActions. It will echo hello world

### `/unit_test`
Often Continuous Integration is maintained by unit testing.
This folder contains a simple python program that is
unit tested by the pipeline. If the testing fails, the 
pipeline fails

### `/simple_package`
For Continuous Deployment, we can use a pipeline to push our
code to a remote repository that others can pull from. This
example pushes our python code to PyPi. We
also use this example to show other coding standards that pipelines
can check such as linting and testing coverage.

### `/`
For Continuous Deployment, we can use a pipeline to push our code
to a server. For UB students, you don't often have to deploy to a server, 
but you do have to submit assignments often. The `action.yml` will 
automatically submit your code to autolab based on your commit message.
You can utilize this by using the `example.yml` file in your own 
repository under `/.github/workflows`. It requires you to set the
`UBITUsername` and `UBITPassword` secrets within the repository though.


PSA: This project was ported from a version I made from GitLab,
so I may have missed some READMEs which may reference old Repo structure
or GitLab functionality.