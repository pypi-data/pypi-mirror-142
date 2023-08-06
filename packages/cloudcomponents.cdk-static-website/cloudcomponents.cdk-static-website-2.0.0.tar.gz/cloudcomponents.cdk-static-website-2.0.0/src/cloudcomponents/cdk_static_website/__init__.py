'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-static-website

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-static-website)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-static-website/)
[![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/kolomied/awesome-cdk)

> Cdk component that creates a static website using S3, configures CloudFront (CDN) and maps a custom domain via Route53 (DNS)

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-static-website
```

Python:

```bash
pip install cloudcomponents.cdk-static-website
```

## How to use

```python
import { StaticWebsite } from '@cloudcomponents/cdk-static-website';
import { RemovalPolicy, Stack, StackProps, aws_route53 } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class StaticWebsiteStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const hostedZone = aws_route53.HostedZone.fromLookup(this, 'HostedZone', {
      domainName: 'cloudcomponents.org',
    });

    new StaticWebsite(this, 'StaticWebsite', {
      hostedZone,
      domainNames: ['cloudcomponents.org', 'www.cloudcomponents.org'],
      removalPolicy: RemovalPolicy.DESTROY,
    });
  }
}
```

### Single page application (SPA)

```python
import { StaticWebsite } from '@cloudcomponents/cdk-static-website';
import { RemovalPolicy, Stack, StackProps, aws_route53 } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class StaticWebsiteStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const hostedZone = aws_route53.HostedZone.fromLookup(this, 'HostedZone', {
      domainName: 'cloudcomponents.org',
    });

    new StaticWebsite(this, 'StaticWebsite', {
      hostedZone,
      domainNames: ['cloudcomponents.org', 'www.cloudcomponents.org'],
      errorResponses: [
        {
          httpStatus: 404,
          responseHttpStatus: 200,
          ttl: props.ttl ?? Duration.seconds(300),
          responsePagePath: '/index.html',
        },
      ],
      removalPolicy: RemovalPolicy.DESTROY,
    });
  }
}
```

### Lambda at edge

```python
import { StaticWebsite } from '@cloudcomponents/cdk-static-website';
import { OriginMutation } from '@cloudcomponents/cdk-lambda-at-edge-pattern';
import { RemovalPolicy, Stack, StackProps, aws_route53 } from 'aws-cdk-lib';

import { Construct } from 'constructs';

