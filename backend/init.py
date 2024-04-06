import config.init_config as config
import utils.database_utils as dbUtils
from services.notes_services import init_notes


def init():
    # Init config file
    config.init_config()

    # Init Database
    dbUtils.setup()

    # Init notes service
    init_notes()
