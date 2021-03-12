# Ansible Role: Raspberry - sshd

[![CI](https://github.com/escalate/ansible-raspberry-sshd/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/escalate/ansible-raspberry-sshd/actions/workflows/ci.yml)

An Ansible role that manages [OpenSSH - sshd](https://www.openssh.com) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.raspberry-sshd
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-sshd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.raspberry-sshd
      tags: sshd
```

## License

MIT
