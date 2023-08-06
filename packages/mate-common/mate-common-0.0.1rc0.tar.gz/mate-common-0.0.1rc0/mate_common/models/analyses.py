from __future__ import annotations

import enum
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, NewType, Optional

from pydantic import BaseModel

from mate_common.state_machine import StateMachineMixin

# TODO(ww): Refine the inner Dict type here.
GraphRequests = NewType("GraphRequests", List[Dict[str, Any]])
"""
A convenience type for a list of FlowFinder graph requests.
"""


@enum.unique
class AnalysisTaskState(StateMachineMixin, str, enum.Enum):
    """Represents the state of an analysis task."""

    Created = "created"
    Duplicate = "duplicate"
    Running = "running"
    Failed = "failed"
    Completed = "completed"

    @lru_cache
    def _valid_transitions(self) -> Dict[AnalysisTaskState, FrozenSet[AnalysisTaskState]]:
        return {
            AnalysisTaskState.Created: frozenset(
                {AnalysisTaskState.Duplicate, AnalysisTaskState.Running}
            ),
            AnalysisTaskState.Duplicate: frozenset(),
            AnalysisTaskState.Running: frozenset(
                {AnalysisTaskState.Completed, AnalysisTaskState.Failed}
            ),
            AnalysisTaskState.Completed: frozenset(),
            AnalysisTaskState.Failed: frozenset(),
        }


@enum.unique
class POIResultComplexity(str, enum.Enum):
    """Represents the "cognitive complexity" of a POI result, corresponding roughly to the expected
    skill level required to correctly evaluate the result."""

    Unknown = "unknown"
    Low = "low"
    Medium = "medium"
    High = "high"


class POIResultInfo(BaseModel):
    """Represents a single POI result, as produced by an analysis task from an underlying
    analysis."""

    poi_result_id: str
    """
    The unique ID for this POI result.
    """

    build_id: str
    """
    The unique ID of the build that this result applies to.
    """

    analysis_task_id: str
    """
    The unique ID of the analysis task that produced this result.
    """

    analysis_id: str
    """
    The unique ID of the underlying analysis that produced this result.
    """

    analysis_name: str
    """
    The name of the analysis that produced this result.
    """

    poi: Dict[str, Any]
    """
    The raw POI result.
    """

    flagged: bool
    """
    True if this POI result has been toggled to ``flagged`` in the UI, False otherwise.
    """

    done: bool
    """
    True if this POI result has been toggled to ``done`` in the UI, False otherwise.
    """

    complexity: POIResultComplexity
    """
    The estimated cognitive complexity of the POI result.
    """

    parent_result_id: Optional[str]
    """
    The ID of the "parent" POI result, if this POI result was created from a parent.
    """

    child_result_ids: List[str]
    """
    Any "child" POI results that were created as a result of this POI result.
    """

    snapshot_ids: List[str]
    """
    Any snapshots that have been created from this POI result.
    """


class FlowFinderSnapshotInfo(BaseModel):
    """Represents a snapshot of a FlowFinder analysis state."""

    snapshot_id: str
    """
    The unique ID for this POI snapshot.
    """

    poi_result_id: Optional[str]
    """
    The unique ID for the POI result that this snapshot was created from, if it was
    created from a POI result.
    """

    build_id: str
    """
    The ID of the build that this snapshot was created from.
    """

    label: str
    """
    A unique human-readable label for this POI snapshot.
    """

    filters: List[str]
    """
    A list of filters applied.
    """

    graph_requests: GraphRequests
    """
    The graph requests needed to reproduce the analysis state.
    """

    hidden_graph_ids: List[str]
    """
    The IDs of any graphs that should be hidden.
    """

    hidden_node_ids: List[str]
    """
    The IDs of any nodes that should be hidden.
    """


class POIDetail(BaseModel):
    """Represents a single POI result, as produced by an analysis task from an underlying
    analysis."""

    poi_result_id: str
    """
    The unique ID for this POI result.
    """

    build_id: str
    """
    The unique ID of the build that this result applies to.
    """

    analysis_name: str
    """
    The name of the analysis that produced this result.
    """

    poi: Dict[str, Any]
    """
    The raw POI result.
    """

    graph_requests: GraphRequests
    """
    A list of objects representing graph requests.
    """

    insight: str
    """
    A textual description of the POI.
    """

    background: str
    """
    A string of background information relating to this type of POI.
    """


class RegisteredAnalysisInfo(BaseModel):
    """Represents an analysis that's been registered with MATE."""

    analysis_id: str
    """
    The unique ID for this analysis.
    """

    name: str
    """
    The human-readable name for this analysis.
    """

    background: str
    """
    Human-readable background text for this analysis.
    """


class AnalysisTaskInfo(BaseModel):
    """Represents a single POI analysis task, which may still be running and may have POI
    results."""

    analysis_task_id: str
    """
    The unique ID of this task.
    """

    analysis_id: str
    """
    The unique ID of the analysis that this task is running.
    """

    analysis_name: str
    """
    The name of the analysis that this task is running.
    """

    build_id: str
    """
    The unique ID of the build that this task is running against.
    """

    poi_result_ids: List[str]
    """
    The IDs of any POI results that have been produced.
    """

    state: AnalysisTaskState
    """
    The state of this analysis task.
    """
