from .types import EventType, ErrorType, BaseConsumerError


class BaseConsumerMethodList:
    """
    Safe methods list that prevents user from calling dunder methods.
    Also, you can mark hidden methods using '__'
    """
    def __init__(self, consumer):
        self.consumer = consumer
        self.allowed_methods = {
            attr_name
            for attr_name in dir(self)
            if (callable(getattr(self, attr_name))
                and not attr_name.startswith('__'))
        }

    async def __call_method__(self, method_name, kwargs: dict = {}, args: list = []):
        if method_name not in self.allowed_methods:
            raise BaseConsumerError(
                f'You do not have permissions to execute this method ({method_name})',
                ErrorType.ACCESS_ERROR
            )
        return await getattr(self, method_name)(*args, **kwargs)


class UserReturnMethodListMixin(BaseConsumerMethodList):
    async def user_return__(self, data=None, *args, **kwargs):
        """Just send given data to the user"""
        try:
            await self.consumer.send_json(data)
        except KeyError as e:
            await self.consumer.send_error("no data for the user_return")

