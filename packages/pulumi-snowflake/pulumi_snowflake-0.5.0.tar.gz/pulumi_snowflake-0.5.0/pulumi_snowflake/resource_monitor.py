# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ResourceMonitorArgs', 'ResourceMonitor']

@pulumi.input_type
class ResourceMonitorArgs:
    def __init__(__self__, *,
                 credit_quota: Optional[pulumi.Input[int]] = None,
                 end_timestamp: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notify_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 set_for_account: Optional[pulumi.Input[bool]] = None,
                 start_timestamp: Optional[pulumi.Input[str]] = None,
                 suspend_immediate_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 suspend_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 warehouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ResourceMonitor resource.
        :param pulumi.Input[int] credit_quota: The number of credits allocated monthly to the resource monitor.
        :param pulumi.Input[str] end_timestamp: The date and time when the resource monitor suspends the assigned warehouses.
        :param pulumi.Input[str] frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        :param pulumi.Input[str] name: Identifier for the resource monitor; must be unique for your account.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users.
        :param pulumi.Input[bool] set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account.
        :param pulumi.Input[str] start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_triggers: A list of percentage thresholds at which to suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] warehouses: A list of warehouses to apply the resource monitor to.
        """
        if credit_quota is not None:
            pulumi.set(__self__, "credit_quota", credit_quota)
        if end_timestamp is not None:
            pulumi.set(__self__, "end_timestamp", end_timestamp)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notify_triggers is not None:
            pulumi.set(__self__, "notify_triggers", notify_triggers)
        if set_for_account is not None:
            pulumi.set(__self__, "set_for_account", set_for_account)
        if start_timestamp is not None:
            pulumi.set(__self__, "start_timestamp", start_timestamp)
        if suspend_immediate_triggers is not None:
            pulumi.set(__self__, "suspend_immediate_triggers", suspend_immediate_triggers)
        if suspend_triggers is not None:
            pulumi.set(__self__, "suspend_triggers", suspend_triggers)
        if warehouses is not None:
            pulumi.set(__self__, "warehouses", warehouses)

    @property
    @pulumi.getter(name="creditQuota")
    def credit_quota(self) -> Optional[pulumi.Input[int]]:
        """
        The number of credits allocated monthly to the resource monitor.
        """
        return pulumi.get(self, "credit_quota")

    @credit_quota.setter
    def credit_quota(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "credit_quota", value)

    @property
    @pulumi.getter(name="endTimestamp")
    def end_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the resource monitor suspends the assigned warehouses.
        """
        return pulumi.get(self, "end_timestamp")

    @end_timestamp.setter
    def end_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_timestamp", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[str]]:
        """
        The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the resource monitor; must be unique for your account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notifyTriggers")
    def notify_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to send an alert to subscribed users.
        """
        return pulumi.get(self, "notify_triggers")

    @notify_triggers.setter
    def notify_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "notify_triggers", value)

    @property
    @pulumi.getter(name="setForAccount")
    def set_for_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the resource monitor should be applied globally to your Snowflake account.
        """
        return pulumi.get(self, "set_for_account")

    @set_for_account.setter
    def set_for_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "set_for_account", value)

    @property
    @pulumi.getter(name="startTimestamp")
    def start_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        """
        return pulumi.get(self, "start_timestamp")

    @start_timestamp.setter
    def start_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_timestamp", value)

    @property
    @pulumi.getter(name="suspendImmediateTriggers")
    def suspend_immediate_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to immediately suspend all warehouses.
        """
        return pulumi.get(self, "suspend_immediate_triggers")

    @suspend_immediate_triggers.setter
    def suspend_immediate_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "suspend_immediate_triggers", value)

    @property
    @pulumi.getter(name="suspendTriggers")
    def suspend_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to suspend all warehouses.
        """
        return pulumi.get(self, "suspend_triggers")

    @suspend_triggers.setter
    def suspend_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "suspend_triggers", value)

    @property
    @pulumi.getter
    def warehouses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of warehouses to apply the resource monitor to.
        """
        return pulumi.get(self, "warehouses")

    @warehouses.setter
    def warehouses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "warehouses", value)


@pulumi.input_type
class _ResourceMonitorState:
    def __init__(__self__, *,
                 credit_quota: Optional[pulumi.Input[int]] = None,
                 end_timestamp: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notify_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 set_for_account: Optional[pulumi.Input[bool]] = None,
                 start_timestamp: Optional[pulumi.Input[str]] = None,
                 suspend_immediate_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 suspend_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 warehouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ResourceMonitor resources.
        :param pulumi.Input[int] credit_quota: The number of credits allocated monthly to the resource monitor.
        :param pulumi.Input[str] end_timestamp: The date and time when the resource monitor suspends the assigned warehouses.
        :param pulumi.Input[str] frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        :param pulumi.Input[str] name: Identifier for the resource monitor; must be unique for your account.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users.
        :param pulumi.Input[bool] set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account.
        :param pulumi.Input[str] start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_triggers: A list of percentage thresholds at which to suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] warehouses: A list of warehouses to apply the resource monitor to.
        """
        if credit_quota is not None:
            pulumi.set(__self__, "credit_quota", credit_quota)
        if end_timestamp is not None:
            pulumi.set(__self__, "end_timestamp", end_timestamp)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notify_triggers is not None:
            pulumi.set(__self__, "notify_triggers", notify_triggers)
        if set_for_account is not None:
            pulumi.set(__self__, "set_for_account", set_for_account)
        if start_timestamp is not None:
            pulumi.set(__self__, "start_timestamp", start_timestamp)
        if suspend_immediate_triggers is not None:
            pulumi.set(__self__, "suspend_immediate_triggers", suspend_immediate_triggers)
        if suspend_triggers is not None:
            pulumi.set(__self__, "suspend_triggers", suspend_triggers)
        if warehouses is not None:
            pulumi.set(__self__, "warehouses", warehouses)

    @property
    @pulumi.getter(name="creditQuota")
    def credit_quota(self) -> Optional[pulumi.Input[int]]:
        """
        The number of credits allocated monthly to the resource monitor.
        """
        return pulumi.get(self, "credit_quota")

    @credit_quota.setter
    def credit_quota(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "credit_quota", value)

    @property
    @pulumi.getter(name="endTimestamp")
    def end_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the resource monitor suspends the assigned warehouses.
        """
        return pulumi.get(self, "end_timestamp")

    @end_timestamp.setter
    def end_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_timestamp", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[str]]:
        """
        The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the resource monitor; must be unique for your account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notifyTriggers")
    def notify_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to send an alert to subscribed users.
        """
        return pulumi.get(self, "notify_triggers")

    @notify_triggers.setter
    def notify_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "notify_triggers", value)

    @property
    @pulumi.getter(name="setForAccount")
    def set_for_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the resource monitor should be applied globally to your Snowflake account.
        """
        return pulumi.get(self, "set_for_account")

    @set_for_account.setter
    def set_for_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "set_for_account", value)

    @property
    @pulumi.getter(name="startTimestamp")
    def start_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        """
        return pulumi.get(self, "start_timestamp")

    @start_timestamp.setter
    def start_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_timestamp", value)

    @property
    @pulumi.getter(name="suspendImmediateTriggers")
    def suspend_immediate_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to immediately suspend all warehouses.
        """
        return pulumi.get(self, "suspend_immediate_triggers")

    @suspend_immediate_triggers.setter
    def suspend_immediate_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "suspend_immediate_triggers", value)

    @property
    @pulumi.getter(name="suspendTriggers")
    def suspend_triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of percentage thresholds at which to suspend all warehouses.
        """
        return pulumi.get(self, "suspend_triggers")

    @suspend_triggers.setter
    def suspend_triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "suspend_triggers", value)

    @property
    @pulumi.getter
    def warehouses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of warehouses to apply the resource monitor to.
        """
        return pulumi.get(self, "warehouses")

    @warehouses.setter
    def warehouses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "warehouses", value)


