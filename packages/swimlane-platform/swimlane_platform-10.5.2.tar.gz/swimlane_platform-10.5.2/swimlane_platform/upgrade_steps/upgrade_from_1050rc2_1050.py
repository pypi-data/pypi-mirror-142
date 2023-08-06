from swimlane_platform.lib import names
from swimlane_platform.lib.debug_decorators import info_function_start_finish, debug_function_args
from swimlane_platform.shared_steps import enable_turbine
from swimlane_platform.upgrade_steps.upgrade_step import UpgradeStep
import semver


class UpgradeFrom1050rc2To1050(UpgradeStep):
    FROM = semver.parse_version_info('10.5.0-rc2')  # type: semver.VersionInfo
    TO = semver.parse_version_info('10.5.0')  # type: semver.VersionInfo

    @info_function_start_finish('Upgrade From 10.5.0-rc2 To 10.5.0')
    def process(self):
        # type: () -> None
        enable_turbine.run(self.config)
        self.upgrade_image_versions(names.INSTALL_DIR, self.config.args.dev)

    @debug_function_args
    def upgrade_image_versions(self, install_dir, dev):
        # type: (str, bool) -> None
        """
        Updates image versions

        :param dev: If the images will be pulled from development repository.
        :param install_dir: Root folder for installation. Where docker-compose resides.
        """
        docker_compose = self.upgrade_standard_images(self.config.args.dev, names.INSTALL_DIR)
        docker_compose.set('mongo:4.4.11', 'services', names.SW_MONGO, 'image')
        docker_compose.save()