export class StaticWebsiteStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const hostedZone = aws_route53.HostedZone.fromLookup(this, 'HostedZone', {
      domainName: 'cloudcomponents.org',
    });

    const originMutation = new OriginMutation(stack, 'OriginMutation');

    new StaticWebsite(this, 'StaticWebsite', {
      hostedZone,
      domainNames: ['cloudcomponents.org', 'www.cloudcomponents.org'],
      edgeLambdas: [originMutation],
      removalPolicy: RemovalPolicy.DESTROY,
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-static-website/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-static-website/LICENSE)
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

import aws_cdk
import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_route53
import aws_cdk.aws_s3
import constructs


class StaticWebsite(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-static-website.StaticWebsite",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        custom_headers: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.ResponseCustomHeader]] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        disable_upload: typing.Optional[builtins.bool] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        edge_lambdas: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.EdgeLambda]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        error_responses: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.ErrorResponse]] = None,
        geo_restriction: typing.Optional[aws_cdk.aws_cloudfront.GeoRestriction] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
        http_version: typing.Optional[aws_cdk.aws_cloudfront.HttpVersion] = None,
        log_bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_headers_behavior: typing.Optional[aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior] = None,
        source: typing.Optional[builtins.str] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param custom_headers: A configuration for a set of custom HTTP response headers. Default: - no custom headers behavior
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param disable_upload: Disable website deployment. Default: - false
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - 403 and 404 are routed as 404 to error.html.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param hosted_zone: Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the destination. Domain names in the hosted zone can include a specific domain (example.com) and its subdomains (acme.example.com, zenith.example.com).
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2021
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param security_headers_behavior: Configuration for a set of security-related HTTP response headers. Default: - DefaultSecurityHeadersBehavior
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        props = StaticWebsiteProps(
            certificate=certificate,
            comment=comment,
            custom_headers=custom_headers,
            default_root_object=default_root_object,
            disable_upload=disable_upload,
            domain_names=domain_names,
            edge_lambdas=edge_lambdas,
            enabled=enabled,
            enable_ipv6=enable_ipv6,
            enable_logging=enable_logging,
            error_responses=error_responses,
            geo_restriction=geo_restriction,
            hosted_zone=hosted_zone,
            http_version=http_version,
            log_bucket=log_bucket,
            log_file_prefix=log_file_prefix,
            log_includes_cookies=log_includes_cookies,
            minimum_protocol_version=minimum_protocol_version,
            price_class=price_class,
            removal_policy=removal_policy,
            security_headers_behavior=security_headers_behavior,
            source=source,
            web_acl_id=web_acl_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addBehaviour")
    def add_behaviour(
        self,
        path_pattern: builtins.str,
        origin: aws_cdk.aws_cloudfront.IOrigin,
        *,
        allowed_methods: typing.Optional[aws_cdk.aws_cloudfront.AllowedMethods] = None,
        cached_methods: typing.Optional[aws_cdk.aws_cloudfront.CachedMethods] = None,
        cache_policy: typing.Optional[aws_cdk.aws_cloudfront.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.EdgeLambda]] = None,
        function_associations: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.FunctionAssociation]] = None,
        origin_request_policy: typing.Optional[aws_cdk.aws_cloudfront.IOriginRequestPolicy] = None,
        response_headers_policy: typing.Optional[aws_cdk.aws_cloudfront.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[aws_cdk.aws_cloudfront.ViewerProtocolPolicy] = None,
    ) -> None:
        '''
        :param path_pattern: -
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        behavior_options = aws_cdk.aws_cloudfront.AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            cache_policy=cache_policy,
            compress=compress,
            edge_lambdas=edge_lambdas,
            function_associations=function_associations,
            origin_request_policy=origin_request_policy,
            response_headers_policy=response_headers_policy,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return typing.cast(None, jsii.invoke(self, "addBehaviour", [path_pattern, origin, behavior_options]))

    @jsii.member(jsii_name="createResponseHeadersPolicy")
    def _create_response_headers_policy(
        self,
        security_headers_behavior: typing.Optional[aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior] = None,
        custom_headers: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.ResponseCustomHeader]] = None,
    ) -> aws_cdk.aws_cloudfront.ResponseHeadersPolicy:
        '''
        :param security_headers_behavior: -
        :param custom_headers: -
        '''
        return typing.cast(aws_cdk.aws_cloudfront.ResponseHeadersPolicy, jsii.invoke(self, "createResponseHeadersPolicy", [security_headers_behavior, custom_headers]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> aws_cdk.aws_s3.Bucket:
        return typing.cast(aws_cdk.aws_s3.Bucket, jsii.get(self, "bucket"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> aws_cdk.aws_cloudfront.Distribution:
        return typing.cast(aws_cdk.aws_cloudfront.Distribution, jsii.get(self, "distribution"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-static-website.StaticWebsiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "comment": "comment",
        "custom_headers": "customHeaders",
        "default_root_object": "defaultRootObject",
        "disable_upload": "disableUpload",
        "domain_names": "domainNames",
        "edge_lambdas": "edgeLambdas",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "error_responses": "errorResponses",
        "geo_restriction": "geoRestriction",
        "hosted_zone": "hostedZone",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "security_headers_behavior": "securityHeadersBehavior",
        "source": "source",
        "web_acl_id": "webAclId",
    },
)
class StaticWebsiteProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        custom_headers: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.ResponseCustomHeader]] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        disable_upload: typing.Optional[builtins.bool] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        edge_lambdas: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.EdgeLambda]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        error_responses: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.ErrorResponse]] = None,
        geo_restriction: typing.Optional[aws_cdk.aws_cloudfront.GeoRestriction] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
        http_version: typing.Optional[aws_cdk.aws_cloudfront.HttpVersion] = None,
        log_bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_headers_behavior: typing.Optional[aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior] = None,
        source: typing.Optional[builtins.str] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param custom_headers: A configuration for a set of custom HTTP response headers. Default: - no custom headers behavior
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param disable_upload: Disable website deployment. Default: - false
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - 403 and 404 are routed as 404 to error.html.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param hosted_zone: Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the destination. Domain names in the hosted zone can include a specific domain (example.com) and its subdomains (acme.example.com, zenith.example.com).
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2021
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param security_headers_behavior: Configuration for a set of security-related HTTP response headers. Default: - DefaultSecurityHeadersBehavior
        :param source: The source from which to deploy the website. Default: - Dummy placeholder
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if isinstance(security_headers_behavior, dict):
            security_headers_behavior = aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior(**security_headers_behavior)
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if comment is not None:
            self._values["comment"] = comment
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if disable_upload is not None:
            self._values["disable_upload"] = disable_upload
        if domain_names is not None:
            self._values["domain_names"] = domain_names
        if edge_lambdas is not None:
            self._values["edge_lambdas"] = edge_lambdas
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if error_responses is not None:
            self._values["error_responses"] = error_responses
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone
        if http_version is not None:
            self._values["http_version"] = http_version
        if log_bucket is not None:
            self._values["log_bucket"] = log_bucket
        if log_file_prefix is not None:
            self._values["log_file_prefix"] = log_file_prefix
        if log_includes_cookies is not None:
            self._values["log_includes_cookies"] = log_includes_cookies
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_headers_behavior is not None:
            self._values["security_headers_behavior"] = security_headers_behavior
        if source is not None:
            self._values["source"] = source
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        '''A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[aws_cdk.aws_certificatemanager.ICertificate], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments you want to include about the distribution.

        :default: - no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.ResponseCustomHeader]]:
        '''A configuration for a set of custom HTTP response headers.

        :default: - no custom headers behavior
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudfront.ResponseCustomHeader]], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/).

        :default: - index.html
        '''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_upload(self) -> typing.Optional[builtins.bool]:
        '''Disable website deployment.

        :default: - false
        '''
        result = self._values.get("disable_upload")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names for this distribution.

        If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name,
        you can add an alternate domain name to your distribution. If you attach a certificate to the distribution,
        you must add (at least one of) the domain names of the certificate to this list.

        :default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        '''
        result = self._values.get("domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def edge_lambdas(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.EdgeLambda]]:
        '''The Lambda@Edge functions to invoke before serving the contents.

        :default: - no Lambda functions will be invoked
        '''
        result = self._values.get("edge_lambdas")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudfront.EdgeLambda]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable the distribution.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address.

        If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses.
        This allows viewers to submit a second request, for an IPv4 address for your distribution.

        :default: true
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_logging(self) -> typing.Optional[builtins.bool]:
        '''Enable access logging for the distribution.

        :default: - false, unless ``logBucket`` is specified.
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.ErrorResponse]]:
        '''How CloudFront should handle requests that are not successful (e.g., PageNotFound).

        :default: - 403 and 404 are routed as 404 to error.html.
        '''
        result = self._values.get("error_responses")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudfront.ErrorResponse]], result)

    @builtins.property
    def geo_restriction(self) -> typing.Optional[aws_cdk.aws_cloudfront.GeoRestriction]:
        '''Controls the countries in which your content is distributed.

        :default: - No geographic restrictions
        '''
        result = self._values.get("geo_restriction")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.GeoRestriction], result)

    @builtins.property
    def hosted_zone(self) -> typing.Optional[aws_cdk.aws_route53.IHostedZone]:
        '''Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the destination.

        Domain names in the hosted zone can include a specific domain (example.com)
        and its subdomains (acme.example.com, zenith.example.com).
        '''
        result = self._values.get("hosted_zone")
        return typing.cast(typing.Optional[aws_cdk.aws_route53.IHostedZone], result)

    @builtins.property
    def http_version(self) -> typing.Optional[aws_cdk.aws_cloudfront.HttpVersion]:
        '''Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront.

        For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI).

        :default: HttpVersion.HTTP2
        '''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.HttpVersion], result)

    @builtins.property
    def log_bucket(self) -> typing.Optional[aws_cdk.aws_s3.IBucket]:
        '''The Amazon S3 bucket to store the access logs in.

        :default: - A bucket is created if ``enableLogging`` is true
        '''
        result = self._values.get("log_bucket")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.IBucket], result)

    @builtins.property
    def log_file_prefix(self) -> typing.Optional[builtins.str]:
        '''An optional string that you want CloudFront to prefix to the access log filenames for this distribution.

        :default: - no prefix
        '''
        result = self._values.get("log_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_includes_cookies(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether you want CloudFront to include cookies in access logs.

        :default: false
        '''
        result = self._values.get("log_includes_cookies")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_protocol_version(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol]:
        '''The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        :default: SecurityPolicyProtocol.TLS_V1_2_2021
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol], result)

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_100
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.PriceClass], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''
        :default: Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def security_headers_behavior(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior]:
        '''Configuration for a set of security-related HTTP response headers.

        :default: - DefaultSecurityHeadersBehavior
        '''
        result = self._values.get("security_headers_behavior")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.ResponseSecurityHeadersBehavior], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The source from which to deploy the website.

        :default: - Dummy placeholder
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example
        ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
        To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.

        :default: - No AWS Web Application Firewall web access control list (web ACL).

        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html#API_CreateDistribution_RequestParameters.
        '''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaticWebsiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StaticWebsite",
    "StaticWebsiteProps",
]

publication.publish()
