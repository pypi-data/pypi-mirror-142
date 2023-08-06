from logging.config import dictConfig
from raft import Collection, Program
from .versioning import version
from . import sewer


dictConfig(dict(
    version=1,
    loggers={
        'sewer': {
            'level': 'DEBUG',
        }
    }
))
ns = Collection.from_module(sewer)
program = Program(version=version, namespace=ns)
