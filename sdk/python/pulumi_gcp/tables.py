# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

_SNAKE_TO_CAMEL_CASE_TABLE = {
    "accelerator_type": "acceleratorType",
    "access_token": "accessToken",
    "account_id": "accountId",
    "ack_deadline_seconds": "ackDeadlineSeconds",
    "additional_zones": "additionalZones",
    "addons_config": "addonsConfig",
    "address_type": "addressType",
    "admission_whitelist_patterns": "admissionWhitelistPatterns",
    "advertised_route_priority": "advertisedRoutePriority",
    "affinity_cookie_ttl_sec": "affinityCookieTtlSec",
    "all_ports": "allPorts",
    "allow_stopping_for_update": "allowStoppingForUpdate",
    "alternative_location_id": "alternativeLocationId",
    "alternative_name_server_config": "alternativeNameServerConfig",
    "app_engine_http_target": "appEngineHttpTarget",
    "archive_size_bytes": "archiveSizeBytes",
    "attached_disks": "attachedDisks",
    "attestation_authority": "attestationAuthority",
    "attestation_authority_note": "attestationAuthorityNote",
    "audit_log_configs": "auditLogConfigs",
    "auth_domain": "authDomain",
    "authorized_network": "authorizedNetwork",
    "auto_create_network": "autoCreateNetwork",
    "auto_create_routes": "autoCreateRoutes",
    "auto_create_subnetworks": "autoCreateSubnetworks",
    "auto_healing_policies": "autoHealingPolicies",
    "autoscaling_policy": "autoscalingPolicy",
    "available_memory_mb": "availableMemoryMb",
    "backend_service": "backendService",
    "backup_pool": "backupPool",
    "base_instance_name": "baseInstanceName",
    "billing_account": "billingAccount",
    "billing_account_id": "billingAccountId",
    "boolean_policy": "booleanPolicy",
    "boot_disk": "bootDisk",
    "bucket_name": "bucketName",
    "cache_control": "cacheControl",
    "can_ip_forward": "canIpForward",
    "candidate_subnets": "candidateSubnets",
    "cdn_policy": "cdnPolicy",
    "cert_serial_number": "certSerialNumber",
    "certificate_id": "certificateId",
    "check_interval_sec": "checkIntervalSec",
    "cidr_block": "cidrBlock",
    "cloud_router_ip_address": "cloudRouterIpAddress",
    "cluster_admission_rules": "clusterAdmissionRules",
    "cluster_autoscaling": "clusterAutoscaling",
    "cluster_config": "clusterConfig",
    "cluster_ipv4_cidr": "clusterIpv4Cidr",
    "code_bucket": "codeBucket",
    "column_families": "columnFamilies",
    "common_name": "commonName",
    "config_id": "configId",
    "connection_draining_timeout_sec": "connectionDrainingTimeoutSec",
    "connection_name": "connectionName",
    "content_disposition": "contentDisposition",
    "content_encoding": "contentEncoding",
    "content_language": "contentLanguage",
    "content_matchers": "contentMatchers",
    "content_type": "contentType",
    "cpu_platform": "cpuPlatform",
    "create_time": "createTime",
    "creation_record": "creationRecord",
    "creation_time": "creationTime",
    "creation_timestamp": "creationTimestamp",
    "crypto_key_id": "cryptoKeyId",
    "current_location_id": "currentLocationId",
    "custom_attributes": "customAttributes",
    "custom_features": "customFeatures",
    "custom_request_headers": "customRequestHeaders",
    "customer_router_ip_address": "customerRouterIpAddress",
    "database_version": "databaseVersion",
    "dataset_id": "datasetId",
    "default_acl": "defaultAcl",
    "default_admission_rule": "defaultAdmissionRule",
    "default_bucket": "defaultBucket",
    "default_hostname": "defaultHostname",
    "default_max_pods_per_node": "defaultMaxPodsPerNode",
    "default_partition_expiration_ms": "defaultPartitionExpirationMs",
    "default_service": "defaultService",
    "default_table_expiration_ms": "defaultTableExpirationMs",
    "delete_contents_on_destroy": "deleteContentsOnDestroy",
    "deletion_protection": "deletionProtection",
    "deletion_time": "deletionTime",
    "dest_range": "destRange",
    "destination_ranges": "destinationRanges",
    "detailed_status": "detailedStatus",
    "detect_md5hash": "detectMd5hash",
    "device_name": "deviceName",
    "disable_dependent_services": "disableDependentServices",
    "disable_on_destroy": "disableOnDestroy",
    "disk_encryption_key": "diskEncryptionKey",
    "disk_size_gb": "diskSizeGb",
    "display_name": "displayName",
    "distribution_policy_zones": "distributionPolicyZones",
    "dns_address": "dnsAddress",
    "dns_name": "dnsName",
    "driver_controls_files_uri": "driverControlsFilesUri",
    "driver_output_resource_uri": "driverOutputResourceUri",
    "edge_availability_domain": "edgeAvailabilityDomain",
    "enable_binary_authorization": "enableBinaryAuthorization",
    "enable_cdn": "enableCdn",
    "enable_flow_logs": "enableFlowLogs",
    "enable_inbound_forwarding": "enableInboundForwarding",
    "enable_kubernetes_alpha": "enableKubernetesAlpha",
    "enable_legacy_abac": "enableLegacyAbac",
    "enable_logging": "enableLogging",
    "enable_tpu": "enableTpu",
    "enabled_features": "enabledFeatures",
    "entity_id": "entityId",
    "entry_point": "entryPoint",
    "environment_variables": "environmentVariables",
    "event_notification_config": "eventNotificationConfig",
    "event_trigger": "eventTrigger",
    "event_types": "eventTypes",
    "expiration_time": "expirationTime",
    "expire_time": "expireTime",
    "failover_ratio": "failoverRatio",
    "feature_settings": "featureSettings",
    "file_shares": "fileShares",
    "first_ip_address": "firstIpAddress",
    "folder_id": "folderId",
    "force_delete": "forceDelete",
    "force_destroy": "forceDestroy",
    "forwarding_config": "forwardingConfig",
    "friendly_name": "friendlyName",
    "gateway_address": "gatewayAddress",
    "gateway_ipv4": "gatewayIpv4",
    "gcr_domain": "gcrDomain",
    "google_reference_id": "googleReferenceId",
    "grpc_config": "grpcConfig",
    "guest_accelerators": "guestAccelerators",
    "hadoop_config": "hadoopConfig",
    "health_checks": "healthChecks",
    "healthy_threshold": "healthyThreshold",
    "hive_config": "hiveConfig",
    "host_project": "hostProject",
    "host_rules": "hostRules",
    "http_check": "httpCheck",
    "http_config": "httpConfig",
    "http_enabled_state": "httpEnabledState",
    "http_health_check": "httpHealthCheck",
    "http_target": "httpTarget",
    "https_health_check": "httpsHealthCheck",
    "https_trigger_url": "httpsTriggerUrl",
    "icmp_idle_timeout_sec": "icmpIdleTimeoutSec",
    "ignored_files": "ignoredFiles",
    "ike_version": "ikeVersion",
    "include_children": "includeChildren",
    "included_files": "includedFiles",
    "initial_node_count": "initialNodeCount",
    "instance_description": "instanceDescription",
    "instance_group": "instanceGroup",
    "instance_group_urls": "instanceGroupUrls",
    "instance_id": "instanceId",
    "instance_name": "instanceName",
    "instance_type": "instanceType",
    "internal_checkers": "internalCheckers",
    "ip_address": "ipAddress",
    "ip_addresses": "ipAddresses",
    "ip_allocation_policy": "ipAllocationPolicy",
    "ip_cidr_range": "ipCidrRange",
    "ip_protocol": "ipProtocol",
    "ip_range": "ipRange",
    "ip_version": "ipVersion",
    "ipv4_range": "ipv4Range",
    "is_cluster": "isCluster",
    "is_internal": "isInternal",
    "key_algorithm": "keyAlgorithm",
    "key_ring": "keyRing",
    "key_ring_id": "keyRingId",
    "label_fingerprint": "labelFingerprint",
    "last_attach_timestamp": "lastAttachTimestamp",
    "last_detach_timestamp": "lastDetachTimestamp",
    "last_modification_time": "lastModificationTime",
    "last_modified_time": "lastModifiedTime",
    "lifecycle_rules": "lifecycleRules",
    "lifecycle_state": "lifecycleState",
    "list_policy": "listPolicy",
    "load_balancing_scheme": "loadBalancingScheme",
    "local_traffic_selectors": "localTrafficSelectors",
    "location_id": "locationId",
    "logging_service": "loggingService",
    "machine_type": "machineType",
    "maintenance_policy": "maintenancePolicy",
    "managed_zone": "managedZone",
    "map_id": "mapId",
    "master_auth": "masterAuth",
    "master_authorized_networks_config": "masterAuthorizedNetworksConfig",
    "master_instance_name": "masterInstanceName",
    "master_version": "masterVersion",
    "max_pods_per_node": "maxPodsPerNode",
    "max_workers": "maxWorkers",
    "memory_size_gb": "memorySizeGb",
    "message_retention_duration": "messageRetentionDuration",
    "metadata_fingerprint": "metadataFingerprint",
    "metadata_startup_script": "metadataStartupScript",
    "min_cpu_platform": "minCpuPlatform",
    "min_master_version": "minMasterVersion",
    "min_ports_per_vm": "minPortsPerVm",
    "min_tls_version": "minTlsVersion",
    "monitored_resource": "monitoredResource",
    "monitoring_service": "monitoringService",
    "mqtt_config": "mqttConfig",
    "mqtt_enabled_state": "mqttEnabledState",
    "name_prefix": "namePrefix",
    "name_servers": "nameServers",
    "named_ports": "namedPorts",
    "nat_ip_allocate_option": "natIpAllocateOption",
    "nat_ips": "natIps",
    "network_endpoints": "networkEndpoints",
    "network_interfaces": "networkInterfaces",
    "network_policy": "networkPolicy",
    "network_tier": "networkTier",
    "next_hop_gateway": "nextHopGateway",
    "next_hop_instance": "nextHopInstance",
    "next_hop_instance_zone": "nextHopInstanceZone",
    "next_hop_ip": "nextHopIp",
    "next_hop_network": "nextHopNetwork",
    "next_hop_vpn_tunnel": "nextHopVpnTunnel",
    "node_config": "nodeConfig",
    "node_count": "nodeCount",
    "node_locations": "nodeLocations",
    "node_pools": "nodePools",
    "node_version": "nodeVersion",
    "notification_channels": "notificationChannels",
    "num_bytes": "numBytes",
    "num_long_term_bytes": "numLongTermBytes",
    "num_nodes": "numNodes",
    "num_rows": "numRows",
    "object_name_prefix": "objectNamePrefix",
    "on_delete": "onDelete",
    "openapi_config": "openapiConfig",
    "org_id": "orgId",
    "output_name": "outputName",
    "pairing_key": "pairingKey",
    "parent_name": "parentName",
    "partner_asn": "partnerAsn",
    "path_matchers": "pathMatchers",
    "payload_format": "payloadFormat",
    "peer_asn": "peerAsn",
    "peer_ip": "peerIp",
    "peer_ip_address": "peerIpAddress",
    "peer_network": "peerNetwork",
    "perimeter_type": "perimeterType",
    "pgp_key": "pgpKey",
    "physical_block_size_bytes": "physicalBlockSizeBytes",
    "pig_config": "pigConfig",
    "pod_security_policy_config": "podSecurityPolicyConfig",
    "policy_data": "policyData",
    "port_name": "portName",
    "port_range": "portRange",
    "predefined_acl": "predefinedAcl",
    "prefix_length": "prefixLength",
    "private_cluster_config": "privateClusterConfig",
    "private_interconnect_info": "privateInterconnectInfo",
    "private_ip_address": "privateIpAddress",
    "private_ip_google_access": "privateIpGoogleAccess",
    "private_key": "privateKey",
    "private_key_encrypted": "privateKeyEncrypted",
    "private_key_fingerprint": "privateKeyFingerprint",
    "private_key_type": "privateKeyType",
    "private_visibility_config": "privateVisibilityConfig",
    "project_id": "projectId",
    "project_team": "projectTeam",
    "protoc_output_base64": "protocOutputBase64",
    "proxy_header": "proxyHeader",
    "proxy_id": "proxyId",
    "public_ip_address": "publicIpAddress",
    "public_key": "publicKey",
    "public_key_type": "publicKeyType",
    "pubsub_target": "pubsubTarget",
    "pubsub_topic_name": "pubsubTopicName",
    "push_config": "pushConfig",
    "pyspark_config": "pysparkConfig",
    "quic_override": "quicOverride",
    "raw_disk": "rawDisk",
    "redis_configs": "redisConfigs",
    "redis_version": "redisVersion",
    "remote_traffic_selectors": "remoteTrafficSelectors",
    "remove_default_node_pool": "removeDefaultNodePool",
    "replica_configuration": "replicaConfiguration",
    "replica_zones": "replicaZones",
    "request_path": "requestPath",
    "requester_pays": "requesterPays",
    "reserved_ip_range": "reservedIpRange",
    "reserved_peering_ranges": "reservedPeeringRanges",
    "resource_group": "resourceGroup",
    "resource_labels": "resourceLabels",
    "restore_policy": "restorePolicy",
    "retain_acked_messages": "retainAckedMessages",
    "retry_config": "retryConfig",
    "role_entities": "roleEntities",
    "role_id": "roleId",
    "rotation_period": "rotationPeriod",
    "routing_mode": "routingMode",
    "scheduling_config": "schedulingConfig",
    "scratch_disks": "scratchDisks",
    "secondary_ip_ranges": "secondaryIpRanges",
    "security_policy": "securityPolicy",
    "selected_regions": "selectedRegions",
    "self_link": "selfLink",
    "server_ca_cert": "serverCaCert",
    "service_account": "serviceAccount",
    "service_account_email": "serviceAccountEmail",
    "service_account_email_address": "serviceAccountEmailAddress",
    "service_account_id": "serviceAccountId",
    "service_label": "serviceLabel",
    "service_name": "serviceName",
    "service_project": "serviceProject",
    "serving_status": "servingStatus",
    "session_affinity": "sessionAffinity",
    "sha1_fingerprint": "sha1Fingerprint",
    "shared_secret": "sharedSecret",
    "shared_secret_hash": "sharedSecretHash",
    "skip_delete": "skipDelete",
    "snapshot_encryption_key": "snapshotEncryptionKey",
    "snapshot_id": "snapshotId",
    "source_archive_bucket": "sourceArchiveBucket",
    "source_archive_object": "sourceArchiveObject",
    "source_disk": "sourceDisk",
    "source_disk_encryption_key": "sourceDiskEncryptionKey",
    "source_disk_link": "sourceDiskLink",
    "source_image_encryption_key": "sourceImageEncryptionKey",
    "source_image_id": "sourceImageId",
    "source_instance_template": "sourceInstanceTemplate",
    "source_range": "sourceRange",
    "source_ranges": "sourceRanges",
    "source_repository": "sourceRepository",
    "source_service_accounts": "sourceServiceAccounts",
    "source_snapshot_encryption_key": "sourceSnapshotEncryptionKey",
    "source_snapshot_id": "sourceSnapshotId",
    "source_subnetwork_ip_ranges_to_nat": "sourceSubnetworkIpRangesToNat",
    "source_tags": "sourceTags",
    "spark_config": "sparkConfig",
    "sparksql_config": "sparksqlConfig",
    "split_keys": "splitKeys",
    "ssl_certificates": "sslCertificates",
    "ssl_health_check": "sslHealthCheck",
    "ssl_policy": "sslPolicy",
    "state_details": "stateDetails",
    "state_notification_config": "stateNotificationConfig",
    "storage_bytes": "storageBytes",
    "storage_class": "storageClass",
    "subject_alternative_names": "subjectAlternativeNames",
    "table_id": "tableId",
    "tags_fingerprint": "tagsFingerprint",
    "target_pools": "targetPools",
    "target_service_accounts": "targetServiceAccounts",
    "target_size": "targetSize",
    "target_tags": "targetTags",
    "target_vpn_gateway": "targetVpnGateway",
    "tcp_check": "tcpCheck",
    "tcp_established_idle_timeout_sec": "tcpEstablishedIdleTimeoutSec",
    "tcp_health_check": "tcpHealthCheck",
    "tcp_transitory_idle_timeout_sec": "tcpTransitoryIdleTimeoutSec",
    "temp_gcs_location": "tempGcsLocation",
    "template_gcs_path": "templateGcsPath",
    "tensorflow_version": "tensorflowVersion",
    "time_partitioning": "timePartitioning",
    "time_zone": "timeZone",
    "timeout_sec": "timeoutSec",
    "tpu_ipv4_cidr_block": "tpuIpv4CidrBlock",
    "transfer_spec": "transferSpec",
    "trigger_http": "triggerHttp",
    "trigger_id": "triggerId",
    "trigger_template": "triggerTemplate",
    "udp_idle_timeout_sec": "udpIdleTimeoutSec",
    "unhealthy_threshold": "unhealthyThreshold",
    "unique_id": "uniqueId",
    "unique_writer_identity": "uniqueWriterIdentity",
    "update_policy": "updatePolicy",
    "update_time": "updateTime",
    "uptime_check_id": "uptimeCheckId",
    "url_dispatch_rules": "urlDispatchRules",
    "url_map": "urlMap",
    "user_labels": "userLabels",
    "valid_after": "validAfter",
    "valid_before": "validBefore",
    "verification_status": "verificationStatus",
    "version_template": "versionTemplate",
    "vlan_tag8021q": "vlanTag8021q",
    "vpn_tunnel": "vpnTunnel",
    "wait_for_instances": "waitForInstances",
    "writer_identity": "writerIdentity",
}

