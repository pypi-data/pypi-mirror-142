#  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import luigi

from servicecatalog_puppet.workflow.generic import generic_for_region_task
from servicecatalog_puppet.workflow.workspaces import workspace_for_task


class WorkspaceForRegionTask(
    generic_for_region_task.GenericForRegionTask, workspace_for_task.WorkspaceForTask
):
    region = luigi.Parameter()
