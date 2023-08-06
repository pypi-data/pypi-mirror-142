from ..exceptions import ProviderBadConfigurationException


class BaseProvider:
    REQUIRED_PARAMS = []

    @classmethod
    def validate_params(cls, params):
        param_keys = list(params.keys())
        for required_param in cls.REQUIRED_PARAMS:
            if required_param not in param_keys:
                raise ProviderBadConfigurationException(missing_param=required_param)

    def get_object(self, key):
        raise NotImplementedError

    def upload_object(self, key, path):
        raise NotImplementedError
