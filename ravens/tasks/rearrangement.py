"""Rearrangement Tasks, following block insertion."""

import numpy as np
from ravens.tasks.task import Task
from ravens.utils import utils
import cv2
import pybullet as p


class Rearrangement(Task):
    """Insertion Task - Base Variant."""

    def __init__(self):
        super().__init__()
        self.max_steps = 3

    def reset(self, env):
        super().reset(env)

        blocks = []
        targ_poses = []

        for i in range(5):
            blocks.append((self.add_block(env), (0, None)))
            targ_poses.append(self.add_fixture(env))
        self.goals.append((blocks, np.ones(shape=(len(blocks), len(blocks))), targ_poses, False, True, 'pose', None, 1))

    def add_block(self, env):
        """Add L-shaped block."""
        size = (0.1, 0.1, 0.04)
        urdf = 'insertion/ell.urdf'
        pose = self.get_random_pose(env, size)
        return env.add_object(urdf, pose)

    def add_fixture(self, env):
        """Add L-shaped fixture to place block."""
        size = (0.1, 0.1, 0.04)
        urdf = 'insertion/fixture.urdf'
        pose = self.get_random_pose(env, size)
        env.add_object(urdf, pose, 'fixed')
        return pose


class RearrangementGoalConditioned(Task):
    def __init__(self):
        super().__init__()
        self.max_steps = 10

    def reset(self, env):
        super().reset(env)
        # do: create some situation that they are definitely in collision.
        #   we can find that this ground truth generation code cannot reason about collision or other precondition.

        # do: when we go back and see these. Oh my god, when sampling initial pose, we can find that collision checking
        #  has been performed. therefore, we first start to do collision free goal-conditioned transportation.
        blocks = []
        targ_poses = []

        for i in range(2):
            blocks.append((self.add_block(env)[0], (0, None)))
            targ_poses.append(self.add_fixture(env)[1])
        self.goals.append((blocks, np.ones(shape=(len(blocks), len(blocks))), targ_poses, False, True, 'pose', None, 1))

        return

        for i in range(5):
            bid, bpose = self.add_block(env)
            blocks.append((bid, (0, None)))
            fid, fpose = self.add_fixture(env)
            targ_poses.append(fpose)
        # colors = env._get_obs()['color']
        # for color in colors:
        #     cv2.imshow('haha', color)
        #     cv2.waitKey(0)
        # exit(0)
        self.goals.append((blocks, np.ones(shape=(len(blocks), len(blocks))), targ_poses, False, True, 'pose', None, 1))

    def add_block(self, env):
        """Add L-shaped block."""
        size = (0.1, 0.1, 0.04)
        urdf = 'insertion/ell.urdf'
        pose = self.get_random_pose(env, size)
        return env.add_object(urdf, pose), pose

    def add_fixture(self, env):
        """Add L-shaped fixture to place block."""
        size = (0.1, 0.1, 0.04)
        # do: don't add fixture.
        urdf = 'insertion/fixture.urdf'
        pose = self.get_random_pose(env, size)
        fid = env.add_object(urdf, pose, 'fixed')
        return fid, pose
