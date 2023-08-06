from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from $package_name.processing import preprocessors as pp
from $package_name.config import config, logging_config

_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(config.LOGS_DIR / f"{__name__}.txt")
formatter = logging_config.FORMATTER
file_handler.setFormatter(formatter)
_logger.addHandler(file_handler)


pipe = Pipeline(
    [
        (
            "first_step",
            pp.CategoricalImputer(variables=config.VARIABLES),
        ),
        (
            "last_step",
            DummyClassifier(strategy="most_frequent")
        )
    ]
)