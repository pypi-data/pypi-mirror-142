# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TeamsListArgs', 'TeamsList']

@pulumi.input_type
class TeamsListArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a TeamsList resource.
        :param pulumi.Input[str] account_id: The account to which the teams list should be added.
        :param pulumi.Input[str] name: Name of the teams list.
        :param pulumi.Input[str] type: The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        :param pulumi.Input[str] description: The description of the teams list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] items: The items of the teams list.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if items is not None:
            pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account to which the teams list should be added.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the teams list.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the teams list.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The items of the teams list.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "items", value)


@pulumi.input_type
class _TeamsListState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TeamsList resources.
        :param pulumi.Input[str] account_id: The account to which the teams list should be added.
        :param pulumi.Input[str] description: The description of the teams list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] items: The items of the teams list.
        :param pulumi.Input[str] name: Name of the teams list.
        :param pulumi.Input[str] type: The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account to which the teams list should be added.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the teams list.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The items of the teams list.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the teams list.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class TeamsList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Teams List resource. Teams lists are referenced when creating secure web gateway policies or device posture rules.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        corporate_devices = cloudflare.TeamsList("corporateDevices",
            account_id="1d5fdc9e88c8a8c4518b068cd94331fe",
            description="Serial numbers for all corporate devices.",
            items=[
                "8GE8721REF",
                "5RE8543EGG",
                "1YE2880LNP",
            ],
            name="Corporate devices",
            type="SERIAL")
        ```

        ## Import

        Teams lists can be imported using a composite ID formed of account ID and teams list ID.

        ```sh
         $ pulumi import cloudflare:index/teamsList:TeamsList corporate_devices cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the teams list should be added.
        :param pulumi.Input[str] description: The description of the teams list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] items: The items of the teams list.
        :param pulumi.Input[str] name: Name of the teams list.
        :param pulumi.Input[str] type: The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamsListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Teams List resource. Teams lists are referenced when creating secure web gateway policies or device posture rules.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        corporate_devices = cloudflare.TeamsList("corporateDevices",
            account_id="1d5fdc9e88c8a8c4518b068cd94331fe",
            description="Serial numbers for all corporate devices.",
            items=[
                "8GE8721REF",
                "5RE8543EGG",
                "1YE2880LNP",
            ],
            name="Corporate devices",
            type="SERIAL")
        ```

        ## Import

        Teams lists can be imported using a composite ID formed of account ID and teams list ID.

        ```sh
         $ pulumi import cloudflare:index/teamsList:TeamsList corporate_devices cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

        :param str resource_name: The name of the resource.
        :param TeamsListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamsListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamsListArgs.__new__(TeamsListArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["description"] = description
            __props__.__dict__["items"] = items
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(TeamsList, __self__).__init__(
            'cloudflare:index/teamsList:TeamsList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            items: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'TeamsList':
        """
        Get an existing TeamsList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the teams list should be added.
        :param pulumi.Input[str] description: The description of the teams list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] items: The items of the teams list.
        :param pulumi.Input[str] name: Name of the teams list.
        :param pulumi.Input[str] type: The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamsListState.__new__(_TeamsListState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["description"] = description
        __props__.__dict__["items"] = items
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        return TeamsList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account to which the teams list should be added.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the teams list.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The items of the teams list.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the teams list.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
        """
        return pulumi.get(self, "type")

