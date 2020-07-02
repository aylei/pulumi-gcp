// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package redis

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// A Google Cloud Redis instance.
//
// To get more information about Instance, see:
//
// * [API documentation](https://cloud.google.com/memorystore/docs/redis/reference/rest/)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/memorystore/docs/redis/)
//
// ## Example Usage
type Instance struct {
	pulumi.CustomResourceState

	// Only applicable to STANDARD_HA tier which protects the instance
	// against zonal failures by provisioning it across two zones.
	// If provided, it must be a different zone from the one provided in
	// [locationId].
	AlternativeLocationId pulumi.StringOutput `pulumi:"alternativeLocationId"`
	// The full name of the Google Compute Engine network to which the
	// instance is connected. If left unspecified, the default network
	// will be used.
	AuthorizedNetwork pulumi.StringOutput `pulumi:"authorizedNetwork"`
	// The connection mode of the Redis instance.
	ConnectMode pulumi.StringPtrOutput `pulumi:"connectMode"`
	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
	// [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
	// [alternativeLocationId] and can change after a failover event.
	CurrentLocationId pulumi.StringOutput `pulumi:"currentLocationId"`
	// An arbitrary and optional user-provided name for the instance.
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
	Host pulumi.StringOutput `pulumi:"host"`
	// Resource labels to represent user provided metadata.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The zone where the instance will be provisioned. If not provided,
	// the service will choose a zone for the instance. For STANDARD_HA tier,
	// instances will be created across two zones for protection against
	// zonal failures. If [alternativeLocationId] is also provided, it must
	// be different from [locationId].
	LocationId pulumi.StringOutput `pulumi:"locationId"`
	// Redis memory size in GiB.
	MemorySizeGb pulumi.IntOutput `pulumi:"memorySizeGb"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// The port number of the exposed Redis endpoint.
	Port pulumi.IntOutput `pulumi:"port"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Redis configuration parameters, according to http://redis.io/topics/config.
	// Please check Memorystore documentation for the list of supported parameters:
	// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
	RedisConfigs pulumi.StringMapOutput `pulumi:"redisConfigs"`
	// The version of Redis software. If not provided, latest supported
	// version will be used. Currently, the supported values are:
	// - REDIS_4_0 for Redis 4.0 compatibility
	// - REDIS_3_2 for Redis 3.2 compatibility
	RedisVersion pulumi.StringOutput `pulumi:"redisVersion"`
	// The name of the Redis region of the instance.
	Region pulumi.StringOutput `pulumi:"region"`
	// The CIDR range of internal addresses that are reserved for this
	// instance. If not provided, the service will choose an unused /29
	// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
	// unique and non-overlapping with existing subnets in an authorized
	// network.
	ReservedIpRange pulumi.StringOutput `pulumi:"reservedIpRange"`
	// The service tier of the instance. Must be one of these values:
	// - BASIC: standalone instance
	// - STANDARD_HA: highly available primary/replica instances
	Tier pulumi.StringPtrOutput `pulumi:"tier"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil || args.MemorySizeGb == nil {
		return nil, errors.New("missing required argument 'MemorySizeGb'")
	}
	if args == nil {
		args = &InstanceArgs{}
	}
	var resource Instance
	err := ctx.RegisterResource("gcp:redis/instance:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("gcp:redis/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// Only applicable to STANDARD_HA tier which protects the instance
	// against zonal failures by provisioning it across two zones.
	// If provided, it must be a different zone from the one provided in
	// [locationId].
	AlternativeLocationId *string `pulumi:"alternativeLocationId"`
	// The full name of the Google Compute Engine network to which the
	// instance is connected. If left unspecified, the default network
	// will be used.
	AuthorizedNetwork *string `pulumi:"authorizedNetwork"`
	// The connection mode of the Redis instance.
	ConnectMode *string `pulumi:"connectMode"`
	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime *string `pulumi:"createTime"`
	// The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
	// [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
	// [alternativeLocationId] and can change after a failover event.
	CurrentLocationId *string `pulumi:"currentLocationId"`
	// An arbitrary and optional user-provided name for the instance.
	DisplayName *string `pulumi:"displayName"`
	// Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
	Host *string `pulumi:"host"`
	// Resource labels to represent user provided metadata.
	Labels map[string]string `pulumi:"labels"`
	// The zone where the instance will be provisioned. If not provided,
	// the service will choose a zone for the instance. For STANDARD_HA tier,
	// instances will be created across two zones for protection against
	// zonal failures. If [alternativeLocationId] is also provided, it must
	// be different from [locationId].
	LocationId *string `pulumi:"locationId"`
	// Redis memory size in GiB.
	MemorySizeGb *int `pulumi:"memorySizeGb"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name *string `pulumi:"name"`
	// The port number of the exposed Redis endpoint.
	Port *int `pulumi:"port"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Redis configuration parameters, according to http://redis.io/topics/config.
	// Please check Memorystore documentation for the list of supported parameters:
	// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
	RedisConfigs map[string]string `pulumi:"redisConfigs"`
	// The version of Redis software. If not provided, latest supported
	// version will be used. Currently, the supported values are:
	// - REDIS_4_0 for Redis 4.0 compatibility
	// - REDIS_3_2 for Redis 3.2 compatibility
	RedisVersion *string `pulumi:"redisVersion"`
	// The name of the Redis region of the instance.
	Region *string `pulumi:"region"`
	// The CIDR range of internal addresses that are reserved for this
	// instance. If not provided, the service will choose an unused /29
	// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
	// unique and non-overlapping with existing subnets in an authorized
	// network.
	ReservedIpRange *string `pulumi:"reservedIpRange"`
	// The service tier of the instance. Must be one of these values:
	// - BASIC: standalone instance
	// - STANDARD_HA: highly available primary/replica instances
	Tier *string `pulumi:"tier"`
}

type InstanceState struct {
	// Only applicable to STANDARD_HA tier which protects the instance
	// against zonal failures by provisioning it across two zones.
	// If provided, it must be a different zone from the one provided in
	// [locationId].
	AlternativeLocationId pulumi.StringPtrInput
	// The full name of the Google Compute Engine network to which the
	// instance is connected. If left unspecified, the default network
	// will be used.
	AuthorizedNetwork pulumi.StringPtrInput
	// The connection mode of the Redis instance.
	ConnectMode pulumi.StringPtrInput
	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime pulumi.StringPtrInput
	// The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
	// [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
	// [alternativeLocationId] and can change after a failover event.
	CurrentLocationId pulumi.StringPtrInput
	// An arbitrary and optional user-provided name for the instance.
	DisplayName pulumi.StringPtrInput
	// Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
	Host pulumi.StringPtrInput
	// Resource labels to represent user provided metadata.
	Labels pulumi.StringMapInput
	// The zone where the instance will be provisioned. If not provided,
	// the service will choose a zone for the instance. For STANDARD_HA tier,
	// instances will be created across two zones for protection against
	// zonal failures. If [alternativeLocationId] is also provided, it must
	// be different from [locationId].
	LocationId pulumi.StringPtrInput
	// Redis memory size in GiB.
	MemorySizeGb pulumi.IntPtrInput
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringPtrInput
	// The port number of the exposed Redis endpoint.
	Port pulumi.IntPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Redis configuration parameters, according to http://redis.io/topics/config.
	// Please check Memorystore documentation for the list of supported parameters:
	// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
	RedisConfigs pulumi.StringMapInput
	// The version of Redis software. If not provided, latest supported
	// version will be used. Currently, the supported values are:
	// - REDIS_4_0 for Redis 4.0 compatibility
	// - REDIS_3_2 for Redis 3.2 compatibility
	RedisVersion pulumi.StringPtrInput
	// The name of the Redis region of the instance.
	Region pulumi.StringPtrInput
	// The CIDR range of internal addresses that are reserved for this
	// instance. If not provided, the service will choose an unused /29
	// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
	// unique and non-overlapping with existing subnets in an authorized
	// network.
	ReservedIpRange pulumi.StringPtrInput
	// The service tier of the instance. Must be one of these values:
	// - BASIC: standalone instance
	// - STANDARD_HA: highly available primary/replica instances
	Tier pulumi.StringPtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// Only applicable to STANDARD_HA tier which protects the instance
	// against zonal failures by provisioning it across two zones.
	// If provided, it must be a different zone from the one provided in
	// [locationId].
	AlternativeLocationId *string `pulumi:"alternativeLocationId"`
	// The full name of the Google Compute Engine network to which the
	// instance is connected. If left unspecified, the default network
	// will be used.
	AuthorizedNetwork *string `pulumi:"authorizedNetwork"`
	// The connection mode of the Redis instance.
	ConnectMode *string `pulumi:"connectMode"`
	// An arbitrary and optional user-provided name for the instance.
	DisplayName *string `pulumi:"displayName"`
	// Resource labels to represent user provided metadata.
	Labels map[string]string `pulumi:"labels"`
	// The zone where the instance will be provisioned. If not provided,
	// the service will choose a zone for the instance. For STANDARD_HA tier,
	// instances will be created across two zones for protection against
	// zonal failures. If [alternativeLocationId] is also provided, it must
	// be different from [locationId].
	LocationId *string `pulumi:"locationId"`
	// Redis memory size in GiB.
	MemorySizeGb int `pulumi:"memorySizeGb"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Redis configuration parameters, according to http://redis.io/topics/config.
	// Please check Memorystore documentation for the list of supported parameters:
	// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
	RedisConfigs map[string]string `pulumi:"redisConfigs"`
	// The version of Redis software. If not provided, latest supported
	// version will be used. Currently, the supported values are:
	// - REDIS_4_0 for Redis 4.0 compatibility
	// - REDIS_3_2 for Redis 3.2 compatibility
	RedisVersion *string `pulumi:"redisVersion"`
	// The name of the Redis region of the instance.
	Region *string `pulumi:"region"`
	// The CIDR range of internal addresses that are reserved for this
	// instance. If not provided, the service will choose an unused /29
	// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
	// unique and non-overlapping with existing subnets in an authorized
	// network.
	ReservedIpRange *string `pulumi:"reservedIpRange"`
	// The service tier of the instance. Must be one of these values:
	// - BASIC: standalone instance
	// - STANDARD_HA: highly available primary/replica instances
	Tier *string `pulumi:"tier"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// Only applicable to STANDARD_HA tier which protects the instance
	// against zonal failures by provisioning it across two zones.
	// If provided, it must be a different zone from the one provided in
	// [locationId].
	AlternativeLocationId pulumi.StringPtrInput
	// The full name of the Google Compute Engine network to which the
	// instance is connected. If left unspecified, the default network
	// will be used.
	AuthorizedNetwork pulumi.StringPtrInput
	// The connection mode of the Redis instance.
	ConnectMode pulumi.StringPtrInput
	// An arbitrary and optional user-provided name for the instance.
	DisplayName pulumi.StringPtrInput
	// Resource labels to represent user provided metadata.
	Labels pulumi.StringMapInput
	// The zone where the instance will be provisioned. If not provided,
	// the service will choose a zone for the instance. For STANDARD_HA tier,
	// instances will be created across two zones for protection against
	// zonal failures. If [alternativeLocationId] is also provided, it must
	// be different from [locationId].
	LocationId pulumi.StringPtrInput
	// Redis memory size in GiB.
	MemorySizeGb pulumi.IntInput
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Redis configuration parameters, according to http://redis.io/topics/config.
	// Please check Memorystore documentation for the list of supported parameters:
	// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
	RedisConfigs pulumi.StringMapInput
	// The version of Redis software. If not provided, latest supported
	// version will be used. Currently, the supported values are:
	// - REDIS_4_0 for Redis 4.0 compatibility
	// - REDIS_3_2 for Redis 3.2 compatibility
	RedisVersion pulumi.StringPtrInput
	// The name of the Redis region of the instance.
	Region pulumi.StringPtrInput
	// The CIDR range of internal addresses that are reserved for this
	// instance. If not provided, the service will choose an unused /29
	// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
	// unique and non-overlapping with existing subnets in an authorized
	// network.
	ReservedIpRange pulumi.StringPtrInput
	// The service tier of the instance. Must be one of these values:
	// - BASIC: standalone instance
	// - STANDARD_HA: highly available primary/replica instances
	Tier pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}
