import inspect

from vkbottle_types.objects import StatusStatus

from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: StatusStatus


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
