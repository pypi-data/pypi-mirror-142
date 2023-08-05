# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from opentelemetry.proto.metrics.experimental import metrics_config_service_pb2 as opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2


class MetricConfigStub(object):
    """MetricConfig is a service that enables updating metric schedules, trace
    parameters, and other configurations on the SDK without having to restart the
    instrumented application. The collector can also serve as the configuration
    service, acting as a bridge between third-party configuration services and
    the SDK, piping updated configs from a third-party source to an instrumented
    application.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMetricConfig = channel.unary_unary(
                '/opentelemetry.proto.metrics.experimental.MetricConfig/GetMetricConfig',
                request_serializer=opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigRequest.SerializeToString,
                response_deserializer=opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigResponse.FromString,
                )


class MetricConfigServicer(object):
    """MetricConfig is a service that enables updating metric schedules, trace
    parameters, and other configurations on the SDK without having to restart the
    instrumented application. The collector can also serve as the configuration
    service, acting as a bridge between third-party configuration services and
    the SDK, piping updated configs from a third-party source to an instrumented
    application.
    """

    def GetMetricConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMetricConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetricConfig,
                    request_deserializer=opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigRequest.FromString,
                    response_serializer=opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opentelemetry.proto.metrics.experimental.MetricConfig', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetricConfig(object):
    """MetricConfig is a service that enables updating metric schedules, trace
    parameters, and other configurations on the SDK without having to restart the
    instrumented application. The collector can also serve as the configuration
    service, acting as a bridge between third-party configuration services and
    the SDK, piping updated configs from a third-party source to an instrumented
    application.
    """

    @staticmethod
    def GetMetricConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opentelemetry.proto.metrics.experimental.MetricConfig/GetMetricConfig',
            opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigRequest.SerializeToString,
            opentelemetry_dot_proto_dot_metrics_dot_experimental_dot_metrics__config__service__pb2.MetricConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
