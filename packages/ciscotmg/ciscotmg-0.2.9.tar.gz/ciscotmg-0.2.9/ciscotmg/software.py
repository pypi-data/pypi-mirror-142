from pip._internal import main as pip
from .meta import Meta


class Software:
    """Manage pypi package"""

    @staticmethod
    def upgrade(version, local=False) -> bool:
        """Upgrade using pip"""
        try:
            if local:
                pip(["install", "-e", "."])
            else:
                pip(["install", f"{Meta.__title__}=={version}"])

        except Exception as error_msg:
            raise Exception(error_msg)

        return True
