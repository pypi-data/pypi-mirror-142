'''
# @sudocdkconstructs/s3-run-fargate-task

It's a very common AWS pattern to run a Fargate task when a file is uploaded to a S3 bucket. Usually developers create a Lambda function that is connected to S3 event notifications and starts the Fargate task.
This construct uses a little different approach. It enables [S3 EventBridge notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventBridge.html) in the bucket and creates a rule that runs the Fargate task. It passes the bucket name and object key to the container as an environment variables. Notice that it does not required a Lambda function.

## Install

TypeScript/JavaScript:

```bash
npm i @sudocdkconstructs/s3-run-fargate-task
```

Python:

```bash
pip install sudocdkconstructs.s3-run-fargate-task
```

## How to use

```python
const bucket = new cdk.aws_s3.Bucket(this, 'Bucket', {
    bucketName: 's3-fargate-bucket'
})

new S3RunFargateTask(this, 'S3RunFargateTask', {
    bucket,
    ruleName: 'cdk-run-fargate-rule',
    clusterName: 'FargateCluster',
    ruleDescription: 's3 event runs fargate task',
    taskDefinitionArn: 'arn:aws:ecs:us-east-1:002020202:task-definition/FargateTask:9',
    containerName: 'processContainer',
    subnetIds: ['subnet-0001', 'subnet-00002'],
    securityGroups: ['sg-00001']
})
```

The bucket name will be in the container environment variable `BUCKET` and the object key in the `KEY` variable.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_events
import aws_cdk.aws_s3
import aws_cdk.aws_sqs
import constructs


class S3RunFargateTask(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@sudocdkconstructs/s3-run-fargate-task.S3RunFargateTask",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        bucket: aws_cdk.aws_s3.Bucket,
        cluster_name: builtins.str,
        container_name: builtins.str,
        rule_name: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        task_definition_arn: builtins.str,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        rule_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param bucket: S3 bucket.
        :param cluster_name: ECS cluster name.
        :param container_name: Container name.
        :param rule_name: The name of the rule.
        :param security_groups: Security groups for Fargate task.
        :param subnet_ids: Subnets IDs for Fargate task.
        :param task_definition_arn: Fargate task ARN.
        :param assign_public_ip: Specify if assign public IP address to task If running in public subnet, this should be true. Default: false
        :param event_bus_name: The name or ARN of the event bus associated with the rule If you omitted, the default event bus is used. Default: default
        :param rule_description: Rule description. Default: '''

        :access: private
        :since: 0.8.0
        :summary: Construct to run a Fargate task when files have been added to S3
        '''
        props = S3RunFargateTaskProps(
            bucket=bucket,
            cluster_name=cluster_name,
            container_name=container_name,
            rule_name=rule_name,
            security_groups=security_groups,
            subnet_ids=subnet_ids,
            task_definition_arn=task_definition_arn,
            assign_public_ip=assign_public_ip,
            event_bus_name=event_bus_name,
            rule_description=rule_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dlq")
    def dlq(self) -> aws_cdk.aws_sqs.Queue:
        return typing.cast(aws_cdk.aws_sqs.Queue, jsii.get(self, "dlq"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rule")
    def rule(self) -> aws_cdk.aws_events.CfnRule:
        return typing.cast(aws_cdk.aws_events.CfnRule, jsii.get(self, "rule"))


@jsii.data_type(
    jsii_type="@sudocdkconstructs/s3-run-fargate-task.S3RunFargateTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "cluster_name": "clusterName",
        "container_name": "containerName",
        "rule_name": "ruleName",
        "security_groups": "securityGroups",
        "subnet_ids": "subnetIds",
        "task_definition_arn": "taskDefinitionArn",
        "assign_public_ip": "assignPublicIp",
        "event_bus_name": "eventBusName",
        "rule_description": "ruleDescription",
    },
)
class S3RunFargateTaskProps:
    def __init__(
        self,
        *,
        bucket: aws_cdk.aws_s3.Bucket,
        cluster_name: builtins.str,
        container_name: builtins.str,
        rule_name: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        task_definition_arn: builtins.str,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        rule_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for S3RunFargate Construct.

        :param bucket: S3 bucket.
        :param cluster_name: ECS cluster name.
        :param container_name: Container name.
        :param rule_name: The name of the rule.
        :param security_groups: Security groups for Fargate task.
        :param subnet_ids: Subnets IDs for Fargate task.
        :param task_definition_arn: Fargate task ARN.
        :param assign_public_ip: Specify if assign public IP address to task If running in public subnet, this should be true. Default: false
        :param event_bus_name: The name or ARN of the event bus associated with the rule If you omitted, the default event bus is used. Default: default
        :param rule_description: Rule description. Default: '''
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "cluster_name": cluster_name,
            "container_name": container_name,
            "rule_name": rule_name,
            "security_groups": security_groups,
            "subnet_ids": subnet_ids,
            "task_definition_arn": task_definition_arn,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if rule_description is not None:
            self._values["rule_description"] = rule_description

    @builtins.property
    def bucket(self) -> aws_cdk.aws_s3.Bucket:
        '''S3 bucket.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.Bucket, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''ECS cluster name.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Container name.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the rule.'''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Security groups for Fargate task.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Subnets IDs for Fargate task.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def task_definition_arn(self) -> builtins.str:
        '''Fargate task ARN.'''
        result = self._values.get("task_definition_arn")
        assert result is not None, "Required property 'task_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''Specify if assign public IP address to task If running in public subnet, this should be true.

        :default: false
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''The name or ARN of the event bus associated with the rule If you omitted, the default event bus is used.

        :default: default
        '''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_description(self) -> typing.Optional[builtins.str]:
        '''Rule description.

        :default: '''
        '''
        result = self._values.get("rule_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3RunFargateTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "S3RunFargateTask",
    "S3RunFargateTaskProps",
]

publication.publish()
