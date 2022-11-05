# CICD_Examples

The following folders can be used for 
testing out GitHub Actions Cicd Pipelines as well as basic
DevOps Practices

To use this repository, simply uncomment sections of the
`.github-actions.yml` file in the `/.github/workflows` directory.

## `simple_package`
This folder contains a simple package that we need to automatically
submit to AutoLab. We will use this python package to run through 
the basics of CI/CD and DevOps.

## `/actions_examples`

### `/pytest`
Often Continuous Integration is maintained by unit testing.
This folder contains a simple python program that is
unit tested by the pipeline. If the testing fails, the 
pipeline fails

### `/pylint`
This action scans our code with a linting tool to make sure our code
follows coding guidelines.

### `/coverage`
This action builds on top of unit testing to also include code
coverage.

### `/twine`
For Continuous Deployment, we can use an action to push our
code to a remote repository that others can pull from. This
example pushes our python code to PyPi.

### `/`
For Continuous Deployment, we can use a pipeline to push our code
to a server. For UB students, you don't often have to deploy to a server, 
but you do have to submit assignments often. The `action.yml` in
https://github.com/JustinKozlowski/AutoLabAutoSubmit will 
automatically submit your code to autolab based on your commit message.
You can utilize this by using the `example.yml` file in your own 
repository under `/.github/workflows`. It requires you to set the
`UBITUsername` and `UBITPassword` secrets within the repository though.


PSA: This project was ported from a version I made from GitLab,
so I may have missed some sections which may reference old Repo structure
or GitLab functionality.