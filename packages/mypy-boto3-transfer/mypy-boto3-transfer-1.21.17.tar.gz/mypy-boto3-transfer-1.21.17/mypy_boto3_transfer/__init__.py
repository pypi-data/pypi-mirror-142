"""
Main interface for transfer service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_transfer import (
        Client,
        ListAccessesPaginator,
        ListExecutionsPaginator,
        ListSecurityPoliciesPaginator,
        ListServersPaginator,
        ListTagsForResourcePaginator,
        ListUsersPaginator,
        ListWorkflowsPaginator,
        ServerOfflineWaiter,
        ServerOnlineWaiter,
        TransferClient,
    )

    session = Session()
    client: TransferClient = session.client("transfer")

    server_offline_waiter: ServerOfflineWaiter = client.get_waiter("server_offline")
    server_online_waiter: ServerOnlineWaiter = client.get_waiter("server_online")

    list_accesses_paginator: ListAccessesPaginator = client.get_paginator("list_accesses")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_security_policies_paginator: ListSecurityPoliciesPaginator = client.get_paginator("list_security_policies")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""
from .client import TransferClient
from .paginator import (
    ListAccessesPaginator,
    ListExecutionsPaginator,
    ListSecurityPoliciesPaginator,
    ListServersPaginator,
    ListTagsForResourcePaginator,
    ListUsersPaginator,
    ListWorkflowsPaginator,
)
from .waiter import ServerOfflineWaiter, ServerOnlineWaiter

Client = TransferClient


__all__ = (
    "Client",
    "ListAccessesPaginator",
    "ListExecutionsPaginator",
    "ListSecurityPoliciesPaginator",
    "ListServersPaginator",
    "ListTagsForResourcePaginator",
    "ListUsersPaginator",
    "ListWorkflowsPaginator",
    "ServerOfflineWaiter",
    "ServerOnlineWaiter",
    "TransferClient",
)
