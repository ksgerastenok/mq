# MQ
This repository contains:
- Ansible playbook for IBM MQ deploy.
- Scripts for creation and initial setup MQ Queue Manager.

Ansible module has features:
- Creates dump of MQ Queue Manager.
- Compares configuration to be deployed with created dump.
- Only differences will be deployed, so the current configuration (such as IP-addresses on different types of MQ Channels) will not be overwritten.
