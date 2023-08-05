# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IntegrationGrantArgs', 'IntegrationGrant']

@pulumi.input_type
class IntegrationGrantArgs:
    def __init__(__self__, *,
                 integration_name: pulumi.Input[str],
                 privilege: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a IntegrationGrant resource.
        :param pulumi.Input[str] integration_name: Identifier for the integration; must be unique for your account.
        :param pulumi.Input[str] privilege: The privilege to grant on the integration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: Grants privilege to these roles.
        :param pulumi.Input[bool] with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        pulumi.set(__self__, "integration_name", integration_name)
        if privilege is not None:
            pulumi.set(__self__, "privilege", privilege)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if with_grant_option is not None:
            pulumi.set(__self__, "with_grant_option", with_grant_option)

    @property
    @pulumi.getter(name="integrationName")
    def integration_name(self) -> pulumi.Input[str]:
        """
        Identifier for the integration; must be unique for your account.
        """
        return pulumi.get(self, "integration_name")

    @integration_name.setter
    def integration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_name", value)

    @property
    @pulumi.getter
    def privilege(self) -> Optional[pulumi.Input[str]]:
        """
        The privilege to grant on the integration.
        """
        return pulumi.get(self, "privilege")

    @privilege.setter
    def privilege(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "privilege", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Grants privilege to these roles.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


@pulumi.input_type
class _IntegrationGrantState:
    def __init__(__self__, *,
                 integration_name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering IntegrationGrant resources.
        :param pulumi.Input[str] integration_name: Identifier for the integration; must be unique for your account.
        :param pulumi.Input[str] privilege: The privilege to grant on the integration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: Grants privilege to these roles.
        :param pulumi.Input[bool] with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        if integration_name is not None:
            pulumi.set(__self__, "integration_name", integration_name)
        if privilege is not None:
            pulumi.set(__self__, "privilege", privilege)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if with_grant_option is not None:
            pulumi.set(__self__, "with_grant_option", with_grant_option)

    @property
    @pulumi.getter(name="integrationName")
    def integration_name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the integration; must be unique for your account.
        """
        return pulumi.get(self, "integration_name")

    @integration_name.setter
    def integration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_name", value)

    @property
    @pulumi.getter
    def privilege(self) -> Optional[pulumi.Input[str]]:
        """
        The privilege to grant on the integration.
        """
        return pulumi.get(self, "privilege")

    @privilege.setter
    def privilege(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "privilege", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Grants privilege to these roles.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


class IntegrationGrant(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        grant = snowflake.IntegrationGrant("grant",
            integration_name="integration",
            privilege="USAGE",
            roles=[
                "role1",
                "role2",
            ],
            with_grant_option=False)
        ```

        ## Import

        # format is integration name ||| privilege | true/false for with_grant_option

        ```sh
         $ pulumi import snowflake:index/integrationGrant:IntegrationGrant example 'intName|||USAGE|true'
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] integration_name: Identifier for the integration; must be unique for your account.
        :param pulumi.Input[str] privilege: The privilege to grant on the integration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: Grants privilege to these roles.
        :param pulumi.Input[bool] with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationGrantArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        grant = snowflake.IntegrationGrant("grant",
            integration_name="integration",
            privilege="USAGE",
            roles=[
                "role1",
                "role2",
            ],
            with_grant_option=False)
        ```

        ## Import

        # format is integration name ||| privilege | true/false for with_grant_option

        ```sh
         $ pulumi import snowflake:index/integrationGrant:IntegrationGrant example 'intName|||USAGE|true'
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationGrantArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationGrantArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
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
            __props__ = IntegrationGrantArgs.__new__(IntegrationGrantArgs)

            if integration_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_name'")
            __props__.__dict__["integration_name"] = integration_name
            __props__.__dict__["privilege"] = privilege
            __props__.__dict__["roles"] = roles
            __props__.__dict__["with_grant_option"] = with_grant_option
        super(IntegrationGrant, __self__).__init__(
            'snowflake:index/integrationGrant:IntegrationGrant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            integration_name: Optional[pulumi.Input[str]] = None,
            privilege: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            with_grant_option: Optional[pulumi.Input[bool]] = None) -> 'IntegrationGrant':
        """
        Get an existing IntegrationGrant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] integration_name: Identifier for the integration; must be unique for your account.
        :param pulumi.Input[str] privilege: The privilege to grant on the integration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: Grants privilege to these roles.
        :param pulumi.Input[bool] with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationGrantState.__new__(_IntegrationGrantState)

        __props__.__dict__["integration_name"] = integration_name
        __props__.__dict__["privilege"] = privilege
        __props__.__dict__["roles"] = roles
        __props__.__dict__["with_grant_option"] = with_grant_option
        return IntegrationGrant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="integrationName")
    def integration_name(self) -> pulumi.Output[str]:
        """
        Identifier for the integration; must be unique for your account.
        """
        return pulumi.get(self, "integration_name")

    @property
    @pulumi.getter
    def privilege(self) -> pulumi.Output[Optional[str]]:
        """
        The privilege to grant on the integration.
        """
        return pulumi.get(self, "privilege")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Grants privilege to these roles.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> pulumi.Output[Optional[bool]]:
        """
        When this is set to true, allows the recipient role to grant the privileges to other roles.
        """
        return pulumi.get(self, "with_grant_option")