class ResourceMonitor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credit_quota: Optional[pulumi.Input[int]] = None,
                 end_timestamp: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notify_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 set_for_account: Optional[pulumi.Input[bool]] = None,
                 start_timestamp: Optional[pulumi.Input[str]] = None,
                 suspend_immediate_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 suspend_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 warehouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        monitor = snowflake.ResourceMonitor("monitor",
            credit_quota=100,
            end_timestamp="2021-12-07 00:00",
            frequency="DAILY",
            notify_triggers=[40],
            start_timestamp="2020-12-07 00:00",
            suspend_immediate_triggers=[90],
            suspend_triggers=[50])
        ```

        ## Import

        ```sh
         $ pulumi import snowflake:index/resourceMonitor:ResourceMonitor example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] credit_quota: The number of credits allocated monthly to the resource monitor.
        :param pulumi.Input[str] end_timestamp: The date and time when the resource monitor suspends the assigned warehouses.
        :param pulumi.Input[str] frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        :param pulumi.Input[str] name: Identifier for the resource monitor; must be unique for your account.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users.
        :param pulumi.Input[bool] set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account.
        :param pulumi.Input[str] start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_triggers: A list of percentage thresholds at which to suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] warehouses: A list of warehouses to apply the resource monitor to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ResourceMonitorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        monitor = snowflake.ResourceMonitor("monitor",
            credit_quota=100,
            end_timestamp="2021-12-07 00:00",
            frequency="DAILY",
            notify_triggers=[40],
            start_timestamp="2020-12-07 00:00",
            suspend_immediate_triggers=[90],
            suspend_triggers=[50])
        ```

        ## Import

        ```sh
         $ pulumi import snowflake:index/resourceMonitor:ResourceMonitor example
        ```

        :param str resource_name: The name of the resource.
        :param ResourceMonitorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceMonitorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credit_quota: Optional[pulumi.Input[int]] = None,
                 end_timestamp: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notify_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 set_for_account: Optional[pulumi.Input[bool]] = None,
                 start_timestamp: Optional[pulumi.Input[str]] = None,
                 suspend_immediate_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 suspend_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 warehouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = ResourceMonitorArgs.__new__(ResourceMonitorArgs)

            __props__.__dict__["credit_quota"] = credit_quota
            __props__.__dict__["end_timestamp"] = end_timestamp
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["name"] = name
            __props__.__dict__["notify_triggers"] = notify_triggers
            __props__.__dict__["set_for_account"] = set_for_account
            __props__.__dict__["start_timestamp"] = start_timestamp
            __props__.__dict__["suspend_immediate_triggers"] = suspend_immediate_triggers
            __props__.__dict__["suspend_triggers"] = suspend_triggers
            __props__.__dict__["warehouses"] = warehouses
        super(ResourceMonitor, __self__).__init__(
            'snowflake:index/resourceMonitor:ResourceMonitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credit_quota: Optional[pulumi.Input[int]] = None,
            end_timestamp: Optional[pulumi.Input[str]] = None,
            frequency: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notify_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            set_for_account: Optional[pulumi.Input[bool]] = None,
            start_timestamp: Optional[pulumi.Input[str]] = None,
            suspend_immediate_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            suspend_triggers: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            warehouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ResourceMonitor':
        """
        Get an existing ResourceMonitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] credit_quota: The number of credits allocated monthly to the resource monitor.
        :param pulumi.Input[str] end_timestamp: The date and time when the resource monitor suspends the assigned warehouses.
        :param pulumi.Input[str] frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        :param pulumi.Input[str] name: Identifier for the resource monitor; must be unique for your account.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users.
        :param pulumi.Input[bool] set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account.
        :param pulumi.Input[str] start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] suspend_triggers: A list of percentage thresholds at which to suspend all warehouses.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] warehouses: A list of warehouses to apply the resource monitor to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourceMonitorState.__new__(_ResourceMonitorState)

        __props__.__dict__["credit_quota"] = credit_quota
        __props__.__dict__["end_timestamp"] = end_timestamp
        __props__.__dict__["frequency"] = frequency
        __props__.__dict__["name"] = name
        __props__.__dict__["notify_triggers"] = notify_triggers
        __props__.__dict__["set_for_account"] = set_for_account
        __props__.__dict__["start_timestamp"] = start_timestamp
        __props__.__dict__["suspend_immediate_triggers"] = suspend_immediate_triggers
        __props__.__dict__["suspend_triggers"] = suspend_triggers
        __props__.__dict__["warehouses"] = warehouses
        return ResourceMonitor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creditQuota")
    def credit_quota(self) -> pulumi.Output[int]:
        """
        The number of credits allocated monthly to the resource monitor.
        """
        return pulumi.get(self, "credit_quota")

    @property
    @pulumi.getter(name="endTimestamp")
    def end_timestamp(self) -> pulumi.Output[Optional[str]]:
        """
        The date and time when the resource monitor suspends the assigned warehouses.
        """
        return pulumi.get(self, "end_timestamp")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Identifier for the resource monitor; must be unique for your account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notifyTriggers")
    def notify_triggers(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        A list of percentage thresholds at which to send an alert to subscribed users.
        """
        return pulumi.get(self, "notify_triggers")

    @property
    @pulumi.getter(name="setForAccount")
    def set_for_account(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the resource monitor should be applied globally to your Snowflake account.
        """
        return pulumi.get(self, "set_for_account")

    @property
    @pulumi.getter(name="startTimestamp")
    def start_timestamp(self) -> pulumi.Output[str]:
        """
        The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.
        """
        return pulumi.get(self, "start_timestamp")

    @property
    @pulumi.getter(name="suspendImmediateTriggers")
    def suspend_immediate_triggers(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        A list of percentage thresholds at which to immediately suspend all warehouses.
        """
        return pulumi.get(self, "suspend_immediate_triggers")

    @property
    @pulumi.getter(name="suspendTriggers")
    def suspend_triggers(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        A list of percentage thresholds at which to suspend all warehouses.
        """
        return pulumi.get(self, "suspend_triggers")

    @property
    @pulumi.getter
    def warehouses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of warehouses to apply the resource monitor to.
        """
        return pulumi.get(self, "warehouses")

