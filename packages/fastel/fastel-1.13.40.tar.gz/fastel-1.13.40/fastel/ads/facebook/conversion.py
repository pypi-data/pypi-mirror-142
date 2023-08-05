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


class ItemsForm(BaseModel):
    order_id: Optional[str] = None
    price: Optional[int] = None
    content: List[ItemForm]


FacebookAdsApi.init(access_token=SdkConfig.conversion_token)


class ConversionApi:
    @classmethod
    def push_event(
        cls,
        action: str,
        user_model: UserForm,
        custom_model: Optional[ItemsForm] = None,
    ) -> Any:
        user_data = UserData(**user_model.dict(exclude_none=True))

        custom_data = None
        if custom_model:
            contents = [
                Content(**item.dict(exclude_none=True)) for item in custom_model.content
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
        event_request = EventRequest(
            events=[event],
            pixel_id=SdkConfig.conversion_id,
        )
        event_result = event_request.execute()
        print("[LOG]", event_result)
        return event_result

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
