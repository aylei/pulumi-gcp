# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'DeviceConfig',
    'DeviceCredential',
    'DeviceCredentialPublicKey',
    'DeviceGatewayConfig',
    'DeviceLastErrorStatus',
    'DeviceState',
    'RegistryCredential',
    'RegistryEventNotificationConfigItem',
]

@pulumi.output_type
class DeviceConfig(dict):
    def __init__(__self__, *,
                 binary_data: Optional[str] = None,
                 cloud_update_time: Optional[str] = None,
                 device_ack_time: Optional[str] = None,
                 version: Optional[str] = None):
        if binary_data is not None:
            pulumi.set(__self__, "binary_data", binary_data)
        if cloud_update_time is not None:
            pulumi.set(__self__, "cloud_update_time", cloud_update_time)
        if device_ack_time is not None:
            pulumi.set(__self__, "device_ack_time", device_ack_time)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="binaryData")
    def binary_data(self) -> Optional[str]:
        return pulumi.get(self, "binary_data")

    @property
    @pulumi.getter(name="cloudUpdateTime")
    def cloud_update_time(self) -> Optional[str]:
        return pulumi.get(self, "cloud_update_time")

    @property
    @pulumi.getter(name="deviceAckTime")
    def device_ack_time(self) -> Optional[str]:
        return pulumi.get(self, "device_ack_time")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeviceCredential(dict):
    def __init__(__self__, *,
                 public_key: 'outputs.DeviceCredentialPublicKey',
                 expiration_time: Optional[str] = None):
        """
        :param 'DeviceCredentialPublicKeyArgs' public_key: A public key used to verify the signature of JSON Web Tokens (JWTs).
               Structure is documented below.
        :param str expiration_time: The time at which this credential becomes invalid.
        """
        pulumi.set(__self__, "public_key", public_key)
        if expiration_time is not None:
            pulumi.set(__self__, "expiration_time", expiration_time)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> 'outputs.DeviceCredentialPublicKey':
        """
        A public key used to verify the signature of JSON Web Tokens (JWTs).
        Structure is documented below.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[str]:
        """
        The time at which this credential becomes invalid.
        """
        return pulumi.get(self, "expiration_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeviceCredentialPublicKey(dict):
    def __init__(__self__, *,
                 format: str,
                 key: str):
        """
        :param str format: The format of the key.
               Possible values are `RSA_PEM`, `RSA_X509_PEM`, `ES256_PEM`, and `ES256_X509_PEM`.
        :param str key: The key data.
        """
        pulumi.set(__self__, "format", format)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of the key.
        Possible values are `RSA_PEM`, `RSA_X509_PEM`, `ES256_PEM`, and `ES256_X509_PEM`.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key data.
        """
        return pulumi.get(self, "key")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeviceGatewayConfig(dict):
    def __init__(__self__, *,
                 gateway_auth_method: Optional[str] = None,
                 gateway_type: Optional[str] = None,
                 last_accessed_gateway_id: Optional[str] = None,
                 last_accessed_gateway_time: Optional[str] = None):
        """
        :param str gateway_auth_method: Indicates whether the device is a gateway.
               Possible values are `ASSOCIATION_ONLY`, `DEVICE_AUTH_TOKEN_ONLY`, and `ASSOCIATION_AND_DEVICE_AUTH_TOKEN`.
        :param str gateway_type: Indicates whether the device is a gateway.
               Default value is `NON_GATEWAY`.
               Possible values are `GATEWAY` and `NON_GATEWAY`.
        :param str last_accessed_gateway_id: -
               The ID of the gateway the device accessed most recently.
        :param str last_accessed_gateway_time: -
               The most recent time at which the device accessed the gateway specified in last_accessed_gateway.
        """
        if gateway_auth_method is not None:
            pulumi.set(__self__, "gateway_auth_method", gateway_auth_method)
        if gateway_type is not None:
            pulumi.set(__self__, "gateway_type", gateway_type)
        if last_accessed_gateway_id is not None:
            pulumi.set(__self__, "last_accessed_gateway_id", last_accessed_gateway_id)
        if last_accessed_gateway_time is not None:
            pulumi.set(__self__, "last_accessed_gateway_time", last_accessed_gateway_time)

    @property
    @pulumi.getter(name="gatewayAuthMethod")
    def gateway_auth_method(self) -> Optional[str]:
        """
        Indicates whether the device is a gateway.
        Possible values are `ASSOCIATION_ONLY`, `DEVICE_AUTH_TOKEN_ONLY`, and `ASSOCIATION_AND_DEVICE_AUTH_TOKEN`.
        """
        return pulumi.get(self, "gateway_auth_method")

    @property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[str]:
        """
        Indicates whether the device is a gateway.
        Default value is `NON_GATEWAY`.
        Possible values are `GATEWAY` and `NON_GATEWAY`.
        """
        return pulumi.get(self, "gateway_type")

    @property
    @pulumi.getter(name="lastAccessedGatewayId")
    def last_accessed_gateway_id(self) -> Optional[str]:
        """
        -
        The ID of the gateway the device accessed most recently.
        """
        return pulumi.get(self, "last_accessed_gateway_id")

    @property
    @pulumi.getter(name="lastAccessedGatewayTime")
    def last_accessed_gateway_time(self) -> Optional[str]:
        """
        -
        The most recent time at which the device accessed the gateway specified in last_accessed_gateway.
        """
        return pulumi.get(self, "last_accessed_gateway_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeviceLastErrorStatus(dict):
    def __init__(__self__, *,
                 details: Optional[Sequence[Mapping[str, Any]]] = None,
                 message: Optional[str] = None,
                 number: Optional[int] = None):
        if details is not None:
            pulumi.set(__self__, "details", details)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if number is not None:
            pulumi.set(__self__, "number", number)

    @property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, Any]]]:
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def number(self) -> Optional[int]:
        return pulumi.get(self, "number")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeviceState(dict):
    def __init__(__self__, *,
                 binary_data: Optional[str] = None,
                 update_time: Optional[str] = None):
        if binary_data is not None:
            pulumi.set(__self__, "binary_data", binary_data)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="binaryData")
    def binary_data(self) -> Optional[str]:
        return pulumi.get(self, "binary_data")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        return pulumi.get(self, "update_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RegistryCredential(dict):
    def __init__(__self__, *,
                 public_key_certificate: Mapping[str, Any]):
        """
        :param Mapping[str, Any] public_key_certificate: A public key certificate format and data.
        """
        pulumi.set(__self__, "public_key_certificate", public_key_certificate)

    @property
    @pulumi.getter(name="publicKeyCertificate")
    def public_key_certificate(self) -> Mapping[str, Any]:
        """
        A public key certificate format and data.
        """
        return pulumi.get(self, "public_key_certificate")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RegistryEventNotificationConfigItem(dict):
    def __init__(__self__, *,
                 pubsub_topic_name: str,
                 subfolder_matches: Optional[str] = None):
        """
        :param str pubsub_topic_name: PubSub topic name to publish device events.
        :param str subfolder_matches: If the subfolder name matches this string exactly, this
               configuration will be used. The string must not include the
               leading '/' character. If empty, all strings are matched. Empty
               value can only be used for the last `event_notification_configs`
               item.
        """
        pulumi.set(__self__, "pubsub_topic_name", pubsub_topic_name)
        if subfolder_matches is not None:
            pulumi.set(__self__, "subfolder_matches", subfolder_matches)

    @property
    @pulumi.getter(name="pubsubTopicName")
    def pubsub_topic_name(self) -> str:
        """
        PubSub topic name to publish device events.
        """
        return pulumi.get(self, "pubsub_topic_name")

    @property
    @pulumi.getter(name="subfolderMatches")
    def subfolder_matches(self) -> Optional[str]:
        """
        If the subfolder name matches this string exactly, this
        configuration will be used. The string must not include the
        leading '/' character. If empty, all strings are matched. Empty
        value can only be used for the last `event_notification_configs`
        item.
        """
        return pulumi.get(self, "subfolder_matches")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


