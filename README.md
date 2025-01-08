# Infactory - Development

This repository contains the back-end execution and query environment for the Infactory platform.

![Latest_Release](https://img.shields.io/github/v/release/infactory-io/dev)
![Tests](https://github.com/infactory-io/dev/actions/workflows/tests.yml/badge.svg)
![Coverage](./docs/images/coverage.svg)
[![Language](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](/#)

## Running Locally

### Using Docker

First, ensure your environment is setup (take a look at the `Contributing: Environment Setup` below):

```bash
# create the multi-platform build environment / driver
docker buildx create --name multiarch --use
docker buildx inspect --bootstrap

# build it
docker compose build --builder multiarch --push
```

Then:

```bash
docker compose up
```

### Using Minikube (Kubernetes)

The Infactory framework leverages [Kubernetes](https://kubernetes.io) to deploy, scale and manage micro services, databases and other containerized applications within the framework. To leverage Kubernetes and run the framework locally, please install both [kubectl](https://kubernetes.io/docs/reference/kubectl/) and [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download) (which runs in Docker).

If you're on a Mac, you can install `kubectl` and `minikube` via Homebrew:

```bash
brew install kubectl
brew install minikube
```

Some folks on Macs report having issues installing the ARM tailored versions using `homebrew`. If that's what you run into, check out [these instructions](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/).

Now, do this:

```bash
cd deploy
chmod u+x ship_it.sh
sh ship_it.sh
```

If you're on the `dev` branch or another branch, this script will deploy the Infactory framework to your local Minikube Kubernetes cluster. If on `staging` or `main`, the deployments will be pushed to the AWS Kubernetes cluster running in EKS, either on the `staging` or `prod` namespaces (respectively).

#### More Info

Minikube will start a local Kubernetes server to deploy the Infactory framework and is essentially a mini Kubernetes cluster running on your local environment - very useful. To get going:

```bash
minikube config set driver docker # first time only, make sure you have Docker installed. You can confirm using `minikube config view`
minikube start
minikube addons enable ingress
kubectl config use-context minikube
kubectl config set-context --current --namespace=dev
kubectl cluster-info
>>>
Kubernetes control plane is running at https://127.0.0.1:57094
CoreDNS is running at https://127.0.0.1:57094/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

To stop the Minikube and any containers within the Minikube Kubernetes environment, simply `minikube stop`. You can then delete all Kubernetes clusters in Minikube by executing `minikube delete --all`.

The Minikube and Infactory Kubernetes environments are managed using [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), which we use the same naming scheme and deployment structure as the cloud environments managed by Terraform: `dev`, `staging` and `prod`. To set and see the existing workspace set:

```bash
kubectl config set-context --current --namespace=<insert-namespace-name-here> # set the new namespace, e.g. dev, staging or prod
kubectl config view --minify | grep namespace: # validate new workspace
```

Note that while minikube is running, the Kubernetes `context` is set to Minikube.

## Contributing

Please use the Linear issue tracker to report any erroneous behavior in need of fixes or desired feature requests.

If you would like to contribute to development, branch off of `dev` and make contributions to a branch which corresponds to an open issue in [Linear](https://linear.app/infactoryio/team/TECH/all). In the Linear user interface, copy the git branch name, e.g. `tech-103-create-readme`:

![linear_copy_git_branch_name](/docs/images/linear_copy_git_branch_name.png)

When integrating fixes and features, open a pull request so that code contributions can be reviewed, tested, and documented using both human reviewers (developers and engineers) and automated checks (continuous integration).

### Commit Messages and Releases

Your commit messages are important - here's why.

Infactory leverages [release-please](https://github.com/googleapis/release-please-action) to help automate the release process using the [Conventional Commits](https://www.conventionalcommits.org/) specification. When pull requests are opened to the `main` branch, release-please will collate the git commit messages and prepare an organized changelog and release notes. This process can be completed because of the Conventional Commits specification.

Conventional Commits provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with SemVer, by describing the features, fixes, and breaking changes made in commit messages. You can check out examples [here](https://www.conventionalcommits.org/en/v1.0.0/#examples). Make a best effort to use the specification when contributing to Infactory code as it dramatically eases the documentation around releases and their features, breaking changes, bug fixes and documentation updates.

### Environment Setup

1. First, install, setup and ensure the [Docker](https://www.docker.com/) engine is running on your local machine.
The Infactory platform runs as a containerized unit.
2. Python is used as part of the build process for the Docker container(s), so ensure Python is installed on your machine (versions 3.8 - 3.12).
3. Create an ssh key to use for pulling Infactory code: `ssh-keygen -t rsa -b 4096 -f ~/.ssh/infactory-A`. Then `cd ~/.ssh`.
4. `chmod 600 infactory-A`
5. `chmod 644 infactory-A.pub`
6. Create the config file `vim config`:

    ```bash
    Host *
    AddKeysToAgent yes
    UseKeychain yes # remove this line if on Linux and not on MacOS
    IdentityFile ~/.ssh/infactory-A
    ```

7. Copy the contents of `cat infactory-A.pub` into Github under >> `Settings` >> `SSH and GPG keys` >> `New SSH key`.

8. Setup and activate the Python virtual environment: `python3 -m venv venv` and `source venv/bin/activate`
9. Install the project requirements by navigating to `py/infactory` and running `pip install .`.
10. Git LFS should be installed per the instructions [here](https://git-lfs.com/).

### Tests

When contributing, please ensure to run unit tests and add additional tests as necessary if adding new functionality. To run the tests and obtain test code coverage statistics, run the following from the root directory:

```bash
pytest --cov=infactory --cov=infactory_api -s -v
coveralls # to submit the report to https://coveralls.io/github/infactory-io/dev
```

You may need to install the Infactory framework in your virtual environment before running the tests along with Poetry:

```bash
poetry install
poetry run pytest --cov=infactory --cov=infactory_api -s -v
```

In addition to being able to execute the tests locally using the above command, Github workflows are executed on the `main` and `dev` branches to ensure that the unit tests pass successfully. See the [coveralls.io](https://coveralls.io/github/infactory-io/dev?branch=main) report to see an interactive unit test code coverage report.

### Versioning

[Semantic versioning](http://semver.org/) is used for this project. If contributing, please conform to semantic
versioning guidelines. Future versioning may be handled by tools such as [release-please](https://github.com/googleapis/release-please-action).

## Deploying

See `deploy/readme.md`.
