from django_dashboard.utils.version import get_version

# major.minor.patch.release.number
# release must be one of alpha, beta, rc, or final
VERSION = (1, 12, 0, "rc", 12)

__version__ = get_version(VERSION)
