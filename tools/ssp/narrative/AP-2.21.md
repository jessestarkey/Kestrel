Every pipeline job will run on a fresh GitLab Runner pod in Platform Prod's AKS cluster, isolated from other jobs and destroyed when it ends. No build runs on a performer laptop or a long-lived host.
