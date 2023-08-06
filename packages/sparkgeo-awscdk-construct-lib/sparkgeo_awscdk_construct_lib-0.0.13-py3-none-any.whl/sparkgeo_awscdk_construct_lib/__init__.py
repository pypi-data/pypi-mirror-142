'''
# replace this
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_route53
import aws_cdk.aws_s3
import constructs


class SinglePageApp(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@sparkgeo/awscdk-constructs-library.SinglePageApp",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        build_path: builtins.str,
        domain_prefix: typing.Optional[builtins.str] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param build_path: The path to the build files that are to be deployed to S3.
        :param domain_prefix: The prefix for this app in the ``privateHostedZone`` for the app. It is assumed the user has checked to ensure the prefix has not been used.
        :param hosted_zone: Private hosted zone for DNS.
        '''
        props = SinglePageAppProps(
            build_path=build_path, domain_prefix=domain_prefix, hosted_zone=hosted_zone
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> aws_cdk.aws_s3.Bucket:
        return typing.cast(aws_cdk.aws_s3.Bucket, jsii.get(self, "bucket"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> aws_cdk.aws_cloudfront.Distribution:
        return typing.cast(aws_cdk.aws_cloudfront.Distribution, jsii.get(self, "distribution"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.DnsValidatedCertificate]:
        return typing.cast(typing.Optional[aws_cdk.aws_certificatemanager.DnsValidatedCertificate], jsii.get(self, "certificate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainName"))


@jsii.data_type(
    jsii_type="@sparkgeo/awscdk-constructs-library.SinglePageAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "build_path": "buildPath",
        "domain_prefix": "domainPrefix",
        "hosted_zone": "hostedZone",
    },
)
class SinglePageAppProps:
    def __init__(
        self,
        *,
        build_path: builtins.str,
        domain_prefix: typing.Optional[builtins.str] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> None:
        '''Construct properties for ``SinglePageApp``.

        :param build_path: The path to the build files that are to be deployed to S3.
        :param domain_prefix: The prefix for this app in the ``privateHostedZone`` for the app. It is assumed the user has checked to ensure the prefix has not been used.
        :param hosted_zone: Private hosted zone for DNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "build_path": build_path,
        }
        if domain_prefix is not None:
            self._values["domain_prefix"] = domain_prefix
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone

    @builtins.property
    def build_path(self) -> builtins.str:
        '''The path to the build files that are to be deployed to S3.'''
        result = self._values.get("build_path")
        assert result is not None, "Required property 'build_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for this app in the ``privateHostedZone`` for the app.

        It is assumed the user has checked to ensure the prefix has not been used.
        '''
        result = self._values.get("domain_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone(self) -> typing.Optional[aws_cdk.aws_route53.IHostedZone]:
        '''Private hosted zone for DNS.'''
        result = self._values.get("hosted_zone")
        return typing.cast(typing.Optional[aws_cdk.aws_route53.IHostedZone], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SinglePageAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SinglePageApp",
    "SinglePageAppProps",
]

publication.publish()
