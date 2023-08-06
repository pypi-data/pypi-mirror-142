import time
from typing import Any, List, Optional

from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi
from pydantic import BaseModel

from fastel.config import SdkConfig


class UserForm(BaseModel):
    email: str
    phone: Optional[str]
    city: Optional[str]
    state: Optional[str]


class ItemForm(BaseModel):
    product_id: str
    quantity: int
    item_price: int
    title: str
    category: Optional[str]


class ItemsForm(BaseModel):
    order_id: Optional[str] = None
    price: Optional[int] = None
    content: List[ItemForm]


class ConversionApi:
    conversion_id: str

    @classmethod
    def init(cls) -> Any:
        cls.conversion_id = SdkConfig.conversion_id
        FacebookAdsApi.init(access_token=SdkConfig.conversion_token)

    @classmethod
    def push_event(
        cls,
        action: str,
        user_model: UserForm,
        custom_model: Optional[ItemsForm] = None,
        raise_exception: bool = False,
    ) -> Any:
        try:
            user_data = UserData(**user_model.dict(exclude_none=True))

            custom_data = None
            if custom_model:
                contents = [
                    Content(**item.dict(exclude_none=True))
                    for item in custom_model.content
                ]
                custom_data = CustomData(
                    currency="twd",
                    order_id=custom_model.order_id,
                    value=custom_model.price,
                    contents=contents,
                )

            event = Event(
                event_name=action,
                event_time=int(time.time()),
                user_data=user_data,
                custom_data=custom_data,
                action_source=ActionSource.WEBSITE,
            )
            events = [event]
            event_request = EventRequest(
                events=events,
                pixel_id=cls.conversion_id,
            )
            event_result = event_request.execute()
            print("[SUCCESS]", event_result)
            return event_result

        except Exception as exc:
            print("[ERROR]", str(exc))
            if raise_exception:
                raise exc

    @classmethod
    def push_register_event(cls, user: UserForm) -> Any:
        cls.push_event("CompleteRegistration", user, None)

    @classmethod
    def push_add_cart_event(cls, user: UserForm, items: ItemsForm) -> Any:
        cls.push_event("AddToCart", user, items)

    @classmethod
    def push_checkout_event(cls, user: UserForm, items: ItemsForm) -> Any:
        cls.push_event("InitiateCheckout", user, items)

    @classmethod
    def push_purchase_event(cls, user: UserForm, items: ItemsForm) -> Any:
        cls.push_event("Purchase", user, items)
