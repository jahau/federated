package(default_visibility = ["//tensorflow_federated/python/core:__subpackages__"])

licenses(["notice"])

py_library(
    name = "framework",
    srcs = ["__init__.py"],
    visibility = ["//visibility:public"],
    deps = [
        "//tensorflow_federated/python/core/impl:caching_executor",
        "//tensorflow_federated/python/core/impl:composite_executor",
        "//tensorflow_federated/python/core/impl:concurrent_executor",
        "//tensorflow_federated/python/core/impl:context_base",
        "//tensorflow_federated/python/core/impl:context_stack_base",
        "//tensorflow_federated/python/core/impl:eager_executor",
        "//tensorflow_federated/python/core/impl:executor_base",
        "//tensorflow_federated/python/core/impl:executor_service",
        "//tensorflow_federated/python/core/impl:executor_stacks",
        "//tensorflow_federated/python/core/impl:executor_value_base",
        "//tensorflow_federated/python/core/impl:federated_executor",
        "//tensorflow_federated/python/core/impl:lambda_executor",
        "//tensorflow_federated/python/core/impl:remote_executor",
        "//tensorflow_federated/python/core/impl:transformations",
        "//tensorflow_federated/python/core/impl:transforming_executor",
        "//tensorflow_federated/python/core/impl:type_utils",
        "//tensorflow_federated/python/core/impl/compiler:building_block_analysis",
        "//tensorflow_federated/python/core/impl/compiler:building_block_factory",
        "//tensorflow_federated/python/core/impl/compiler:building_blocks",
        "//tensorflow_federated/python/core/impl/compiler:intrinsic_defs",
        "//tensorflow_federated/python/core/impl/compiler:transformation_utils",
        "//tensorflow_federated/python/core/impl/compiler:transformations",
        "//tensorflow_federated/python/core/impl/compiler:tree_analysis",
        "//tensorflow_federated/python/core/impl/wrappers:computation_wrapper_instances",
        "//tensorflow_federated/python/core/impl/wrappers:get_context_stack",
        "//tensorflow_federated/python/core/impl/wrappers:set_default_context",
        "//tensorflow_federated/python/core/impl/wrappers:set_default_executor",
    ],
)
