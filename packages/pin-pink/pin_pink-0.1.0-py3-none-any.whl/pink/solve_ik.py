#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Stéphane Caron.
#
# This file is part of Pink.
#
# Pink is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Pink is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pink. If not, see <http://www.gnu.org/licenses/>.

"""
Function to solve inverse kinematics.
"""

from typing import Iterable, Tuple

import numpy as np

from qpsolvers import solve_qp

from .configuration import Configuration
from .limits import compute_velocity_limits
from .tasks import Task


def compute_qp_objective(
    configuration: Configuration, tasks: Iterable[Task], damping: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute the Hessian matrix :math:`H` and linear vector :math:`c` of the
    QP objective function:

    .. math::

        \\frac{1}{2} \\Delta q^T H \\Delta q + c^T q

    The configuration displacement :math:`\\Delta q` is the output of inverse
    kinematics (we divide it by :math:`\\Delta t` to get a commanded velocity).

    Args:
        configuration: Robot configuration to read kinematics from.
        tasks: List of kinematic tasks to fulfill at (weighted) best.
        damping: weight of Tikhonov (everywhere) regularization. Its unit is
            `[cost]^2 / [tangent]` where `[tangent]` is "the" unit of robot
            velocities. Improves numerical stability, but larger values slow
            down all tasks.

    Returns:
        Pair :math:`(H, c)` of Hessian matrix and linear vector of the QP
        objective.
    """
    H = damping * np.eye(configuration.model.nv)
    c = np.zeros((configuration.model.nv,))
    for task in tasks:
        H_task, c_task = task.compute_qp_objective(configuration)
        H += H_task
        c += c_task
    return (H, c)


def solve_ik(
    configuration: Configuration,
    tasks: Iterable[Task],
    dt: float,
    damping: float = 1e-12,
    solver: str = "quadprog",
) -> np.ndarray:
    """
    Compute a velocity tangent to the current robot configuration that
    satisfies at (weighted) best a given set of kinematic tasks.

    Args:
        configuration: Robot configuration to read kinematics from.
        tasks: List of kinematic tasks.
        dt: Integration timestep in [s].
        damping: weight of Tikhonov (everywhere) regularization. Its unit is
            :math:`[\\mathrm{cost}]^2 / [\\mathrm{tangent}]` where
            :math:`[\\mathrm{tangent}]` is "the" unit of robot velocities.
            Improves numerical stability, but larger values slow down all
            tasks.
        solver: Backend quadratic programming solver.

    Returns:
        Velocity :math:`v` in tangent space.

    Raises:
        NotWithinConfigurationLimits: if the current configuration is not
            within limits.

    Note:
        Our Tikhonov damping is isotropic despite tangent velocities not being
        homogeneous. If it helps we can add a tangent-space scaling to damp the
        floating base differently from joint angular velocities.
    """
    # TODO(scaron): configuration.check_limits()
    H, c = compute_qp_objective(configuration, tasks, damping)
    v_max, v_min = compute_velocity_limits(configuration, dt)
    tangent_eye = np.eye(configuration.model.nv)
    A = np.vstack([tangent_eye, -tangent_eye])
    b = np.hstack([v_max * dt, -v_min * dt])
    Delta_q = solve_qp(H, c, A, b, solver=solver)
    assert Delta_q is not None
    v: np.ndarray = Delta_q / dt
    return v
