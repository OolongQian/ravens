### Motivation

Project reading log.

1. Read dataset collection code -> scripted task in PyBullet, I know it fairly well (in gym style).
2. Train policy in server -> see how much time it takes to train the network.
3. Run evaluate code to see how to use the model (in gym style).
4. See task environment observation in detail.

### Observation

I may pay attention to the hyper-parameter tuning, this may not be as harsh as the benchmarks in computer vision.

I observe that some standard camera would have some fixed intrinsics.

I realize that Andy Zeng has done what I was trying to do fairly well. I think this means that I should be agile to do
good AI.

I realize that there's full of unknown in AI research.

I observe that block insertion works pretty well after just a little training.

Andy Zeng implements pick-place and push, and I realize that this is pretty simple. Previously, without enough
tech-communication, I failed to focus on what is important.

Finally, Let us see the network input-output. We can see that the network ultimately predicts two arguments -> pick pose
and place pose. And the env step is accomplished by these primitives. Then, let's see the models.

I suddenly understand that, I would build on this project to construct a rearrangement task. Since we have a
goal-conditioned ravens here.

### Task

Set up a rearrangement task using this repository.

### Source code reading

I read Andy Zeng's source code, beneficial to me. In task.py, we have def oracle(self, env) method. We first unpack the
task goal -> some matching between object and its target. Then we check which objects have already arrived their target
pose, and filter them out. Again, we compute the pairwise distances between the object to be rearranged, and sort them
according to the distance. Pick-and-place the farthest one first. After deciding which one to pick, we retrieve its
segmentation mask -> then we sample a pixel over the segmentation mask.

Then we learn how to build upon other's source code.

1. Remove fixture (find this project cannot reason about collision and occlusion).
2. Visualize input image -> there is some vision camera projection computation here (multi-view, orthographical,
   heightmap).
3. We can see that Andy Zeng provides various agent models without directly runnable code, which encourages the user to
   further dig into it -> my intuition is right. And then, what I gonna do is to learn from this piece of code.
4. In order to use the goal conditioned implementation, I realized that I need to pay attention to the model invocation,
   demo data collection, dataset output, and model computation.
5. I have had a runnable goal-conditioned transporter, then I need to investigate the semantics of the data itself. The
   semantics is nothing to see, there's nothing there.
6. Then, I need to generate the goal. I realize that the goal is the last observation of a whole oracle execution. The
   current scripted demo.py has collected it. I find deep learning in robotics has a different notion of generalization.
   Then, I need to generate data that only contains objects, and visualize the fixture in the goal image. 
