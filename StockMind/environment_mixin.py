import os


class EnvironmentMixin(object):
    """Mixin to another class to provide access to a User's ``Score``."""

    @property
    def is_production(self):
        """Get the latest score for the User who saved this Job."""
        if os.environ.get('DJANGO_PRODUCTION') is not None:
            return True
        return False
