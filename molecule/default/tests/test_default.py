"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize(
    "config",
    [
        # https://complianceascode.github.io/content-pages/guides/ssg-debian12-guide-cis_level1_server.html
        ("LogLevel INFO"),
        ("LoginGraceTime 60"),
        ("PermitRootLogin no"),
        ("MaxAuthTries 4"),
        ("MaxSessions 10"),
        ("HostbasedAuthentication no"),
        ("IgnoreRhosts yes"),
        ("PermitEmptyPasswords no"),
        ("UsePAM yes"),
        ("X11Forwarding no"),
        ("PermitUserEnvironment no"),
        ("ClientAliveInterval 300"),
        ("ClientAliveCountMax 0"),
        ("MaxStartups 10:30:60"),
        ("AllowGroups operator"),
        # https://complianceascode.github.io/content-pages/guides/ssg-debian12-guide-cis_level2_server.html
        ("GSSAPIAuthentication no"),
        # Public key authentication only
        ("PubkeyAuthentication yes"),
        ("PasswordAuthentication no"),
    ],
)
def test_sshd_config(host, config):
    """Check sshd config file"""
    f = host.file("/etc/ssh/sshd_config")
    assert config in f.content_string


def test_sshd_service(host):
    """Check sshd service"""
    s = host.service("sshd")
    assert s.is_running
    assert s.is_enabled