_CAMEL_TO_SNAKE_CASE_TABLE = {
    "acceleratorType": "accelerator_type",
    "accessToken": "access_token",
    "accountId": "account_id",
    "ackDeadlineSeconds": "ack_deadline_seconds",
    "additionalZones": "additional_zones",
    "addonsConfig": "addons_config",
    "addressType": "address_type",
    "admissionWhitelistPatterns": "admission_whitelist_patterns",
    "advertisedRoutePriority": "advertised_route_priority",
    "affinityCookieTtlSec": "affinity_cookie_ttl_sec",
    "allPorts": "all_ports",
    "allowStoppingForUpdate": "allow_stopping_for_update",
    "alternativeLocationId": "alternative_location_id",
    "alternativeNameServerConfig": "alternative_name_server_config",
    "appEngineHttpTarget": "app_engine_http_target",
    "archiveSizeBytes": "archive_size_bytes",
    "attachedDisks": "attached_disks",
    "attestationAuthority": "attestation_authority",
    "attestationAuthorityNote": "attestation_authority_note",
    "auditLogConfigs": "audit_log_configs",
    "authDomain": "auth_domain",
    "authorizedNetwork": "authorized_network",
    "autoCreateNetwork": "auto_create_network",
    "autoCreateRoutes": "auto_create_routes",
    "autoCreateSubnetworks": "auto_create_subnetworks",
    "autoHealingPolicies": "auto_healing_policies",
    "autoscalingPolicy": "autoscaling_policy",
    "availableMemoryMb": "available_memory_mb",
    "backendService": "backend_service",
    "backupPool": "backup_pool",
    "baseInstanceName": "base_instance_name",
    "billingAccount": "billing_account",
    "billingAccountId": "billing_account_id",
    "booleanPolicy": "boolean_policy",
    "bootDisk": "boot_disk",
    "bucketName": "bucket_name",
    "cacheControl": "cache_control",
    "canIpForward": "can_ip_forward",
    "candidateSubnets": "candidate_subnets",
    "cdnPolicy": "cdn_policy",
    "certSerialNumber": "cert_serial_number",
    "certificateId": "certificate_id",
    "checkIntervalSec": "check_interval_sec",
    "cidrBlock": "cidr_block",
    "cloudRouterIpAddress": "cloud_router_ip_address",
    "clusterAdmissionRules": "cluster_admission_rules",
    "clusterAutoscaling": "cluster_autoscaling",
    "clusterConfig": "cluster_config",
    "clusterIpv4Cidr": "cluster_ipv4_cidr",
    "codeBucket": "code_bucket",
    "columnFamilies": "column_families",
    "commonName": "common_name",
    "configId": "config_id",
    "connectionDrainingTimeoutSec": "connection_draining_timeout_sec",
    "connectionName": "connection_name",
    "contentDisposition": "content_disposition",
    "contentEncoding": "content_encoding",
    "contentLanguage": "content_language",
    "contentMatchers": "content_matchers",
    "contentType": "content_type",
    "cpuPlatform": "cpu_platform",
    "createTime": "create_time",
    "creationRecord": "creation_record",
    "creationTime": "creation_time",
    "creationTimestamp": "creation_timestamp",
    "cryptoKeyId": "crypto_key_id",
    "currentLocationId": "current_location_id",
    "customAttributes": "custom_attributes",
    "customFeatures": "custom_features",
    "customRequestHeaders": "custom_request_headers",
    "customerRouterIpAddress": "customer_router_ip_address",
    "databaseVersion": "database_version",
    "datasetId": "dataset_id",
    "defaultAcl": "default_acl",
    "defaultAdmissionRule": "default_admission_rule",
    "defaultBucket": "default_bucket",
    "defaultHostname": "default_hostname",
    "defaultMaxPodsPerNode": "default_max_pods_per_node",
    "defaultPartitionExpirationMs": "default_partition_expiration_ms",
    "defaultService": "default_service",
    "defaultTableExpirationMs": "default_table_expiration_ms",
    "deleteContentsOnDestroy": "delete_contents_on_destroy",
    "deletionProtection": "deletion_protection",
    "deletionTime": "deletion_time",
    "destRange": "dest_range",
    "destinationRanges": "destination_ranges",
    "detailedStatus": "detailed_status",
    "detectMd5hash": "detect_md5hash",
    "deviceName": "device_name",
    "disableDependentServices": "disable_dependent_services",
    "disableOnDestroy": "disable_on_destroy",
    "diskEncryptionKey": "disk_encryption_key",
    "diskSizeGb": "disk_size_gb",
    "displayName": "display_name",
    "distributionPolicyZones": "distribution_policy_zones",
    "dnsAddress": "dns_address",
    "dnsName": "dns_name",
    "driverControlsFilesUri": "driver_controls_files_uri",
    "driverOutputResourceUri": "driver_output_resource_uri",
    "edgeAvailabilityDomain": "edge_availability_domain",
    "enableBinaryAuthorization": "enable_binary_authorization",
    "enableCdn": "enable_cdn",
    "enableFlowLogs": "enable_flow_logs",
    "enableInboundForwarding": "enable_inbound_forwarding",
    "enableKubernetesAlpha": "enable_kubernetes_alpha",
    "enableLegacyAbac": "enable_legacy_abac",
    "enableLogging": "enable_logging",
    "enableTpu": "enable_tpu",
    "enabledFeatures": "enabled_features",
    "entityId": "entity_id",
    "entryPoint": "entry_point",
    "environmentVariables": "environment_variables",
    "eventNotificationConfig": "event_notification_config",
    "eventTrigger": "event_trigger",
    "eventTypes": "event_types",
    "expirationTime": "expiration_time",
    "expireTime": "expire_time",
    "failoverRatio": "failover_ratio",
    "featureSettings": "feature_settings",
    "fileShares": "file_shares",
    "firstIpAddress": "first_ip_address",
    "folderId": "folder_id",
    "forceDelete": "force_delete",
    "forceDestroy": "force_destroy",
    "forwardingConfig": "forwarding_config",
    "friendlyName": "friendly_name",
    "gatewayAddress": "gateway_address",
    "gatewayIpv4": "gateway_ipv4",
    "gcrDomain": "gcr_domain",
    "googleReferenceId": "google_reference_id",
    "grpcConfig": "grpc_config",
    "guestAccelerators": "guest_accelerators",
    "hadoopConfig": "hadoop_config",
    "healthChecks": "health_checks",
    "healthyThreshold": "healthy_threshold",
    "hiveConfig": "hive_config",
    "hostProject": "host_project",
    "hostRules": "host_rules",
    "httpCheck": "http_check",
    "httpConfig": "http_config",
    "httpEnabledState": "http_enabled_state",
    "httpHealthCheck": "http_health_check",
    "httpTarget": "http_target",
    "httpsHealthCheck": "https_health_check",
    "httpsTriggerUrl": "https_trigger_url",
    "icmpIdleTimeoutSec": "icmp_idle_timeout_sec",
    "ignoredFiles": "ignored_files",
    "ikeVersion": "ike_version",
    "includeChildren": "include_children",
    "includedFiles": "included_files",
    "initialNodeCount": "initial_node_count",
    "instanceDescription": "instance_description",
    "instanceGroup": "instance_group",
    "instanceGroupUrls": "instance_group_urls",
    "instanceId": "instance_id",
    "instanceName": "instance_name",
    "instanceType": "instance_type",
    "internalCheckers": "internal_checkers",
    "ipAddress": "ip_address",
    "ipAddresses": "ip_addresses",
    "ipAllocationPolicy": "ip_allocation_policy",
    "ipCidrRange": "ip_cidr_range",
    "ipProtocol": "ip_protocol",
    "ipRange": "ip_range",
    "ipVersion": "ip_version",
    "ipv4Range": "ipv4_range",
    "isCluster": "is_cluster",
    "isInternal": "is_internal",
    "keyAlgorithm": "key_algorithm",
    "keyRing": "key_ring",
    "keyRingId": "key_ring_id",
    "labelFingerprint": "label_fingerprint",
    "lastAttachTimestamp": "last_attach_timestamp",
    "lastDetachTimestamp": "last_detach_timestamp",
    "lastModificationTime": "last_modification_time",
    "lastModifiedTime": "last_modified_time",
    "lifecycleRules": "lifecycle_rules",
    "lifecycleState": "lifecycle_state",
    "listPolicy": "list_policy",
    "loadBalancingScheme": "load_balancing_scheme",
    "localTrafficSelectors": "local_traffic_selectors",
    "locationId": "location_id",
    "loggingService": "logging_service",
    "machineType": "machine_type",
    "maintenancePolicy": "maintenance_policy",
    "managedZone": "managed_zone",
    "mapId": "map_id",
    "masterAuth": "master_auth",
    "masterAuthorizedNetworksConfig": "master_authorized_networks_config",
    "masterInstanceName": "master_instance_name",
    "masterVersion": "master_version",
    "maxPodsPerNode": "max_pods_per_node",
    "maxWorkers": "max_workers",
    "memorySizeGb": "memory_size_gb",
    "messageRetentionDuration": "message_retention_duration",
    "metadataFingerprint": "metadata_fingerprint",
    "metadataStartupScript": "metadata_startup_script",
    "minCpuPlatform": "min_cpu_platform",
    "minMasterVersion": "min_master_version",
    "minPortsPerVm": "min_ports_per_vm",
    "minTlsVersion": "min_tls_version",
    "monitoredResource": "monitored_resource",
    "monitoringService": "monitoring_service",
    "mqttConfig": "mqtt_config",
    "mqttEnabledState": "mqtt_enabled_state",
    "namePrefix": "name_prefix",
    "nameServers": "name_servers",
    "namedPorts": "named_ports",
    "natIpAllocateOption": "nat_ip_allocate_option",
    "natIps": "nat_ips",
    "networkEndpoints": "network_endpoints",
    "networkInterfaces": "network_interfaces",
    "networkPolicy": "network_policy",
    "networkTier": "network_tier",
    "nextHopGateway": "next_hop_gateway",
    "nextHopInstance": "next_hop_instance",
    "nextHopInstanceZone": "next_hop_instance_zone",
    "nextHopIp": "next_hop_ip",
    "nextHopNetwork": "next_hop_network",
    "nextHopVpnTunnel": "next_hop_vpn_tunnel",
    "nodeConfig": "node_config",
    "nodeCount": "node_count",
    "nodeLocations": "node_locations",
    "nodePools": "node_pools",
    "nodeVersion": "node_version",
    "notificationChannels": "notification_channels",
    "numBytes": "num_bytes",
    "numLongTermBytes": "num_long_term_bytes",
    "numNodes": "num_nodes",
    "numRows": "num_rows",
    "objectNamePrefix": "object_name_prefix",
    "onDelete": "on_delete",
    "openapiConfig": "openapi_config",
    "orgId": "org_id",
    "outputName": "output_name",
    "pairingKey": "pairing_key",
    "parentName": "parent_name",
    "partnerAsn": "partner_asn",
    "pathMatchers": "path_matchers",
    "payloadFormat": "payload_format",
    "peerAsn": "peer_asn",
    "peerIp": "peer_ip",
    "peerIpAddress": "peer_ip_address",
    "peerNetwork": "peer_network",
    "perimeterType": "perimeter_type",
    "pgpKey": "pgp_key",
    "physicalBlockSizeBytes": "physical_block_size_bytes",
    "pigConfig": "pig_config",
    "podSecurityPolicyConfig": "pod_security_policy_config",
    "policyData": "policy_data",
    "portName": "port_name",
    "portRange": "port_range",
    "predefinedAcl": "predefined_acl",
    "prefixLength": "prefix_length",
    "privateClusterConfig": "private_cluster_config",
    "privateInterconnectInfo": "private_interconnect_info",
    "privateIpAddress": "private_ip_address",
    "privateIpGoogleAccess": "private_ip_google_access",
    "privateKey": "private_key",
    "privateKeyEncrypted": "private_key_encrypted",
    "privateKeyFingerprint": "private_key_fingerprint",
    "privateKeyType": "private_key_type",
    "privateVisibilityConfig": "private_visibility_config",
    "projectId": "project_id",
    "projectTeam": "project_team",
    "protocOutputBase64": "protoc_output_base64",
    "proxyHeader": "proxy_header",
    "proxyId": "proxy_id",
    "publicIpAddress": "public_ip_address",
    "publicKey": "public_key",
    "publicKeyType": "public_key_type",
    "pubsubTarget": "pubsub_target",
    "pubsubTopicName": "pubsub_topic_name",
    "pushConfig": "push_config",
    "pysparkConfig": "pyspark_config",
    "quicOverride": "quic_override",
    "rawDisk": "raw_disk",
    "redisConfigs": "redis_configs",
    "redisVersion": "redis_version",
    "remoteTrafficSelectors": "remote_traffic_selectors",
    "removeDefaultNodePool": "remove_default_node_pool",
    "replicaConfiguration": "replica_configuration",
    "replicaZones": "replica_zones",
    "requestPath": "request_path",
    "requesterPays": "requester_pays",
    "reservedIpRange": "reserved_ip_range",
    "reservedPeeringRanges": "reserved_peering_ranges",
    "resourceGroup": "resource_group",
    "resourceLabels": "resource_labels",
    "restorePolicy": "restore_policy",
    "retainAckedMessages": "retain_acked_messages",
    "retryConfig": "retry_config",
    "roleEntities": "role_entities",
    "roleId": "role_id",
    "rotationPeriod": "rotation_period",
    "routingMode": "routing_mode",
    "schedulingConfig": "scheduling_config",
    "scratchDisks": "scratch_disks",
    "secondaryIpRanges": "secondary_ip_ranges",
    "securityPolicy": "security_policy",
    "selectedRegions": "selected_regions",
    "selfLink": "self_link",
    "serverCaCert": "server_ca_cert",
    "serviceAccount": "service_account",
    "serviceAccountEmail": "service_account_email",
    "serviceAccountEmailAddress": "service_account_email_address",
    "serviceAccountId": "service_account_id",
    "serviceLabel": "service_label",
    "serviceName": "service_name",
    "serviceProject": "service_project",
    "servingStatus": "serving_status",
    "sessionAffinity": "session_affinity",
    "sha1Fingerprint": "sha1_fingerprint",
    "sharedSecret": "shared_secret",
    "sharedSecretHash": "shared_secret_hash",
    "skipDelete": "skip_delete",
    "snapshotEncryptionKey": "snapshot_encryption_key",
    "snapshotId": "snapshot_id",
    "sourceArchiveBucket": "source_archive_bucket",
    "sourceArchiveObject": "source_archive_object",
    "sourceDisk": "source_disk",
    "sourceDiskEncryptionKey": "source_disk_encryption_key",
    "sourceDiskLink": "source_disk_link",
    "sourceImageEncryptionKey": "source_image_encryption_key",
    "sourceImageId": "source_image_id",
    "sourceInstanceTemplate": "source_instance_template",
    "sourceRange": "source_range",
    "sourceRanges": "source_ranges",
    "sourceRepository": "source_repository",
    "sourceServiceAccounts": "source_service_accounts",
    "sourceSnapshotEncryptionKey": "source_snapshot_encryption_key",
    "sourceSnapshotId": "source_snapshot_id",
    "sourceSubnetworkIpRangesToNat": "source_subnetwork_ip_ranges_to_nat",
    "sourceTags": "source_tags",
    "sparkConfig": "spark_config",
    "sparksqlConfig": "sparksql_config",
    "splitKeys": "split_keys",
    "sslCertificates": "ssl_certificates",
    "sslHealthCheck": "ssl_health_check",
    "sslPolicy": "ssl_policy",
    "stateDetails": "state_details",
    "stateNotificationConfig": "state_notification_config",
    "storageBytes": "storage_bytes",
    "storageClass": "storage_class",
    "subjectAlternativeNames": "subject_alternative_names",
    "tableId": "table_id",
    "tagsFingerprint": "tags_fingerprint",
    "targetPools": "target_pools",
    "targetServiceAccounts": "target_service_accounts",
    "targetSize": "target_size",
    "targetTags": "target_tags",
    "targetVpnGateway": "target_vpn_gateway",
    "tcpCheck": "tcp_check",
    "tcpEstablishedIdleTimeoutSec": "tcp_established_idle_timeout_sec",
    "tcpHealthCheck": "tcp_health_check",
    "tcpTransitoryIdleTimeoutSec": "tcp_transitory_idle_timeout_sec",
    "tempGcsLocation": "temp_gcs_location",
    "templateGcsPath": "template_gcs_path",
    "tensorflowVersion": "tensorflow_version",
    "timePartitioning": "time_partitioning",
    "timeZone": "time_zone",
    "timeoutSec": "timeout_sec",
    "tpuIpv4CidrBlock": "tpu_ipv4_cidr_block",
    "transferSpec": "transfer_spec",
    "triggerHttp": "trigger_http",
    "triggerId": "trigger_id",
    "triggerTemplate": "trigger_template",
    "udpIdleTimeoutSec": "udp_idle_timeout_sec",
    "unhealthyThreshold": "unhealthy_threshold",
    "uniqueId": "unique_id",
    "uniqueWriterIdentity": "unique_writer_identity",
    "updatePolicy": "update_policy",
    "updateTime": "update_time",
    "uptimeCheckId": "uptime_check_id",
    "urlDispatchRules": "url_dispatch_rules",
    "urlMap": "url_map",
    "userLabels": "user_labels",
    "validAfter": "valid_after",
    "validBefore": "valid_before",
    "verificationStatus": "verification_status",
    "versionTemplate": "version_template",
    "vlanTag8021q": "vlan_tag8021q",
    "vpnTunnel": "vpn_tunnel",
    "waitForInstances": "wait_for_instances",
    "writerIdentity": "writer_identity",
}
